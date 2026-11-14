"""WorldAI Mini session store: create, locate and expire without scans.

Plan: docs/superpowers/plans/2026-11-07-worldai-mini-mcp.md (roadmap repo),
Task 2. Design: docs/superpowers/specs/2026-11-07-worldai-mini-mcp-design.md
(2026-11-08 amendments take precedence where they correct section 4).

Session, transaction and guarded tool primitives:

- Server-generated 192-bit capability key (``mini_`` + 32 base64url chars).
  The key is the resume credential; only its SHA-256 digest is persisted, as
  the Firestore document ID, so every lookup is exactly one addressed read
  and no collection stream/query ever runs.
- Every creation, populated or empty, gets revision 0, created/updated
  timestamps and exactly 90-day idle expiry. Reads at or after expiry fail
  as SESSION_UNAVAILABLE; malformed, unknown and expired capabilities are
  intentionally indistinguishable.
- The public ``session_id`` is an opaque random label, never authority.
- The server-owned ``gm_note_guard`` ledger lives outside model-owned
  ``state``; it is not patchable or exported. Creation protects every initial note
  string leaf before revision zero; Task 3 maintains tombstones on saves.
- The raw capability is never stored in the session document or logged.

Versioned saves, receipts, durable dice and guarded exports share this store. Domain
dictionaries (player/gm_notes contents) are opaque to this module.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import json
import re
import secrets
import unicodedata
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from functools import lru_cache
from pathlib import Path
from typing import Any

SESSIONS_COLLECTION = "mini_sessions"
SESSION_KEY_PREFIX = "mini_"
SESSION_KEY_ENTROPY_BYTES = 24  # 192 bits -> 32 base64url chars, no padding
SESSION_KEY_PATTERN = re.compile(r"^mini_[A-Za-z0-9_-]{32}$")
SESSION_TTL = timedelta(days=90)
TITLE_MAX_CHARS = 120


class SessionUnavailable(Exception):  # noqa: N818 - existing public API
    """Malformed, unknown or expired capability; responses are identical."""


def _utcnow() -> datetime:
    return datetime.now(UTC)


def validate_capability_format(session_key: Any) -> str:
    """Require the strict prefix/encoding/length before any lookup."""
    if not isinstance(session_key, str) or not SESSION_KEY_PATTERN.match(session_key):
        raise SessionUnavailable()
    try:
        raw = base64.urlsafe_b64decode(session_key[len(SESSION_KEY_PREFIX) :] + "==")
    except (binascii.Error, ValueError) as exc:
        raise SessionUnavailable() from exc
    if len(raw) != SESSION_KEY_ENTROPY_BYTES:
        raise SessionUnavailable()
    return session_key


def locate_key(session_key: Any) -> str:
    """Map a validated capability to its one addressed document ID."""
    raw = validate_capability_format(session_key)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def require_live(document: dict | None, now: datetime) -> dict:
    if document is None:
        raise SessionUnavailable()
    expires_at = datetime.fromisoformat(document["expires_at"])
    if expires_at <= now:
        raise SessionUnavailable()
    return document


def _generate_session_key() -> str:
    return SESSION_KEY_PREFIX + base64.urlsafe_b64encode(
        secrets.token_bytes(SESSION_KEY_ENTROPY_BYTES)
    ).decode("ascii")


def _normalize_initial_state(initial_state: dict | None) -> dict:
    """Validate the control envelope without repairing or filtering domain data."""
    initial = {} if initial_state is None else initial_state
    if not isinstance(initial, dict) or set(initial) - {"player", "gm_notes", "recap"}:
        raise ValueError("Invalid initial state envelope")
    for key, kind in (("player", dict), ("gm_notes", dict), ("recap", str)):
        if key in initial and not isinstance(initial[key], kind):
            raise ValueError("Invalid initial container type")
    return {
        "player": initial.get("player", {}),
        "gm_notes": initial.get("gm_notes", {}),
        "recap": initial.get("recap", ""),
    }


@lru_cache(maxsize=1)
def _limits() -> dict:
    schema = Path(__file__).parent / "schemas" / "mini_state.schema.json"
    return json.loads(schema.read_text(encoding="utf-8"))["limits"]


def _json_bytes(value: Any) -> int:
    return len(
        json.dumps(
            value, ensure_ascii=False, allow_nan=False, separators=(",", ":")
        ).encode("utf-8")
    )


def _check_bound(value: Any, limit_name: str) -> None:
    if _json_bytes(value) > _limits()[limit_name]:
        raise ValueError("CAPACITY_EXCEEDED: " + limit_name)


def _check_state_capacity(state: dict) -> None:
    # Iteration avoids recursion before an adversarially deep input is rejected.
    pending = [(state, 1)]
    while pending:
        value, depth = pending.pop()
        if depth > _limits()["max_json_depth"]:
            raise ValueError("CAPACITY_EXCEEDED: max_json_depth")
        children = (
            value.values()
            if isinstance(value, dict)
            else value
            if isinstance(value, list)
            else ()
        )
        pending.extend((child, depth + 1) for child in children)
    for container in ("player", "gm_notes", "recap"):
        _check_bound(state[container], container + "_bytes")


def _initial_note_guard(notes: dict) -> dict:
    """Record immutable leaf identity separately from normalized match text."""
    entries = []

    def visit(value: Any, path: str) -> None:
        if isinstance(value, str):
            entries.append(
                {
                    "path": path,
                    "digest": hashlib.sha256(value.encode("utf-8")).hexdigest(),
                    "normalized_text": " ".join(
                        unicodedata.normalize("NFKC", value).split()
                    ),
                    "tombstoned": False,
                    "revealed": False,
                }
            )
        elif isinstance(value, dict):
            for key, item in value.items():
                escaped = key.replace("~", "~0").replace("/", "~1")
                visit(item, path + "/" + escaped)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                visit(item, path + "/" + str(index))

    visit(notes, "")
    return {"entries": entries}


def _visible_projection(state: dict) -> dict:
    """Player-visible state: gm_notes never appear in creation/state echoes."""
    return {"player": state["player"], "recap": state["recap"]}


def create_session(
    store: Any,
    clock: Callable[[], datetime] | None = None,
    *,
    initial_state: dict | None = None,
    title: str | None = None,
    provenance: dict | None = None,
) -> dict:
    """Create a session; return the capability exactly once.

    The write is one addressed document set. If the write's outcome is
    uncertain (the store raises), the exception propagates and no key is
    returned: an uncertain create is never claimed as saved or recoverable,
    and the submitted initial state stays with the host.
    """
    now = (clock or _utcnow)()
    if title is not None and (
        not isinstance(title, str) or len(title) > TITLE_MAX_CHARS
    ):
        raise ValueError("title must be a string of at most 120 characters")
    state = _normalize_initial_state(initial_state)
    _check_state_capacity(state)
    session_key = _generate_session_key()
    digest = locate_key(session_key)
    expires_at = now + SESSION_TTL
    document = {
        "session_id": secrets.token_hex(16),  # opaque public label, not authority
        "revision": 0,
        "state": state,
        "gm_note_guard": _initial_note_guard(state["gm_notes"]),
        "recent_rolls": [],
        "last_operation": None,
        "title": title,
        "created_at": now.isoformat(),
        "updated_at": now.isoformat(),
        "expires_at": expires_at.isoformat(),
    }
    if provenance is not None:
        document["provenance"] = dict(provenance)
    _check_bound(document["gm_note_guard"], "guard_ledger_bytes")
    _check_bound(document, "session_document_bytes")
    _admit_document(document)
    store.set(SESSIONS_COLLECTION, digest, document)
    return {
        "session_key": session_key,
        "session_id": document["session_id"],
        "revision": 0,
        "state": _visible_projection(state),
        "expires_at": expires_at.isoformat(),
    }


def get_session(
    store: Any,
    clock: Callable[[], datetime] | None,
    session_key: Any,
    *,
    include_gm_notes: bool = True,
) -> dict:
    """Locate a live session with exactly one addressed document read.

    ``gm_notes`` is returned separately from the player-visible ``state``
    projection; the transport layer (Task 6) maps it to structuredContent
    only. A malformed capability is rejected before any lookup; an unknown
    or expired one costs exactly one read and fails identically.
    """
    now = (clock or _utcnow)()
    digest = locate_key(session_key)
    document = require_live(store.get(SESSIONS_COLLECTION, digest), now)
    state = document["state"]
    result = {
        "session_id": document["session_id"],
        "revision": document["revision"],
        "state": _visible_projection(state),
        "last_operation": document.get("last_operation"),
        "recent_rolls": document.get("recent_rolls", []),
        "expires_at": document["expires_at"],
    }
    if include_gm_notes:
        result["gm_notes"] = state["gm_notes"]
    return result


class MiniError(Exception):
    """Safe domain outcome; never includes request or exception text."""

    def __init__(self, code, **details):
        super().__init__(code)
        self.code = code
        self.details = details


def _state_result(document, include_gm_notes=True):
    result = {
        k: document.get(k)
        for k in (
            "session_id",
            "revision",
            "last_operation",
            "recent_rolls",
            "expires_at",
        )
    }
    result["state"] = _visible_projection(document["state"])
    if include_gm_notes:
        result["gm_notes"] = document["state"]["gm_notes"]
    return result


def _string_leaves(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from _string_leaves(item)
    elif isinstance(value, list):
        for item in value:
            yield from _string_leaves(item)


def _normalize_text(value):
    return " ".join(unicodedata.normalize("NFKC", value).split())


def _guard_visible(document, visible):
    # A set of 32-code-point windows gives an exact contiguous-overlap test.
    windows = set()
    for entry in document["gm_note_guard"]["entries"]:
        if not entry["revealed"]:
            text = entry["normalized_text"]
            windows.update(text[i : i + 32] for i in range(max(0, len(text) - 31)))
    for leaf in _string_leaves(visible):
        text = _normalize_text(leaf)
        if any(text[i : i + 32] in windows for i in range(max(0, len(text) - 31))):
            raise MiniError("EXPORT_CONTAMINATION")


def _export_result(document):
    checkpoint = _visible_projection(document["state"])
    _guard_visible(document, checkpoint)
    from mvp_site.mini_wire import encode

    return {
        "session_id": document["session_id"],
        "revision": document["revision"],
        "checkpoint": checkpoint,
        "content_sha256": hashlib.sha256(encode(checkpoint)).hexdigest(),
        "expires_at": document["expires_at"],
    }


def _admit_document(document):
    from mvp_site.mini_wire import call_result, encode, rpc_result

    _check_state_capacity(document["state"])
    _check_bound(document["gm_note_guard"], "guard_ledger_bytes")
    _check_bound(document, "session_document_bytes")
    try:
        export = call_result(_export_result(document))
    except MiniError as exc:
        export = call_result(
            error={
                "code": exc.code,
                "message": "Remove protected copied material from visible state, save, read back, and retry.",
            }
        )
    for response in (call_result(_state_result(document)), export):
        # IDs are bounded at transport; reserve its maximum encoded string size.
        if (
            len(encode(rpc_result(response, "\x00" * 128)))
            > _limits()["response_body_bytes"]
        ):
            raise MiniError("CAPACITY_EXCEEDED")


def export_checkpoint(store, clock, session_key):
    document = require_live(
        store.get(SESSIONS_COLLECTION, locate_key(session_key)), (clock or _utcnow)()
    )
    return _export_result(document)


def get_image_description(store, clock, session_key, character_id):
    document = require_live(
        store.get(SESSIONS_COLLECTION, locate_key(session_key)), (clock or _utcnow)()
    )
    profiles = document["state"]["player"].get("image_descriptions", {})
    if not isinstance(profiles, dict):
        raise MiniError("INVALID_ARGUMENT")
    profile = profiles.get(character_id)
    if character_id in profiles and not isinstance(profile, dict):
        raise MiniError("INVALID_ARGUMENT")
    _guard_visible(document, {"character_id": character_id, "profile": profile})
    return {
        "session_id": document["session_id"],
        "revision": document["revision"],
        "character_id": character_id,
        "found": character_id in profiles,
        "profile": profile,
    }


def _merge_patch(target, patch):
    # RFC7396, no gameplay-field allowlist or semantic normalization.
    import copy

    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    result = copy.deepcopy(target) if isinstance(target, dict) else {}
    for key, value in patch.items():
        if value is None:
            result.pop(key, None)
        else:
            result[key] = _merge_patch(result.get(key), value)
    return result


def _updated_guard(prior, state, reveals, operation_id, now):
    import copy

    old = _initial_note_guard(prior["state"]["gm_notes"])["entries"]
    new = _initial_note_guard(state["gm_notes"])["entries"]
    old_ids = {(e["path"], e["digest"]) for e in old}
    new_ids = {(e["path"], e["digest"]) for e in new}
    ledger = copy.deepcopy(prior["gm_note_guard"])
    indexed = {(e["path"], e["digest"]): e for e in ledger["entries"]}
    for e in new:
        if (e["path"], e["digest"]) not in indexed:
            ledger["entries"].append(e)
            indexed[(e["path"], e["digest"])] = e
    for identity, e in indexed.items():
        e["tombstoned"] = identity not in new_ids
    seen = set()
    audit = []
    for reveal in reveals:
        identity = (reveal["path"], reveal["content_sha256"])
        if identity in seen or identity not in old_ids or identity not in new_ids:
            raise MiniError("INVALID_ARGUMENT")
        seen.add(identity)
        if len(reveal["path"].encode("utf-8")) > 1024:
            raise MiniError("INVALID_ARGUMENT")
        if not reveal["turn"].strip() or not reveal["scene"].strip():
            raise MiniError("INVALID_ARGUMENT")
        record = {
            "path": identity[0],
            "digest": identity[1],
            "turn": reveal["turn"].strip(),
            "scene": reveal["scene"].strip(),
            "operation_id": operation_id,
            "timestamp": now.isoformat(),
        }
        indexed[identity].update(
            revealed=True,
            revealed_at_turn=record["turn"],
            revealed_in_scene=record["scene"],
            reveal_receipt=record,
        )
        audit.append(record)
    return ledger, audit


class OperationResult(dict):
    """Receipt bytes stay identical; internal telemetry sees replay disposition."""

    replayed = False


OPERATIONS_COLLECTION = "mini_operations"


def _mutate(
    store,
    clock,
    session_key,
    *,
    expected_revision,
    operation_id,
    tool,
    arguments,
    candidate=None,
):
    import copy

    from mvp_site.operation_identity import canonical_operation_id, request_fingerprint

    now = (clock or _utcnow)()
    digest = locate_key(session_key)
    operation_id = canonical_operation_id(operation_id, "operation_id")
    if (
        operation_id is None
        or type(expected_revision) is not int
        or expected_revision < 0
    ):
        raise MiniError("INVALID_ARGUMENT")
    arguments = {
        **arguments,
        "operation_id": operation_id,
        "expected_revision": expected_revision,
    }
    fingerprint = request_fingerprint(arguments, tool, {"session_key"})

    def commit(tx):
        document = require_live(tx.get(SESSIONS_COLLECTION, digest), now)
        receipt_id = document.get("operation_namespace", digest) + "_" + operation_id
        receipt = tx.get(OPERATIONS_COLLECTION, receipt_id)
        if receipt and datetime.fromisoformat(receipt["expires_at"]) > now:
            if receipt["fingerprint"] != fingerprint:
                raise MiniError("IDEMPOTENCY_CONFLICT")
            result = OperationResult(receipt["result"])
            result.replayed = True
            return result
        if document["revision"] != expected_revision:
            raise MiniError("REVISION_CONFLICT", current_revision=document["revision"])
        proposed = copy.deepcopy(document)
        revision = expected_revision + 1
        expires = now + SESSION_TTL
        audit = []
        if tool == "mini_save_state":
            patch = arguments["patch"]
            if not isinstance(patch, dict) or set(patch) - {
                "player",
                "gm_notes",
                "recap",
            }:
                raise MiniError("INVALID_ARGUMENT")
            proposed["state"] = _merge_patch(document["state"], patch)
            state = proposed["state"]
            if (
                set(state) != {"player", "gm_notes", "recap"}
                or not isinstance(state["player"], dict)
                or not isinstance(state["gm_notes"], dict)
                or not isinstance(state["recap"], str)
            ):
                raise MiniError("INVALID_ARGUMENT")
            proposed["gm_note_guard"], audit = _updated_guard(
                document, state, arguments.get("reveals", []), operation_id, now
            )
            from mvp_site.mini_wire import encode

            result = {
                "session_id": document["session_id"],
                "revision": revision,
                "operation_id": operation_id,
                "saved_at": now.isoformat(),
                "state_digest": hashlib.sha256(encode(state)).hexdigest(),
                "expires_at": expires.isoformat(),
            }
        else:
            result = {
                **candidate,
                "session_id": document["session_id"],
                "revision": revision,
                "operation_id": operation_id,
                "rolled_at": now.isoformat(),
            }
            proposed["recent_rolls"] = (proposed["recent_rolls"] + [result])[
                -_limits()["max_roll_receipts"] :
            ]
        proposed.update(
            revision=revision,
            updated_at=now.isoformat(),
            expires_at=expires.isoformat(),
            last_operation=result,
        )
        _admit_document(proposed)
        receipt = {
            "fingerprint": fingerprint,
            "result": result,
            "reveals": audit,
            "expires_at": min(now + timedelta(days=7), expires).isoformat(),
        }
        tx.set(SESSIONS_COLLECTION, digest, proposed)
        tx.set(OPERATIONS_COLLECTION, receipt_id, receipt)
        return OperationResult(result)

    try:
        return store.transaction(commit)
    except (MiniError, SessionUnavailable, ValueError):
        raise
    except Exception:
        raise MiniError("SERVICE_UNAVAILABLE", outcome_unknown=True) from None


def save_state(
    store, clock, session_key, *, expected_revision, operation_id, patch, reveals=None
):
    return _mutate(
        store,
        clock,
        session_key,
        expected_revision=expected_revision,
        operation_id=operation_id,
        tool="mini_save_state",
        arguments={"patch": patch, "reveals": reveals or []},
    )


def roll_dice(
    store,
    clock,
    session_key,
    *,
    expected_revision,
    operation_id,
    notation,
    mode="normal",
    purpose="",
):
    from mvp_site import dice

    if not isinstance(notation, str) or re.match(r"^\s*\d+\s*x", notation, re.I):
        raise MiniError("INVALID_ARGUMENT")
    parsed = dice._parse_bounded_dice_notation(notation)
    if not parsed or mode not in ("normal", "advantage", "disadvantage"):
        raise MiniError("INVALID_ARGUMENT")
    pools, modifier, _ = parsed
    if mode != "normal" and pools != [(1, 20)]:
        raise MiniError("INVALID_ARGUMENT")
    # Reject malformed capabilities before drawing even unpublished randomness.
    locate_key(session_key)
    # Shared parser and arithmetic; no legacy audit logger carrying free text.
    rolled = dice.roll_bounded_pools(pools, modifier, advantage=mode != "normal")
    raw = rolled["raw_faces"]
    selected = (
        raw if mode == "normal" else [max(raw) if mode == "advantage" else min(raw)]
    )
    candidate = {
        "receipt_id": secrets.token_hex(16),
        "raw_faces": raw,
        "pools": rolled["pools"],
        "selected_faces": selected,
        "modifier": modifier,
        "total": sum(selected) + modifier,
        "notation": notation,
        "mode": mode,
    }
    return _mutate(
        store,
        clock,
        session_key,
        expected_revision=expected_revision,
        operation_id=operation_id,
        tool="mini_roll_dice",
        arguments={"notation": notation, "mode": mode, "purpose": purpose},
        candidate=candidate,
    )
