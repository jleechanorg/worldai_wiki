---
title: RestAndDeath
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic]
sources: []
---

# Rest & Death

How characters recover and what happens at 0 HP.

## Short rest

A short rest is ~1 hour of light activity. During a short rest, you can:
- Spend hit dice to recover HP (one at a time, rolling the hit die + CON modifier)
- Use class features that recharge on short rest (e.g., Fighter Second Wind, Warlock spell slots)

## Long rest

A long rest is ~8 hours, with at least 6 hours of sleep. After a long rest:
- HP restored to maximum
- Half your spent hit dice recovered (minimum 1)
- Most class features and ability uses restored
- Spell slots restored to maximum
- Conditions like exhaustion reduced by 1

You can only benefit from one long rest per 24-hour period. Interrupting the rest with more than 2 hours of activity forfeits it.

## Death & dying

When you drop to 0 HP:
- You fall **unconscious**.
- If the damage that dropped you was from a critical hit or a melee attack, you start with one failed death save.
- Otherwise, you start with 0 successes and 0 failures.
- At the start of each of your turns, roll `1d20`:
  - **10+**: one death save success.
  - **9 or lower**: one death save failure.
  - **Natural 20**: you regain 1 HP and become conscious.
  - **Natural 1**: counts as two failures.
- **3 successes**: you stabilize. Unconscious but no longer dying.
- **3 failures**: you die.

## Stabilizing

- A creature can be stabilized by a successful DC 10 Medicine check.
- Spare the Dying (cantrip) auto-stabilizes.
- A healing potion restores 1 HP (conscious, no longer dying).

## Resurrection

Magical resurrection (Revivify, Raise Dead, Resurrection, True Resurrection, etc.) can bring back the dead. Higher-level spells restore more time and additional features. Some settings restrict resurrection (no-rez worlds).

## Player tips

- **Short rest often**: many classes (Warlock, Fighter, Monk) recover major features on short rest. Hit dice are precious.
- **Long rest before tough fights**: make sure you have full HP and resources before a boss.
- **Healing potions in combat**: drinking a potion uses your action. Don't waste turns.
- **Death saves are dangerous**: any healing brings you back. Even 1 HP.

See [[concepts/Combat]], [[concepts/Healing]].
