"""Recovery requests must never buffer an unbounded client body."""

import io

from flask import Flask

from mvp_site import mini_mcp
from mvp_site.mini_recovery import register_routes
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore


class CountingStream(io.BytesIO):
    def __init__(self, data):
        super().__init__(data)
        self.bytes_read = 0

    def read(self, size=-1):
        data = super().read(size)
        self.bytes_read += len(data)
        return data

    def readinto(self, buffer):
        count = super().readinto(buffer)
        self.bytes_read += count
        return count


def test_chunked_recovery_body_is_rejected_without_unbounded_read(monkeypatch):
    monkeypatch.setattr(mini_mcp, "emit", lambda event: None)
    store = AtomicStore()
    store.set("mini_runtime_control", "default", {"enabled": True})
    app = Flask(__name__)
    register_routes(
        app,
        lambda: store,
        Clock(),
        claims_verifier=lambda: {
            "uid": "synthetic-user",
            "email": "user@example.test",
            "email_verified": True,
        },
    )
    stream = CountingStream(b" " * 65536)
    response = app.test_client().open(
        "/api/mini-recovery/list",
        method="POST",
        content_type="application/json",
        environ_overrides={
            "wsgi.input": stream,
            "wsgi.input_terminated": True,
            "CONTENT_LENGTH": "",
        },
    )
    assert response.status_code == 413
    assert stream.bytes_read <= 4097, (
        f"read {stream.bytes_read} bytes from oversized body"
    )


def test_valid_small_recovery_body_still_works(monkeypatch):
    monkeypatch.setattr(mini_mcp, "emit", lambda event: None)
    store = AtomicStore()
    store.set("mini_runtime_control", "default", {"enabled": True})
    app = Flask(__name__)
    register_routes(
        app,
        lambda: store,
        Clock(),
        claims_verifier=lambda: {
            "uid": "synthetic-user",
            "email": "user@example.test",
            "email_verified": True,
        },
    )
    response = app.test_client().post("/api/mini-recovery/list", json={})
    assert response.status_code == 200
    assert response.json == {"sessions": []}


def test_chunked_recovery_body_at_limit_remains_valid(monkeypatch):
    monkeypatch.setattr(mini_mcp, "emit", lambda event: None)
    store = AtomicStore()
    store.set("mini_runtime_control", "default", {"enabled": True})
    app = Flask(__name__)
    register_routes(
        app,
        lambda: store,
        Clock(),
        claims_verifier=lambda: {
            "uid": "synthetic-user",
            "email": "user@example.test",
            "email_verified": True,
        },
    )
    stream = CountingStream(b"{}" + b" " * 4094)
    response = app.test_client().open(
        "/api/mini-recovery/list",
        method="POST",
        content_type="application/json",
        environ_overrides={
            "wsgi.input": stream,
            "wsgi.input_terminated": True,
            "CONTENT_LENGTH": "",
        },
    )
    assert response.status_code == 200
    assert response.json == {"sessions": []}
    assert stream.bytes_read == 4096
