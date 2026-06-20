# AGENTS.md

> Repo-wide agent contract for `jleechanorg/worldai_wiki`. Read this before
> you write anything. The companion file [`CLAUDE.md`](CLAUDE.md) has
> Claude-Code-specific guidance; this file is the cross-tool contract.

## Purpose

`jleechanorg/worldai_wiki` is the **public, player-facing reference wiki** for
[WorldArchitect.AI](https://worldarchitect.ai). It is a curated Markdown wiki
hosted on GitHub, not the game itself and not the private code repo.

**Three audiences:**

1. **Players** — learning to play, design campaigns, prompt god mode.
2. **External developers / integrators** — using MCP, REST, or
   OpenAI-compatible API.
3. **Operator-curators** — keeping the wiki accurate as the game evolves.

**Source of truth for game behaviour**: the private
[`jleechanorg/worldarchitect.ai`](https://github.com/jleechanorg/worldarchitect.ai)
repo. If the two ever disagree, the private repo wins; this wiki needs an
update.

## Non-negotiables

- **No internal code paths.** Do not expose file:line references into
  `mvp_site/`, internal class names, or implementation details that would
  change with the next refactor.
- **No fabricated facts.** If the existing page, the `raw/` mirror, or the
  live product does not back a claim, do not write it.
- **No credentials in examples.** Use placeholders (`<your-api-key>`,
  `<your-uid>`, `<your-campaign-id>`). The CI scans for this; do not bypass
  it.
- **No force-push to `main`.** Ever.
- **No orphan pages.** New pages must be added to `index.md` under the
  correct section. Edited pages must keep their existing outbound links.
- **No ad-hoc tags or types.** Use the closed taxonomy in `SCHEMA.md`. Add to
  the taxonomy first, then use it.

## Schema contract

`SCHEMA.md` is the single source of truth for wiki conventions. The summary:

- **File names**: lowercase, hyphens, no spaces.
- **Frontmatter** is required on every page:
  ```yaml
  ---
  title: Page Title
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary | source | schema
  tags: [from-taxonomy]
  sources: [raw/<path>]
  ---
  ```
- **Markdown links only.** No Obsidian-style `[[wikilinks]]`.
- **At least 2 outbound links** to other wiki pages per page.
- **`## Sources` section** required when the page ingests raw material.
- **Page thresholds**: ~250 lines max; split before that. Archive fully
  superseded pages to `_archive/` and remove from index.

## Editing protocol (required)

Before touching any file, document (in your reasoning, not in the file):

1. **GOAL** — what this change is for and which audience it serves.
2. **MODIFICATION** — exactly which paragraphs / sections change.
3. **NECESSITY** — why a new page is needed (or why an existing page is the
   better home).
4. **INTEGRATION PROOF** — at least one existing wiki page that already
   touches this topic, plus the entry you'll add to `index.md` and `log.md`.

Default to **integrating into existing pages**. New file creation is last
resort. Integration order:

1. Existing similar page (most common).
2. Existing utility / FAQ.
3. Existing summary / overview.
4. Existing `concepts/` or `queries/` page that already covers the system.
5. New `concepts/<system>.md` only if no existing page fits.
6. New page type (e.g. `comparisons/`) only with justification in `log.md`.

## Update protocol (required)

When you modify any file:

1. **Frontmatter**: bump `updated` to today's date.
2. **`## Sources`**: extend, do not remove.
3. **`index.md`**: if you added a page, register it under the correct
   section.
4. **`log.md`**: append a one-line entry in the format
   `## [YYYY-MM-DD] action | subject` where `action` is one of
   `ingest, update, query, lint, create, archive, delete`.
5. **Run lints**:
   ```bash
   python -m pytest tests/ -v -m "not slow"
   python scripts/lint_wikilinks.py
   ```
6. **Commit** with a clear message in the form
   `type(scope): short summary` (e.g. `docs(external-stories): add US-026..US-100 public-facing equivalents`).

## Source ingestion protocol

When you ingest a new raw source (e.g. an updated internal spec):

1. **Save the raw file** under `raw/` with a clear filename.
2. **Reference it** from the relevant wiki page's frontmatter `sources:`
   array.
3. **Summarize, do not duplicate.** Wiki pages describe what the raw file
   says in player-facing language; they do not copy-paste code or internal
   identifiers.
4. **Flag contradictions** in frontmatter `contradictions: [page-name]` and
   call them out in the lint report.

## Skills discovery

Before starting work, scan:

- `~/.claude/skills/` (personal)
- `.claude/skills/` (project)
- `.codex/skills/` (Codex mirror of selected Claude skills)

Relevant skills for this repo include:

- `hermes-deploy-pipeline` — staging-first → production push pattern (if the
  wiki is published via the same Hermes pipeline).
- `worldarchitect` — high-level context on the WorldArchitect.AI project.
- `pr-clean-worktree` and `pr-branch-from-main` — worktree hygiene for PRs.

Personal skills win when conflicts exist.

## Voice and style

- **Active voice**, present tense for behaviour, past tense for actions.
- **Short paragraphs** (2–4 sentences).
- **Tables** for system matrices and configuration references.
- **Code blocks** for example prompts, JSON, dice notation, CLI invocations.
- **No emoji** in section headers; emoji are fine inline for status flags.
- **No marketing fluff**. Operational and evidence-led. Match the existing
  pages.

## Build, lint, test

The wiki has no build step. CI runs:

```bash
python -m pytest tests/ -v -m "not slow"     # fast: wikilink + markdown regressions
python scripts/lint_wikilinks.py              # no broken [[wikilinks]] / .md links
python scripts/check_http_links.py            # slow: external HTTP link check
```

The HTTP check runs only on `push` to `main` and on a weekly schedule; it
skips PRs.

## PR and commit workflow

1. **Branch from `origin/main`** in a fresh worktree:
   ```bash
   git worktree add ~/.worktrees/<branch-name> -b <branch> origin/main
   ```
2. Make your edits, commit, push the branch.
3. Open a PR. Default base is `main`. Include:
   - A short summary
   - The affected pages listed
   - `## User Stories` section (or `N/A` with one-line justification)
   - `## Evidence` if you reference live screenshots or API contracts
4. Wait for CI. The HTTP link check is non-blocking for PRs.
5. Wait for human review. Wiki merges are reviewer-gated.

## Things agents must never do

- **Never** rewrite or remove existing `## Sources` sections.
- **Never** close / archive a page without updating `index.md` and `log.md`.
- **Never** use `bd` for issue tracking in this repo — there is no issue
  tracker configured here.
- **Never** commit `requirements-dev.txt` changes that have not been
  verified against `python -m pip install -r requirements-dev.txt`.
- **Never** push to a branch other than the one the PR targets.

## File organization

```
/
├── README.md                  # top-level orientation
├── CLAUDE.md                  # Claude Code–specific guidance
├── AGENTS.md                  # this file (cross-tool contract)
├── SCHEMA.md                  # wiki conventions
├── index.md                   # full page catalog
├── log.md                     # chronological action log
├── concepts/                  # concept pages (combat, dice, factions, ...)
├── entities/                  # entity pages (campaigns, characters, systems)
├── queries/                   # question-answering pages (FAQs, how-tos, user stories)
├── comparisons/               # side-by-side comparisons
├── raw/                       # mirrored internal source files
├── scripts/                   # lint + link-check scripts
├── tests/                     # pytest wikilink + markdown regressions
└── .github/workflows/         # CI workflows (lint, HTTP check)
```

## See also

- [`CLAUDE.md`](CLAUDE.md) — Claude Code-specific guidance.
- [`SCHEMA.md`](SCHEMA.md) — wiki conventions, tag and type taxonomy.
- [`README.md`](README.md) — public-facing overview.
- [`index.md`](index.md) — page catalog.
- [`log.md`](log.md) — chronological change log.
- [`raw/`](raw/) — mirrored internal source files.