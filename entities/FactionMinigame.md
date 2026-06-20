---
title: FactionMinigame
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [wa-system, wa-mechanic]
sources: []
---

# Faction Minigame

The orchestration layer that ties together [FactionSystem](../concepts/FactionSystem.md), [FactionBattleSim](FactionBattleSim.md), [FactionIntel](FactionIntel.md), [FactionRankings](FactionRankings.md), and [FactionPower](../concepts/FactionPower.md).

## What it does

When faction mode is on:
1. **Initial setup**: you start with a small faction. Choose starting members, territory, resources.
2. **Faction turns**: between major plot beats, you plan and resolve faction actions.
3. **Resource management**: track gold, influence, materials, members, territory.
4. **Diplomacy**: negotiate with other factions.
5. **Combat resolution**: when factions fight, the [FactionBattleSim](FactionBattleSim.md) resolves.
6. **Ranking updates**: after each turn, rankings are recalculated.

## State util module

The faction minigame uses a state util module to keep persistent state:
- Faction definitions
- Member rosters
- Territory ownership
- Resource pools
- Diplomacy state

See [FactionManagement](../concepts/FactionManagement.md) for player-facing controls.

## Sources

- `~/worldarchitect.ai/mvp_site/faction/` (private code).
- `~/llm_wiki/wiki/entities/FactionStateUtil.md` — module reference.
- See [NocturneBg3](NocturneBg3.md) for the case study.
