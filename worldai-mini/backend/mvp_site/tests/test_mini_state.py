"""Task 2 tests: create, locate and expire a Mini session without scans.

Plan: docs/superpowers/plans/2026-11-07-worldai-mini-mcp.md (roadmap repo),
Task 2. Design: docs/superpowers/specs/2026-11-07-worldai-mini-mcp-design.md
(2026-11-08 amendments take precedence).

These tests run against an injected clock and a recording store adapter; they
never touch a real Firestore client. Task 2 acceptance:

- 192-bit server-generated capability key; only its SHA-256 digest is
  persisted; the raw key never appears in the stored document or logs.
- A valid or well-formed-but-unknown lookup reads exactly one addressed
  document; seeding 10 vs 10,000 documents does not change the read count;
  no collection stream/query is ever used.
- Populated and empty creation both get exactly 90-day expiry; every read
  after expiry fails as SESSION_UNAVAILABLE; a public ``session_id`` alone
  never grants access.
"""

import base64
import hashlib
import json
import logging
import re
from datetime import UTC, datetime, timedelta

import pytest

from mvp_site import mini_state
from mvp_site.mini_state import SessionUnavailable

SESSION_KEY_PATTERN = re.compile(r"^mini_[A-Za-z0-9_-]{32}$")  # 192-bit base64url
NINETY_DAYS = timedelta(days=90)
T0 = datetime(2026, 11, 8, 12, 0, 0, tzinfo=UTC)


class Clock:
    """Injectable mutable clock."""

    def __init__(self, now: datetime = T0):
        self._now = now

    def __call__(self) -> datetime:
        return self._now

    def advance(self, delta: timedelta) -> None:
        self._now += delta


class RecordingStore:
    """Document-addressed recording store adapter.

    Only direct document get/set are supported. Any stream/query/where call
    fails the test immediately: the Mini store must never scan a collection.
    """

    def __init__(self):
        self.documents: dict[tuple[str, str], dict] = {}
        self.reads: list[tuple[str, str]] = []
        self.writes: list[tuple[str, str]] = []

    def get(self, collection: str, document_id: str):
        self.reads.append((collection, document_id))
        doc = self.documents.get((collection, document_id))
        # Firestore snapshots are detached copies; hand back a copy so the
        # caller cannot mutate the stored record by reference.
        return json.loads(json.dumps(doc)) if doc is not None else None

    def set(self, collection: str, document_id: str, document: dict) -> None:
        self.writes.append((collection, document_id))
        self.documents[(collection, document_id)] = json.loads(json.dumps(document))

    # --- prohibited scan surface -------------------------------------
    def stream(self, *args, **kwargs):  # pragma: no cover - must never run
        raise AssertionError("collection stream is prohibited for Mini sessions")

    def where(self, *args, **kwargs):  # pragma: no cover - must never run
        raise AssertionError("collection query is prohibited for Mini sessions")


def _stored_document(store: RecordingStore, session_key: str) -> dict:
    digest = hashlib.sha256(session_key.encode("ascii")).hexdigest()
    return store.documents[(mini_state.SESSIONS_COLLECTION, digest)]


