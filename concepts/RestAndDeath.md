---
title: RestAndDeath
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic]
sources: []
---

# Rest & Death

How characters recover, and what happens at 0 HP.

## Short rest

About an hour of light activity. On a short rest you can:

- Spend hit dice to get HP back — one at a time, rolling the die and adding
  your CON modifier. Spent hit dice do not come back until a long rest.
- Recharge class features that refresh on a short rest, such as a Fighter's
  Second Wind or a Warlock's spell slots.

## Long rest

About eight hours, with at least six of them asleep. When it finishes:

- HP back to maximum
- Half of your spent hit dice restored (rounded down, minimum one)
- Spell slots back to maximum
- Most class features and limited-use abilities restored
- Exhaustion reduced by one level

You can only benefit from one long rest per 24 hours. An hour or more of
strenuous activity during the rest — fighting, marching, casting spells —
interrupts it, and you have to start over.

Going without one has a cost: after 24 hours awake you start making CON saves
or picking up exhaustion, and the save gets harder every day after that.
Pushing a forced march past eight hours does the same.

## Death & dying

When you drop to 0 HP:

- If a single hit dealt damage equal to or more than your maximum HP, you die
  outright — no unconsciousness, no death saves.
- Otherwise you fall **unconscious** and start making death saves.
- You always start at 0 successes and 0 failures, no matter what dropped you.
- At the start of each of your turns, roll `1d20`:
  - **10 or higher**: one success.
  - **9 or lower**: one failure.
  - **Natural 20**: you wake up with 1 HP.
  - **Natural 1**: counts as two failures.
- **3 successes**: you stabilize — still unconscious, no longer dying.
- **3 failures**: you die.
- Taking any further damage while at 0 HP costs you a failure, or two if that
  damage was a critical hit.

## Stabilizing someone

- A DC 10 Medicine check stabilizes a dying creature.
- The Spare the Dying cantrip stabilizes automatically.
- A healing potion restores its full rolled amount — 2d4+2 for a common one
  ([Healing](Healing.md)). Any healing at all takes you above 0 HP, which ends
  the dying state and wakes you up.

## Resurrection

Revivify, Raise Dead, Resurrection and True Resurrection can bring the dead
back; the higher-level spells work after longer delays and restore more of what
was lost. Some settings rule resurrection out entirely, and you can set that up
front when you design the campaign ([CampaignDesign](CampaignDesign.md)).

## Player tips

- **Ask for a short rest often.** Warlocks, Fighters, and Monks get their best
  features back on one, and hit dice are your main source of HP between fights.
- **Long rest before a boss.** Full HP and full spell slots — but only half your
  spent hit dice come back, so a long rest does not undo a brutal day in one go.
- **Drinking a potion costs your whole action in combat.** Plan for it rather
  than reaching for one on the turn you were going to lose anyway.
- **Death saves are recoverable.** Any healing brings a dying character back,
  even 1 HP — so heal early rather than big.

See [Combat](Combat.md), [Healing](Healing.md).
