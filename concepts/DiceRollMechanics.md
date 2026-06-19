---
title: DiceRollMechanics
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic]
sources: []
---

# Dice Roll Mechanics

What actually happens when a die is rolled.

## The pipeline

1. **Action declared** (player says "I attack").
2. **Roll type determined** (1d20+5 for attack, 2d6+3 if hit, etc.).
3. **Roll generated** by the platform's RNG (server-side, logged).
4. **Result displayed** to player and GM.
5. **Outcome applied** (hit/miss, damage, conditions, state changes).
6. **Narration generated** by the LLM based on the actual outcome.

## When rolls happen automatically

- Initiative at combat start
- Death saves at 0 HP
- Saving throws when triggered
- Loot tables (some)
- Random encounters (in some modes)

## When rolls happen on player click

- Attack rolls
- Skill checks (when player initiates)
- Ability checks (when player initiates)
- Damage rolls (after a hit)
- Healing rolls
- Spell attack rolls

## Sources

- `~/worldarchitect.ai/docs/user-stories-general.md` (private) — US-002 through US-004.
- See [[concepts/Dice]].
