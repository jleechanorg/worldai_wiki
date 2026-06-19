---
title: FactionBattleSim
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [wa-system, wa-mechanic]
sources: []
---

# Faction Battle Simulator

The system that resolves faction-vs-faction combat. When you declare an attack on a rival, the simulator runs.

## How it works

1. **Power calculation**: each side's power is calculated from members, resources, intel, equipment.
2. **Intel modifier**: the attacker gains a bonus if they have intel on the defender.
3. **Random roll**: a deterministic RNG roll determines the outcome.
4. **Outcome application**: casualties, territory changes, resource transfers applied.

## What's NOT the battle sim

- **Personal combat**: your character fighting an enemy in initiative order is NOT the faction battle sim. That's regular combat ([[concepts/Combat]]).
- **Diplomacy**: negotiating with another faction is a separate action.
- **Single duels**: 1v1 fights use the regular combat system.

## Player tips

- **Gather intel first**: each point of intel gives a combat bonus.
- **Recruit named NPCs**: each named member contributes more power than generic troops.
- **Diversify resources**: a faction with all melee is vulnerable to mages.

See [[concepts/FactionSystem]], [[concepts/FactionPower]], [[concepts/FactionPlay]].
