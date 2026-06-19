---
title: FactionSystem
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-system, wa-mechanic]
sources: []
---

# Faction System

WorldArchitect.AI includes a complete faction minigame: lead a faction, gather intel, fight rivals, climb the rankings.

## What you do as a faction leader

1. **Manage resources**: gold, members, influence, territory.
2. **Gather intel**: scout rival factions, learn their plans, find weaknesses.
3. **Recruit and train**: build up your roster of named NPCs.
4. **Combat rivals**: send your forces against enemy factions, or defend your holdings.
5. **Climb the rankings**: from street gang to kingdom-level organization.

## Core subsystems

- **Intel** ([[entities/FactionIntel]]): information-gathering. Higher intel = better combat odds against that faction.
- **Combat** ([[entities/FactionBattleSim]]): faction-vs-faction battle resolution. Doesn't replace personal combat; runs alongside it.
- **Power** ([[concepts/FactionPower]]): calculated from members, resources, territory, equipment.
- **Rankings** ([[entities/FactionRankings]]): how your faction is ranked against others. Climb by winning battles and growing power.
- **State util** ([[entities/FactionMinigame]]): the orchestration layer that ties everything together.

## How a faction turn works

A "faction turn" typically happens between major plot beats:

1. **Plan**: declare what you want your faction to do this turn (gather intel, attack rival X, recruit, fortify).
2. **Resolve**: the system simulates the faction's actions, including:
   - Intel gains
   - Combat outcomes (if any)
   - Resource changes
   - Reputation shifts
3. **Narrate**: the GM describes what happened in faction terms.

## When does faction mode activate?

Faction mode is opt-in. When you create a campaign, you can flag it as a faction-led campaign. Once active, the FactionManagement agent handles faction turns alongside the main story.

## The Nocturne BG3 V3 example

The 600+ scene Nocturne BG3 V3 campaign is a faction-mode showcase. The player leads a Baldur's Gate 3 faction through:
- Intel operations against the Goblin Camp
- Combat against the Duergar
- Alliance-building with the Tieflings
- Territory expansion into the Underdark
- Power escalation to mid-game power levels

See [[entities/NocturneBg3]] for the case study.

## Player tips

- **Intel before combat**: always scout before attacking. Unprepared attacks can lose you members.
- **Diversify holdings**: don't put all your resources in one territory.
- **Recruit named NPCs**: a party with named characters (each with stats) fights better than a horde of generic soldiers.
- **Watch the rankings**: rankings determine who attacks you. Climb too fast and rivals notice.

See [[concepts/FactionPlay]], [[concepts/FactionPower]], [[concepts/FactionManagement]].

## Sources

- `~/worldarchitect.ai/mvp_site/faction/` (private code).
- `~/llm_wiki/wiki/sources/faction-nocturne-bg3-v3-entry-*.md` — 600+ scene campaign dump.
