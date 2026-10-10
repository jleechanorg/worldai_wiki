---
title: LootAndRewards
created: 2026-06-19
updated: 2026-10-10
type: concept
tags: [wa-mechanic]
sources: []
---

# Loot & Rewards

What you get for encounters, quests, and milestones — and where it shows up.

While narrative prose keeps raw XP numbers out of character dialogue and storytelling, the game renders a dedicated **Inline Reward Display Card** directly beneath the scene in the story flow whenever rewards are earned (`✨ REWARDS (encounter)`, `✨ REWARDS (quest)`). The card displays your exact XP gain (`+{xp_gained} XP`), level progress percentage (`XP: {current_xp}/{next_level_xp} ({progress_percent}%)`), any `LEVEL UP AVAILABLE!` notification, and itemized loot and coin deltas (`+{gold} gold`, `+{quantity} {item_name}`). XP is also tracked in the status header as `XP: current/next`.

## XP

XP is paced, not counted up from enemy stats. Every award is a slice of your
current level's full XP span — the gap between the threshold you reached and the
next one — so progress feels about the same at level 3 and at level 13:

- **Routine wins give nothing** — an easy fight, an ordinary skill check, or
  re-checking something you already finished.
- **A solid accomplishment** — a competent encounter, a useful social win —
  gives a small slice.
- **A hard-won encounter or a real victory** gives a noticeably bigger one.
- **Finishing a multi-session storyline** gives the largest awards.

Enemy difficulty (its Challenge Rating, the monster's difficulty number) tells
the GM how big a win it was. It is never multiplied into an XP number. Expect
roughly one level per extended arc of play, not one per fight. When your XP
crosses a threshold you level up ([LevelUp](LevelUp.md)).

## Risk and planning

When the GM offers you a plan with options, the option you pick changes the
payout, not just the odds:

- **Safe / low risk**: normal difficulty, normal rewards.
- **Medium risk**: same difficulty, about a quarter more XP and 10% more money.
- **High risk**: a harder check, but about half again the XP, 25% more money,
  and a shot at a bonus item.

How well you argue the plan matters too: a *Brilliant* plan adds roughly
another 10% and a chance at an uncommon item, a *Masterful* one adds about 25%
and a chance at a rare item. The two stack, so a masterful high-risk success is
close to double XP.

One catch: if you ignore the offered options and improvise something crude
instead, you keep the risk without the planning bonus, and the GM raises the
difficulty to match what you actually tried.

## Money

Your money is tracked in gold pieces and updates dynamically across your campaign. In the status header, it appears on the **Resources** line (for example, `Resources: Spells: L1 2/2 | Gold: 120gp`). The GM narrates it in whatever the setting calls money — credits, scrip, coin — while the server maintains the underlying numeric balance. When creating a character, starting wealth adheres to Wealth By Level (WBL) bounds scaled to your background's socioeconomic tier (from Destitute up to Royal).

You earn it from treasure, defeated enemies, quest payouts, and selling what
you do not need. You spend it on gear ([Equipment](Equipment.md)), on services
like guides, passage, and bribes, and on the lifestyle your character keeps
between adventures.

## Items & Inventory Stacking

The GM describes items in the usual 5e rarity language, and that language is a rough promise about power:

- **Common**: mundane but useful — rope, torches, basic weapons.
- **Uncommon**: a small magical edge, such as a +1 weapon or a Bag of Holding.
- **Rare**: genuinely powerful, such as a Flame Tongue or Winged Boots.
- **Very Rare**: campaign-defining, such as a Holy Avenger.
- **Legendary** and **Artifact**: named, world-shaping things.

Identical consumable items (healing potions, rations, ammunition) stack automatically into a single entry with an updated quantity count when looted or purchased, so your inventory stays organized.

Your sheet does not carry a rarity band, an identified mark or a curse mark on
anything. What an item is lives in its description and in the GM's memory of it,
which is why a nasty surprise can sit unnoticed in your pack for sessions.

Some magic items need **attunement** — a short bonding period before they work
for you — and you can normally hold three attunements at once. Potions,
scrolls, ammunition, and plain +1/+2/+3 gear never need it. Your campaign can
raise or remove the limit if you ask for a higher-magic game
([GodMode](GodMode.md)).

## Player tips

- **Say you are searching.** Describe looking through bodies, crates, and rooms
  rather than assuming it happened. The GM rewards explicit searching.
- **Ask to sell.** Tell the GM you want to find a buyer; merchants and prices
  are improvised in the scene, not picked from a fixed shop menu.
- **Take the risky option when you can afford it.** The reward multipliers are
  real, and a well-argued plan multiplies them again.
- **Spend attunement on things you use every fight**, not on situational items
  you will forget about.

See [LevelUp](LevelUp.md), [Equipment](Equipment.md).
