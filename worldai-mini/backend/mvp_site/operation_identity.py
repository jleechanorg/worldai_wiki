"""Shared identity helpers for client-supplied operation IDs and request binding."""

from __future__ import annotations

import hashlib
import json
import uuid
from collections.abc import Collection, Mapping
from typing import Any

# Server-admitted campaign creation control state; clients may never supply it.
RESERVED_CREATION_FIELDS: frozenset[str] = frozenset(
    {"creation_operation_id", "_creation_campaign_id"}
)


def has_reserved_creation_fields(arguments: Mapping[str, Any]) -> bool:
    return bool(RESERVED_CREATION_FIELDS & arguments.keys())


def canonical_operation_id(value: Any, field_name: str) -> str | None:
    """Return a lowercase canonical UUID, None when absent, or raise ValueError.

    Canonicalizing means case or hyphen variants cannot address different
    operation documents.
    """
    if value is None or value == "":
        return None
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a UUID string")
    try:
        return str(uuid.UUID(value))
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a UUID string") from exc


def request_fingerprint(
    request_body: Mapping[str, Any], route_kind: str, excluded_keys: Collection[str]
) -> str:
    """Bind the full client payload and route to one operation identity."""
    request = {k: v for k, v in request_body.items() if k not in excluded_keys}
    canonical = json.dumps(
        {"route_kind": route_kind, "request": request},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
