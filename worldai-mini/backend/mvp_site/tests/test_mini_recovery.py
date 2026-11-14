"""Recovery control state is separate from model-owned campaign state."""

import json
import uuid

import pytest

from mvp_site import mini_recovery as r, mini_state as s
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore, save


def test_verified_owner_link_recover_and_replay():
    store, clock = AtomicStore(), Clock()
    created = s.create_session(
        store, clock, title="Recovery test", initial_state={"player": {"unknown": 42}}
    )
    key = created["session_key"]
    operation = str(uuid.uuid4())
    receipt = save(
        store, clock, key, patch={"recap": "At the pier."}, operation_id=operation
    )
    linked = r.link_session(store, clock, "owner", "verified@example.test", key)
    assert linked["session_id"] == created["session_id"]
    assert r.list_sessions(store, clock, "other") == []
    assert (
        r.list_sessions(store, clock, "owner")[0]["session_id"] == created["session_id"]
    )
    with pytest.raises(s.SessionUnavailable):
        r.recover_session(store, clock, "other", created["session_id"])
    recovered = r.recover_session(store, clock, "owner", created["session_id"])
    assert recovered["session_key"] != key
    with pytest.raises(s.SessionUnavailable):
        s.get_session(store, clock, key)
    assert (
        s.get_session(store, clock, recovered["session_key"])["state"]["player"][
            "unknown"
        ]
        == 42
    )
    assert (
        save(
            store,
            clock,
            recovered["session_key"],
            patch={"recap": "At the pier."},
            operation_id=operation,
        )
        == receipt
    )
    assert recovered["session_key"] not in json.dumps(
        list(store.documents.values()), default=str
    )
    assert key not in json.dumps(list(store.documents.values()), default=str)
    with pytest.raises(s.MiniError):
        r.link_session(
            store, clock, "attacker", "verified2@example.test", recovered["session_key"]
        )


def test_recovery_routes_require_verified_signed_identity_and_consent(monkeypatch):
    from mvp_site.tests.test_mini_transport import make_app

    app, store = make_app()
    client = app.test_client()
    claims = {"uid": "owner", "email": "verified@example.test", "email_verified": True}

    def verify(token, **kwargs):
        assert kwargs["check_revoked"] is True
        if token != "valid":
            raise ValueError("bad")
        return claims

    monkeypatch.setattr(r.auth, "verify_id_token", verify)
    assert client.post("/api/mini-recovery/list", json={}).status_code == 401
    headers = {"Authorization": "Bearer valid"}
    claims["email_verified"] = False
    assert (
        client.post("/api/mini-recovery/list", headers=headers, json={}).status_code
        == 401
    )
    claims["email_verified"] = True
    created = s.create_session(store, Clock(), initial_state={})
    assert (
        client.post(
            "/api/mini-recovery/link",
            headers=headers,
            json={"session_key": created["session_key"], "consent": False},
        ).status_code
        == 400
    )
    assert (
        client.post(
            "/api/mini-recovery/link",
            headers=headers,
            json={"session_key": created["session_key"], "consent": True},
        ).status_code
        == 200
    )
    listed = client.post("/api/mini-recovery/list", headers=headers, json={})
    assert listed.json["sessions"][0]["session_id"] == created["session_id"]
    claims["uid"] = "other"
    assert (
        client.post(
            "/api/mini-recovery/recover",
            headers=headers,
            json={"session_id": created["session_id"]},
        ).status_code
        == 404
    )
    assert (
        client.post(
            "/api/mini-recovery/list",
            headers=headers,
            json={"email": "verified@example.test"},
        ).status_code
        == 400
    )


def test_expired_session_not_recoverable_and_consent_cannot_reassign():
    from datetime import timedelta

    store, clock = AtomicStore(), Clock()
    created = s.create_session(store, clock, initial_state={})
    r.link_session(
        store, clock, "owner", "verified@example.test", created["session_key"]
    )
    clock.advance(timedelta(days=91))
    with pytest.raises(s.SessionUnavailable):
        r.recover_session(store, clock, "owner", created["session_id"])


def test_frontend_recovery_does_not_mount_main_game_auth_shell():
    from pathlib import Path

    root = Path(__file__).parents[1] / "frontend_v1"
    js = (root / "auth.js").read_text()
    assert "firebase.initializeApp(window.MINI_FIREBASE_CONFIG)" in js
    assert "main game" not in js.lower()
    page = (root / "mini-recovery.js").read_text()
    assert "user.emailVerified" in page
    assert "window.confirm" in page
    assert "console.log" not in page


def test_remove_recovery_erases_email_links_and_preserves_live_capability():
    store, clock = AtomicStore(), Clock()
    created = s.create_session(store, clock, initial_state={"player": {"unknown": 42}})
    key = created["session_key"]
    r.link_session(store, clock, "owner", "private@example.test", key)
    assert r.remove_recovery(store, clock, "other") == {"removed": True}
    assert r.list_sessions(store, clock, "owner")
    result = r.remove_recovery(store, clock, "owner")
    assert result == {"removed": True}
    assert r.list_sessions(store, clock, "owner") == []
    assert "private@example.test" not in json.dumps(list(store.documents.values()))
    assert s.get_session(store, clock, key)["state"]["player"]["unknown"] == 42
    with pytest.raises(s.SessionUnavailable):
        r.recover_session(store, clock, "owner", created["session_id"])
    r.link_session(store, clock, "new-owner", "new@example.test", key)
    assert r.list_sessions(store, clock, "new-owner")


def test_recovery_remove_route_requires_verified_identity(monkeypatch):
    from mvp_site.tests.test_mini_transport import make_app

    app, store = make_app()
    c = app.test_client()
    assert c.post("/api/mini-recovery/remove", json={}).status_code == 401
    monkeypatch.setattr(
        r.auth,
        "verify_id_token",
        lambda *a, **kw: {
            "uid": "owner",
            "email": "owner@example.test",
            "email_verified": True,
        },
    )
    response = c.post(
        "/api/mini-recovery/remove", headers={"Authorization": "Bearer good"}, json={}
    )
    assert response.status_code == 200
    assert response.json == {"removed": True}
