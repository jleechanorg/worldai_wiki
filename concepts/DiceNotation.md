---
title: DiceNotation
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-glossary]
sources: []
---

# Dice Notation

The grammar behind every roll in the dice area. You will mostly be reading it rather than typing it, since the game produces the rolls for you.

## Basic

- **`NdS`** — roll N dice with S sides. `2d6` is two six-sided dice.
- **`NdS+M`** — roll them, sum them, add M. `1d20+5`.
- **`NdS-M`** — subtract M. `1d20-2`.

## Keep and drop — including advantage

- **`NdSkhK`** — keep the K highest. `2d20kh1` is **advantage**.
- **`NdSklK`** — keep the K lowest. `2d20kl1` is **disadvantage**.
- **`NdSdlK`** — drop the K lowest, the mirror image of keep-highest.
- **`NdSdhK`** — drop the K highest.

Nearly every keep/drop roll you will see is `2d20kh1` or `2d20kl1`. There is no `adv` or `dis` suffix — `1d20+5 (advantage)` is not valid notation here.

The modifier is added once, to the kept die only: `2d20kh1+5` on faces 8 and 17 totals 22, not 30. Both faces stay on screen so you can see which one was dropped.

## Rerolls

There is no reroll suffix. When a feature lets you reroll, the game shows two separate rolls — the original and the replacement. The replacement is the one that counts; the original stays visible so you can see what was discarded.

## One roll per line

Each roll gets its own entry. A Bardic Inspiration die added to a Persuasion check shows as two lines, `1d20+11` and `1d10`, never as a combined `1d20+11+1d10`. Two attacks in a turn show as two `1d20+11` lines, not `2x 1d20+11`.

Modifiers are collapsed into a single signed number and the explanation goes in the label, so you see `1d20+11 (Persuasion: CHA +5, proficiency +3, crown +3)` rather than the breakdown crammed inside the notation.

Dice are bounded too: at most 100 dice in one roll, at most 1000 sides per die, and a die must have at least one side.

## Examples in play

| Roll | Use case |
|------|----------|
| `1d20+5` | Attack roll for a level 5 fighter with +5 to hit |
| `2d6+3` | Longsword damage |
| `2d20kh1+7` | Stealth check with advantage |
| `8d6` | Fireball damage |
| `1d20+12` | A saving throw at high level |

Ability scores are never rolled — character creation uses Point Buy, the Standard Array, or scores you type yourself. See [AbilityScores](AbilityScores.md).

## Common pitfalls

- **The number before the `d` is how many dice, not how many sides.** `1d20` is a single twenty-sided die rolled once — not twenty rolls, and not twenty dice. `20d6` would be twenty six-sided dice, which is a completely different roll.
- **Modifiers are added once**, not per die. `2d6+3` is two d6 summed, then +3 — not 2 × (d6+3).
- **On an advantage roll the modifier applies to the kept die only.** `2d20kh1+5` on faces 8 and 17 totals 22. The dropped face is shown but adds nothing.
- **Negative modifiers are applied straight.** `1d20-5` ranges from -4 to 15; the total is not floored at 0 or 1. What a negative total means is up to the rule being checked — a check simply fails.
- **Critical hits** (a natural 20 on an attack roll) double the damage dice, not the flat damage bonus.

See [Dice](Dice.md) for the broader dice system and [DiceFAQ](../queries/DiceFAQ.md) for common questions.

## Sources

- D&D 5e Basic Rules (free SRD).
