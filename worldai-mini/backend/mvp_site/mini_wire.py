"""Single production encoder for Mini admission and HTTP responses."""

import copy
import json

from mcp.types import CallToolResult, TextContent


def canonical(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def call_result(data=None, error=None):
    envelope = {"schema_version": "1", "ok": error is None}
    envelope["data" if error is None else "error"] = data if error is None else error
    visible = copy.deepcopy(envelope)
    if error is None:
        visible["data"].pop("gm_notes", None)
    return CallToolResult(
        content=[TextContent(type="text", text=canonical(visible))],
        structuredContent=envelope,
        isError=error is not None,
    ).model_dump(by_alias=True, exclude_none=True)


def rpc_result(result, request_id=0):
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def encode(value):
    return canonical(value).encode("utf-8")
