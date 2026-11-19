import copy
import threading
import uuid

import pytest

from mvp_site import mini_state as s
from mvp_site.tests.test_mini_state import Clock, RecordingStore


class AtomicStore(RecordingStore):
    def __init__(self):
        super().__init__()
        self.lock = threading.RLock()

    def transaction(self, callback):
        with self.lock:
            original = copy.deepcopy(self.documents)
            try:
                return callback(self)
            except BaseException:
                self.documents = original
                raise


def save(store, clock, key, revision=0, patch=None, operation_id=None, **kw):
    return s.save_state(
        store,
        clock,
        key,
        expected_revision=revision,
        operation_id=operation_id or str(uuid.uuid4()),
        patch=patch or {},
        **kw,
    )


def test_merge_revision_and_replay():
    store, clock = AtomicStore(), Clock()
    c = s.create_session(
        store, clock, initial_state={"player": {"x": 1, "a": [1], "unknown": {"v": 9}}}
    )
    op = str(uuid.uuid4())
    r = save(
        store,
        clock,
        c["session_key"],
        patch={"player": {"x": None, "a": [2], "revision": 900}},
        operation_id=op,
    )
    assert r["revision"] == 1
    assert (
        save(
            store,
            clock,
            c["session_key"],
            patch={"player": {"x": None, "a": [2], "revision": 900}},
            operation_id=op,
        )
        == r
    )
    with pytest.raises(s.MiniError, match="IDEMPOTENCY_CONFLICT"):
        save(
            store, clock, c["session_key"], patch={"player": {"x": 2}}, operation_id=op
        )
    with pytest.raises(s.MiniError, match="REVISION_CONFLICT"):
        save(store, clock, c["session_key"])
    state = s.get_session(store, clock, c["session_key"])["state"]["player"]
    assert state == {"a": [2], "unknown": {"v": 9}, "revision": 900}


def test_deletion_tombstone_reveal_and_clean_export():
    store, clock = AtomicStore(), Clock()
    secret = "A hidden unique guardian waits behind the northern wall."
    c = s.create_session(
        store,
        clock,
        initial_state={"gm_notes": {"hidden": secret}, "player": {"copy": secret}},
    )
    k = c["session_key"]
    with pytest.raises(s.MiniError, match="EXPORT_CONTAMINATION"):
        s.export_checkpoint(store, clock, k)
    save(store, clock, k, patch={"gm_notes": {"hidden": None}})
    with pytest.raises(s.MiniError, match="EXPORT_CONTAMINATION"):
        s.export_checkpoint(store, clock, k)
    save(store, clock, k, 1, {"player": {"copy": None}})
    assert s.export_checkpoint(store, clock, k)["checkpoint"]["player"] == {}


def test_uncommitted_write_returns_unknown_not_success():
    store, clock = AtomicStore(), Clock()
    c = s.create_session(store, clock)
    store.transaction = lambda cb: (_ for _ in ()).throw(OSError("private canary"))
    with pytest.raises(s.MiniError) as e:
        save(store, clock, c["session_key"])
    assert e.value.code == "SERVICE_UNAVAILABLE"
    assert e.value.details["outcome_unknown"]


def test_two_writers_same_revision_exactly_one_commits():
    from concurrent.futures import ThreadPoolExecutor

    store, clock = AtomicStore(), Clock()
    created = s.create_session(store, clock)

    def writer(value):
        try:
            return save(
                store, clock, created["session_key"], patch={"player": {"value": value}}
            )
        except s.MiniError as error:
            return error.code

    with ThreadPoolExecutor(max_workers=2) as executor:
        outcomes = list(executor.map(writer, [1, 2]))
    assert sum(isinstance(result, dict) for result in outcomes) == 1
    assert "REVISION_CONFLICT" in outcomes
    assert s.get_session(store, clock, created["session_key"])["revision"] == 1


def test_receipt_expiry_cannot_reexecute_stale_revision():
    from datetime import timedelta

    store, clock = AtomicStore(), Clock()
    created = s.create_session(store, clock)
    op = str(uuid.uuid4())
    save(store, clock, created["session_key"], operation_id=op)
    clock.advance(timedelta(days=8))
    with pytest.raises(s.MiniError, match="REVISION_CONFLICT"):
        save(store, clock, created["session_key"], operation_id=op)
