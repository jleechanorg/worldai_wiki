# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-06-21] update | External user stories — review fixes
- Re-prefixed story IDs from US-NNN to EXT-NNN throughout
  `queries/ExternalUserStories.md` to avoid collision with US-001..US-075 in
  [PlayerUserStories](PlayerUserStories.md). Added an EXT↔US mapping table at
  the top of the page.
- Removed the `[Settings](#)` placeholder link in EXT-027.
- Removed internal CSS class names from EXT-033 (replaced with behavioural
  descriptions).
- Fixed cross-link text in US-068: progression reasoner now points to
  [US-015 Level-Up Modal Lock & Atomicity](PlayerUserStories.md#us-015-level-up-modal-lock-atomicity)
  and Campaign Wizard onboarding now points to
  [Campaign Wizard](../entities/CampaignWizard.md).
- Removed `mvp_site/` mentions from ExternalUserStories body and
  CLAUDE.md/AGENTS.md (kept the term only where it documents the negative
  "we do not expose" rule).
- Refactored CLAUDE.md from a 166-line duplicate of AGENTS.md to an 83-line
  thin pointer that defers to AGENTS.md on shared sections (per Greptile
  P2 on PR #4: avoid content duplication that drifts on first update).
- Bumped `updated` in ExternalUserStories frontmatter to 2026-06-21.

## [2026-06-20] update | External user stories (US-026–US-100)
- Added `queries/ExternalUserStories.md` — 75 external-facing stories mirroring internal PR
  [#7709](https://github.com/jleechanorg/worldarchitect.ai/pull/7709) sections 13–20.
- Audience rewrite: no internal code paths, no file:line refs; player and external-developer language only.
- Cross-linked from `queries/PlayerUserStories.md`, `index.md`, and `README.md`.

## [2026-06-20] create | CLAUDE.md and AGENTS.md
- Added `CLAUDE.md` — Claude-Code-specific guidance (scope, voice, build/lint, PR workflow).
- Added `AGENTS.md` — repo-wide agent contract (schema, editing protocol, source ingestion, non-negotiables).
- Updated frontmatter `updated` on existing pages; added cross-links in `index.md`.

## [2026-06-19] create | worldai_wiki initialized
- Domain: WorldArchitect.AI player-facing wiki
- Repo: `jleechanorg/worldai_wiki` (public)
- Structure created with SCHEMA.md, index.md, log.md, README.md, LICENSE
- Skeleton pages for core concepts
- Initial content batch: ~50 entity/concept pages copied & rewritten from `~/llm_wiki`
- Campaign synthesis: CampaignDesign, GodModePrompting, CampaignShowcase, ItachiGaiden
- Player user stories: 75 stories ingested from `jleechanorg/worldarchitect.ai/docs/user-stories-general.md` and expanded

## [2026-06-19] ingest | Player user stories from worldarchitect.ai/docs/user-stories-general.md
- 25 baseline stories copied + 50 new stories synthesized from mvp_site/ surface area
- See `queries/PlayerUserStories.md`
- Source: https://github.com/jleechanorg/worldarchitect.ai/blob/main/docs/user-stories-general.md (private repo, public-read summary)

## [2026-06-19] ingest | Game-relevant content from ~/llm_wiki
- 40+ entity/concept pages copied and rewritten for player audience
- Source paths: `~/llm_wiki/wiki/entities/{WorldAI,WorldArchitect,DnD5eSRD,...}.md`, `~/llm_wiki/wiki/concepts/{Combat,GodMode,Faction*,Dice*,...}.md`
- Player-facing rewrite: removed mvp_site/ code paths, kept behavioral descriptions

## [2026-06-19] synthesize | Campaign + god-mode guide
- Walked Itachi V2 (432 scenes, 1.27 MB) and Aristocrat V2 (50 scenes, 280 KB) campaign dumps
- Extracted directive patterns, level progression, player-prompt patterns
- Output: concepts/CampaignDesign.md (3000+ words), concepts/GodModePrompting.md (2500+ words), entities/ItachiGaiden.md (campaign case study)

## [2026-06-22] update | raw/ mirror wikilink render-safety
- Replaced 2 raw `[[queries/PlayerUserStories]]` wikilinks in `raw/worldarchitect.ai-docs-user-stories-general.md` with github.com-compatible markdown links (`[queries/PlayerUserStories](../queries/PlayerUserStories.md)`). Raw Obsidian-style wikilinks render as literal `[[brackets]]` text on github.com and break navigation for any reader clicking through from a wiki page to a raw/ source mirror.
- Extended `scripts/lint_wikilinks.py` with a render-safety scan over `RENDER_SAFETY_DIRS` (currently `raw/`) — flags any raw `[[wikilink]]` in those files, independent of whether the target resolves. The broken-wikilink scan still excludes `raw/` (raw/ files may legitimately reference pages that don't exist in the wiki).
- Added 2 tests: `test_no_raw_wikilinks_in_raw_directory` pins the contract that the shipped wiki has zero raw wikilinks in `raw/`; `test_lint_script_catches_raw_directory_wikilinks` pins the contract that the linter's render-safety scan covers `raw/`.
- Updated `AGENTS.md` and `SCHEMA.md` to make the `raw/`-also-rendered-on-github.com rule explicit.
- Bug-ref: 2026-06-22 — Jeffrey reported the player-facing systems table on `entities/WorldArchitect.md` rendered `[[concepts/Combat]]` literal text. Root cause was a raw/ mirror file in the same surface area, not the entity page itself.

## [2026-08-04] create | House of the Dragon custom-campaign template (paste-ready 9-section bible + setup walkthrough verified live against worldarchitect.ai Custom Campaign wizard)

## [2026-08-05] update | HotD wiki — Character-field customization note per Slack ts=1785909171.805539

## [2026-08-05] update | HotD wiki — restructure into Quick Setup + More Details per Slack ts=1785909171.805539

## [2026-08-05] update | HotD wiki — address 7 CodeRabbit review comments (index date, fenced code MD040, dragon-size consistency, Blood-of-the-Dragon reachability, Baela/Jacaerys relationships, bible-size unit, log-line format)

## [2026-08-05] update | HotD wiki — correct wizard checkbox defaults (verified live against `mvp_site/frontend_v1/js/campaign-wizard.js` + local `TESTING_AUTH_BYPASS=true` Playwright run): Narrative/Mechanics/Companions/Default-World are ALL checked by default; only Default-World needs unchecking for ASOIAF/HotD

## [2026-08-05] update | HotD wiki — promote character-customization examples into Quick Setup (gender, age, class, dragon name, parent swap, look, starting relationship per Slack ts=1785909171.805539 OOB); /advice review (deleg_765bfb72) flagged 354-line page length + missing "after Enter the World" section

## [2026-08-13] create | House of the Dragon — The Ashen Crown (Rhaenyra) — hardcore political-realism campaign bible (per user request 2026-08-13)

- New query: `queries/house-of-the-dragon-ashen-crown-rhaenyra.md` — slimmed paste-bible for the WorldArchitect.AI Custom Campaign wizard (≤16K chars), with the Quick Setup walkthrough, character-customization hooks, LLM-edit meta-prompt, and troubleshooting.
- New raw mirror: `raw/hotd-ashen-crown-source-link.md` — pointer page to the long-form source at https://github.com/jleechanorg/llm-wiki/blob/main/wiki/sources/house-of-the-dragon-ashen-crown.md (50,786 bytes / ~8,500 words).
- Updated `index.md` Start-here list with one-line summary.
- Show anchor: House of the Dragon Season 3 finale (post-Tumbleton, Helaena-dead, Jace-dead-at-Gullet, Aegon-alive-on-Dragonstone). Book (Fire & Blood 2018) fallback only where Season 3 cut off or diverged.
- Class: Bard (College of Swords) Level 11 + custom Dragonrider subclass Levels 1-20. Divine Ascension track at L25 (optional, gated).
- GRRM-faithful magic only — blood of the dragon, dragon dreams, dragon-egg pyre resurrection. No 5e spells above L6.
- Quad-Pillar mechanics: Crown Stability (CS) / Treasury Liquidity (TL) / Paranoia & Tyranny Rating (PTR) / Dragonseed Loyalty (DL) with quantified baselines (22% / 350gp / 65 / -15..+60).
- 7-archetype dragon class system (Sovereign / Blood Wyrm / Bronze Titan / Silver Swift-Wing / Ancient Colossus / Wild Drake / Sun Drake [Maimed Miracle]).
- 12 NPC dramatis personae + 10-house Allegiance matrix + Shepherd's Mob non-house faction.
- Level-up XP rule (per user 2026-08-13): `0.34 × (next_level_threshold - current_level_threshold)` per die roll using standard D&D 5e cumulative thresholds (L2=300..L20=355000). NO XP during god mode or time-frozen turns.
- Companion to the existing Bastard's Claim template (`queries/house-of-the-dragon-campaign.md`) — different character (Rhaenyra canon vs Daemon bastard), different starting state (post-Tumbleton vs eve of Dance).
- Source provenance: Gemini 3.6 Flash share `share.gemini.google/jVxwLgRd0jCK` (canonical long-id `e449d2a6c718?skid=c2d0d9e2-95fc-49cc-8349-c981ee022bd0`) captured 2026-08-13 via `~/.hermes/skills/read-gemini-share-link/SKILL.md`. Authored by hermes-agent (MiniMax-M3).
