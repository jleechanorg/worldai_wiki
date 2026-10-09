---
title: Combat
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Combat

Combat follows D&D 5th Edition: initiative order, action economy, attack rolls, saving throws, damage, conditions.

The GM keeps the turn order. If you try to take a regular action when it isn't your turn, you'll be told whose turn it is and that you'll act when yours comes up in initiative. (Reactions are the exception — those you can use any time their trigger fires.) Nobody's turn gets dropped along the way: every combatant in the order, allies and enemies included, acts once per round.

## Turn flow

1. **Initiative.** Every combatant rolls `1d20 + DEX modifier`, and the order runs high to low. The game defines no tie-break, so if two combatants roll the same total the GM picks an order for them. See [Initiative](Initiative.md).
2. **Turns run in that order**, one turn each per round.
3. **Each turn you get**: 1 Action; 1 Bonus Action, if a class feature, spell, or item grants you one; Movement up to your speed, which you can split before and after your action; 1 free object interaction (draw or sheathe a weapon, open a door, pick up an item); and as much brief free action as is reasonable (a sentence of speech, dropping an item, dropping prone). You also have 1 Reaction, which you can spend between your turns.
4. **Your turn does not end on its own.** Attacking, casting a spell, or moving spends only that one resource — the rest stays yours. After each thing you do, the GM re-lists what you have left and asks whether there's anything else. The turn ends only when you say so: "end turn", "done", "pass", or "that's my turn". Only then does the GM run everyone else in initiative order.
5. **End of round.** Once everyone has acted, the round counter ticks over and initiative starts again from the top.

See [Dice](Dice.md) for how attack rolls and damage rolls are actually rolled.

## What combat looks like on screen

There's no separate combat panel or turn tracker. At the start of every round the GM writes a round summary into the story text itself, alongside the usual per-turn header lines:

- the round number,
- every combatant in initiative order, with the number they rolled in brackets, their HP current/max, their AC, and a status tag (OK, Wounded, Bloodied, Critical, Defeated),
- and, on your turn, what you have left: Action, Bonus Action, Movement remaining, Reaction, free object interaction, and any once-per-turn feature such as Sneak Attack.

Your character sheet shows your initiative *modifier*. It does not show the turn order.

## Conditions

Conditions are 5e-standard: Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious. Each grants mechanical advantages or disadvantages and limits what you can do. Campaigns can also invent their own conditions, so you may see names outside this list.

## Reactions

Some class features and spells trigger as reactions — an opportunity attack when an enemy leaves your reach, Shield against an incoming hit, Counterspell against an enemy caster. The GM pauses and offers you the window before resolving the trigger ("It's leaving your reach — Opportunity Attack?"), so you don't have to watch for it yourself.

You can also spend your Action to *ready* a reaction for a trigger you name. See [Initiative](Initiative.md).

## Rest and recovery

See [RestAndDeath](RestAndDeath.md). A short rest lets you spend hit dice to recover HP; a long rest restores all HP, half your spent hit dice, and most ability uses.

## Death and dying

At 0 HP you fall unconscious and start rolling death saves (`1d20`): 10 or higher is a success, a natural 20 puts you back on your feet at 1 HP, and a natural 1 counts as **two** failures. Three successes stabilize you; three failures kill you.

One shortcut skips all of that: a single hit that deals damage equal to or greater than your maximum HP kills outright, with no death saves. Full detail in [RestAndDeath](RestAndDeath.md).

## Player tips

- **Spend the whole turn.** Your turn stays open until you end it, so check the resource list before you say "done" — an unspent bonus action or 30 feet of movement is a wasted turn.
- **Describe your positioning.** There's no battle grid, so the GM works from what you say. "I back up to the doorway so only one of them can reach me" is worth more than a stated distance, and it's what the GM weighs when deciding whether an enemy can close on you.
- **Conditions win fights.** Stunned, Restrained, Prone, and Frightened swing combats harder than raw damage.

See [Initiative](Initiative.md), [CombatVictoryProtocol](CombatVictoryProtocol.md), [Dice](Dice.md), [RestAndDeath](RestAndDeath.md), [AbilityScores](AbilityScores.md).

## Sources

- D&D 5e Basic Rules (free SRD).
