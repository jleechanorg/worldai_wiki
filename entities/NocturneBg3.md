---
title: NocturneBg3
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [wa-campaign, wa-faction]
sources: [raw/faction-nocturne-bg3-v3-entry-001.md, raw/faction-nocturne-bg3-v3-entry-100.md, raw/faction-nocturne-bg3-v3-entry-500.md]
scene_count: 600
---

# Nocturne BG3 V3 — Faction-Mode Case Study

A 600+ scene Baldur's Gate 3 faction-mode campaign. Demonstrates the faction minigame end-to-end: intel gathering, faction combat, power rankings, resource management, multi-faction diplomacy.

## What this campaign is

The player leads a Baldur's Gate 3 faction through the early-game events of the BG3 narrative. The faction-mode toggle is on, so each scene can include:

- **Faction turns** (planning + resolution)
- **Personal combat** (the PC as an individual)
- **Faction combat** (the faction's forces vs rivals)
- **Diplomacy** (with other factions like the Tieflings, Goblins, Druids, Duergar)

## What the campaign demonstrates

### 1. Faction mode is end-to-end playable

600+ scenes show that the faction minigame is not a side feature — it's a full game mode. The player can run a faction as their primary activity, with personal combat as occasional interruption.

### 2. Intel → combat → power is the core loop

The Nocturne BG3 V3 campaign follows this pattern:

1. **Intel**: send scouts to learn about a rival.
2. **Combat**: attack with intel advantage.
3. **Power gain**: defeated faction's resources add to your power.
4. **Ranking climb**: higher ranking attracts more rivals.

This is the same loop the [Faction System documentation](../concepts/FactionSystem.md) describes, played out over 600 scenes.

### 3. Diplomacy matters

The campaign includes interactions with multiple factions:
- **Goblins**: early antagonist; the player can ally, fight, or ignore.
- **Tieflings**: refugees in the druid grove; ally-able.
- **Druids**: grove defenders; can be allied or fought.
- **Duergar**: deep gnomes in the Underdark; hostile by default.
- **Mind flayers**: the absolute enemy; late-game threat.

The player chooses when to fight and when to negotiate. Faction mode rewards strategic diplomacy.

### 4. Power ranks escalate

By scene 600+, the player faction was a major regional power. The progression went:
- **Scenes 1-50**: small camp, defending territory.
- **Scenes 50-200**: building roster, taking first rival camps.
- **Scenes 200-400**: regional dominance, multi-faction alliances.
- **Scenes 400-600+**: planar threats emerge, faction grows to handle them.

The arc mirrors a typical BG3 run: local → regional → planar.

## Source notes

The 600+ per-scene entries live in `~/llm_wiki/wiki/sources/faction-nocturne-bg3-v3-entry-XXX.md` (numbered 001 through 600+). Each entry is a single scene dump. For the player-facing wiki, we synthesize them rather than copy them — see [FactionPlay](../concepts/FactionPlay.md) and [FactionSystem](../concepts/FactionSystem.md) for the gameplay loop.

## Key takeaways for your own campaign

1. **Faction mode is a real game mode**, not a side feature. 600+ scenes prove it.
2. **Intel → combat → power** is the core loop. Plan around it.
3. **Diplomacy** with multiple factions is rewarded.
4. **Power rankings** escalate over time. Plan for the jump from local to regional.
5. **Faction-mode campaigns** benefit from a longer planned arc than solo campaigns.

## Sources

- `~/llm_wiki/wiki/sources/faction-nocturne-bg3-v3-entry-*.md` (600+ files).
- See [FactionSystem](../concepts/FactionSystem.md), [FactionPlay](../concepts/FactionPlay.md), [FactionPower](../concepts/FactionPower.md).
