---
title: CombatVictoryProtocol
created: 2026-06-19
updated: 2026-10-09
type: concept
tags: [wa-mechanic]
sources: []
---

# Combat Victory Protocol

How a fight ends, and what happens once it does. Turn order and the action economy live in [Combat](Combat.md); this page starts at the moment the fighting stops.

## How combat ends

Combat ends when the enemies are defeated, flee, or surrender — and also when your party gets away, when you talk your way out mid-fight, or when something bigger interrupts (a collapse, a flood, a third party arriving).

You can ask to negotiate or to run at any point in a fight. If you flee, the encounter is recorded as *fled* rather than won: those enemies survive, may pursue you, and will remember it later.

Surrendering enemies count as fully defeated. Forcing a surrender is treated as a win, not a discount — you get the same credit as if you had killed them.

If your party drops instead, see [RestAndDeath](RestAndDeath.md) for what happens at 0 HP.

## The rewards block

Immediately following combat, an **Inline Reward Display Card** renders in the story flow (`✨ REWARDS (combat)` or `✨ REWARDS (encounter)`). It itemizes your exact XP award (`+{xp_gained} XP`), progress toward your next level (`XP: {current_xp}/{next_level_xp}`), any level-up notification, and acquired coin and loot (`+{gold} gold`, `+{quantity} {item}`).

Alongside the reward card, the narrative summarizes:

- **Enemies defeated** — each one named, with its challenge rating, and marked SURRENDERED where that applies.
- **Loot obtained** — gold, dropped equipment, consumables, quest items.
- **Resources consumed** — spell slots, class resources, ammunition, HP lost.

Your running total also updates in the session header (`XP: current/next`). Challenge ratings tell you how hard the fight was; they are not the raw arithmetic of the award. See [LootAndRewards](LootAndRewards.md) and [LevelUp](LevelUp.md).

## Right after the fight

The GM narrates the aftermath and offers a short menu of next moves — typically searching the fallen, taking a short rest, pressing onward, or securing the area. Each comes with a one-line description and a chevron you can expand to see its pros and cons. Pick one, or ignore the menu and type your own action; either way you're back in normal play.

## Special cases

- **A fight can end on the opening strike** when an ambush is set up well enough to justify it — one of the few things that lets an enemy die faster than its HP says. Surprise is not a free round, though, and how it's weighed is covered in [Initiative](Initiative.md).
- **Enemies breaking and running** is a GM call, not a dice mechanic. There's no morale roll in personal combat; if a fight is going badly for them, the GM may have them flee, and the encounter ends there. (The faction minigame *does* have a numeric morale system — see [FactionSystem](FactionSystem.md).)
- **Boss fights last longer on purpose.** Enemy HP is never quietly reduced so you can win faster. High-level enemies use Legendary Resistance to shrug off a failed save, Legendary Actions between turns, Multiattack, and defensive reactions like Parry and Uncanny Dodge. Expect to spend resources.

See [Combat](Combat.md), [Initiative](Initiative.md), [Dice](Dice.md).
