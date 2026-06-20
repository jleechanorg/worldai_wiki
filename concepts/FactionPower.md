---
title: FactionPower
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Faction Power

How strong your faction is, calculated from members, resources, territory, and equipment.

## Power sources

- **Members**: each named NPC contributes their personal combat power.
- **Generic troops**: foot soldiers, archers, mages. Cheaper but weaker per unit.
- **Resources**: gold for hiring, food for sustaining, materials for building.
- **Territory**: zones you control. Each zone has economic value and defensive bonuses.
- **Equipment**: better gear multiplies your members' effectiveness.
- **Reputation**: standing in the world. Affects recruitment and diplomacy.

## Calculation

The system computes a faction's power as a sum of:
- Member levels (sum or weighted average)
- Resource stockpiles
- Territory value
- Defensive structures

The exact formula is internal, but the in-game UI shows your faction's current power and its rank.

## What power affects

- **Rankings**: higher power = higher rank.
- **Battle outcomes**: power differential shifts combat odds.
- **AI aggression**: powerful factions attract attention from NPCs.

## Player tips

- **Named NPCs > generic troops**: one named character at level 10 is worth more than 20 level-1 footmen.
- **Diversify**: a faction with all fighters is vulnerable to mages. Build a balanced roster.
- **Invest in intel**: intelligence multiplies your effective power.
- **Don't overextend**: more territory = more places to defend. Consolidate before expanding.

See [FactionSystem](FactionSystem.md), [FactionPlay](FactionPlay.md), [FactionRankings](../entities/FactionRankings.md).
