---
title: DiceAuthenticity
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Dice Authenticity

Nobody in this game decides what a die landed on — not you, and not the AI running the game. Every roll comes out of real random-number code, and the server does the arithmetic and calls success or failure itself.

## Why it works this way

If either side could simply announce a result, the rules would stop meaning anything: crits whenever you wanted them, failures never. So neither side gets to announce one. When you fail a save, you take the damage. When the goblin crits you, you are at 0 HP. Nothing softens it afterwards.

## What the game guarantees

1. **You describe the action; the game produces the roll.** You type "I attack the orc." There is no Attack button and no Roll button — the roll comes back with the narration.
2. **The difficulty is fixed before the dice.** The GM has to state the target number and explain it before any die is generated, and turns where that order breaks down get flagged. It cannot see the roll, dislike the outcome, and move the goalposts.
3. **The roll has to use the seed the server committed to.** Before the turn, the server generates a secret seed and records its fingerprint. Afterwards it checks that the roll used that exact seed.
4. **Every face has to be possible.** A d6 cannot come back as a 9.
5. **The server recomputes the arithmetic.** It takes the raw faces, applies keep-highest or keep-lowest, applies the modifier, and decides success or failure. Where the GM's numbers disagree, the server's answer is what gets stored and shown.
6. **Natural 1 and natural 20 are absolute.** A raw 1 on the kept d20 always fails and a raw 20 always succeeds, whatever your modifier and whatever the DC.
7. **Each roll is stored with its turn** — the notation, every raw face, the modifier, the kept face, the total, the target number, and what the roll was for. Rolls are ordered by the turn they belong to rather than stamped with their own clock time.

When something does not line up, the turn gets flagged rather than quietly accepted. You cannot hand the game a result you made up, and neither can the GM.

## What you can see

Every turn shows its own rolls in the dice area above the narration, so scrolling back through the story shows every roll in order.

There is no roll-history screen, no replay view, and no export.

Turning on **Settings → Debug Mode** shows you more, not less: alongside the GM's notes and its reasoning about state changes, each turn lists its rolls in full, including ones normally kept behind the screen — a guard's Perception check against your Stealth, for instance.

What nothing in the app shows yet is the fairness record itself. The seed, its fingerprint, and the verification result are stored with every turn, but there is no screen that displays them.

## Common questions

- **"Can I roll my own d20?"** Not in standard play. The game produces the roll.
- **"Can you just say I rolled a 15?"** The GM is the game; it will not fudge a number for you.
- **"Where did my numbers go?"** Probably the **Hide dice rolls** display setting — see [Dice](Dice.md).

## What you actually do

You type what your character does. The rolls, the target numbers, and the outcome come back together with the narration. [Dice](Dice.md) has the full turn sequence.

See [Dice](Dice.md), [DiceNotation](DiceNotation.md), [DiceFAQ](../queries/DiceFAQ.md).

## Sources

- D&D 5e Basic Rules (free SRD).
