import uuid

import pytest

from mvp_site import mini_state as s
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore


@pytest.mark.parametrize(
    "notation", ["garbage", "2x1d20", "1x1d20", "101d6", "1d20+1000001", "x" * 65]
)
def test_invalid_never_rolls(notation):
    db, clock = AtomicStore(), Clock()
    c = s.create_session(db, clock)
    with pytest.raises(s.MiniError, match="INVALID_ARGUMENT"):
        s.roll_dice(
            db,
            clock,
            c["session_key"],
            expected_revision=0,
            operation_id=str(uuid.uuid4()),
            notation=notation,
        )
    assert s.get_session(db, clock, c["session_key"])["revision"] == 0


@pytest.mark.parametrize("mode", ["normal", "advantage", "disadvantage"])
def test_durable_receipt_replay(mode):
    db, clock = AtomicStore(), Clock()
    c = s.create_session(db, clock)
    kw = {
        "expected_revision": 0,
        "operation_id": str(uuid.uuid4()),
        "notation": "1d20+3",
        "mode": mode,
    }
    r = s.roll_dice(db, clock, c["session_key"], **kw)
    assert s.roll_dice(db, clock, c["session_key"], **kw) == r
    assert r["total"] == sum(r["selected_faces"]) + 3
    assert len(r["raw_faces"]) == (1 if mode == "normal" else 2)
    assert s.get_session(db, clock, c["session_key"])["recent_rolls"] == [r]


def test_compound_pool_receipt_preserves_each_pool():
    db, clock = AtomicStore(), Clock()
    created = s.create_session(db, clock)
    receipt = s.roll_dice(
        db,
        clock,
        created["session_key"],
        expected_revision=0,
        operation_id=str(uuid.uuid4()),
        notation="2d6+1d8+3",
    )
    assert [(pool["count"], pool["sides"]) for pool in receipt["pools"]] == [
        (2, 6),
        (1, 8),
    ]
    assert [face for pool in receipt["pools"] for face in pool["faces"]] == receipt[
        "raw_faces"
    ]


def test_malformed_capability_fails_before_randomness(monkeypatch):
    from mvp_site import dice

    def forbidden(*args, **kwargs):
        raise AssertionError("randomness before capability validation")

    monkeypatch.setattr(dice, "roll_bounded_pools", forbidden)
    with pytest.raises(s.SessionUnavailable):
        s.roll_dice(
            AtomicStore(),
            Clock(),
            "invalid",
            expected_revision=0,
            operation_id=str(uuid.uuid4()),
            notation="1d20",
        )
