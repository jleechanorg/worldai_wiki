---
title: DiceFAQ
created: 2026-06-19
updated: 2026-06-19
type: query
tags: [wa-faq, wa-mechanic]
sources: []
---

# Dice FAQ

Common dice questions answered.

## Q: Can I roll my own dice?

**A**: No. The platform rolls dice server-side. This is part of the game's anti-fabrication. You can't declare "I rolled a 20."

## Q: Why did my d20 show as a 1?

**A**: 1d20 has a 5% chance of each face. A 1 happens 5% of the time. Statistically normal.

## Q: Can I see the roll history?

**A**: Yes. The campaign debug view shows every roll with timestamp, dice, modifiers, result.

## Q: What does "1d20+5" mean?

**A**: Roll 1 twenty-sided die, add 5. The +5 is typically your attack bonus or skill modifier. See [[concepts/DiceNotation]].

## Q: What's advantage?

**A**: Roll 2d20, take the higher. Common when you have a tactical advantage (flanking, target prone, etc.). See [[concepts/AdvantageDisadvantage]].

## Q: What's disadvantage?

**A**: Roll 2d20, take the lower. Common when you have a tactical disadvantage (blinded, restrained, etc.).

## Q: Can advantage and disadvantage stack?

**A**: No. If you have advantage from one source and disadvantage from another, they cancel. Roll a single d20.

## Q: What does "nat 20" mean?

**A**: Natural 20 — the d20 shows 20. This is a critical hit (attack rolls) or auto-success (most other rolls).

## Q: What does "nat 1" mean?

**A**: Natural 1 — the d20 shows 1. This is an auto-miss (attack rolls) or auto-failure (most other rolls). For death saves, it's two failures.

## Q: Why did my attack hit but do no damage?

**A**: Possible causes:
- The attack roll hit, but the damage roll was 0 (e.g., a 1d4-1 damage roll).
- Resistance: the target has resistance to that damage type.
- Immunity: the target is immune to that damage type.

## Q: Why did I fail a save even with a high modifier?

**A**: Saves work the same as checks: `1d20 + save modifier vs DC`. The DC could be very high. Roll high enough to beat it.

## Q: Can I use a higher-level slot to upcast a spell?

**A**: Yes, if the spell has an upcast effect. For example, Fireball at 4th level does +1d6 per slot level above 3rd. See [[concepts/Spellcasting]].

## Q: Why is my character so squishy?

**A**: Low HP comes from low CON or low hit die rolls. Fix options:
- Take Tough feat at next ASI: +2 HP per level.
- Multiclass into a tanky class (Fighter, Barbarian) for d10/d12 hit die.
- Ask the GM for narrative explanation (e.g., "I survive because of plot armor").

## Q: What is a death save?

**A**: When you drop to 0 HP, you roll a death save each turn: 10+ = success, 9 or below = failure. Three successes stabilize you. Three failures kill you. See [[concepts/RestAndDeath]].

## Q: Can I bring back a dead character?

**A**: Depends on the campaign. Standard D&D has resurrection magic (Revivify, Raise Dead). Some campaigns disable resurrection (no-rez worlds).

See [[concepts/DiceAuthenticity]] for more.
