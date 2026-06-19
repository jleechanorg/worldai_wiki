---
title: Wiki Schema
created: 2026-06-19
updated: 2026-06-19
type: schema
tags: [meta, conventions]
---

# Wiki Schema

This schema constrains how every page in this wiki is written. Following it keeps the wiki browseable, navigable, and durable as content grows.

## Domain

WorldArchitect.AI player-facing wiki — how to play the game, how to design campaigns, how to write god-mode directives that shape narration, how the major systems (combat, factions, dice, level-up, character creation) work.

This is the **player-facing** companion to the private `jleechanorg/worldarchitect.ai` code repo. We explain what the game does; we do not expose proprietary code paths.

## File Conventions

- **File names:** lowercase, hyphens, no spaces. Examples: `combat.md`, `god-mode-prompting.md`, `itachi-gaiden.md`.
- **Every wiki page** starts with YAML frontmatter (see below).
- **Every wiki page** has at least 2 outbound `[[wikilinks]]`.
- **Every wiki page** ends with a `## Sources` section listing raw files referenced.
- When updating a page, bump the `updated` date.
- New pages must be added to `index.md` under the correct section.
- Every action appends to `log.md`.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | schema | source
tags: [from taxonomy below]
sources: [raw/<path>]
---
```

Required fields: `title`, `created`, `updated`, `type`, `tags`. `sources` is optional but recommended when raw files exist.

## Tag Taxonomy

Use ONLY these tags. Add new tags to this taxonomy first, then use them.

**Game systems**
- `wa-game` — the game itself (WorldArchitect.AI)
- `wa-mechanic` — a game mechanic (combat, dice, level-up)
- `wa-system` — a large internal system (faction minigame, living world, god mode)

**Content types**
- `wa-campaign` — campaign content (design guide, walkthrough, showcase)
- `wa-prompt` — prompt-crafting content (god mode directives, character creation prompts)
- `wa-character` — character sheet or character guide
- `wa-persona` — NPC personalities, MBTI, alignment

**Player-facing**
- `wa-tutorial` — how-to-play guides
- `wa-faq` — frequently asked questions

**Reference**
- `wa-glossary` — glossary terms
- `wa-comparison` — comparison with other tools
- `wa-history` — historical / changelog

**Meta**
- `meta` — pages about the wiki itself
- `placeholder` — skeleton stub awaiting content

If you need a new tag, add it to this list before using it.

## Type Taxonomy

- `entity` — a noun: the game, a character, a system, a campaign
- `concept` — an idea: combat, god mode, dice integrity
- `comparison` — side-by-side (e.g. WA vs AI Dungeon)
- `query` — answered research question
- `summary` — synthesis of multiple sources
- `source` — raw source reference (campaign dumps, transcripts)
- `schema` — meta page (this file, taxonomy)
- `tutorial` — step-by-step how-to (deprecated alias of `concept` with `wa-tutorial` tag)

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source.
- **Add to existing page** when a source mentions something already covered.
- **DON'T create a page** for passing mentions or trivia.
- **Split a page** when it exceeds ~250 lines.
- **Archive a page** when content is fully superseded — move to `_archive/`, remove from index.

## Entity Pages

One page per notable entity (the game, a campaign, a character archetype, a system).
Include:
- Overview / what it is
- Key facts
- Relationships to other entities via `[[wikilinks]]`
- Source references

## Concept Pages

One page per concept. Include:
- Definition / explanation
- How it works in play
- Why a player cares
- Related concepts via `[[wikilinks]]`

## Comparison Pages

Side-by-side. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy

When new information conflicts with existing content:
1. Check the dates — newer sources supersede older.
2. If genuinely contradictory, note both positions with dates and sources.
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`.
4. Flag for player review in the lint report.
