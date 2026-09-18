---
title: Dice
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Dice

The game rolls the dice, not you. You describe what your character does, and every roll that action needs is produced, checked, and resolved before the reply comes back. Typing "I rolled a 20" does nothing.

## What a roll looks like

Rolls appear above the narration under a **🎲 Dice Rolls** heading, one line each:

```
1d20+11 = 23 vs DC 18 - Success (Persuasion: CHA +5, proficiency +3, crown +3)
2d20kh1+5 = 22 vs DC 15 - Success (Sera Quill - Stealth, advantage)
1d10 = 7 (Bardic Inspiration die)
```

Read it left to right: the notation, the total, the number you had to beat (the DC) and whether you beat it, then — in brackets — who rolled and what for. Damage rolls have no DC, so they show no success or failure.

## Notation

| Notation | Meaning |
|----------|---------|
| `1d20` | Roll one twenty-sided die |
| `1d20+5` | Roll 1d20, add 5 — a typical attack roll at +5 |
| `2d6+3` | Roll two six-sided dice, add 3 — a typical damage roll |
| `2d20kh1+5` | Advantage: roll two d20, keep the higher, add 5 |
| `2d20kl1+5` | Disadvantage: roll two d20, keep the lower, add 5 |

There is no `adv` or `dis` suffix. Advantage is spelled out as two d20 with a keep-highest or keep-lowest marker, so you can always see both faces that were rolled. Full grammar: [DiceNotation](DiceNotation.md).

Ability scores are never rolled here. Character creation offers Point Buy (27 points), the Standard Array (15, 14, 13, 12, 10, 8), or scores you type yourself — no stat-rolling step at all. See [AbilityScores](AbilityScores.md).

## How a roll happens

1. **You describe an action** — "I attack the goblin", "I try to talk the guard down".
2. **The GM works out what to roll** and, for anything with a pass or fail, fixes the target number and records why — before any dice exist.
3. **The dice are produced** from a secret seed the server committed to in advance.
4. **The server checks and recomputes.** It confirms the seed, confirms every face is possible for that die, applies the keep-highest or keep-lowest rule, adds the modifier, and decides success or failure itself. Its numbers are the ones stored and shown.
5. **You see the rolls and the narration together**, and your HP, conditions, and resources update.

There is no Roll button, no Attack button, and no dice tray. Which side physically generates the numbers depends on the AI model running your campaign: on the default models, the model runs real random-number code in a sandbox using the server's seed; on others the server rolls directly. Either way the server owns the arithmetic and the verdict — see [DiceAuthenticity](DiceAuthenticity.md).

## When dice come out

Because of something you did:

- Attack rolls, and damage when the attack lands
- Ability checks — STR, DEX, CON, INT, WIS, CHA
- Skill checks — Athletics, Stealth, Perception, and the rest
- Spell attacks and healing

Because of the situation, whether you asked or not:

- Initiative when combat starts
- Saving throws forced on you by a spell, a trap, or an effect
- Death saving throws while you are at 0 HP
- Loot rolls when a boss or special enemy is defeated

Both kinds are resolved the same way and show up in the same dice area.

## Hiding the numbers

If you would rather read the story than the arithmetic, turn on **Settings → Display → Hide dice rolls**. The dice area then shows a short phrase describing how the roll went instead of the raw numbers. Tap that phrase to reveal the actual roll for five seconds. Combat summaries and loot stay visible either way.

A campaign creator can set this as the default for their campaign. Your own setting always wins over theirs.

## Player tips

- **One d20 is swingy.** Every face is equally likely, so a plan that only works on a high roll fails about as often as it works.
- **Your modifier is the reliable part.** As it grows, the die decides less and less of the outcome.
- **Advantage beats a small flat bonus.** Keeping the higher of two d20 lifts your average result from 10.5 to about 13.8, and against a middling target number it swings your chance of success as far as a +5 would. It does not stack — one source of advantage is the same as three — and any disadvantage cancels it out completely. See [AdvantageDisadvantage](AdvantageDisadvantage.md).

See [DiceRollMechanics](DiceRollMechanics.md), [DiceAuthenticity](DiceAuthenticity.md), [DiceNotation](DiceNotation.md), [DiceFAQ](../queries/DiceFAQ.md), [AbilityScores](AbilityScores.md).

## Sources

- D&D 5e Basic Rules (free SRD).