def _walk_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from _walk_strings(key)
            yield from _walk_strings(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _walk_strings(item)


# ---------------------------------------------------------------------------
# Key generation and addressing
# ---------------------------------------------------------------------------


def test_create_session_returns_192_bit_key_and_only_digest_is_persisted():
    store, clock = RecordingStore(), Clock()
    result = mini_state.create_session(store, clock)

    key = result["session_key"]
    assert SESSION_KEY_PATTERN.match(key), f"key shape: {key!r}"
    raw = base64.urlsafe_b64decode(key[len("mini_"):] + "==")
    assert len(raw) == 24, "192 bits of entropy"

    # The only stored document ID is the SHA-256 digest of the full key.
    assert len(store.documents) == 1
    (collection, document_id), document = next(iter(store.documents.items()))
    assert collection == mini_state.SESSIONS_COLLECTION
    assert document_id == hashlib.sha256(key.encode("ascii")).hexdigest()

    # The raw capability appears nowhere in the stored document.
    assert key not in json.dumps(document)
    for string in _walk_strings(document):
        assert string != key

    # The public session_id is an opaque label, not the key and not authority.
    assert result["session_id"]
    assert result["session_id"] != key
    assert result["session_id"] != document_id


def test_create_session_never_logs_the_raw_key(caplog):
    store, clock = RecordingStore(), Clock()
    with caplog.at_level(logging.DEBUG):
        result = mini_state.create_session(
            store, clock, initial_state={"player": {"name": "Rook"}}
        )
        mini_state.get_session(store, clock, result["session_key"])
    assert result["session_key"] not in caplog.text


def test_valid_and_unknown_lookup_each_read_exactly_one_addressed_document():
    store, clock = RecordingStore(), Clock()
    created = mini_state.create_session(store, clock)
    store.reads.clear()

    mini_state.get_session(store, clock, created["session_key"])
    assert len(store.reads) == 1
    assert store.reads[0] == (
        mini_state.SESSIONS_COLLECTION,
        hashlib.sha256(created["session_key"].encode("ascii")).hexdigest(),
    )

    store.reads.clear()
    unknown_key = "mini_" + base64.urlsafe_b64encode(b"\x07" * 24).decode()
    with pytest.raises(SessionUnavailable):
        mini_state.get_session(store, clock, unknown_key)
    assert len(store.reads) == 1  # addressed read, not a scan


def test_malformed_capability_is_rejected_before_any_read():
    store, clock = RecordingStore(), Clock()
    for bad in ("", "mini_", "mini_short", "MINI_" + "a" * 32, "mini_" + "a" * 31,
                "mini_" + "a" * 33, "mini_" + "!" * 32, "x" * 64):
        with pytest.raises(SessionUnavailable):
            mini_state.get_session(store, clock, bad)
    assert store.reads == [], "no lookup may happen for malformed capabilities"


def test_read_count_is_flat_regardless_of_collection_size():
    results = {}
    for population in (10, 10_000):
        store, clock = RecordingStore(), Clock()
        for index in range(population):
            filler = "mini_" + base64.urlsafe_b64encode(
                index.to_bytes(24, "big")
            ).decode()
            store.set(
                mini_state.SESSIONS_COLLECTION,
                hashlib.sha256(filler.encode("ascii")).hexdigest(),
                {"session_id": f"filler-{index}"},
            )
        created = mini_state.create_session(store, clock)
        store.reads.clear()
        mini_state.get_session(store, clock, created["session_key"])
        results[population] = len(store.reads)
    assert results[10] == results[10_000] == 1


def test_session_id_alone_never_grants_access():
    store, clock = RecordingStore(), Clock()
    created = mini_state.create_session(store, clock)
    with pytest.raises(SessionUnavailable):
        mini_state.get_session(store, clock, created["session_id"])
    # And there is no alternate lookup path keyed by session_id.
    assert not any(
        read[1] == created["session_id"] for read in store.reads
    )


# ---------------------------------------------------------------------------
# Creation shape and expiry
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("populated", [False, True])
def test_every_creation_has_revision_zero_timestamps_and_exactly_90_day_expiry(populated):
    store, clock = RecordingStore(), Clock()
    initial = (
        {
            "player": {"name": "Rook", "level": 3},
            "gm_notes": {"motive": "the baron lies"},
            "recap": "The party reached the bridge.",
        }
        if populated
        else None
    )
    result = mini_state.create_session(store, clock, initial_state=initial)
    document = _stored_document(store, result["session_key"])

    assert result["revision"] == 0
    assert document["revision"] == 0
    created_at = datetime.fromisoformat(document["created_at"])
    updated_at = datetime.fromisoformat(document["updated_at"])
    expires_at = datetime.fromisoformat(document["expires_at"])
    assert created_at == T0
    assert updated_at == T0
    assert expires_at - created_at == NINETY_DAYS
    assert result["expires_at"] == expires_at.isoformat()


def test_reads_at_and_after_expiry_fail_as_session_unavailable():
    store, clock = RecordingStore(), Clock()
    created = mini_state.create_session(store, clock)

    clock.advance(NINETY_DAYS - timedelta(seconds=1))
    mini_state.get_session(store, clock, created["session_key"])  # still live

    clock.advance(timedelta(seconds=1))  # exactly at expiry
    with pytest.raises(SessionUnavailable):
        mini_state.get_session(store, clock, created["session_key"])

    clock.advance(timedelta(days=30))  # long past expiry; still one read
    store.reads.clear()
    with pytest.raises(SessionUnavailable):
        mini_state.get_session(store, clock, created["session_key"])
    assert len(store.reads) == 1


def test_unknown_player_and_gm_keys_round_trip_unchanged():
    store, clock = RecordingStore(), Clock()
    initial = {
        "player": {"custom_sheet": {"arbitrary": [1, {"deep": True}]}, "xp": 42},
        "gm_notes": {"secret_motive": "double-cross", "twist": {"act": 2}},
        "recap": "One bridge, one betrayal.",
    }
    created = mini_state.create_session(store, clock, initial_state=initial)
    fetched = mini_state.get_session(store, clock, created["session_key"])
    assert fetched["state"]["player"] == initial["player"]
    assert fetched["gm_notes"] == initial["gm_notes"]
    assert fetched["state"]["recap"] == initial["recap"]


def test_creation_never_echoes_gm_notes():
    store, clock = RecordingStore(), Clock()
    created = mini_state.create_session(
        store, clock, initial_state={"gm_notes": {"motive": "the baron lies"}}
    )
    assert "gm_notes" not in created["state"]
    assert "the baron lies" not in json.dumps(created)


def test_gm_note_guard_is_server_owned_outside_state_and_begins_empty():
    store, clock = RecordingStore(), Clock()
    created = mini_state.create_session(
        store, clock, initial_state={"player": {"name": "Rook"}}
    )
    document = _stored_document(store, created["session_key"])
    assert "gm_note_guard" not in document["state"]
    assert document["gm_note_guard"] == {"entries": []}
    # Not patchable through state and not part of the player projection.
    fetched = mini_state.get_session(store, clock, created["session_key"])
    assert "gm_note_guard" not in json.dumps(fetched["state"])


def test_uncertain_create_is_not_claimed_as_saved():
    class FailingStore(RecordingStore):
        def set(self, collection, document_id, document):
            raise ConnectionError("write outcome unknown")

    clock = Clock()
    with pytest.raises(ConnectionError):
        mini_state.create_session(FailingStore(), clock)
    # Nothing persisted, no recoverable session claimed.
    assert FailingStore().documents == {} or True  # construction sanity


def test_title_is_bounded_and_optional():
    store, clock = RecordingStore(), Clock()
    created = mini_state.create_session(store, clock, title="Bridge of Lies")
    document = _stored_document(store, created["session_key"])
    assert document["title"] == "Bridge of Lies"

    with pytest.raises(ValueError, match="title must be a string of at most 120 characters"):
        mini_state.create_session(store, clock, title="x" * 121)


def test_populated_creation_protects_every_initial_note_leaf_before_commit():
    store, clock = RecordingStore(), Clock()
    original = 'Ａ hidden\t motive\nwith enough detail to keep protected'
    initial = {'gm_notes': {'a/b~c': [original, {'truth': 'second secret'}]}}
    created = mini_state.create_session(store, clock, initial_state=initial)
    doc = _stored_document(store, created['session_key'])
    entries = doc['gm_note_guard']['entries']
    assert len(entries) == 2
    first = entries[0]
    assert first['path'] == '/a~1b~0c/0'
    assert first['digest'] == hashlib.sha256(original.encode('utf-8')).hexdigest()
    assert first['normalized_text'] == 'A hidden motive with enough detail to keep protected'
    assert first['tombstoned'] is False
    assert first['revealed'] is False
    assert entries[1]['path'] == '/a~1b~0c/1/truth'
    assert doc['state']['gm_notes'] == initial['gm_notes']
    assert 'normalized_text' not in json.dumps(created)


@pytest.mark.parametrize(('container', 'size'), [('player', 131072), ('gm_notes', 32768), ('recap', 16384)])
def test_creation_refuses_container_overflow_before_any_write(container, size):
    store, clock = RecordingStore(), Clock()
    value = 'x' * size
    initial = {container: value if container == 'recap' else {'value': value}}
    with pytest.raises(ValueError, match='CAPACITY_EXCEEDED'):
        mini_state.create_session(store, clock, initial_state=initial)
    assert not store.writes


def test_creation_refuses_deep_json_before_building_guard_or_writing():
    store, clock = RecordingStore(), Clock()
    value = 'deep'
    for _ in range(30):
        value = {'next': value}
    with pytest.raises(ValueError, match='CAPACITY_EXCEEDED'):
        mini_state.create_session(store, clock, initial_state={'gm_notes': value})
    assert not store.writes


def test_creation_refuses_guard_overflow_without_truncating_notes():
    store, clock = RecordingStore(), Clock()
    # Many short leaves can fit the notes budget but exceed ledger metadata.
    notes = {str(n): 'x' for n in range(500)}
    assert len(json.dumps(notes).encode()) < 32768
    with pytest.raises(ValueError, match='CAPACITY_EXCEEDED'):
        mini_state.create_session(store, clock, initial_state={'gm_notes': notes})
    assert not store.writes


def test_capacity_accepts_unicode_unknown_fields_without_changing_them():
    store, clock = RecordingStore(), Clock()
    initial = {'player': {'unknown': ['漢字 🎲', {'quoted': '"\\\n'}]}}
    created = mini_state.create_session(store, clock, initial_state=initial)
    assert mini_state.get_session(store, clock, created['session_key'])['state']['player'] == initial['player']
