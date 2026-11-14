import hashlib

import pytest

from mvp_site import mini_state as s
from mvp_site.tests.test_mini_state import Clock
from mvp_site.tests.test_mini_transactions import AtomicStore, save


@pytest.mark.parametrize(
    ("text", "match"),
    [
        ("a" * 32, True),
        ("a" * 31, False),
        ("A" * 40, False),
        ("a" * 20 + "\u2003" + "a" * 20, True),
    ],
)
def test_decoded_overlap(text, match):
    db, clock = AtomicStore(), Clock()
    c = s.create_session(
        db, clock, initial_state={"gm_notes": {"x": "a" * 40}, "player": {"x": text}}
    )
    # Whitespace inserted inside a run breaks overlap; use normalized note for it.
    if "\u2003" in text:
        c = s.create_session(
            db,
            clock,
            initial_state={
                "gm_notes": {"x": "a" * 20 + " " + "a" * 20},
                "player": {"x": text},
            },
        )
    if match:
        with pytest.raises(s.MiniError, match="EXPORT_CONTAMINATION"):
            s.export_checkpoint(db, clock, c["session_key"])
    else:
        assert (
            s.export_checkpoint(db, clock, c["session_key"])["checkpoint"]["player"][
                "x"
            ]
            == text
        )


def test_reveal_immutable_identity_and_deleted_tombstone():
    db, clock = AtomicStore(), Clock()
    text = "a hidden original secret text longer than thirty two characters"
    c = s.create_session(
        db, clock, initial_state={"gm_notes": {"a/b": text}, "player": {"copy": text}}
    )
    k = c["session_key"]
    reveal = {
        "path": "/a~1b",
        "content_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "turn": "t1",
        "scene": "s1",
    }
    with pytest.raises(s.MiniError):
        save(db, clock, k, patch={"gm_notes": {"a/b": text + "x"}}, reveals=[reveal])
    r = save(db, clock, k, reveals=[reveal])
    assert r["revision"] == 1
    assert s.export_checkpoint(db, clock, k)["checkpoint"]["player"]["copy"] == text
    save(db, clock, k, 1, {"gm_notes": {"a/b": None}})
    doc = db.get(s.SESSIONS_COLLECTION, s.locate_key(k))
    entry = doc["gm_note_guard"]["entries"][0]
    assert entry["revealed"]
    assert entry["tombstoned"]
    assert entry["reveal_receipt"]["turn"] == "t1"


def test_image_profile_roundtrip_and_echo_guard():
    db, clock = AtomicStore(), Clock()
    text = "secret long sentence which must never be visible in a profile"
    profile = {"custom": {"scar": "left cheek"}, "unknown": [1, 2]}
    c = s.create_session(
        db,
        clock,
        initial_state={
            "player": {"image_descriptions": {"npc-1": profile}},
            "gm_notes": {"n": text},
        },
    )
    k = c["session_key"]
    assert s.get_image_description(db, clock, k, "npc-1")["profile"] == profile
    assert s.get_image_description(db, clock, k, "missing")["found"] is False
    with pytest.raises(s.MiniError, match="EXPORT_CONTAMINATION"):
        s.get_image_description(db, clock, k, text)


def test_helpers_preserve_supplied_fields_and_no_context_echo():
    from mvp_site.mini_mcp import supporting_tool

    assert "campaign_context" not in supporting_tool(
        "mini_get_playbook",
        {"topic": "start", "campaign_context": {"secret": "not echoed"}},
    )
    supplied = {
        "subject": "npc",
        "appearance": "violet alien",
        "setting": "tower",
        "composition": "portrait",
        "style": "ink",
        "avoid": ["armor"],
    }
    r = supporting_tool("mini_prepare_image_description", supplied)
    assert r["description_parts"] == supplied
    assert r["image_generated"] is False
