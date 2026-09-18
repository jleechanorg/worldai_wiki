---
title: SmartSkillChecks
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Smart Skill Checks

A skill check is `1d20` plus your modifiers against a target number (the DC). The die is an ordinary d20 and your bonus is fixed by your character sheet. What moves is the **target number** — the GM sets it from who or what you're up against and how good your declared plan was, writes down the reasoning, and only then rolls.

## Which check your action calls for

You never have to name a skill. Describe what your character does in plain language and the GM picks the skill and ability it maps to — sneaking past a sentry becomes Stealth on DEX, talking a merchant down becomes Persuasion on CHA — then works out the difficulty and rolls. You'll see the result under a `🎲 Dice Rolls:` heading, with the total, the DC, whether it succeeded, who rolled, and what it was for:

```
1d20+6 = 24 vs DC 12 - Success (Sera Quill - Shadow Surveillance & Eavesdropping)
```

The mapping follows your wording, so if you meant to lean on someone rather than reason with them, say that plainly — "I loom over him and let the axe show" reads as Intimidation, not Persuasion.

## What goes into your roll

`1d20 + ability modifier + proficiency bonus (if proficient)`

That's the whole formula. Circumstances — tools, preparation, high ground, being drunk — never change your roll; they change the DC instead.

**Proficiency** depends only on your level:

| Level | Proficiency |
|-------|-------------|
| 1–4 | +2 |
| 5–8 | +3 |
| 9–12 | +4 |
| 13–16 | +5 |
| 17–20 | +6 |

**Expertise** (Rogue, Bard) adds your proficiency bonus a second time for one skill — +4 instead of +2 at low levels, up to +12 instead of +6 at level 20.

Social checks have one extra wrinkle: a smart or physically imposing character can lean on a stat other than Charisma. See [AbilityScores](AbilityScores.md).

## How the difficulty is set

The GM starts from a base DC for the target:

| Who or what you're up against | Base DC |
|---|---|
| Distracted civilian, routine chore | 10 |
| Town watch, mercenary scout, standard lock | 12–14 |
| Alert guard, veteran commander, fortified vault | 15–17 |
| Sovereign king, high council, mortal archmage | 18–19 |
| Lesser deity | 20 |
| Intermediate deity | 22 |
| Greater deity | 24 |
| Primordial / overgod | 30 |

Then your approach shifts it by 1 to 3 in either direction. A coordinated ambush, real leverage over the person you're talking to, or a plan that exploits the terrain makes it easier. Charging an alerted choke point, threatening someone far above your weight class, or telling a lie the facts already contradict makes it harder. A plain, direct attempt is neutral — a terse "I pick the lock" is never penalized for being short.

Three limits keep this honest:

- All adjustments together can shift the DC by at most **±4**.
- No DC goes above **30**, and none drops below the floor for that tier.
- The reasoning is written down **before** the dice are rolled, and isn't revised afterwards.

## What the roll can produce

- **Natural 20**: the check succeeds no matter how high the DC was.
- **Natural 1**: it fails no matter how big your bonuses are. (In this game both apply to skill checks and saving throws, not just attacks — standard 5e is narrower.)
- **Everything else**: you succeed if your total meets or beats the DC. There's no middle band — a check either makes the number or it doesn't. What a failure *costs* is up to the story: sometimes you simply don't manage it, sometimes it goes badly.
- **Advantage** from a Help action, a spell, or the situation means rolling two d20s and keeping the higher. See [AdvantageDisadvantage](AdvantageDisadvantage.md).

A spell or class feature that grants a bonus die (Bardic Inspiration, Bless) is rolled as its own separate roll and shown to you separately. It's never quietly folded into the check total.

## Examples

- **Lockpicking**: a level 5 Rogue with 20 DEX and Expertise in Thieves' Tools rolls `1d20 +5 (DEX) +6 (double proficiency)` = `1d20+11`. Against a standard iron lock at DC 14, anything but a 1 or a 2 opens it.
- **Persuasion**: a level 5 Bard with 20 CHA and Persuasion proficiency rolls `1d20 +5 (CHA) +3 (proficiency)` = `1d20+8`.
- **Stealth in heavy armor**: heavy armor you aren't trained in imposes disadvantage, so you roll twice and keep the *lower*. High DEX doesn't save you.

## Player tips

- **Say what you're actually doing.** The DC moves on your declared approach, not on how many words you use. "I wedge the door shut behind me first" is worth more than a paragraph of atmosphere.
- **Build the bonus, not the moment.** Proficiency, expertise, and a high ability score apply to every roll; a clever setup is capped at 4 points of DC.
- **Ask what you're rolling against.** The DC and its reasoning are fixed before the dice come out, so asking can't move the number.

See [AbilityScores](AbilityScores.md), [AdvantageDisadvantage](AdvantageDisadvantage.md), [DiceNotation](DiceNotation.md), [Dice](Dice.md).
