"""Stateless anonymous Mini MCP boundary, isolated from full-game dispatch."""

from __future__ import annotations

import copy
import hashlib
import json
import logging
import os
import time
import uuid
from datetime import UTC, datetime, timedelta
from functools import lru_cache
from pathlib import Path

import jsonschema
from flask import Response, g, request

from mvp_site import mini_state as state
from mvp_site.mini_wire import call_result, encode, rpc_result
from mvp_site.schemas.validation import load_schema

VERSIONS = ("2025-03-26", "2025-06-18", "2025-11-25")
ORIGINS = frozenset(
    ("https://chatgpt.com", "https://chat.openai.com", "https://worldarchitect.ai", "https://worldrpg.ai")
)
LOG = logging.getLogger(__name__)

def mini_icons():
    """Use an optional deployment-owned icon rather than a hosted dependency."""
    url = os.getenv("MINI_ICON_URL", "")
    return [{"src": url, "mimeType": "image/png", "sizes": ["192x192"]}] if url else []

MINI_DISCOVERY_INSTRUCTIONS = (
    "Before new play or resume, call mini_get_playbook for the matching topic. "
    "For a new custom campaign, guide one unanswered question at a time: "
    "world or story idea, timeline/era, protagonist, starting setting, plot/what-if, "
    "title, optional campaign details. Reuse supplied answers; allow skips, "
    "free input and suggestions. Show a review and wait for the player's "
    "confirmation before mini_create_session and consequential play. "
    "Honor an explicit quick start without forcing the questionnaire. "
    "For resume, load existing saved state rather than create a replacement."
)


@lru_cache(maxsize=1)
def tool_definitions():
    # Existing schema utility owns immutable loading. The historical filename
    # is shared with Task 1 and intentionally remains mini_tools.json.
    return tuple(
        json.loads((Path(__file__).parent / "schemas/mini_tools.json").read_text())[
            "tools"
        ]
    )


@lru_cache(maxsize=1)
def gameplay_instructions():
    return (Path(__file__).parent / "prompts" / "mini_gameplay.md").read_text()


@lru_cache(maxsize=1)
def playbooks():
    return json.loads(
        (Path(__file__).parent / "prompts/mini/playbooks.json").read_text()
    )


