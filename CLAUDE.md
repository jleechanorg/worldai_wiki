# CLAUDE.md

> Claude-Code-specific guidance for working in `jleechanorg/worldai_wiki`.
> Most operational rules (scope, voice, schema, build/lint, PR workflow,
> non-negotiables) live in [`AGENTS.md`](AGENTS.md) — this file only adds
> the Claude-Code-specific delta. **Read `AGENTS.md` first.**

## What this file adds over `AGENTS.md`

Nothing in `AGENTS.md` is contradicted here; this file is a thin pointer for
Claude Code sessions that land in the repo without a full agent-contract
handshake. If `AGENTS.md` is silent on a topic and `CLAUDE.md` is silent
too, default to the wiki's [`SCHEMA.md`](SCHEMA.md) and the existing pages
in the affected directory.

| Topic | Source of truth |
|-------|-----------------|
| Repo purpose, audience, scope | [`AGENTS.md`](AGENTS.md) |
| Wiki schema (frontmatter, tags, types, page thresholds) | [`SCHEMA.md`](SCHEMA.md) |
| Editing / update / source-ingestion protocol | [`AGENTS.md`](AGENTS.md) |
| Voice and style | [`AGENTS.md`](AGENTS.md) |
| Build, lint, test commands | [`AGENTS.md`](AGENTS.md) |
| PR and commit workflow | [`AGENTS.md`](AGENTS.md) |
| Non-negotiables | [`AGENTS.md`](AGENTS.md) |

## Claude-Code-specific notes

### Skills discovery

Before starting any non-trivial edit, scan the same skills you would on
`jleechanorg/worldarchitect.ai`, plus these:

- **`worldarchitect` skill** (in your `~/.claude/skills/` or `~/.hermes_prod/skills/`)
  — has the canonical reference
  `references/worldai-wiki-authoring.md` covering the schema, the
  internal-spec → external-audience rewrite recipe (worked example:
  [PR #4](https://github.com/jleechanorg/worldai_wiki/pull/4)), the
  CLAUDE.md/AGENTS.md authoring convention, the auto-merge race recipe,
  and the **4 common review-bot fix patterns** (orphan screenshots,
  auth-bypass disclosure, internal paths, wikilink→markdown race).

### Auto-merge race on this repo

The wiki repo's branch protection does **not** block auto-merge. The
review window between "PR opened" and "PR auto-merged" is typically
**under 10 minutes** (Lint passes in ~10s, CodeRabbit in ~30s, Greptile in
~2-3 min, no human in the loop).

**Implication:** if a substantive review might uncover issues (Greptile
review-bot fix patterns** (orphan screenshots, auth-bypass disclosure,
internal code-path leaks in body text, story-ID collisions), **do the review
BEFORE opening the PR**:

1. Read the diff against `origin/main`.
2. Predict the bot's likely flags using the `references/worldai-wiki-authoring.md`
   "Common review-fix patterns" section.
3. Fix them in the branch.
4. Only then push and open the PR.

If a PR is merged before review fixes can land, follow the auto-merge race
recovery recipe in the wiki skill (separate follow-up branch from
`origin/main`, surgical diff, reference the original PR in the body).

### Things you should never do here

See `AGENTS.md` "Things agents must never do" — that list is canonical.
This file adds one Claude-Code-specific item:

- **Never** open a wiki PR from this session and then wait for human review
  to push fixes. Push fixes **before** opening. If the bot reviews and finds
  issues after open, the PR is likely to auto-merge before you can land the
  fixes.

## See also

- [`AGENTS.md`](AGENTS.md) — canonical cross-tool contract.
- [`SCHEMA.md`](SCHEMA.md) — wiki conventions, tag and type taxonomy.
- [`index.md`](index.md) — page catalog.
- [`log.md`](log.md) — chronological change log.
- [`raw/worldarchitect.ai-docs-user-stories-general.md`](raw/worldarchitect.ai-docs-user-stories-general.md) —
  mirrored internal spec.
- `~/.claude/skills/worldarchitect/references/worldai-wiki-authoring.md` —
  the wiki skill reference with the rewrite recipe, the CLAUDE.md/AGENTS.md
  authoring convention, and the 4 review-bot fix patterns.