"""Optional verified-account recovery, isolated from anonymous MCP authority."""

from __future__ import annotations

import hashlib
import logging
from datetime import UTC, datetime

from firebase_admin import auth
from flask import jsonify, request

from mvp_site import mini_state as state
from mvp_site.waitlist_access import parse_bearer_token, verify_firebase_id_token

OWNERS = "mini_recovery_owners"
MAX_LINKS = 100


def _owner_key(uid):
    return hashlib.sha256(uid.encode()).hexdigest()


def link_session(store, clock, uid, email, session_key):
    now = clock()
    digest = state.locate_key(session_key)
    owner_key = _owner_key(uid)

    def commit(tx):
        doc = state.require_live(tx.get(state.SESSIONS_COLLECTION, digest), now)
        owner = tx.get(OWNERS, owner_key) or {"sessions": {}}
        if doc.get("recovery_owner") not in (None, owner_key):
            raise state.MiniError("INVALID_ARGUMENT")
        sessions = owner["sessions"]
        if doc["session_id"] not in sessions and len(sessions) >= MAX_LINKS:
            raise state.MiniError("CAPACITY_EXCEEDED")
        sessions[doc["session_id"]] = {
            "digest": digest,
            "title": doc.get("title"),
            "linked_at": now.isoformat(),
        }
        owner.update(email=email, email_verified=True, consented_at=now.isoformat())
        doc["recovery_owner"] = owner_key
        tx.set(state.SESSIONS_COLLECTION, digest, doc)
        tx.set(OWNERS, owner_key, owner)
        return {"session_id": doc["session_id"], "linked": True}

    return store.transaction(commit)


def list_sessions(store, _clock, uid):
    owner = store.get(OWNERS, _owner_key(uid)) or {"sessions": {}}
    return [
        {"session_id": sid, "title": entry.get("title")}
        for sid, entry in owner["sessions"].items()
    ]


def recover_session(store, clock, uid, session_id):
    now = clock()
    owner_key = _owner_key(uid)
    # Generated only inside server memory; only the digest is persisted.
    key = state._generate_session_key()
    new_digest = state.locate_key(key)

    def commit(tx):
        owner = tx.get(OWNERS, owner_key)
        if not owner or session_id not in owner["sessions"]:
            raise state.SessionUnavailable()
        entry = owner["sessions"][session_id]
        old_digest = entry["digest"]
        doc = state.require_live(tx.get(state.SESSIONS_COLLECTION, old_digest), now)
        if doc.get("recovery_owner") != owner_key:
            raise state.SessionUnavailable()
        doc["operation_namespace"] = doc.get("operation_namespace", old_digest)
        # Expiring old envelope revokes it without deleting campaigns or receipts.
        revoked = {"expires_at": now.isoformat(), "recovered": True}
        entry["digest"] = new_digest
        tx.set(state.SESSIONS_COLLECTION, old_digest, revoked)
        tx.set(state.SESSIONS_COLLECTION, new_digest, doc)
        tx.set(OWNERS, owner_key, owner)
        return {
            "session_id": session_id,
            "session_key": key,
            "revision": doc["revision"],
            "expires_at": doc["expires_at"],
        }

    return store.transaction(commit)


def remove_recovery(store, _clock, uid):
    """Forget consented email/index; do not delete campaigns or revoke play keys."""
    owner_key = _owner_key(uid)

    def commit(tx):
        owner = tx.get(OWNERS, owner_key) or {"sessions": {}}
        # Read every envelope before queueing writes for Firestore transactions.
        documents = [
            (entry["digest"], tx.get(state.SESSIONS_COLLECTION, entry["digest"]))
            for entry in owner["sessions"].values()
        ]
        for digest, doc in documents:
            if doc and doc.get("recovery_owner") == owner_key:
                doc.pop("recovery_owner")
                tx.set(state.SESSIONS_COLLECTION, digest, doc)
        # Empty pseudonymous control record retains no email, consent or links.
        tx.set(OWNERS, owner_key, {"sessions": {}})
        return {"removed": True}

    return store.transaction(commit)


