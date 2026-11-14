"""HTTP integration against the standalone app with an isolated in-memory store."""

import json
import threading
import urllib.request
import uuid

from werkzeug.serving import make_server

from mvp_site.tests.test_mini_transactions import AtomicStore
from server import create_app


def test_mini_http_create_save_roll_and_export():
    store = AtomicStore()
    store.set("mini_runtime_control", "default", {"enabled": True})
    server = make_server("127.0.0.1", 0, create_app(lambda: store))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    endpoint = f"http://127.0.0.1:{server.server_port}/mini-mcp"

    def rpc(method, params, request_id):
        body = json.dumps(
            {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}
        ).encode()
        request = urllib.request.Request(
            endpoint,
            data=body,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "MCP-Protocol-Version": "2025-11-25",
            },
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            assert response.status == 200
            return json.load(response)

    def tool(name, arguments, request_id):
        result = rpc("tools/call", {"name": name, "arguments": arguments}, request_id)[
            "result"
        ]
        assert result["isError"] is False
        return result["structuredContent"]["data"]

    try:
        tools = rpc("tools/list", {}, 1)["result"]["tools"]
        assert len(tools) == 8 and all(
            item.get("description", "").strip() for item in tools
        )
        created = tool(
            "mini_create_session",
            {"initial_state": {"player": {"name": "Synthetic Hero"}}},
            2,
        )
        key = created["session_key"]
        saved = tool(
            "mini_save_state",
            {
                "session_key": key,
                "expected_revision": 0,
                "operation_id": str(uuid.uuid4()),
                "patch": {"player": {"level": 2}},
            },
            3,
        )
        assert saved["revision"] == 1
        state = tool("mini_get_state", {"session_key": key}, 4)
        assert state["state"]["player"]["level"] == 2
        rolled = tool(
            "mini_roll_dice",
            {
                "session_key": key,
                "expected_revision": 1,
                "operation_id": str(uuid.uuid4()),
                "notation": "1d20",
            },
            5,
        )
        assert rolled["revision"] == 2 and 1 <= rolled["total"] <= 20
        exported = tool("mini_export_checkpoint", {"session_key": key}, 6)
        assert exported["checkpoint"]["player"]["level"] == 2
        assert key not in json.dumps(exported)
    finally:
        server.shutdown()
        thread.join(timeout=10)
        server.server_close()
