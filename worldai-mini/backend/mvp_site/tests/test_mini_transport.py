import json
import uuid

import pytest
from flask import Flask

from mvp_site.mini_mcp import register_routes
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
    "MCP-Protocol-Version": "2025-06-18",
}


def make_app(db=None, telemetry=lambda event: None):
    db = db or AtomicStore()
    db.set("mini_runtime_control", "default", {"enabled": True})
    app = Flask(__name__)
    register_routes(app, lambda: db, Clock(), telemetry)
    return app, db


def call(client, name, args, id=1):
    return client.post(
        "/mini-mcp",
        headers=HEADERS,
        json={
            "jsonrpc": "2.0",
            "id": id,
            "method": "tools/call",
            "params": {"name": name, "arguments": args},
        },
    )


def test_discovered_tools_have_descriptions():
    app, _ = make_app()
    response = app.test_client().post(
        "/mini-mcp",
        headers=HEADERS,
        json={"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
    )
    assert response.status_code == 200
    tools = response.json["result"]["tools"]
    assert len(tools) == 8
    missing = [tool["name"] for tool in tools if not tool.get("description", "").strip()]
    assert not missing, f"Missing tool descriptions: {missing}"


def test_full_wire_split_and_durable_sequence():
    app, db = make_app()
    c = app.test_client()
    listing = c.post(
        "/mini-mcp",
        headers=HEADERS,
        json={"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
    ).json
    assert len(listing["result"]["tools"]) == 8
    secret = "hidden long unique spoiler canary behind the gate"
    created = call(
        c, "mini_create_session", {"initial_state": {"gm_notes": {"hidden": secret}}}
    ).json
    assert "session_key" in created["result"]["structuredContent"]["data"]
    assert secret not in json.dumps(created)
    key = created["result"]["structuredContent"]["data"]["session_key"]
    state = call(c, "mini_get_state", {"session_key": key}).json["result"]
    assert secret not in state["content"][0]["text"]
    assert state["structuredContent"]["data"]["gm_notes"]["hidden"] == secret
    args = {
        "session_key": key,
        "expected_revision": 0,
        "operation_id": str(uuid.uuid4()),
        "patch": {"player": {"custom": [1, 2]}},
    }
    saved = call(c, "mini_save_state", args).json
    assert saved == call(c, "mini_save_state", args).json
    exported = call(c, "mini_export_checkpoint", {"session_key": key}).json
    assert exported["result"]["structuredContent"]["data"]["checkpoint"]["player"] == {
        "custom": [1, 2]
    }
    assert key not in json.dumps(exported)
    assert secret not in json.dumps(exported)


@pytest.mark.parametrize("method", ["GET", "DELETE", "OPTIONS"])
def test_stateless_methods(method):
    app, _ = make_app()
    r = app.test_client().open("/mini-mcp", method=method)
    assert r.status_code == 405
    assert r.headers["Allow"] == "POST"


def test_protocol_http_boundaries():
    app, _ = make_app()
    c = app.test_client()
    assert (
        c.post("/mini-mcp", data="x", headers=HEADERS).json["error"]["code"] == -32700
    )
    assert c.post("/mini-mcp", data="x" * 262145, headers=HEADERS).status_code == 413
    assert (
        c.post("/mini-mcp", headers={"Content-Type": "text/plain"}).status_code == 415
    )
    assert (
        c.post(
            "/mini-mcp", headers={**HEADERS, "Origin": "https://evil.invalid"}
        ).status_code
        == 403
    )
    r = c.post(
        "/mini-mcp",
        headers=HEADERS,
        json={"jsonrpc": "2.0", "method": "notifications/initialized"},
    )
    assert r.status_code == 202
    assert not r.data
    r = c.post(
        "/mini-mcp",
        headers=HEADERS,
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2025-06-18",
                "capabilities": {},
                "clientInfo": {"name": "test", "version": "1"},
            },
        },
    )
    assert r.json["result"]["capabilities"] == {"tools": {}}
    assert "Mcp-Session-Id" not in r.headers
    assert call(c, "roll_dice", {}).json["error"]["code"] == -32602
    assert call(c, "mini_save_state", {}).json["result"]["isError"]