def verified_claims():
    claims = verify_firebase_id_token(
        auth, parse_bearer_token(request.headers.get("Authorization", ""))
    )
    if (
        not isinstance(claims.get("uid"), str)
        or not claims["uid"]
        or len(claims["uid"]) > 128
        or claims.get("email_verified") is not True
        or not isinstance(claims.get("email"), str)
        or not claims["email"]
        or len(claims["email"]) > 320
    ):
        raise ValueError("Verified email required")
    return claims


def register_routes(app, store_factory, clock=None, claims_verifier=verified_claims):
    clock = clock or (lambda: datetime.now(UTC))

    def safe_emit(event):
        from mvp_site.mini_mcp import emit

        try:
            emit(event)
        except Exception:
            logging.getLogger(__name__).warning("mini_recovery_telemetry_dropped")

    @app.after_request
    def recovery_telemetry(response):
        if request.path.startswith("/api/mini-recovery/"):
            safe_emit(
                {
                    "source": "mini_recovery",
                    "outcome": "ok" if response.status_code < 400 else "rejected",
                    "status": response.status_code,
                }
            )
            response.headers["Cache-Control"] = "no-store"
            response.headers["Referrer-Policy"] = "no-referrer"
        return response

    @app.route("/api/mini-recovery/<action>", methods=["POST"])
    def recovery_endpoint(action):  # noqa: PLR0911, PLR0912 - explicit auth/action matrix
        from mvp_site.mini_mcp import admit, safe_error

        try:
            store = store_factory()
            admit(store, clock(), request.remote_addr or "unknown")
        except Exception as exc:
            error = safe_error(exc)
            return jsonify({"error": error["code"]}), 429 if error[
                "code"
            ] == "RATE_LIMITED" else 503
        try:
            claims = claims_verifier()
        except Exception:
            return jsonify({"error": "VERIFIED_SIGN_IN_REQUIRED"}), 401
        if request.content_length and request.content_length > 4096:
            return jsonify({"error": "INVALID_ARGUMENT"}), 413
        if request.mimetype != "application/json":
            return jsonify({"error": "INVALID_ARGUMENT"}), 415
        if len(request.get_data(cache=True)) > 4096:
            return jsonify({"error": "INVALID_ARGUMENT"}), 413
        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return jsonify({"error": "INVALID_ARGUMENT"}), 400
        allowed = {
            "list": set(),
            "remove": set(),
            "link": {"session_key", "consent"},
            "recover": {"session_id"},
        }
        if action not in allowed or set(body) != allowed[action]:
            return jsonify({"error": "INVALID_ARGUMENT"}), 400
        try:
            if action == "list":
                result = {"sessions": list_sessions(store, clock, claims["uid"])}
            elif action == "remove":
                result = remove_recovery(store, clock, claims["uid"])
            elif action == "link":
                if body["consent"] is not True:
                    raise ValueError("Consent required")
                result = link_session(
                    store, clock, claims["uid"], claims["email"], body["session_key"]
                )
            else:
                if (
                    not isinstance(body["session_id"], str)
                    or len(body["session_id"]) != 32
                ):
                    raise ValueError("Invalid label")
                result = recover_session(
                    store, clock, claims["uid"], body["session_id"]
                )
            response = jsonify(result)
            response.headers["Cache-Control"] = "no-store"
            response.headers["Referrer-Policy"] = "no-referrer"
            return response
        except state.SessionUnavailable:
            return jsonify({"error": "SESSION_UNAVAILABLE"}), 404
        except (state.MiniError, ValueError, TypeError):
            return jsonify({"error": "REQUEST_REJECTED"}), 400
        except Exception:
            return jsonify({"error": "SERVICE_UNAVAILABLE"}), 503
