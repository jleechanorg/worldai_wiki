---
title: Wiki Schema
created: 2026-06-19
updated: 2026-09-18
type: schema
tags: [meta]
---

# Wiki Schema

How every page in this wiki is written. Following it keeps the wiki browseable, navigable, and durable as content grows.

**Content pages** live in `comparisons/`, `concepts/`, `entities/` and `queries/`. The rules below apply to them and to this file. `README.md`, `index.md`, `log.md`, `AGENTS.md` and `CLAUDE.md` are repo furniture and carry no frontmatter.

## Domain

WorldArchitect.AI player-facing wiki — how to play the game, how to design campaigns, how to write god-mode directives that shape narration, how the major systems (combat, factions, dice, level-up, character creation) work.

This is the **player-facing** companion to the private `jleechanorg/worldarchitect.ai` code repo. We explain what the game does; we do not expose proprietary code paths.

## File Conventions

- **File names:** PascalCase, no spaces, matching the page's subject — `Combat.md`, `GodModePrompting.md`, `ItachiGaiden.md`. That is what almost every page on disk uses. The exception is `queries/`, where a page answering a long question may use lowercase-with-hyphens instead: `how-to-play-worldai.md`, `house-of-the-dragon-campaign.md`. Never rename an existing page without updating every inbound link.
- **Every content page** starts with YAML frontmatter (see below).
- **Every content page** has at least 2 outbound links to other wiki pages. Use github.com-compatible markdown links (e.g. `[Display Text](path/Page.md)`), not Obsidian-style wikilinks (`[[Page]]`), so the wiki is clickable on github.com blob view. Run `python3 scripts/lint_wikilinks.py` to verify, and `python3 scripts/check_http_links.py` when you add external URLs.
- **Never link to something a reader can't open.** The game's code repo is private, so a `github.com/jleechanorg/worldarchitect.ai/...` link gives a public reader a 404. Link to the live site or to another wiki page instead.
- **Cite what a reader can check.** A page that asserts something about the world outside this wiki — a competitor's features, published rules, an external tool — ends with a `## Sources` section naming those sources with a date checked. Pages that only describe how WorldArchitect.AI behaves do not need one; most concept pages have none, and that is correct.
- When updating a page, bump the `updated` date.
- New pages must be added to `index.md` under the correct section. **Never list a page in `index.md` or `README.md` before it has content** — an advertised stub is worse than a missing page.
- Every editing session appends an entry to `log.md`, newest first.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | schema
tags: [from taxonomy below]
sources: [path/ToAnotherPage.md]
---
```

Required: `title`, `created`, `updated`, `type`, `tags`. `sources` is optional — use it when the page was written from another wiki page, and leave it as `[]` otherwise.

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
- `wa-faction` — faction play: armies, intel, rankings, faction campaigns

**Player-facing**
- `wa-tutorial` — how-to-play guides
- `wa-faq` — frequently asked questions

**Reference**
- `wa-glossary` — glossary terms
- `wa-comparison` — comparison with other tools
- `wa-history` — historical / changelog

**Meta**
- `meta` — pages about the wiki itself

If you need a new tag, add it to this list before using it. There is deliberately no stub tag: write the page or don't create the file.

## Type Taxonomy

Only these five are in use:

- `entity` — a noun: the game, a character, a system, a campaign
- `concept` — an idea: combat, god mode, dice integrity
- `comparison` — side-by-side (e.g. WA vs AI Dungeon)
- `query` — an answered player question, including step-by-step guides (tag those `wa-tutorial`)
- `schema` — meta page (this file)

## Page Thresholds

- **Create a page** when a player would look for that subject by name, and there is enough to say to fill one.
- **Add to an existing page** when the subject is a facet of something already covered.
- **DON'T create a page** for passing mentions or trivia, and never create an empty one.
- **Past ~250 lines**, look for a split. Three pages currently run longer because they are single walkthroughs that would be worse in pieces; that is the bar for an exception.
- **Archive a page** when content is fully superseded — move to `_archive/`, remove from index, and repoint every inbound link.

## Voice

Write for a player who has never seen the code and never will.

- Say what the player sees, clicks and types. Never name an internal field, module, function, collection or file path — if a sentence needs one to make sense, the sentence is aimed at the wrong reader.
- Put the reader's question before the answer. A heading they'd actually ask beats a noun.
- Don't assert what you can't check. If the game doesn't define something, say so — "the game doesn't decide this; the GM does" is a real answer.
- Shorter is the goal. A page that loses a third of its words and gains a reader is a good edit.

## Page Shapes

**Entity** — a notable noun: the game, a campaign, a character archetype, a system. What it is, the facts that matter, and how it connects to other pages.

**Concept** — one idea: combat, god mode, dice integrity. What it means, how it works in play, and why a player should care.

**Comparison** — what is being compared and why, a table of the dimensions, then what each side is actually good at. Every claim about the other product needs a dated source.

**Query** — one player question, answered, including step-by-step walkthroughs.

## Update Policy

When new information conflicts with what a page says:

1. Check dates — newer wins.
2. Check the game itself before rewriting. The page is wrong more often than the game is.
3. Resolve the conflict rather than recording both sides. Two pages that disagree is a bug, not a nuance; fix every page that carries the stale claim, not just the one you're in.
4. If you genuinely cannot resolve it, say which parts are uncertain in the page text, with the date you checked.
