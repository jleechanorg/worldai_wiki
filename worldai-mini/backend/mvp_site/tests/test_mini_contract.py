"""Contract tests for the WorldAI Mini MCP tool definitions and state schema.

Task 1 of docs/superpowers/plans/2026-11-07-worldai-mini-mcp.md (roadmap repo):
define executable contracts before handlers. These tests bind the design's
normative API (design section 4, corrected by sections 11-13, which take
precedence per the 2026-11-08 amendments) to the committed schema artifacts:

- mvp_site/schemas/mini_tools.json        (tool inventory, IO schemas, annotations)
- mvp_site/schemas/mini_state.schema.json (session/state envelope + limits)

Design section 12 adds `mini_get_image_description`; the canonical inventory is
therefore EIGHT tools, superseding the historical seven-tool sample block in the
plan (amendment precedence notice at the top of both documents).
"""

import json
import pathlib
import re
import uuid

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMAS = REPO_ROOT / "mvp_site" / "schemas"

EXPECTED_TOOLS = {
    "mini_create_session",
    "mini_get_state",
    "mini_save_state",
    "mini_roll_dice",
    "mini_export_checkpoint",
    "mini_get_playbook",
    "mini_prepare_image_description",
    "mini_get_image_description",  # design section 12 (2026-11-08 amendment)
}

# Common error contract (design section 4), with EXPORT_CONTAMINATION added by
# design section 11 item 4 (normative precedence).
ERROR_CODES = {
    "INVALID_ARGUMENT",
    "SESSION_UNAVAILABLE",
    "REVISION_CONFLICT",
    "IDEMPOTENCY_CONFLICT",
    "CAPACITY_EXCEEDED",
    "RATE_LIMITED",
    "SERVICE_UNAVAILABLE",
    "EXPORT_CONTAMINATION",
}

# Serialized limits from design section 4 (UTF-8 byte counts).
LIMITS = {
    "player_bytes": 128 * 1024,
    "gm_notes_bytes": 32 * 1024,
    "recap_bytes": 16 * 1024,
    "guard_ledger_bytes": 64 * 1024,
    "session_document_bytes": 512 * 1024,
    "request_body_bytes": 256 * 1024,
    "response_body_bytes": 1024 * 1024,
    "max_json_depth": 24,
    "max_roll_receipts": 200,
    "title_max_chars": 120,
    "purpose_max_chars": 240,
}

SESSION_KEY_PATTERN = re.compile(r"^mini_[A-Za-z0-9_-]{32}$")  # 192-bit base64url


def load_tools():
    path = SCHEMAS / "mini_tools.json"
    assert path.is_file(), "mvp_site/schemas/mini_tools.json must exist"
    return json.loads(path.read_text(encoding="utf-8"))


def load_state_schema():
    path = SCHEMAS / "mini_state.schema.json"
    assert path.is_file(), "mvp_site/schemas/mini_state.schema.json must exist"
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def tools_doc():
    return load_tools()


@pytest.fixture(scope="module")
def tools(tools_doc):
    return {tool["name"]: tool for tool in tools_doc["tools"]}


@pytest.fixture(scope="module")
def state_schema():
    return load_state_schema()


class TestToolInventory:
    def test_exact_tool_names(self, tools):
        assert set(tools) == EXPECTED_TOOLS

    def test_unique_names(self, tools_doc):
        names = [tool["name"] for tool in tools_doc["tools"]]
        assert len(names) == len(set(names))

    def test_all_names_mini_prefixed(self, tools):
        for name in tools:
            assert name.startswith("mini_")
        assert "roll_dice" not in tools  # legacy test-only tool, never registered

    def test_schema_version_is_one(self, tools_doc):
        assert str(tools_doc["schema_version"]) == "1"

    def test_error_code_enum_complete(self, tools_doc):
        declared = set(tools_doc["error_codes"])
        assert declared == ERROR_CODES


