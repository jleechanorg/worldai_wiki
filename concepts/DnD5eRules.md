---
title: DnD5eRules
created: 2026-06-19
updated: 2026-10-21
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# D&D 5e Rules

You do not need to know Dungeons & Dragons to play WorldArchitect.AI. Describe what your character tries to do. The Game Master (GM), your narrator, resolves the action and describes what happens. When an action needs a dice check, the calculation details explain the recorded result.

The full rules are in the free [System Reference Document](https://dnd.wizards.com/resources/systems-reference-document). For a page-by-page tour of this wiki, see [index.md](../index.md).

## Reading a calculation

Open **Show calculation** beneath an Outcome to see the numbers recorded for that action. Older turns may have fewer details.

- **Dice rolled**: the numbers that came up. A `d20` is a 20-sided die.
- **Recorded result**: the dice result used before bonuses and penalties.
- **Modifier**: a bonus added to the roll, or a penalty subtracted from it. Training, abilities, equipment, or circumstances can affect a check, but the total alone does not say which ones applied.
- **Total**: the final score after the modifier.
- **Difficulty class (DC)** or **difficulty target**: the target number for the check. The recorded success or failure tells you the outcome; special rules can affect it.

For example, a recorded dice result of 15 with a +5 modifier gives a total of 20. If the target is 13, the score exceeds it. Check the recorded outcome rather than assuming every kind of roll follows the same rule.

A notation such as `2d20kh1+5` means roll two 20-sided dice, keep the higher number, then add 5. With dice of 15 and 2, the number used is 15. See [Advantage and disadvantage](AdvantageDisadvantage.md) for when extra dice apply.

### Where does the modifier come from?

When a breakdown is available, it lists the recorded bonuses and penalties and their explanations. An **ability modifier** comes from a character stat, such as Strength or Intelligence. A **proficiency bonus** represents training in a skill or tool. Not every check uses every bonus; [Ability scores](AbilityScores.md) explains the terms.

If the app says individual modifier components are unavailable, the total was recorded but a usable breakdown was not supplied. You can still read the final score, but you cannot tell which bonuses made up the total. Do not reconstruct a past roll from today's character sheet: the character or circumstances may have changed.

Routine, uncontested actions may succeed without a roll. Checks are for uncertain, hazardous, or opposed actions; see [Skill checks](SmartSkillChecks.md).

## Rules based on 5e

These are the underlying rules the game uses as guidance, not a promise that every rule is automatically enforced. Campaign-specific rules can differ.

- **Ability modifiers**: `(score - 10) / 2`, rounded down. See [AbilityScores](AbilityScores.md).
- **Proficiency by level**: +2 at levels 1–4, rising to +6 at 17–20, added only to things you're trained in. Expertise adds it a second time.
- **Saving throws**: each class is proficient in two.
- **Advantage and disadvantage**: roll twice, keep the better or worse die, and any of each cancels to a plain d20. See [AdvantageDisadvantage](AdvantageDisadvantage.md).
- **Combat**: initiative on `1d20 + DEX`, the standard action economy, conditions, death saves. See [Combat](Combat.md).
- **Spellcasting**: slots, preparation, concentration. See [Spellcasting](Spellcasting.md).

## What this game does differently

- **A natural 20 or 1 is absolute on every d20 roll**, not just attacks. A 20 succeeds against any DC; a 1 fails regardless of your bonuses. Standard 5e applies that only to attack rolls.
- **Difficulty comes from a tier ledger.** Rather than a GM picking a number by feel, the target's tier sets a base DC and your declared approach shifts it by up to 4 in either direction, with a hard ceiling of 30. See [SmartSkillChecks](SmartSkillChecks.md).
- **Social checks can borrow half a non-Charisma modifier** when the approach fits — Intelligence for a reasoned argument, Strength for a threat. See [AbilityScores](AbilityScores.md).
- **You decide when your turn ends.** Attacking doesn't pass the turn; you keep your remaining resources until you say "end turn". See [Combat](Combat.md).
- **Surrendered enemies count as fully defeated**, with no reduction in reward. See [CombatVictoryProtocol](CombatVictoryProtocol.md).

## What isn't 5e at all

The faction minigame — armies, territory, upkeep, mass battle — is original to WorldArchitect.AI. See [FactionSystem](FactionSystem.md).

So is god mode, which lets you edit the world and its rules directly instead of playing through your character. See [GodMode](GodMode.md).

## Custom settings

Naruto, Game of Thrones, Baldur's Gate 3, and isekai campaigns keep the 5e spine and re-skin it: the Sharingan is a class feature, a house allegiance is a background feature. The dice, modifiers, and DCs work the same underneath. See [CampaignDesign](CampaignDesign.md).

See [Combat](Combat.md), [AbilityScores](AbilityScores.md), [SmartSkillChecks](SmartSkillChecks.md), [PlayerUserStories](../queries/PlayerUserStories.md).
