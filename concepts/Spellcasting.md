---
title: Spellcasting
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic]
sources: []
---

# Spellcasting

Magic-using classes — Cleric, Druid, Bard, Sorcerer, Warlock, Wizard,
Artificer, and the half-casters Paladin and Ranger — cast spells using spell
slots. If you invented a custom class, its spell access comes from how you
described it during character creation
([CharacterCreation](CharacterCreation.md)).

Paladins and Rangers get no spells at level 1; the resources line above each
turn reads "No Spells Yet (Level 2+)" until they come online at level 2. That is
expected, not a bug.

## Spell slots

You have a limited number of slots at each spell level, set by your class and
level. A 5th-level Wizard, for instance, has four 1st-level slots, three
2nd-level, and two 3rd-level.

A bigger slot can cast a smaller spell, and the spell gets stronger for it —
this is **upcasting**. That same Wizard can spend a 3rd-level slot on Fireball,
or on Burning Hands for an extra 2d6 of damage — an upcast spell gains its
bonus die for each slot level above its own level.

Slots only come back when you actually rest ([RestAndDeath](RestAndDeath.md)) —
long rest for most casters, short rest for Warlocks. In ordinary play the GM
will not hand them back early; if you want them restored without a rest, God
Mode can set your slots directly ([GodMode](GodMode.md)).

## Casting time

- **Action**: most spells.
- **Bonus action**: a few, such as Healing Word or Shillelagh. Cast one of
  these and the only other spell you can cast that turn is a cantrip.
- **Reaction**: a few, such as Shield or Counterspell — cast in response to
  something, on someone else's turn.
- **Ritual**: ten extra minutes of casting, and it does not spend a slot.
  Wizards, Clerics, Druids, and Bards can do this with ritual spells.

## Concentration

Some spells last only while you concentrate on them, and you can concentrate on
exactly one at a time. Casting a second concentration spell drops the first.
Taking damage forces a CON save — DC 10, or half the damage you took if that
is higher — and failing it drops the spell.

## Prepared vs known

- **Prepared casters** (Cleric, Druid, Wizard): choose a fresh list each long
  rest. You prepare your spellcasting modifier + your class level worth of
  spells, minimum one. Wizards choose from their spellbook rather than the
  whole class list.
- **Paladins** also prepare, but get fewer: your CHA modifier + half your
  paladin level, rounded down, minimum one.
- **Known casters** (Bard, Sorcerer, Warlock, Ranger): a fixed list of known
  spells that changes only when you level. Less flexibility, no daily prep.

## Cantrips

Level 0 spells — Fire Bolt, Eldritch Blast, Sacred Flame, Mage Hand. Unlimited
casts, no slot, forever.

## Player tips

- **Cantrips keep up.** Fire Bolt does 2d10 at level 5 and 3d10 at level 11, so
  your at-will option never becomes dead weight.
- **Don't stack concentration.** If you are holding Bless, a second
  concentration spell simply cancels it.
- **Upcast when it counts.** The same spell gets better in a bigger slot — Cure
  Wounds heals 1d8 + your modifier from a 1st-level slot and 3d8 + your
  modifier from a 3rd-level one.

See [CharacterCreation](CharacterCreation.md), [LevelUp](LevelUp.md), [Healing](Healing.md).