def supporting_tool(name, args):
    if name == "mini_get_playbook":
        return {
            "topic": args["topic"],
            "template_version": "2",
            "instructions": gameplay_instructions()
            + "\n\n## Topic instructions\n\n"
            + playbooks()[args["topic"]],
        }
    parts = copy.deepcopy(args)
    return {
        "description_parts": parts,
        "description": "\n".join(
            f"{k}: " + (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
            for k, v in parts.items()
        ),
        "template_version": "1",
        "image_generated": False,
    }


def admit(store, now, ip, tool=None, session_key=None, *, count_ip=True):
    """Atomic shared quotas. Fail closed and count replays before domain reads."""
    minute = int(now.timestamp()) // 60
    day = int(now.timestamp()) // 86400
    ip_digest = hashlib.sha256(ip.encode()).hexdigest()

    def commit(tx):
        control = tx.get("mini_runtime_control", "default")
        if not control or control.get("enabled") is not True:
            raise state.MiniError("SERVICE_UNAVAILABLE")
        limits = [("ip:" + ip_digest + ":" + str(minute), 60, 60)] if count_ip else []
        if tool:
            limits.append(
                (
                    "global:" + str(day),
                    min(20000, int(control.get("daily_calls", 20000))),
                    86400,
                )
            )
        if tool == "mini_create_session":
            limits.extend(
                [
                    ("create:" + ip_digest + ":" + str(day), 10, 86400),
                    (
                        "global-create:" + str(day),
                        min(1000, int(control.get("daily_sessions", 1000))),
                        86400,
                    ),
                ]
            )
        if tool in ("mini_get_state", "mini_get_image_description"):
            limits.append(("lookup:" + ip_digest + ":" + str(minute), 5, 60))
        if session_key:
            digest = hashlib.sha256(session_key.encode()).hexdigest()
            limits.append(("session:" + digest + ":" + str(minute), 60, 60))
        counters = []
        for key, maximum, window in limits:
            counter_id = hashlib.sha256(key.encode()).hexdigest()
            doc = tx.get("mini_counters", counter_id) or {"count": 0}
            if doc["count"] >= maximum:
                raise state.MiniError(
                    "RATE_LIMITED",
                    retry_after_seconds=window - int(now.timestamp()) % window,
                )
            counters.append((counter_id, doc, window))
        for key, doc, window in counters:
            tx.set(
                "mini_counters",
                key,
                {
                    "count": doc["count"] + 1,
                    "expires_at": (now + timedelta(seconds=window * 2)).isoformat(),
                },
            )

    try:
        store.transaction(commit)
    except state.MiniError:
        raise
    except Exception:
        raise state.MiniError("SERVICE_UNAVAILABLE") from None


def dispatch(store, clock, name, args, *, provenance=None):
    if name == "mini_create_session":
        return state.create_session(store, clock, **args, provenance=provenance)
    if name in ("mini_get_playbook", "mini_prepare_image_description"):
        return supporting_tool(name, args)
    handlers = {
        "mini_get_state": state.get_session,
        "mini_save_state": state.save_state,
        "mini_roll_dice": state.roll_dice,
        "mini_export_checkpoint": state.export_checkpoint,
        "mini_get_image_description": state.get_image_description,
    }
    return handlers[name](store, clock, **args)


def safe_error(exc):
    if isinstance(exc, state.MiniError):
        code = exc.code
        details = exc.details
    elif isinstance(exc, state.SessionUnavailable):
        code = "SESSION_UNAVAILABLE"
        details = {}
    elif isinstance(exc, (ValueError, TypeError, KeyError, jsonschema.ValidationError)):
        code = (
            "CAPACITY_EXCEEDED"
            if isinstance(exc, ValueError) and str(exc).startswith("CAPACITY_EXCEEDED")
            else "INVALID_ARGUMENT"
        )
        details = {}
    else:
        code = "SERVICE_UNAVAILABLE"
        details = {"outcome_unknown": True}
    messages = {
        "EXPORT_CONTAMINATION": "Remove protected copied material from visible state, save, read back and retry.",
        "REVISION_CONFLICT": "Read current state and reconcile the retained unsaved patch.",
        "SERVICE_UNAVAILABLE": "Service unavailable. Preserve intent and operation identity; read back before retrying.",
    }
    return {
        "code": code,
        "message": messages.get(code, code.replace("_", " ").capitalize()),
        **details,
    }


def emit(event):
    # Standalone deployments use their logging platform rather than WorldAI's
    # BigQuery-specific sink. Event fields remain bounded metadata, never prose.
    LOG.info("mini_request_outcome", extra={"json_fields": {"mini": event}})


def readiness(store):
    try:
        tool_definitions()
        load_schema("mini_state")
        control = store.get("mini_runtime_control", "default")
        return {
            "ready": bool(
                control
                and control.get("enabled") is True
                and not os.getenv("DICE_SEED")
            )
        }
    except Exception:
        return {"ready": False}


def register_routes(app, store_factory, clock=None, telemetry=emit):  # noqa: PLR0915 - route owner and local response helpers
    clock = clock or (lambda: datetime.now(UTC))

    @app.before_request
    def mini_request_start():
        if request.path != "/mini-mcp":
            return
        # User-Agent is a self-reported transport hint, never authentication.
        product = request.user_agent.string.partition("/")[0]
        g.mini_started = time.monotonic()
        g.mini_event = {
            "source": "mini",
            "surface": "mini_mcp",
            "client": "chatgpt_plugin" if product == "openai-mcp" else "unknown",
            "origin_verified": False,
            "request_id": uuid.uuid4().hex,
            "method": "unknown",
            "outcome": "protocol_error",
            "replay": False,
            "schema_version": "2",
            "build": os.getenv("GIT_COMMIT", "unknown")[:40],
        }

    @app.after_request
    def mini_request_finish(result):
        if request.path != "/mini-mcp" or not hasattr(g, "mini_event"):
            return result
        event = g.mini_event
        event.update(
            status=result.status_code,
            duration_ms=round((time.monotonic() - g.mini_started) * 1000),
            request_bytes=request.content_length or 0,
            response_bytes=result.calculate_content_length() or 0,
        )
        if result.status_code >= 400 and event["outcome"] == "protocol_error":
            event["outcome"] = "http_error"
        result.headers["X-Mini-Request-ID"] = event["request_id"]
        try:
            telemetry(event)
        except Exception:
            LOG.warning("mini_telemetry_dropped")
        return result

    def response(value, status=200, headers=None):
        return Response(
            encode(value) if value is not None else b"",
            status=status,
            content_type="application/json",
            headers=headers,
        )

    def protocol(code, message, id=None):
        return response(
            {"jsonrpc": "2.0", "id": id, "error": {"code": code, "message": message}}
        )

    @app.route("/mini-mcp", methods=["POST", "GET", "DELETE", "OPTIONS"])
    def mini_endpoint():  # noqa: PLR0911, PLR0912, PLR0915 - explicit protocol matrix
        name = None
        operation = None
        replay = False
        label = None
        outcome = "protocol_error"
        if request.method != "POST":
            return response(None, 405, {"Allow": "POST"})
        if request.headers.get("Origin") and request.headers["Origin"] not in ORIGINS:
            return response(None, 403)
        if request.mimetype != "application/json":
            return response(None, 415)
        accept = request.headers.get("Accept", "")
        if "application/json" not in accept or "text/event-stream" not in accept:
            return response(None, 406)
        if (
            request.content_length
            and request.content_length > state._limits()["request_body_bytes"]
        ):
            return response(None, 413)
        try:
            store = store_factory()
            admit(store, clock(), request.remote_addr or "unknown")
        except Exception as exc:
            error = safe_error(exc)
            g.mini_event["outcome"] = error["code"]
            return response(
                {"error": error}, 429 if error["code"] == "RATE_LIMITED" else 503
            )
        raw = request.stream.read(state._limits()["request_body_bytes"] + 1)
        if len(raw) > state._limits()["request_body_bytes"]:
            return response(None, 413)
        try:
            body = json.loads(raw)
        except (ValueError, UnicodeError, RecursionError):
            return protocol(-32700, "Parse error")
        if (
            not isinstance(body, dict)
            or set(body) - {"jsonrpc", "id", "method", "params"}
            or body.get("jsonrpc") != "2.0"
            or not isinstance(body.get("method"), str)
        ):
            return protocol(-32600, "Invalid request")
        id = body.get("id")
        method = body["method"]
        g.mini_event["method"] = (
            method
            if method
            in (
                "initialize",
                "notifications/initialized",
                "tools/call",
                "tools/list",
                "ping",
            )
            else "unknown"
        )
        params = body.get("params", {})
        if "id" in body and (
            type(id) not in (str, int)
            or isinstance(id, str)
            and len(id) > 128
            or isinstance(id, int)
            and len(encode(id)) > 128
        ):
            return protocol(-32600, "Invalid request")
        if not isinstance(params, dict):
            return protocol(-32602, "Invalid params", id)
        if (
            method != "initialize"
            and request.headers.get("MCP-Protocol-Version") not in VERSIONS
        ):
            return response(None, 400)
        if method == "notifications/initialized":
            if "id" not in body:
                g.mini_event["outcome"] = "ok"
            return (
                response(None, 202)
                if "id" not in body
                else protocol(-32600, "Invalid notification", id)
            )
        if "id" not in body:
            return protocol(-32600, "Request id required")
        try:
            if os.getenv("DICE_SEED"):
                raise state.MiniError("SERVICE_UNAVAILABLE")
            if method == "tools/call":
                if (
                    set(params) - {"name", "arguments", "_meta"}
                    or not isinstance(params.get("name"), str)
                    or not isinstance(params.get("arguments", {}), dict)
                ):
                    return protocol(-32602, "Invalid params", id)
                name = params["name"]
                definitions = {d["name"]: d for d in tool_definitions()}
                if name not in definitions:
                    return protocol(-32602, "Unknown tool", id)
                args = params.get("arguments", {})
                # Admission before schema validation/session lookup. Never trust
                # unqualified forwarded headers here; main's proxy owner resolves IP.
                admit(
                    store,
                    clock(),
                    request.remote_addr or "unknown",
                    name,
                    args.get("session_key")
                    if isinstance(args.get("session_key"), str)
                    else None,
                    count_ip=False,
                )
                try:
                    jsonschema.Draft202012Validator(
                        definitions[name]["inputSchema"],
                        format_checker=jsonschema.FormatChecker(),
                    ).validate(args)
                    data = dispatch(
                        store,
                        clock,
                        name,
                        args,
                        provenance={
                            "surface": "mini_mcp",
                            "client": g.mini_event["client"],
                            "verified": False,
                            "request_id": g.mini_event["request_id"],
                        },
                    )
                    outcome = "ok"
                    label = data.get("session_id")
                    operation = data.get("operation_id")
                    replay = getattr(data, "replayed", False)
                    result = call_result(data)
                except Exception as exc:
                    error = safe_error(exc)
                    outcome = error["code"]
                    result = call_result(error=error)
                payload = rpc_result(result, id)
                if len(encode(payload)) > state._limits()["response_body_bytes"]:
                    return response(None, 413)
                return response(payload)
            if method == "initialize":
                if (
                    not isinstance(params.get("protocolVersion"), str)
                    or not isinstance(params.get("capabilities"), dict)
                    or not isinstance(params.get("clientInfo"), dict)
                ):
                    return protocol(-32602, "Invalid initialize params", id)
                version = (
                    params["protocolVersion"]
                    if params["protocolVersion"] in VERSIONS
                    else VERSIONS[-1]
                )
                g.mini_event["outcome"] = "ok"
                return response(
                    rpc_result(
                        {
                            "protocolVersion": version,
                            "capabilities": {"tools": {}},
                            "serverInfo": {
                                "name": "worldai-mini", "version": "1",
                                "title": "WorldAI mini",
                                "icons": mini_icons(),
                            },
                            "instructions": MINI_DISCOVERY_INSTRUCTIONS,
                        },
                        id,
                    )
                )
            if method == "ping":
                g.mini_event["outcome"] = "ok"
                return response(rpc_result({}, id))
            if method == "tools/list":
                from mcp.types import Tool

                tools = []
                for source_definition in tool_definitions():
                    definition = copy.deepcopy(source_definition)
                    definition["outputSchema"] = json.loads(
                        (Path(__file__).parent / "schemas/mini_tools.json").read_text()
                    )["result_schema"]
                    tools.append(
                        Tool.model_validate(definition).model_dump(
                            by_alias=True, exclude_none=True
                        )
                    )
                g.mini_event["outcome"] = "ok"
                return response(rpc_result({"tools": tools}, id))
            return protocol(-32601, "Method not found", id)
        except Exception as exc:
            error = safe_error(exc)
            outcome = error["code"]
            return response(
                {"error": error}, 429 if error["code"] == "RATE_LIMITED" else 503
            )
        finally:
            if name:
                g.mini_event.update(
                    tool=name
                    if name in {d["name"] for d in tool_definitions()}
                    else "unknown",
                    outcome=outcome,
                    replay=replay,
                )
                if label:
                    g.mini_event["session_id"] = label
                if operation:
                    g.mini_event["operation_id"] = operation

    def mini_readiness():
        try:
            return readiness(store_factory())
        except Exception:
            return {"ready": False}

    app.extensions["mini_readiness"] = mini_readiness
    from mvp_site import mini_recovery

    mini_recovery.register_routes(app, store_factory, clock)
