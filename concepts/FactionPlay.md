---
title: FactionPlay
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Faction Play

What faction-mode gameplay looks like scene-by-scene.

## The faction turn

A faction turn is a discrete planning + resolution cycle. The system prompts you for orders, simulates the results, and narrates the outcome.

### Example turn

> **Turn 7 — Faction Turn**
>
> Plan:
> 1. Send scouts to the Goblin Camp (intel).
> 2. Hire 5 archers (cost: 200gp).
> 3. Defend our territory.
>
> Resolve:
> - Intel operation: success. +3 Goblin intel, learned that the camp has 30 goblins and a shaman.
> - Recruitment: success. 5 archers joined.
> - Defense: no attacks this turn.
>
> Narrative: "Your scouts return from the western woods with maps of the Goblin Camp. The five new archers report for duty at the garrison. All quiet on the eastern front."

## Combat resolution

When two factions fight, the system runs a [FactionBattleSim](../entities/FactionBattleSim.md):
1. Power comparison (with intel modifier).
2. Roll for initiative, casualties, outcome.
3. Apply consequences: member losses, territory changes, reputation shifts.

## Player tips

- **Plan ahead**: faction turns take time. Don't neglect them.
- **Balance offense and defense**: an undefended faction is a target.
- **Build relationships**: NPC factions can be allies or rivals. Diplomacy matters.

See [FactionSystem](FactionSystem.md), [FactionPower](FactionPower.md), [NocturneBg3](../entities/NocturneBg3.md) for the case study.
