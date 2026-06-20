# CLAUDE.md

> Guidance for Claude Code (and other AI coding assistants) working in this
> repository.

## What this repo is

`jleechanorg/worldai_wiki` is the **public, player-facing reference wiki** for
[WorldArchitect.AI](https://worldarchitect.ai). It is a Markdown wiki, hosted on
GitHub, written for three audiences:

1. **Players** learning how to play, how to design a campaign, and how to
   prompt god mode.
2. **External developers / integrators** who want to use the game's MCP
   endpoint, OpenAI-compatible chat surface, or REST API.
3. **Operator-curators** who keep the wiki accurate as the underlying game
   evolves.

The wiki is **not**:

- The source of truth for game behaviour. The private
  [`jleechanorg/worldarchitect.ai`](https://github.com/jleechanorg/worldarchitect.ai)
  repo is. If the two ever disagree, the private repo wins and this wiki
  needs an update.
- A documentation dump of `mvp_site/`. We describe behaviour; we do not expose
  internal code paths, file:line references, or implementation details that
  would change with the next refactor.
- A marketing site. Tone is operational, neutral, and evidence-led. Match the
  voice of the existing pages.

## How to read this repo

Before you write anything, read:

1. [`SCHEMA.md`](SCHEMA.md) — file naming, frontmatter, tag taxonomy, page
   thresholds. **Required reading.**
2. [`README.md`](README.md) — high-level shape of the wiki and its TOC.
3. [`index.md`](index.md) — current page catalog.
4. [`log.md`](log.md) — recent changes. Append-only.
5. One or two example pages in each of `concepts/`, `entities/`, `queries/`,
   `comparisons/` to internalize the voice.

Then read the relevant source. The internal reference is mirrored at
[`raw/worldarchitect.ai-docs-user-stories-general.md`](raw/worldarchitect.ai-docs-user-stories-general.md).
The full private repo is **read-only** for you — do not assume you can open
issues there, run tests against it, or push branches. Mirror the behaviour you
observe into wiki prose.

## How agents should work here

### Scope

You are working on a **public documentation site**. That means:

- **Do not** expose private code paths, internal file:line references,
  endpoints that aren't part of the public API surface, or names of internal
  services / agents.
- **Do** describe behaviour at the level a player or external developer would
  observe or use.
- **Do** link to existing wiki pages via relative Markdown links
  (`[Text](../concepts/Concept.md)`). Do **not** use Obsidian-style
  `[[wikilinks]]` — they do not render on github.com.
- **Do** cite the source raw file in the frontmatter `sources:` array when you
  ingest from `raw/`.

### File conventions (summary — see `SCHEMA.md` for the full version)

- **File names**: lowercase, hyphens, no spaces (e.g. `god-mode-prompting.md`,
  `itachi-gaiden.md`).
- **Frontmatter** is required. Required keys: `title`, `created`, `updated`,
  `type`, `tags`. `sources` is recommended when raw files exist.
- **Tag taxonomy** is closed. If you need a new tag, add it to `SCHEMA.md`
  first, then use it. No ad-hoc tags.
- **Type taxonomy** is closed (`entity`, `concept`, `comparison`, `query`,
  `summary`, `source`, `schema`).
- Every page must end with a `## Sources` section when it ingests raw
  material.
- New pages must be added to `index.md` under the correct section.
- Every action appends to `log.md`.

### Editing rules

- **Prefer updating existing pages over creating new ones.** The wiki is
  curated; we don't want a page explosion. If a topic already has a page
  (e.g. `concepts/Dice.md`), extend that page rather than writing
  `concepts/DiceAntiFabrication.md`.
- **Update the `updated` frontmatter field** on every change.
- **Append a `## [YYYY-MM-DD] action | subject` entry** to `log.md`.
- **No source-code or gameplay behaviour claims without a backing source.**
  When in doubt, link to the underlying `raw/` file or the existing wiki page
  that established the claim.
- **No fake user stories or API endpoints.** If you are rewriting an internal
  story for an external audience, follow the structure of the existing
  `queries/PlayerUserStories.md` and `queries/ExternalUserStories.md` pages.

### Voice and style

- **Active voice**, present tense for behaviour ("the wizard shows…"), past
  tense for actions already taken.
- **Short paragraphs** (2–4 sentences).
- **Tables** for system matrices, story mappings, and configuration
  references.
- **Code blocks** for example prompts, JSON, dice notation, and CLI
  invocations.
- **Screenshots** are allowed; capture them from the live product against the
  Dragon Knight campaign and reference them in frontmatter.
- **Markdown links only** — no HTML except for tables or `<details>` blocks
  that cannot be expressed in Markdown.

### Build, lint, test

The wiki is plain Markdown; there is no build step. The CI lint runs:

```bash
python -m pytest tests/ -v -m "not slow"   # wikilink + markdown link regressions
python scripts/lint_wikilinks.py            # no broken wikilinks / .md links
python scripts/check_http_links.py          # external HTTP link check (slow)
```

Run the fast ones locally before opening a PR:

```bash
python -m pytest tests/ -v -m "not slow" && python scripts/lint_wikilinks.py
```

### Pull request workflow

1. Create a fresh worktree from `origin/main`:
   ```bash
   git worktree add ~/.worktrees/<branch-name> -b <branch> origin/main
   ```
2. Edit, commit, push the branch.
3. Open a PR with a short summary, the user story bullet (or N/A with
   justification), and the affected pages listed.
4. Wait for CI to pass. The HTTP link check runs only on push to `main` and
   weekly on schedule, not on PRs.
5. Wait for human review. Wiki merges are reviewer-gated.

### When you don't know

If a fact is uncertain — for example, "does the level-up modal lock release
automatically on commit?" — **read the existing page first**, then check
`raw/` for the source, then **ask** before writing a contradictory claim.
Don't fabricate to fill a gap; leave a `## Sources` placeholder or flag the
open question in `log.md`.

## Things you should never do here

- **Never** commit API keys, PATs, or real user identifiers. Examples and
  fixtures must use placeholders (`<your-firebase-api-key>`, `<your-uid>`).
- **Never** rewrite pages to match a private code change you haven't
  confirmed via the mirror or the existing page. The wiki updates after the
  private repo lands, not before.
- **Never** remove the `## Sources` section when editing — extend it.
- **Never** force-push to `main`.
- **Never** close or archive a page without updating `index.md` and adding a
  log entry.

## See also

- [`AGENTS.md`](AGENTS.md) — repo-wide agent guidelines (cross-tool).
- [`SCHEMA.md`](SCHEMA.md) — frontmatter, tag taxonomy, page thresholds.
- [`index.md`](index.md) — page catalog.
- [`log.md`](log.md) — chronological change log.
- [`raw/worldarchitect.ai-docs-user-stories-general.md`](raw/worldarchitect.ai-docs-user-stories-general.md) —
  mirrored internal spec.