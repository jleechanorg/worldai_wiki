"""A lost recovery response must not silently erase the last access path."""

from flask import Flask

from mvp_site import mini_mcp, mini_recovery, mini_state
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore


def test_lost_recovery_response_blocks_unlink_until_new_key_confirmed(monkeypatch):
    monkeypatch.setattr(mini_mcp, "emit", lambda event: None)
    store, clock = AtomicStore(), Clock()
    store.set("mini_runtime_control", "default", {"enabled": True})
    created = mini_state.create_session(store, clock, initial_state={})
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", created["session_key"]
    )
    app = Flask(__name__)
    mini_recovery.register_routes(
        app,
        lambda: store,
        clock,
        claims_verifier=lambda: {
            "uid": "synthetic-user",
            "email": "user@example.test",
            "email_verified": True,
        },
    )
    client = app.test_client()
    # The server commits a rotation, but the client loses the returned capability.
    assert (
        client.post(
            "/api/mini-recovery/recover", json={"session_id": created["session_id"]}
        ).status_code
        == 200
    )
    response = client.post("/api/mini-recovery/remove", json={})
    assert response.status_code == 409
    assert response.json == {"error": "RECOVERY_CONFIRMATION_REQUIRED"}
    assert len(mini_recovery.list_sessions(store, clock, "synthetic-user")) == 1

    # Recovery can be repeated; linking the new key confirms possession.
    recovered = client.post(
        "/api/mini-recovery/recover", json={"session_id": created["session_id"]}
    ).json
    key = recovered["session_key"]
    assert (
        client.post(
            "/api/mini-recovery/link", json={"session_key": key, "consent": True}
        ).status_code
        == 200
    )
    assert client.post("/api/mini-recovery/remove", json={}).status_code == 200
    assert (
        mini_state.get_session(store, clock, key)["session_id"] == created["session_id"]
    )


def test_only_explicit_discard_can_remove_an_unconfirmed_recovery(monkeypatch):
    monkeypatch.setattr(mini_mcp, "emit", lambda event: None)
    store, clock = AtomicStore(), Clock()
    store.set("mini_runtime_control", "default", {"enabled": True})
    created = mini_state.create_session(store, clock, initial_state={})
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", created["session_key"]
    )
    app = Flask(__name__)
    mini_recovery.register_routes(
        app,
        lambda: store,
        clock,
        claims_verifier=lambda: {
            "uid": "synthetic-user",
            "email": "user@example.test",
            "email_verified": True,
        },
    )
    client = app.test_client()
    recovered = client.post(
        "/api/mini-recovery/recover", json={"session_id": created["session_id"]}
    ).json
    for invalid in (
        {"discard_unconfirmed": False},
        {"discard_unconfirmed": "true"},
        {"discard_unconfirmed": True, "extra": 1},
    ):
        assert client.post("/api/mini-recovery/remove", json=invalid).status_code == 400
    assert client.post("/api/mini-recovery/remove", json={}).status_code == 409
    assert client.post(
        "/api/mini-recovery/remove", json={"discard_unconfirmed": True}
    ).json == {"removed": True}
    assert (
        mini_state.get_session(store, clock, recovered["session_key"])["session_id"]
        == created["session_id"]
    )


def test_every_unconfirmed_campaign_must_be_confirmed_before_normal_removal():
    import pytest

    store, clock = AtomicStore(), Clock()
    created = [
        mini_state.create_session(store, clock, initial_state={}) for _ in range(2)
    ]
    for campaign in created:
        mini_recovery.link_session(
            store, clock, "synthetic-user", "user@example.test", campaign["session_key"]
        )
    keys = [
        mini_recovery.recover_session(
            store, clock, "synthetic-user", campaign["session_id"]
        )["session_key"]
        for campaign in created
    ]
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", keys[0]
    )
    with pytest.raises(mini_state.MiniError, match="RECOVERY_CONFIRMATION_REQUIRED"):
        mini_recovery.remove_recovery(store, clock, "synthetic-user")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", keys[1]
    )
    assert mini_recovery.remove_recovery(store, clock, "synthetic-user") == {
        "removed": True
    }
