"""Standalone recovery preserves verified-token and revocation checks."""

import pytest

from mvp_site.waitlist_access import parse_bearer_token, verify_firebase_id_token


def test_token_verification_checks_revocation_and_limits_clock_skew():
    class Auth:
        def verify_id_token(self, token, *, check_revoked, clock_skew_seconds):
            assert token == "synthetic-token"
            assert check_revoked is True
            assert clock_skew_seconds == 60
            return {"uid": "synthetic-user", "email_verified": True}

    assert verify_firebase_id_token(Auth(), "synthetic-token")["email_verified"] is True


@pytest.mark.parametrize("header", ["", "token", "Basic x", "Bearer", "Bearer a b"])
def test_invalid_bearer_headers_are_rejected(header):
    with pytest.raises(ValueError):
        parse_bearer_token(header)