class TestPerToolContracts:
    def test_create_session_inputs(self, tools):
        schema = tools["mini_create_session"]["inputSchema"]
        assert "initial_state" in schema["required"]
        props = schema["properties"]
        assert props["initial_state"]["type"] == "object"
        assert props["title"]["maxLength"] == LIMITS["title_max_chars"]

    def test_stateful_tools_require_session_key_except_creation(self, tools):
        for name, tool in tools.items():
            if name in ("mini_create_session", "mini_get_playbook",
                        "mini_prepare_image_description"):
                continue
            assert "session_key" in tool["inputSchema"]["required"], name

    def test_save_and_roll_require_revision_and_operation_id(self, tools):
        for name in ("mini_save_state", "mini_roll_dice"):
            required = tools[name]["inputSchema"]["required"]
            assert "expected_revision" in required, name
            assert "operation_id" in required, name

    def test_unknown_control_fields_rejected(self, tools):
        for name, tool in tools.items():
            schema = tool["inputSchema"]
            assert schema.get("additionalProperties") is False, name

    def test_model_owned_containers_extensible(self, state_schema):
        # additionalProperties:false applies only to control objects; the
        # model-owned domain containers preserve unknown keys.
        containers = state_schema["properties"]["state"]["properties"]
        for container in ("player", "gm_notes"):
            assert containers[container]["type"] == "object"
            assert containers[container].get("additionalProperties") is not False
        assert containers["recap"]["type"] == "string"

    def test_expected_revision_is_nonnegative_integer(self, tools):
        for name in ("mini_save_state", "mini_roll_dice"):
            prop = tools[name]["inputSchema"]["properties"]["expected_revision"]
            assert prop["type"] == "integer"
            assert prop.get("minimum", 0) >= 0

    def test_operation_id_is_uuid_format(self, tools):
        for name in ("mini_save_state", "mini_roll_dice"):
            prop = tools[name]["inputSchema"]["properties"]["operation_id"]
            assert prop.get("format") == "uuid"
            # spot-check the declared pattern accepts real UUIDs
            sample = str(uuid.uuid4())
            if "pattern" in prop:
                assert re.match(prop["pattern"], sample), name

    def test_roll_dice_mode_enum(self, tools):
        mode = tools["mini_roll_dice"]["inputSchema"]["properties"]["mode"]
        assert set(mode["enum"]) == {"normal", "advantage", "disadvantage"}

    def test_playbook_topic_enum(self, tools):
        topic = tools["mini_get_playbook"]["inputSchema"]["properties"]["topic"]
        assert set(topic["enum"]) == {
            "start", "continue", "character", "rules", "checkpoint", "image"}

    def test_image_description_tool_contract(self, tools):
        # design section 12: read-only, idempotent; response carries
        # session_id, revision, character_id, found and profile.
        tool = tools["mini_get_image_description"]
        required = tool["inputSchema"]["required"]
        assert "session_key" in required
        assert "character_id" in required
        out = tool["outputSchema"]["properties"]["data"]["properties"]
        for field in ("session_id", "revision", "character_id", "found", "profile"):
            assert field in out, field
        assert tool["annotations"]["readOnlyHint"] is True
        assert tool["annotations"]["idempotentHint"] is True


class TestAnnotations:
    READ_ONLY = {"mini_get_state", "mini_export_checkpoint", "mini_get_playbook",
                 "mini_prepare_image_description", "mini_get_image_description"}
    IDEMPOTENT_MUTATIONS = {"mini_save_state", "mini_roll_dice"}

    def test_read_only_hints(self, tools):
        for name in self.READ_ONLY:
            assert tools[name]["annotations"]["readOnlyHint"] is True, name

    def test_mutations_not_read_only(self, tools):
        for name in {"mini_create_session"} | self.IDEMPOTENT_MUTATIONS:
            assert tools[name]["annotations"]["readOnlyHint"] is False, name

    def test_idempotent_hints(self, tools):
        for name in self.IDEMPOTENT_MUTATIONS | self.READ_ONLY:
            assert tools[name]["annotations"]["idempotentHint"] is True, name
        assert tools["mini_create_session"]["annotations"]["idempotentHint"] is False

    def test_save_state_destructive_hint(self, tools):
        # design section 13: RFC7396 explicitly permits deleting keys, so
        # mini_save_state must advertise destructiveHint:true.
        assert tools["mini_save_state"]["annotations"]["destructiveHint"] is True

    def test_open_world_hint_closed(self, tools):
        for name, tool in tools.items():
            assert tool["annotations"]["openWorldHint"] is False, name


class TestResultEnvelope:
    def test_discriminated_union(self, tools_doc):
        result = tools_doc["result_schema"]
        assert "ok" in result["required"]
        assert result["properties"]["ok"]["type"] == "boolean"
        # ok:true carries data, ok:false carries error
        assert "data" in result["properties"]
        error = result["properties"]["error"]["properties"]
        assert "code" in error
        assert error["code"]["enum"] == sorted(ERROR_CODES) or \
            set(error["code"]["enum"]) == ERROR_CODES

    def test_error_payload_options(self, tools_doc):
        error = tools_doc["result_schema"]["properties"]["error"]["properties"]
        assert "current_revision" in error          # revision conflicts
        assert "retry_after_seconds" in error       # throttling
        assert "outcome_unknown" in error           # uncertain writes

    def test_every_structured_tool_declares_output_schema(self, tools):
        # strict SDK clients reject structured data without outputSchema
        for name, tool in tools.items():
            assert "outputSchema" in tool, name

    def test_gm_notes_only_in_structured_output(self, tools):
        # spoiler boundary: gm_notes may appear only in structuredContent
        # output, never in the text projection contract.
        data = tools["mini_get_state"]["outputSchema"]["properties"]["data"]["properties"]
        assert "gm_notes" in data["state"]["properties"]
        projection = tools["mini_get_state"]["text_projection"]["properties"]
        assert "gm_notes" not in projection["state"]["properties"]
        for field in ("session_id", "revision", "state", "expires_at"):
            assert field in projection, field


