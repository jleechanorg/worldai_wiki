---
title: DnD5eRules
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# D&D 5e Rules

WorldArchitect.AI runs on D&D 5th Edition (SRD-derived). If you know 5e, you already know how to play; this page covers only where the game agrees with 5e, where it bends it, and where it leaves 5e behind entirely.

The full rules are in the free [System Reference Document](https://dnd.wizards.com/resources/systems-reference-document). For a page-by-page tour of this wiki, see [index.md](../index.md).

## What works exactly like 5e

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
