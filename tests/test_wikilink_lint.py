"""Tests for the wikilink linter.

Wikilinks (`[[Page]]`, `[[Page|alias]]`, `[[path/Page]]`) render as plain text
on github.com blob view. The wiki must instead ship with github.com-compatible
markdown links `[Text](path/Page.md)` so readers can actually click through.

These tests enforce both:
1. No broken wikilinks (target file must exist).
2. No raw `[[wikilinks]]` survive in shipped content — they must have been
   converted to `[text](path.md)` for github.com rendering.

The linter script `scripts/lint_wikilinks.py` is responsible for both:
reporting problems and (with --fix) rewriting files in place.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
LINT_SCRIPT = REPO_ROOT / "scripts" / "lint_wikilinks.py"

# All wiki content directories
WIKI_DIRS = ["concepts", "entities", "comparisons", "queries"]
# Top-level standalone pages
TOP_LEVEL_PAGES = ["README.md", "SCHEMA.md", "index.md"]

WIKILINK_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")


def _strip_code_blocks(text: str) -> str:
    """Same masking the linter uses: hide fenced and inline code regions."""
    masked = re.sub(r"```.*?```", lambda m: " " * len(m.group(0)), text, flags=re.DOTALL)
    masked = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), masked)
    return masked


def _all_md_files() -> list[Path]:
    files: list[Path] = []
    for d in WIKI_DIRS:
        for p in (REPO_ROOT / d).glob("*.md"):
            files.append(p)
    for name in TOP_LEVEL_PAGES:
        p = REPO_ROOT / name
        if p.exists():
            files.append(p)
    return files


def _run_lint(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(LINT_SCRIPT), *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


def test_lint_script_exists():
    """The linter script must ship with the wiki."""
    assert LINT_SCRIPT.exists(), f"Missing linter: {LINT_SCRIPT}"


def test_lint_script_is_runnable():
    """Linter must run without arguments and exit 0 on a clean wiki."""
    result = _run_lint()
    # After the fix this should pass; before the fix it surfaces broken links / unwikilinked refs.
    assert result.returncode == 0, (
        f"lint failed:\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )


def test_lint_script_clean_exit_on_clean_wiki(tmp_path: Path):
    """If we strip all [[wikilinks]] (replacing with markdown), lint must pass.

    Builds a self-contained fake wiki with hand-crafted content rather than
    copying the real repo (the real repo has external links into raw/ that
    are out of scope for the lint).
    """
    fake_root = tmp_path / "wiki"
    (fake_root / "concepts").mkdir(parents=True)
    (fake_root / "entities").mkdir()
    (fake_root / "README.md").write_text(
        "---\ntitle: Wiki\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: summary\ntags: [meta]\n---\n\n"
        "Home. See [Combat](concepts/Combat.md) and [Dice](concepts/Dice.md).\n"
    )
    (fake_root / "concepts" / "Combat.md").write_text(
        "---\ntitle: Combat\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "Combat involves [Dice](Dice.md) and [LevelUp](LevelUp.md).\n"
    )
    (fake_root / "concepts" / "Dice.md").write_text(
        "---\ntitle: Dice\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "Dice are rolled by the platform.\n"
    )
    (fake_root / "concepts" / "LevelUp.md").write_text(
        "---\ntitle: LevelUp\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "Level up happens at thresholds.\n"
    )

    result = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), "--root", str(fake_root)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"lint should pass on a fully-converted wiki:\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )


def test_lint_script_flags_broken_wikilink(tmp_path: Path):
    """A wikilink to a non-existent target must be flagged (exit non-zero)."""
    fake_root = tmp_path / "wiki"
    (fake_root / "concepts").mkdir(parents=True)
    (fake_root / "concepts" / "BrokenPage.md").write_text(
        "---\ntitle: Broken\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "See [[concepts/NonExistent]].\n"
    )

    result = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), "--root", str(fake_root)],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "NonExistent" in (result.stdout + result.stderr)


def test_no_unconverted_wikilinks_in_shipped_wiki():
    """Every [[wikilink]] (outside code) in the shipped wiki must be resolvable.

    Until the fix lands this fails because the shipped wiki has hundreds of
    raw [[wikilinks]] that github.com can't render. After the fix it must
    pass — either the wiki has been rewritten to use markdown links, or the
    remaining [[wikilinks]] all point at existing files.

    Wikilinks INSIDE code fences or inline code are syntax examples, not real
    links — those are skipped.
    """
    # First, count remaining raw wikilinks (outside code) that survive
    remaining = []
    for p in _all_md_files():
        text = p.read_text()
        scan_text = _strip_code_blocks(text)
        for m in WIKILINK_RE.finditer(scan_text):
            remaining.append((p, m.group(1)))

    # After the fix we may legitimately have ZERO remaining [[wikilinks]]
    # (preferred: convert all to markdown links for github.com rendering).
    # Or we may keep [[wikilinks]] but every one of them must resolve.
    if not remaining:
        return

    # If any remain, they must ALL resolve.
    for path, target in remaining:
        # Parse the wikilink target
        if "|" in target:
            target = target.split("|", 1)[0]
        target = target.strip()
        if "/" not in target:
            target = f"concepts/{target}"
        target = re.sub(r"\.md$", "", target)
        resolved = REPO_ROOT / f"{target}.md"
        assert resolved.exists(), (
            f"Broken wikilink in {path.relative_to(REPO_ROOT)}: [[{target}]] "
            f"-> {resolved} does not exist"
        )


def test_all_md_links_in_wiki_resolve():
    """Every markdown link to another wiki file must resolve.

    Catches the case where someone writes `[Combat](concepts/Combat.md)` but
    the file is actually at `concepts/Combat.md` (case mismatch, etc.).

    Links INSIDE code fences or inline code are syntax examples and skipped,
    matching the linter's behavior.
    """
    MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]*)?\)")
    for p in _all_md_files():
        text = p.read_text()
        scan_text = _strip_code_blocks(text)
        for m in MD_LINK_RE.finditer(scan_text):
            link = m.group(1)
            if link.startswith(("http://", "https://", "/")):
                continue
            # Resolve relative to the file's location
            resolved = (p.parent / link).resolve()
            assert resolved.exists(), (
                f"Broken markdown link in {p.relative_to(REPO_ROOT)}: "
                f"{link} -> {resolved}"
            )


def test_player_facing_systems_table_uses_markdown_links():
    """The exact bug Jeffrey reported: the player-facing systems table
    on entities/WorldArchitect.md must render as clickable github.com links."""
    page = REPO_ROOT / "entities" / "WorldArchitect.md"
    text = page.read_text()
    # Find the section
    assert "Player-facing systems at a glance" in text
    # Extract the table area
    start = text.index("Player-facing systems at a glance")
    section = text[start:]

    # Each row should now contain a markdown link, not a raw [[wikilink]]
    rows = [line for line in section.splitlines() if line.startswith("|") and "|" in line[1:]]
    assert rows, "expected table rows"
    md_links = sum(1 for r in rows if re.search(r"\[[^\]]+\]\([^)]+\.md\)", r))
    raw_wikilinks = sum(1 for r in rows if "[[" in r)

    # All seven rows must be markdown links now
    assert md_links >= 7, (
        f"Expected ≥7 markdown links in player-facing systems table, "
        f"found {md_links} (raw [[wikilinks]] still present: {raw_wikilinks})"
    )
    assert raw_wikilinks == 0, (
        f"Raw [[wikilinks]] still present in player-facing systems table:\n{section}"
    )


def test_lint_fix_converts_wikilinks_in_place(tmp_path: Path):
    """`--fix` must rewrite [[Page]] -> [Page](path.md) on disk."""
    fake_root = tmp_path / "wiki"
    (fake_root / "concepts").mkdir(parents=True)
    target = fake_root / "concepts" / "Target.md"
    target.write_text(
        "---\ntitle: Target\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "See [[concepts/Target]] for details.\n"
    )
    source = fake_root / "concepts" / "Source.md"
    source.write_text(
        "---\ntitle: Source\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "Links: [[concepts/Target]] and [[Target|the target page]].\n"
    )

    r = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), "--root", str(fake_root), "--fix"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr

    new_text = source.read_text()
    # Bare wikilink converted to markdown link
    assert "[[concepts/Target]]" not in new_text
    assert "[Target](Target.md)" in new_text
    # Aliased wikilink converted preserving display text
    assert "[[Target|the target page]]" not in new_text
    assert "[the target page](Target.md)" in new_text


def test_lint_fix_preserves_section_anchors(tmp_path: Path):
    """`[[Page#section]]` should preserve the anchor in the markdown link."""
    fake_root = tmp_path / "wiki"
    (fake_root / "concepts").mkdir(parents=True)
    (fake_root / "concepts" / "Anchored.md").write_text(
        "---\ntitle: Anchored\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "## how it works\n\nBody.\n"
    )
    source = fake_root / "concepts" / "Source.md"
    source.write_text(
        "---\ntitle: Source\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "See [[concepts/Anchored#how it works]] for the loop.\n"
    )

    r = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), "--root", str(fake_root), "--fix"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    new_text = source.read_text()
    assert "[Anchored](Anchored.md#how it works)" in new_text


def test_no_raw_wikilinks_in_raw_directory():
    """raw/ mirror files are also rendered on github.com and therefore must
    not contain raw [[wikilinks]]. The conversion-only linter
    (scripts/lint_wikilinks.py) intentionally excludes raw/ because the
    source-mirror is supposed to be a verbatim copy of an internal spec —
    but the wiki is a public, github.com-rendered surface, and raw/
    wikilinks render as literal `[[brackets]]` text.

    This test pins the contract: any future raw/ file added to the wiki
    must be written with github.com-compatible markdown links, not
    Obsidian-style [[wikilinks]].

    Bug-ref: 2026-06-22 — Jeffrey reported the player-facing systems table
    rendered as `[[concepts/Combat]]` on github.com. Root cause: a raw/
    mirror file contained `[[queries/PlayerUserStories]]` literal syntax
    that the linter (which excludes raw/) silently allowed through.
    """
    raw_dir = REPO_ROOT / "raw"
    if not raw_dir.exists():
        pytest.skip("no raw/ directory in this wiki")

    bad: list[tuple[Path, str]] = []
    for path in sorted(raw_dir.rglob("*.md")):
        text = path.read_text()
        # Mask code fences and inline code — wikilinks there are syntax examples.
        scan = re.sub(r"```.*?```", lambda m: " " * len(m.group(0)), text, flags=re.DOTALL)
        scan = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), scan)
        for m in WIKILINK_RE.finditer(scan):
            rel = path.relative_to(REPO_ROOT)
            bad.append((rel, m.group(1)))

    assert not bad, (
        "raw/ mirror files must not contain raw [[wikilinks]] — they render as\n"
        "literal `[[brackets]]` on github.com, breaking navigation. Convert to\n"
        "github.com-compatible markdown links like\n"
        "`[Display Text](queries/Page.md)`. Offending files:\n"
        + "\n".join(f"  {p}: [[{inner}]]" for p, inner in bad)
    )


def test_lint_script_catches_raw_directory_wikilinks(tmp_path: Path):
    """The wikilink linter must also flag raw/ files for github-render safety.

    The original linter design (and the existing test_no_unconverted_wikilinks_in_shipped_wiki
    test) intentionally exclude raw/ because the source-mirror is supposed
    to be a verbatim copy of an internal spec. That exemption is correct
    for the *broken-wikilink* check (raw/ files can legitimately reference
    pages that don't exist in the wiki), but it is WRONG for the
    github-render check (raw/ files are still rendered on github.com and
    therefore must not display as literal `[[brackets]]` text).

    This test pins the contract: the linter must run its render-safety
    scan over raw/ files, even if it keeps the broken-wikilink scan
    limited to the wiki content directories.
    """
    fake_root = tmp_path / "wiki"
    (fake_root / "raw").mkdir(parents=True)
    (fake_root / "concepts").mkdir()
    (fake_root / "concepts" / "Combat.md").write_text(
        "---\ntitle: Combat\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\nCombat page.\n"
    )
    (fake_root / "raw" / "source-mirror.md").write_text(
        "---\ntitle: Source\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: source\ntags: [wa-system]\n---\n\n"
        "See [[concepts/Combat]] for the system.\n"
    )

    r = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), "--root", str(fake_root)],
        capture_output=True, text=True,
    )
    # Must flag the raw/ wikilink as a render-safety issue (even though the
    # broken-wikilink scan legitimately skips raw/).
    assert r.returncode != 0, (
        f"linter must flag raw/ wikilinks as a github-render issue:\n"
        f"stdout: {r.stdout}\nstderr: {r.stderr}"
    )
    combined = (r.stdout + r.stderr).lower()
    assert "raw" in combined, (
        f"linter must mention raw/ when flagging the violation:\n"
        f"stdout: {r.stdout}\nstderr: {r.stderr}"
    )
    assert "concepts/combat" in combined, (
        f"linter must mention the offending target path:\n"
        f"stdout: {r.stdout}\nstderr: {r.stderr}"
    )


def test_lint_skips_wikilinks_inside_code(tmp_path: Path):
    """Wikilinks inside ```fences``` or `inline code` are syntax examples,
    not real links — they must not be converted or flagged."""
    fake_root = tmp_path / "wiki"
    (fake_root / "concepts").mkdir(parents=True)
    (fake_root / "concepts" / "Source.md").write_text(
        "---\ntitle: Source\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "Use `[[Page]]` syntax inside `inline code`.\n\n"
        "```\n[[Page]] is the wikilink format.\n```\n\n"
        "But a real link: [[concepts/Source]].\n"
    )
    (fake_root / "concepts" / "Source2.md").write_text(
        "---\ntitle: Source2\ncreated: 2026-06-19\nupdated: 2026-06-19\n"
        "type: concept\ntags: [wa-mechanic]\n---\n\n"
        "Target.\n"
    )

    r = subprocess.run(
        [sys.executable, str(LINT_SCRIPT), "--root", str(fake_root), "--fix"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    new_text = (fake_root / "concepts" / "Source.md").read_text()
    # Inline-code and fenced-code wikilinks untouched
    assert "`[[Page]]`" in new_text
    assert "```\n[[Page]] is the wikilink format.\n```" in new_text
    # Real wikilink converted
    assert "[Source](Source.md)" in new_text