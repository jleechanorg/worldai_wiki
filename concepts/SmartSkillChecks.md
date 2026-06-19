---
title: SmartSkillChecks
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Smart Skill Checks

WorldArchitect.AI uses an intelligent skill check system: rather than rolling a flat d20, the system considers context, modifiers, and partial successes.

## Standard skill check

`1d20 + ability modifier + proficiency (if proficient) + circumstantial modifiers`

Circumstantial modifiers can be:
- +5 from a tool (thieves' tools for lockpicking)
- +5 from preparation (planning the heist)
- -5 from distraction (rolling Stealth while drunk)
- +2 from a relevant feature (e.g., Rogue's Expertise)

## Smart adjudication

Beyond the raw roll, the system considers:
- **Partial successes**: a roll that's close to the DC might succeed with a complication.
- **Critical successes (nat 20)**: automatically succeed + bonus.
- **Critical failures (nat 1)**: automatically fail + complication.
- **Help action**: an ally can use the Help action to grant advantage on a check.
- **Guidance cantrip**: +1d4 to a check.

## Examples

- **Lockpicking**: a Rogue with thieves' tools and Expertise gets +5 (DEX) + 2*proficiency + 2 (tools) = +13. A nat 1 still fails, but a 7+ succeeds.
- **Persuasion**: a Bard with Persuasion proficiency and Friends cantrip gets +5 (CHA) + 4 (proficiency at level 5) + 1d4 (Friends) = +10 + 1d4.
- **Stealth (in heavy armor)**: disadvantage + lack of proficiency = likely to fail even with high DEX.

## Player tips

- **Build for your checks**: expertise, proficiency, advantage.
- **Set up your rolls**: don't Stealth while drunk. Plan before picking a lock.
- **Use Help**: an ally's Help action gives you advantage on their check.
- **Cantrips add up**: Guidance is +1d4 per use, free.

See [[concepts/AbilityScores]], [[concepts/DiceNotation]].
