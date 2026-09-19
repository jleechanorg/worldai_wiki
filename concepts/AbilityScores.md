---
title: AbilityScores
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-glossary]
sources: []
---

# Ability Scores

D&D 5e's six core attributes, and what each one does for you.

| Score | Abbreviation | What it governs | Check example | Save example |
|-------|--------------|-----------------|---------------|--------------|
| Strength | STR | Melee attacks, grappling, carrying, jumping | Kick down a door | Avoid being shoved off a ledge |
| Dexterity | DEX | Ranged attacks, AC in light armor, initiative, Stealth, Acrobatics | Balance on a beam | Dodge a fireball |
| Constitution | CON | HP, hit dice, concentration, endurance | Hold your breath | Resist poison |
| Intelligence | INT | Wizard spells, Arcana, History, Investigation | Recall lore | Resist mind control |
| Wisdom | WIS | Cleric and Druid spells, Perception, Insight, Medicine | Sense a lie | Shake off a fear effect |
| Charisma | CHA | Bard, Paladin, Sorcerer, and Warlock spells, Persuasion, Deception, Intimidation | Persuade a guard | Resist banishment |

A **check** is you trying something; a **saving throw** is you resisting something. Both roll `1d20 + the ability modifier`, plus your proficiency bonus when it applies. Each class is proficient in two saves.

## Modifiers

A score's modifier is `(score - 10) / 2`, rounded down.

| Score | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|-------|---|----|----|----|----|----|----|
| Modifier | -1 | +0 | +1 | +2 | +3 | +4 | +5 |

## Base vs effective scores

Your sheet keeps two numbers for every ability: the **base** score you built the character with, and the **effective** score after magic items. A belt reading `+2 STR (Max 20)` raises your effective Strength by 2 but never past 20 — and the bonus disappears the moment you unequip it.

Opening **Stats** shows both, with the gear bonus broken out:

| Stat | Base | Effective | Mod | Bonus |
|------|------|-----------|-----|-------|
| STR | 16 | 16 → 18 | +4 | +2 |
| DEX | 14 | 14 | +2 | — |

Everything downstream — attack rolls, spell save DC, initiative, AC — uses the effective score.

## The 15 cap at character creation

Before racial bonuses, no starting score may exceed 15. That's the ceiling for both Point Buy and the Standard Array, and the game checks it. If your character arrives with something higher — from a template, an AI-generated sheet, or a number you asked for — the character review step flags that stat with a warning and offers you a choice that pulls the scores back to standard starting limits.

Racial and background bonuses stacked on top of 15 are fine; the cap is checked against your base scores only. Campaigns that explicitly use epic or mythic creation rules skip the warning.

## Social checks aren't pure Charisma

Social checks run on Charisma, but you can lean on what you're actually good at. If a smarter, wiser, or more physically imposing approach fits the moment, **half** that modifier is added to the check:

| Check | Stat that can help |
|-------|--------------------|
| Intimidation | STR or DEX, whichever is higher |
| Persuasion (a logical argument) | INT |
| Persuasion (an empathetic appeal) | WIS |
| Deception | INT or WIS |

Only one stat can help per check, and it adds nothing unless that stat's modifier actually beats your Charisma modifier — a tie gives nothing, so a Bard with CHA 18 gains nothing from WIS 14, and CHA 14 with INT 14 gains nothing either. But a Wizard with INT 18 (+4) and CHA 8 (-1) rolls `d20+1` on a reasoned argument instead of `d20-1`. Proficiency still applies normally.

## Related

Some rolls are made twice and the better or worse die kept — see [AdvantageDisadvantage](AdvantageDisadvantage.md). How the target number for a check is chosen is covered in [SmartSkillChecks](SmartSkillChecks.md).

See [Combat](Combat.md), [ASI](ASI.md), [CharacterCreation](CharacterCreation.md).
