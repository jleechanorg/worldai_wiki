from datetime import timedelta

import pytest

from mvp_site.mini_mcp import admit
from mvp_site.mini_state import MiniError
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore


@pytest.mark.parametrize(
    ("tool", "allowed"),
    [
        ("mini_create_session", 10),
        ("mini_get_state", 5),
        ("mini_get_image_description", 5),
    ],
)
def test_shared_limits_before_lookup(tool, allowed):
    db, clock = AtomicStore(), Clock()
    db.set("mini_runtime_control", "default", {"enabled": True})
    for _ in range(allowed):
        admit(db, clock(), "ip", tool)
    reads = len(db.reads)
    with pytest.raises(MiniError, match="RATE_LIMITED"):
        admit(db, clock(), "ip", tool)
    assert all(c != "mini_sessions" for c, k in db.reads[reads:])
    clock.advance(timedelta(days=1))
    admit(db, clock(), "ip", tool)


def test_control_absent_and_disabled_fail_closed():
    db, clock = AtomicStore(), Clock()
    with pytest.raises(MiniError, match="SERVICE_UNAVAILABLE"):
        admit(db, clock(), "ip")
    db.set("mini_runtime_control", "default", {"enabled": False})
    with pytest.raises(MiniError, match="SERVICE_UNAVAILABLE"):
        admit(db, clock(), "ip")


def test_global_cap():
    db, clock = AtomicStore(), Clock()
    db.set("mini_runtime_control", "default", {"enabled": True, "daily_calls": 1})
    admit(db, clock(), "one", "mini_get_playbook")
    with pytest.raises(MiniError, match="RATE_LIMITED"):
        admit(db, clock(), "two", "mini_get_playbook")


def test_two_service_instances_share_ip_and_session_limits():
    db, clock = AtomicStore(), Clock()
    db.set("mini_runtime_control", "default", {"enabled": True})

    def instance_one(ip):
        admit(db, clock(), ip, "mini_get_playbook", "mini_" + "a" * 32)

    def instance_two(ip):
        admit(db, clock(), ip, "mini_get_playbook", "mini_" + "a" * 32)

    for index in range(60):
        (instance_one if index % 2 else instance_two)(str(index))
    with pytest.raises(MiniError, match="RATE_LIMITED"):
        instance_one("fresh-ip")
    for _index in range(60):
        admit(db, clock(), "one-ip", "mini_get_playbook")
    with pytest.raises(MiniError, match="RATE_LIMITED"):
        admit(db, clock(), "one-ip", "mini_get_playbook")


def test_counter_failure_has_no_local_fallback():
    db, clock = AtomicStore(), Clock()
    db.transaction = lambda callback: (_ for _ in ()).throw(OSError("private"))
    with pytest.raises(MiniError, match="SERVICE_UNAVAILABLE"):
        admit(db, clock(), "ip", "mini_get_playbook")
