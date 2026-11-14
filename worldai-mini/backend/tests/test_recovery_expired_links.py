"""Expired recovery links must not consume all available slots forever."""

import hashlib
from datetime import timedelta

from mvp_site import mini_recovery, mini_state
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore


def test_expired_links_are_pruned_without_deleting_campaigns(monkeypatch):
    monkeypatch.setattr(mini_recovery, "MAX_LINKS", 2)
    store, clock = AtomicStore(), Clock()
    old = mini_state.create_session(store, clock, title="expired")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", old["session_key"]
    )
    clock.advance(timedelta(days=91))
    live = mini_state.create_session(store, clock, title="live")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", live["session_key"]
    )
    new = mini_state.create_session(store, clock, title="new")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", new["session_key"]
    )
    ids = {
        entry["session_id"]
        for entry in mini_recovery.list_sessions(store, clock, "synthetic-user")
    }
    assert ids == {live["session_id"], new["session_id"]}
    old_digest = hashlib.sha256(old["session_key"].encode()).hexdigest()
    assert store.get(mini_state.SESSIONS_COLLECTION, old_digest) is not None
    assert (
        mini_state.get_session(store, clock, live["session_key"])["session_id"]
        == live["session_id"]
    )


def test_capacity_still_rejects_when_every_link_is_live(monkeypatch):
    import pytest

    monkeypatch.setattr(mini_recovery, "MAX_LINKS", 1)
    store, clock = AtomicStore(), Clock()
    first = mini_state.create_session(store, clock, title="live")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", first["session_key"]
    )
    second = mini_state.create_session(store, clock, title="new")
    with pytest.raises(mini_state.MiniError, match="CAPACITY_EXCEEDED"):
        mini_recovery.link_session(
            store, clock, "synthetic-user", "user@example.test", second["session_key"]
        )
    ids = {
        entry["session_id"]
        for entry in mini_recovery.list_sessions(store, clock, "synthetic-user")
    }
    assert ids == {first["session_id"]}


def test_missing_expired_record_no_longer_blocks_a_new_link(monkeypatch):
    monkeypatch.setattr(mini_recovery, "MAX_LINKS", 1)
    store, clock = AtomicStore(), Clock()
    old = mini_state.create_session(store, clock, title="removed by TTL")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", old["session_key"]
    )
    old_digest = hashlib.sha256(old["session_key"].encode()).hexdigest()
    del store.documents[(mini_state.SESSIONS_COLLECTION, old_digest)]
    new = mini_state.create_session(store, clock, title="new")
    mini_recovery.link_session(
        store, clock, "synthetic-user", "user@example.test", new["session_key"]
    )
    ids = {
        entry["session_id"]
        for entry in mini_recovery.list_sessions(store, clock, "synthetic-user")
    }
    assert ids == {new["session_id"]}
