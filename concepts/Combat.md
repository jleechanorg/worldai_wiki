---
title: Combat
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: [raw/worldarchitect.ai-docs-user-stories-general.md]
---

# Combat

Combat in WorldArchitect.AI follows D&D 5th Edition rules: initiative order, action economy, attack rolls, saving throws, damage, conditions. The game enforces turn order strictly and refuses to let players or NPCs take consecutive turns out of order.

## Turn flow

1. **Initiative**: every combatant rolls `1d20 + DEX modifier`. Order is high-to-low; ties broken by DEX score, then coin flip.
2. **Turns proceed in initiative order**: each combatant gets one turn per round.
3. **Each turn**: a combatant gets one Action, one Bonus Action, one Reaction, and free Movement (based on speed). See [action economy](https://www.dndbeyond.com/sources/basic-rules/combat#Movement) for details.
4. **End of turn**: combatant declares "end turn". The next in order takes their turn.
5. **End of round**: top of initiative starts again.

## Initiative display

The active actor is highlighted in the UI and in narration. The current turn number, HP, conditions, and remaining resources are shown.

## Conditions

Conditions are 5e-standard: Blinded, Charmed, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious. Each grants mechanical advantages/disadvantages and limits actions.

See [[concepts/Dice]] for how attack rolls and damage rolls work.

## Reactions

Some class features and spells trigger as reactions. The system prompts when a reaction is available (e.g., opportunity attacks when an enemy leaves your reach).

## Rest & recovery

See [[concepts/RestAndDeath]]. Short rest = spend hit dice to recover HP. Long rest = recover all HP, half spent hit dice, restore most ability uses.

## Death & dying

At 0 HP, a creature is unconscious and starts making death saving throws (`1d20`, 10+ = success, nat 20 = regain 1 HP, three successes = stabilize, three failures = die). Some creatures have special death rules (e.g., undead might just stop).

## Player tips

- **Use your action economy**: Action + Bonus Action + Movement + Reaction. Wasting any of these is a missed opportunity.
- **Position matters**: ranged attackers should be on high ground. Melee should flank. AoE spells work better when enemies are clustered.
- **Conditions win fights**: Stunned, Restrained, Prone, and Frightened swing combats harder than raw damage.

See [[concepts/Initiative]], [[concepts/Dice]], [[concepts/RestAndDeath]], [[concepts/AbilityScores]].

## Sources

- D&D 5e Basic Rules (free SRD).
- `~/worldarchitect.ai/docs/user-stories-general.md` (private) — US-001 through US-014.
