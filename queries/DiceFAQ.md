---
title: DiceFAQ
created: 2026-06-19
updated: 2026-09-18
type: query
tags: [wa-faq, wa-mechanic]
sources: []
---

# Dice FAQ

Common dice questions answered.

## Q: Can I roll my own dice?

**A**: No, and you cannot report a roll either — typing "I rolled a 20" does nothing mechanically. The game produces every roll itself and the server checks the arithmetic, so neither you nor the GM can hand it a number. See [DiceAuthenticity](../concepts/DiceAuthenticity.md).

## Q: My dice rolls disappeared and I just see a phrase. What happened?

**A**: **Hide dice rolls** is on. Either you turned it on in Settings → Display, or the campaign creator set it as that campaign's default. Tap the phrase to see the actual roll for five seconds, or switch the setting off in Settings → Display — your own setting always overrides the campaign default.

## Q: Can I see the roll history?

**A**: Only by scrolling. Every turn shows its own rolls in the 🎲 Dice Rolls area above the narration, so scrolling back through the story walks you through every roll in order.

Turning on **Settings → Debug Mode** adds more to each turn: the GM's roll-by-roll working, including rolls normally made behind the screen, such as a guard's Perception check against your Stealth. It is still turn by turn, though — there is no separate roll-log screen and no way to export the rolls.

## Q: What does "1d20+5" mean?

**A**: Roll one twenty-sided die, add 5. The +5 is typically your attack bonus or skill modifier. See [DiceNotation](../concepts/DiceNotation.md).

## Q: What's advantage?

**A**: Roll two d20 and take the higher — written `2d20kh1`. Common when you have a tactical edge such as flanking or a prone target. It swings your odds further than a small flat bonus does — against a middling target number, about as far as a +5 would. It does not stack, and disadvantage cancels it. See [AdvantageDisadvantage](../concepts/AdvantageDisadvantage.md).

## Q: What's disadvantage?

**A**: Roll two d20 and take the lower — written `2d20kl1`. Common when you are blinded, restrained, or otherwise impaired.

## Q: Can advantage and disadvantage stack?

**A**: No. If you have advantage from one source and disadvantage from another, they cancel and you roll a single d20.

## Q: What does "nat 20" mean?

**A**: Natural 20 — the d20 itself shows 20, before any modifier. Here a nat 20 succeeds on *every* d20 check, not just attacks: it beats any DC and any AC no matter what your modifier is. On an attack it is also a critical hit, which doubles the damage dice but not the flat damage bonus. Damage rolls have no success or failure, so a 20 on a damage die is simply good damage.

## Q: What does "nat 1" mean?

**A**: Natural 1 — the d20 itself shows 1, before any modifier. A nat 1 fails *every* d20 check here, however large your bonus or low the DC. On a death save it is worse than a normal failure — it counts as two (see [RestAndDeath](../concepts/RestAndDeath.md)). Damage rolls have no success or failure, so a 1 on a damage die is just low damage.

## Q: Why did my d20 show as a 1?

**A**: Each face of a d20 comes up 5% of the time. A 1 every twenty rolls or so is exactly what the dice are supposed to do.

## Q: Why did my attack hit but do no damage?

**A**: Usually one of three things — the damage roll itself came out at or below zero, the target resists that damage type, or the target is immune to it. The dice line shows the damage roll, so you can tell which.

## Q: Why did I fail a save even with a high modifier?

**A**: Saves work like every other check: your d20 plus your save modifier against the DC. A high DC can outrun a good modifier, and a natural 1 fails regardless.

## Q: What is a death save?

**A**: When you drop to 0 HP you roll a death save each turn: 10 or higher is a success, 9 or below is a failure. Three successes stabilize you; three failures kill you. See [RestAndDeath](../concepts/RestAndDeath.md).

## Not a dice question?

- Spell slots and upcasting — [Spellcasting](../concepts/Spellcasting.md)
- Hit points, feats, and hit dice — [LevelUp](../concepts/LevelUp.md)
- Dying, resurrection, and resting — [RestAndDeath](../concepts/RestAndDeath.md)

See [Dice](../concepts/Dice.md) for how rolls work end to end.
