---
title: FactionBattleSim
created: 2026-06-19
updated: 2026-09-18
type: entity
tags: [wa-system, wa-mechanic]
sources: []
---

# Faction Battle Simulator

When you order one faction to attack another, the server — not the GM's imagination — resolves the fight. This is the piece that decides who wins.

## What decides the battle

**Only the two armies.** How many soldiers and elites each side fields, what kind of elites they are — a veteran and a high-level champion are not the same unit — and how fortified the defender is, on a scale of 0 to 3. Your gold, your territory and your Faction Power score play no part. Spies do not fight.

**Not intel.** A successful spy operation gives you a stated combat bonus of +5% to +20% for a few turns, but the battle itself is worked out from troops and fortifications alone. Say that you are attacking on the strength of your scouting report, so the GM works the advantage into how the fight is narrated.

## How it resolves

1. **Line up.** Each side's units are built into blocks with hit points, armour and damage. The defender's fortifications make its troops harder to hit.
2. **Rounds of attrition.** The two armies trade casualties round by round, for up to 100 rounds.
3. **No dice, by default.** The result comes from average damage rather than rolls, so the same two armies always produce the same outcome. Bring more troops or fewer — the fight is not going to surprise you.
4. **Rout.** A side cut to a quarter of its starting strength breaks and runs, and the battle ends there.
5. **Spoils.** The simulator reports casualties, the winner, and how long it took. What you actually take — territory, gold, prisoners — the GM applies afterwards, within the caps below.

## Picking your attack

| Order | Territory you can take | What it needs |
|---|---:|---|
| `assault` | up to 10% | Survivors worth 5x the target's territory; full upkeep; captures forts |
| `skirmish` | up to 5% | Survivors worth 2.5x the target's territory; the defender's forts count for less |
| `pillage` | varies | Burns farms and steals citizens and gold rather than holding ground |

## What this is not

- **Your character's own fights.** One character swinging a sword in initiative order is ordinary [Combat](../concepts/Combat.md), not this.
- **Mass combat.** Field 20 or more units in a scene and the game switches to army-vs-army tactical rules with initiative, terrain and morale checks. That happens automatically and is separate from the faction minigame's battle tool.
- **Diplomacy.** Proposing an alliance is its own action and is never resolved by a fight.

## Tips

- **Bring fortifications home, buy them abroad.** A defender's forts hurt. Yours make you expensive to attack and are worth 1,000 [Faction Power](../concepts/FactionPower.md) each.
- **Count survivors, not victories.** An assault that wins but leaves you below 5x the target's territory takes nothing.
- **Elites are worth their price.** A handful of high-level elites changes a fight far more than the same gold spent on line troops.

See [FactionSystem](../concepts/FactionSystem.md), [FactionPower](../concepts/FactionPower.md), [FactionIntel](FactionIntel.md).
