"""Self-hosted discovery must not depend on WorldAI's hosted icon."""

from mvp_site.tests.test_mini_transactions import AtomicStore
from server import create_app


def test_discovery_uses_optional_deployment_owned_icon(monkeypatch):
    store = AtomicStore()
    store.set("mini_runtime_control", "default", {"enabled": True})
    client = create_app(lambda: store).test_client()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-11-25",
            "capabilities": {},
            "clientInfo": {"name": "test", "version": "1"},
        },
    }
    monkeypatch.delenv("MINI_ICON_URL", raising=False)
    info = client.post("/mini-mcp", headers=headers, json=payload).json["result"][
        "serverInfo"
    ]
    assert not info.get("icons")
    monkeypatch.setenv("MINI_ICON_URL", "https://example.test/mini.png")
    info = client.post("/mini-mcp", headers=headers, json=payload).json["result"][
        "serverInfo"
    ]
    assert info["icons"][0]["src"] == "https://example.test/mini.png"
