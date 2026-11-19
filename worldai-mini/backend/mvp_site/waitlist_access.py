"""Minimal token helpers used by Mini's optional recovery endpoints.

Standalone Mini does not install the host application's global clock-skew patch.
Firebase verifies signature, expiration, and revocation using the SDK.
"""


def parse_bearer_token(auth_header):
    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise ValueError("Invalid authorization scheme")
    token = parts[1].strip()
    if not token:
        raise ValueError("Empty token")
    return token


def verify_firebase_id_token(firebase_auth, id_token, *, check_revoked=True):
    return firebase_auth.verify_id_token(
        id_token, check_revoked=check_revoked, clock_skew_seconds=60
    )
