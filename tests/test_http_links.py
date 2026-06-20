"""Tests for the HTTP link checker.

Unit tests use mock HTTP to avoid network calls in the fast test suite.
The integration test (marked slow) actually hits github.com and is run only
on push-to-main in CI via the `http-links` workflow job.
"""
from __future__ import annotations

import re
import subprocess
import sys
import unittest.mock as mock
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
CHECK_SCRIPT = REPO_ROOT / "scripts" / "check_http_links.py"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from check_http_links import (  # noqa: E402
    _collect_links,
    _check_url,
    _is_ok,
    _strip_code_blocks,
    GITHUB_BLOB_BASE,
)


# ── helpers ──────────────────────────────────────────────────────────────────

def _make_wiki(tmp_path: Path, files: dict[str, str]) -> Path:
    root = tmp_path / "wiki"
    for rel, content in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    return root


# ── unit tests ───────────────────────────────────────────────────────────────

def test_is_ok_2xx():
    assert _is_ok(200)
    assert _is_ok(204)
    assert _is_ok(301)
    assert _is_ok(302)


def test_is_ok_4xx_5xx():
    assert not _is_ok(404)
    assert not _is_ok(500)
    assert not _is_ok(None)


def test_strip_code_blocks_masks_urls():
    text = "Real link https://example.com/real and `https://example.com/code`."
    masked = _strip_code_blocks(text)
    assert "https://example.com/real" in masked
    assert "https://example.com/code" not in masked


def test_collect_links_finds_external_urls(tmp_path: Path):
    root = _make_wiki(tmp_path, {
        "concepts/Foo.md": (
            "---\ntitle: Foo\ncreated: 2026-06-20\nupdated: 2026-06-20\n"
            "type: concept\ntags: []\n---\n\n"
            "See https://openai.com and https://anthropic.com for details.\n"
        ),
    })
    links = _collect_links(root)
    assert "https://openai.com" in links
    assert "https://anthropic.com" in links


def test_collect_links_skips_code_fence_urls(tmp_path: Path):
    root = _make_wiki(tmp_path, {
        "concepts/Foo.md": (
            "---\ntitle: Foo\ncreated: 2026-06-20\nupdated: 2026-06-20\n"
            "type: concept\ntags: []\n---\n\n"
            "```\nhttps://example-in-code.com/should-be-skipped\n```\n"
        ),
    })
    links = _collect_links(root)
    # localhost/example.com are in SKIP_PATTERNS but the code-fence should
    # strip it before patterns even run.  Confirm neither appears.
    assert not any("example-in-code" in u for u in links)


def test_collect_links_converts_relative_md_to_github_blob(tmp_path: Path):
    root = _make_wiki(tmp_path, {
        "concepts/Combat.md": (
            "---\ntitle: Combat\ncreated: 2026-06-20\nupdated: 2026-06-20\n"
            "type: concept\ntags: []\n---\n\n"
            "Uses [Dice](Dice.md) rolling.\n"
        ),
        "concepts/Dice.md": (
            "---\ntitle: Dice\ncreated: 2026-06-20\nupdated: 2026-06-20\n"
            "type: concept\ntags: []\n---\n\n"
            "Dice are random.\n"
        ),
    })
    links = _collect_links(root)
    expected = f"{GITHUB_BLOB_BASE}/concepts/Dice.md"
    assert expected in links, f"Expected {expected} in collected links. Got: {list(links)[:5]}"


def test_check_url_ok(monkeypatch):
    """_check_url returns the HTTP status from the server."""
    class FakeResp:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *a): pass

    with mock.patch("urllib.request.urlopen", return_value=FakeResp()):
        url, status, err = _check_url("https://github.com/jleechanorg/worldai_wiki")
    assert status == 200
    assert err == ""


def test_check_url_404(monkeypatch):
    import urllib.error
    with mock.patch(
        "urllib.request.urlopen",
        side_effect=urllib.error.HTTPError(
            "https://github.com/404", 404, "Not Found", {}, None
        ),
    ):
        url, status, err = _check_url("https://github.com/404")
    assert status == 404


def test_check_url_405_falls_back_to_get(monkeypatch):
    """If HEAD returns 405, _check_url retries with GET."""
    import urllib.error

    call_count = {"n": 0}

    class FakeResp:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *a): pass

    def side_effect(req, timeout):
        call_count["n"] += 1
        if req.method == "HEAD":
            raise urllib.error.HTTPError("u", 405, "Method Not Allowed", {}, None)
        return FakeResp()

    with mock.patch("urllib.request.urlopen", side_effect=side_effect):
        url, status, err = _check_url("https://example.org/api")
    assert status == 200
    assert call_count["n"] == 2  # HEAD then GET


# ── integration test (slow — network required) ────────────────────────────────

@pytest.mark.slow
def test_internal_github_blob_links_resolve():
    """All internal wiki links must resolve on github.com after push.

    This test is marked slow and only runs in the `http-links` CI job
    (push to main), not in the fast local test suite.

    It verifies that relative [text](path.md) links in the shipped wiki
    all return HTTP 200 on github.com/blob/main/... — the proof that
    github.com actually renders them as clickable links.
    """
    result = subprocess.run(
        [sys.executable, str(CHECK_SCRIPT), "--github-only", "--workers", "4"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 0, (
        f"Internal GitHub blob links broken:\n{result.stdout}\n{result.stderr}"
    )