class TestSizeBudget:
    """Worst-case serialized get-state/export results must fit 1 MiB after
    text/structuredContent duplication (design section 4 + plan Task 1.1)."""

    def _worst_case_result_bytes(self, limits):
        visible = limits["player_bytes"] + limits["recap_bytes"]
        structured = visible + limits["gm_notes_bytes"]
        # text channel carries the visible projection JSON-encoded as a string
        # (escaping doubles the bound in the worst case), structured carries full.
        worst_roll_history = limits["max_roll_receipts"] * 512  # bounded receipt
        envelope = 16 * 1024
        return 2 * visible + structured + worst_roll_history + envelope

    def test_get_state_result_fits_response_cap(self):
        assert self._worst_case_result_bytes(LIMITS) <= LIMITS["response_body_bytes"]

    def test_limits_present_in_state_schema(self, state_schema):
        declared = state_schema["limits"]
        for key, value in LIMITS.items():
            assert declared[key] == value, key

    def test_session_document_cap_exceeds_container_sum(self):
        containers = (LIMITS["player_bytes"] + LIMITS["gm_notes_bytes"]
                      + LIMITS["recap_bytes"] + LIMITS["guard_ledger_bytes"])
        assert containers <= LIMITS["session_document_bytes"]

    def test_worst_case_strings_validate_as_utf8(self):
        # quote, slash, newline and Unicode stress strings must round-trip
        # through JSON serialization unchanged (encoder parity for budgeting).
        stress = ['"', "\\", "\n", "emoji 🎲 and cjk 漢字", "a" * 1024]
        for s in stress:
            assert json.loads(json.dumps(s)) == s


class TestSessionKeyContract:
    def test_pattern_matches_spec(self):
        # server-generated 192-bit base64url capability, mini_ prefix
        assert SESSION_KEY_PATTERN.match("mini_" + "A" * 32)
        assert not SESSION_KEY_PATTERN.match("mini_short")
        assert not SESSION_KEY_PATTERN.match("noprefix_" + "A" * 32)

    def test_state_schema_declares_key_pattern(self, state_schema):
        assert state_schema["session_key_pattern"] == SESSION_KEY_PATTERN.pattern

    def test_document_key_is_hashed_capability(self, state_schema):
        # Firestore document key is SHA256(session_key); raw capability never stored
        assert state_schema["document_key"] == "SHA256(session_key)"

class TestAmendedContracts:
    def test_result_union_rejects_missing_or_mixed_branches(self, tools_doc):
        validate = Draft202012Validator(tools_doc['result_schema']).is_valid
        assert validate({'schema_version': '1', 'ok': True, 'data': {}})
        error = {'code': 'INVALID_ARGUMENT', 'message': 'invalid'}
        assert validate({'schema_version': '1', 'ok': False, 'error': error})
        for value in [
            {'schema_version': '1', 'ok': True},
            {'schema_version': '1', 'ok': False},
            {'schema_version': '1', 'ok': True, 'data': {}, 'error': error},
            {'schema_version': '1', 'ok': False, 'data': {}, 'error': error},
        ]:
            assert not validate(value), value

    def test_save_reveals_are_bounded_control_entries(self, tools):
        validate = Draft202012Validator(tools['mini_save_state']['inputSchema']).is_valid
        base = {'session_key': 'mini_' + 'A' * 32, 'expected_revision': 0,
                'operation_id': str(uuid.uuid4()), 'patch': {}}
        entry = {'path': '/secret', 'content_sha256': 'a' * 64, 'turn': '1', 'scene': 'harbor'}
        assert validate({**base, 'reveals': [entry]})
        assert not validate({**base, 'reveals': [entry] * 33})
        for wrong in ({**entry, 'turn': ''}, {**entry, 'scene': 'a' * 121},
                      {**entry, 'content_sha256': 'A' * 64}, {**entry, 'extra': True}):
            assert not validate({**base, 'reveals': [wrong]})

    def test_playbook_does_not_advertise_context_echo(self, tools):
        out = tools['mini_get_playbook']['outputSchema']['properties']['data']
        assert 'campaign_context' not in out['properties']
        assert out['additionalProperties'] is False

    def test_character_id_bounds(self, tools):
        validate = Draft202012Validator(tools['mini_get_image_description']['inputSchema']).is_valid
        base = {'session_key': 'mini_' + 'A' * 32}
        assert validate({**base, 'character_id': 'x'})
        assert validate({**base, 'character_id': 'x' * 120})
        assert not validate({**base, 'character_id': ''})
        assert not validate({**base, 'character_id': 'x' * 121})
