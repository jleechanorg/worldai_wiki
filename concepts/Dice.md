---
title: Dice
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: [raw/worldarchitect.ai-docs-user-stories-general.md]
---

# Dice

WorldArchitect.AI uses real D&D 5e dice rolling with strict anti-fabrication enforcement. You cannot type "I rolled a 20" — the system rolls the dice for you.

## Notation

Standard D&D 5e notation is supported:

| Notation | Meaning |
|----------|---------|
| `1d20` | Roll 1 twenty-sided die |
| `1d20+5` | Roll 1d20, add 5 (typical attack roll at +5) |
| `2d6+3` | Roll 2 six-sided dice, add 3 (typical damage roll) |
| `4d6kh3` | Roll 4d6, keep highest 3 (ability score generation) |
| `1d20+5 adv` | Roll 1d20+5 with advantage (roll twice, take higher) |
| `1d20+5 dis` | Roll 1d20+5 with disadvantage (roll twice, take lower) |

See [DiceNotation](DiceNotation.md) for the full grammar.

## How it works

1. **You or the GM declares an action** ("I attack the goblin").
2. **The system determines what to roll** (e.g., 1d20+5 for the attack, then 1d6+2 if it hits).
3. **You click "Roll" or the system auto-rolls** (depending on context).
4. **The system displays the result** and updates the relevant state (HP, conditions, etc.).

The LLM does NOT generate dice results. The platform rolls the dice using its own RNG, then the LLM narrates the outcome.

## Integrity guarantees

- **Anti-fabrication**: you can't declare a roll result. The platform rolls.
- **Provable randomness**: each roll's result is logged (visible in the campaign's debug view).
- **Visible results**: rolls and modifiers are shown next to the narration.
- **No retroactive rolls**: rolls happen when the action is taken, not retroactively.

## When the system rolls for you

- **Attack rolls**: any melee, ranged, or spell attack.
- **Saving throws**: when something forces a save.
- **Ability checks**: STR/DEX/CON/INT/WIS/CHA checks.
- **Skill checks**: Athletics, Stealth, Perception, etc.
- **Initiative**: at the start of combat.
- **Damage**: when an attack hits.
- **Death saves**: at 0 HP.
- **Ability score generation**: at character creation.

## Player tips

- **High variance**: 1d20 has a wide spread. Don't plan around a single roll.
- **Modifiers scale**: at high levels, your +15 modifier matters more than the d20. A level 20 fighter rarely misses.
- **Use advantage**: every point of advantage roughly equals +5 in expected value.

See [DiceAuthenticity](DiceAuthenticity.md), [DiceNotation](DiceNotation.md), [DiceRollMechanics](DiceRollMechanics.md), [AbilityScores](AbilityScores.md).

## Sources

- D&D 5e Basic Rules (free SRD).
- `~/worldarchitect.ai/docs/user-stories-general.md` (private) — US-002 dice integrity.
