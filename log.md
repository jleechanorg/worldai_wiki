# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

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
