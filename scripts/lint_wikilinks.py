#!/usr/bin/env python3
"""Lint and (optionally) fix wikilinks in the WorldArchitect.AI wiki.

Background
----------
Obsidian-style `[[wikilinks]]` render as plain text on github.com blob view.
To make the wiki actually clickable for GitHub readers, every `[[Foo]]` must
be converted to a standard markdown link `[Foo](path/Foo.md)`.

This script:

* Parses every `[[wikilink]]` (with optional alias `[[Foo|display text]]` or
  section anchor `[[Foo#section]]`) across the wiki.
* Verifies each link target resolves to an existing `.md` file.
* Verifies every `[text](path.md)` markdown link points at an existing file.
* In `--fix` mode, rewrites raw `[[wikilinks]]` to github.com-friendly
  `[text](path.md)` markdown links IN PLACE, leaving aliases and section
  anchors intact.

Exit codes:
  0 — no problems (and --fix applied cleanly if requested)
  1 — broken wikilink or markdown link found
  2 — internal error
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

WIKI_DIRS = ["concepts", "entities", "comparisons", "queries"]
# raw/ files are intentionally excluded from the *broken-wikilink* check
# (the source-mirror is supposed to be a verbatim copy of an internal spec,
# and may reference pages that don't exist in the wiki). But raw/ files ARE
# rendered on github.com and therefore must not display as literal
# `[[brackets]]` text — that breaks navigation for any reader who clicks
# through to a raw/ file from a wiki page. See _check_render_safety().
RENDER_SAFETY_DIRS = ["raw"]
# raw/ is intentionally excluded — sources are immutable per the wiki skill.
TOP_LEVEL_PAGES = ["README.md", "SCHEMA.md", "index.md"]
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\n]+?)(?:\s+\"[^\"]*\")?\)")


def _strip_code_blocks(text: str) -> str:
    """Remove ``` fenced blocks and `inline code` so wikilink detection
    inside code does not flag false positives. Returns the masked text.

    Wikilinks INSIDE code are literal syntax examples, not real links.
    """
    # Mask fenced code blocks
    masked = re.sub(r"```.*?```", lambda m: " " * len(m.group(0)), text, flags=re.DOTALL)
    # Mask inline code spans
    masked = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), masked)
    return masked


def _all_md_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for d in WIKI_DIRS:
        dpath = root / d
        if dpath.exists():
            files.extend(sorted(dpath.glob("*.md")))
    for name in TOP_LEVEL_PAGES:
        p = root / name
        if p.exists():
            files.append(p)
    return files


def _render_safety_files(root: Path) -> list[Path]:
    """Files that get the render-safety scan but not the broken-wikilink scan.

    raw/ files are mirrored internal specs that may legitimately reference
    pages that don't exist in the wiki. But they ARE rendered on github.com
    — a raw/ page that contains `[[queries/PlayerUserStories]]` will
    display as literal `[[brackets]]` text to a reader clicking through
    from a wiki page. The render-safety check flags any raw `[[wikilink]]`
    in these files, independent of whether the target resolves.
    """
    files: list[Path] = []
    for d in RENDER_SAFETY_DIRS:
        dpath = root / d
        if dpath.exists():
            files.extend(sorted(dpath.rglob("*.md")))
    return files


def _check_render_safety(text: str, source: Path, root: Path) -> list[str]:
    """Flag any raw [[wikilink]] in a file that gets rendered on github.com.

    Mirrors the wikilink-detection logic from `_convert_wikilinks` but only
    reports problems (no rewrite). Used for files like raw/ mirror pages
    that should never have raw wikilinks in shipped content, regardless of
    whether the wikilink target resolves.
    """
    problems: list[str] = []
    scan_text = _strip_code_blocks(text)
    for m in WIKILINK_RE.finditer(scan_text):
        problems.append(
            f"{source.relative_to(root)}: raw [[wikilink]] in github-rendered "
            f"surface — wikilinks render as literal `[[brackets]]` on github.com. "
            f"Replace with `[Display Text](path/Page.md)` markdown link. "
            f"Offending wikilink: [[{m.group(1)}]]"
        )
    return problems


def _split_wikilink(inner: str) -> tuple[str, str | None, str | None]:
    """Parse a wikilink's inner text into (target, alias, anchor).

    `concepts/Combat`            -> ("concepts/Combat", None, None)
    `Combat|combat system`      -> ("Combat", "combat system", None)
    `concepts/Combat#how it works` -> ("concepts/Combat", None, "how it works")
    `Combat|alias#section`       -> ("Combat", "alias", "section")
    """
    page = inner.strip()
    anchor: str | None = None
    if "#" in page:
        page, anchor = page.split("#", 1)
        page = page.strip()
        anchor = anchor.strip()
    alias: str | None = None
    if "|" in page:
        page, alias = page.split("|", 1)
        page = page.strip()
        alias = alias.strip()
    return page, alias, anchor


def _resolve_target(page: str, source: Path, root: Path) -> Path | None:
    """Resolve a wikilink target like `concepts/Combat` to an absolute .md path."""
    # Strip trailing .md if the wikilink explicitly includes the extension
    # (raw/ files sometimes show up that way).
    page = re.sub(r"\.md$", "", page)
    if "/" not in page:
        # Bare name → look in the same directory as the source page first,
        # then fall back to concepts/ (most wiki pages are concept links).
        candidates = [source.parent / f"{page}.md", root / "concepts" / f"{page}.md"]
    else:
        candidates = [root / f"{page}.md"]
    for c in candidates:
        if c.exists():
            return c
    return None


def _link_from_source(source: Path, target_path: Path) -> str:
    """Compute relative path from `source`'s directory to `target_path`.

    Both paths are absolute on disk. We need a POSIX-style relative path
    that github.com can resolve when the user clicks the link in the
    rendered blob view (relative to the SOURCE FILE, not the repo root).
    """
    src_dir = Path(source).resolve().parent
    target = Path(target_path).resolve()
    rel = Path(target).relative_to(Path(src_dir).parent.parent)
    # If target is not under the wiki root (it always should be), fall back
    # to os.path.relpath which handles arbitrary cases.
    try:
        rel = Path(os.path.relpath(target, start=src_dir))
    except ValueError:
        rel = Path(target).relative_to(src_dir)
    return rel.as_posix()


def _convert_wikilinks(text: str, source: Path, root: Path) -> tuple[str, list[str]]:
    """Return (new_text, warnings).

    Each `[[Foo]]` becomes `[Foo](path.md)`. Aliases and anchors are preserved.
    Wikilinks inside code fences or inline code are LEFT ALONE — those are
    literal syntax examples (e.g. SCHEMA.md describing the wikilink syntax).
    Warnings is non-empty if any target didn't resolve.
    """
    warnings: list[str] = []

    # Build a list of (start, end) ranges that are code — don't touch those.
    code_ranges: list[tuple[int, int]] = []
    for m in re.finditer(r"```.*?```", text, flags=re.DOTALL):
        code_ranges.append((m.start(), m.end()))
    for m in re.finditer(r"`[^`\n]*`", text):
        code_ranges.append((m.start(), m.end()))
    code_ranges.sort()

    def _in_code(pos: int) -> bool:
        for s, e in code_ranges:
            if s <= pos < e:
                return True
        return False

    def repl(m: re.Match) -> str:
        if _in_code(m.start()):
            return m.group(0)
        inner = m.group(1)
        page, alias, anchor = _split_wikilink(inner)
        resolved = _resolve_target(page, source, root)
        if resolved is None:
            warnings.append(
                f"{source.relative_to(root)}: [[{inner}]] -> "
                f"{page}.md not found"
            )
            return m.group(0)  # leave broken link untouched
        display = alias if alias else page.split("/")[-1]
        rel = _link_from_source(source, resolved)
        if anchor:
            return f"[{display}]({rel}#{anchor})"
        return f"[{display}]({rel})"

    new_text = WIKILINK_RE.sub(repl, text)
    return new_text, warnings


def _check_md_links(text: str, source: Path, root: Path) -> list[str]:
    """Find broken `[text](path.md)` links in `text`.

    Markdown links INSIDE code fences or inline code are syntax examples and
    are ignored — same convention as wikilink handling.
    """
    problems: list[str] = []
    scan_text = _strip_code_blocks(text)
    for m in MD_LINK_RE.finditer(scan_text):
        link = m.group(2).strip()
        # Strip inline anchor
        anchor = ""
        if "#" in link:
            link, anchor = link.split("#", 1)
        # Skip external / absolute
        if link.startswith(("http://", "https://", "/", "mailto:")):
            continue
        if not link.endswith(".md"):
            continue
        resolved = (source.parent / link).resolve()
        if not resolved.exists():
            problems.append(
                f"{source.relative_to(root)}: broken markdown link "
                f"[{m.group(1)}]({m.group(2)})"
            )
    return problems


def lint(root: Path, fix: bool = False) -> int:
    files = _all_md_files(root)
    safety_files = _render_safety_files(root)
    all_warnings: list[str] = []
    all_md_problems: list[str] = []
    all_render_safety_problems: list[str] = []
    total_wikilinks = 0
    total_converted = 0

    for path in files:
        text = path.read_text()
        # Scan for wikilinks ONLY outside code blocks / inline code
        scan_text = _strip_code_blocks(text)
        wikilinks = list(WIKILINK_RE.finditer(scan_text))
        total_wikilinks += len(wikilinks)

        # Always check for broken wikilinks (even without --fix).
        # The conversion function returns warnings for unresolved targets;
        # we use it here just to enumerate the broken ones, without writing.
        if wikilinks:
            _, warnings = _convert_wikilinks(text, path, root)
            all_warnings.extend(warnings)
            if fix:
                new_text, fix_warnings = _convert_wikilinks(text, path, root)
                if new_text != text:
                    converted_here = len(wikilinks) - sum(
                        1 for w in fix_warnings if str(path.relative_to(root)) in w
                    )
                    total_converted += converted_here
                    path.write_text(new_text)
                    text = new_text

        # Also check markdown links for breakage (independent of --fix)
        all_md_problems.extend(_check_md_links(text, path, root))

    # Render-safety pass over raw/ files (and any future RENDER_SAFETY_DIRS).
    # These files don't get the broken-wikilink check (they may legitimately
    # reference pages that don't exist in the wiki) but they DO get the
    # github-render check — a raw [[wikilink]] in raw/ is just as broken as
    # one in concepts/ from a reader's perspective.
    for path in safety_files:
        text = path.read_text()
        all_render_safety_problems.extend(_check_render_safety(text, path, root))

    # Report
    if fix:
        print(f"--fix applied: {total_converted} wikilinks converted "
              f"out of {total_wikilinks} found")

    if all_warnings:
        print(f"\n{len(all_warnings)} broken wikilinks:", file=sys.stderr)
        for w in all_warnings:
            print(f"  {w}", file=sys.stderr)

    if all_md_problems:
        print(f"\n{len(all_md_problems)} broken markdown links:", file=sys.stderr)
        for p in all_md_problems:
            print(f"  {p}", file=sys.stderr)

    if all_render_safety_problems:
        print(
            f"\n{len(all_render_safety_problems)} render-safety issues "
            f"(raw [[wikilinks]] in github-rendered files):",
            file=sys.stderr,
        )
        for p in all_render_safety_problems:
            print(f"  {p}", file=sys.stderr)

    if all_warnings or all_md_problems or all_render_safety_problems:
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Wiki root directory (default: current directory)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Rewrite raw [[wikilinks]] to github.com-compatible markdown links",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2
    return lint(root, fix=args.fix)


if __name__ == "__main__":
    raise SystemExit(main())