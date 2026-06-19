---
title: DiceAuthenticity
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Dice Authenticity

WorldArchitect.AI enforces anti-fabrication on dice rolls. This is one of the game's defining features.

## The problem

In freeform LLM play (e.g., AI Dungeon, raw ChatGPT), the player can just *say* they rolled a 20. The LLM has no way to verify. This breaks the game — critical hits become common, failures never happen, and the rules stop mattering.

## The solution

The platform owns dice rolling:

1. **The system, not the player, rolls.** When you click "Attack", the platform rolls `1d20+modifier` server-side.
2. **The result is shown verbatim** alongside the narration.
3. **The LLM doesn't see the roll until after it's been rolled.** It can't "remember" a fake roll.
4. **Each roll is logged** in the campaign state with timestamp, roll, modifier, and result.
5. **You can't declare a result.** Typing "I rolled a 20" in chat does nothing mechanically.

## Why it matters

Dice authenticity is what makes the game *playable* as a tabletop RPG instead of a collaborative fiction engine. When you fail a save, you actually take the damage. When the goblin crits you, you're actually at 0 HP. The stakes are real.

## Player experience

- You declare an action ("I swing my sword at the orc").
- The system tells you to roll (or auto-rolls).
- You see the result.
- The GM narrates the outcome *based on the actual roll*.
- The state updates (HP, conditions, etc.).

There's no way to "cheat" because there's no opportunity to cheat. The platform rolls, the platform records, the platform enforces.

## Edge cases

- **Player asks to roll manually** ("Can I roll my own d20?"): not supported in standard play. The platform rolls.
- **Player wants to fudge a roll** ("Just say I rolled a 15"): the GM is the platform; it won't lie.
- **Debug / replay mode**: campaign owners can view the roll log to audit outcomes.

See [[concepts/Dice]], [[concepts/DiceRollMechanics]], [[queries/DiceFAQ]].

## Sources

- `~/worldarchitect.ai/docs/user-stories-general.md` (private) — US-002 Dice Anti-Fabrication.
