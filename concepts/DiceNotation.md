---
title: DiceNotation
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-glossary]
sources: []
---

# Dice Notation

The grammar for describing a dice roll. WorldArchitect.AI supports standard D&D 5e notation plus a few extensions.

## Basic

- **`NdS`**: roll N dice with S sides. Example: `2d6` = roll 2 six-sided dice.
- **`NdS+M`**: roll N dice, sum them, add M. Example: `1d20+5` = 1d20 + 5.
- **`NdS-M`**: subtract M. Example: `1d20-2`.

## Keep / drop

- **`NdSkhK`**: roll N dice, keep the K highest. Example: `4d6kh3` = ability score generation.
- **`NdSklK`**: keep the K lowest.
- **`NdSdhK`**: drop the K highest.
- **`NdSdlK`**: drop the K lowest.

## Advantage / disadvantage

- **`1d20 adv`**: roll twice, take the higher.
- **`1d20 dis`**: roll twice, take the lower.

## Reroll

- **`NdSr1`**: reroll any 1s once.

## Exploding

- **`NdS!`**: if any die shows its max value, roll it again and add. Example: `3d6!` on 6+6+5 = 6+6+5+1 (the 6 exploded into another d6).

## Examples in play

| Roll | Use case |
|------|----------|
| `1d20+5` | Standard attack roll (level 5 fighter with +5 to hit) |
| `2d6+3` | Longsword damage |
| `1d20+7 adv` | Stealth check with advantage |
| `4d6kh3` | Rolling an ability score (do this 6 times) |
| `8d6` | Fireball damage |
| `1d20+12` | High-level save (DC 20 vs level 15 monk) |

## Common pitfalls

- **`d20` is one die**, not twenty `d20` rolls.
- **Modifiers are added once**, not per die. `2d6+3` is not `2*(d6+3)`.
- **Negative modifiers** can drop the result below 1 but never below the die's minimum. `1d20-5` is in `[0, 15]`.
- **Critical hits** (nat 20 on attack roll) double the damage dice, not the modifier.

See [Dice](Dice.md) for the broader dice system.
