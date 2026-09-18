---
title: PlayerUserStories
created: 2026-06-19
updated: 2026-09-18
type: query
tags: [wa-system, wa-tutorial]
---

# Player User Stories

What the game does, system by system: combat, levelling, companions, spells, gear, the living world, God Mode, and saving your story. Written for any campaign, not a specific one.

For the app around the game — signing in, the dashboard, settings, API keys, sharing — see [Player Features Reference](ExternalUserStories.md).

**How to read this page.** Each system opens with a table you can scan in one screen. Under it, the few behaviours that are particular to WorldArchitect.AI — rather than 5e as you already know it — get the full **As a / I want / So that** treatment. Where the game does less than a tabletop player would expect, the row says so *in italics*, and [Rules the game doesn't track](#rules-the-game-doesnt-track) at the bottom collects the ones it leaves out entirely.

| System | Stories |
|--------|---------|
| [1. Combat](#1-combat) | US-001 – US-014a |
| [2. Levelling up](#2-levelling-up) | US-015 – US-024 |
| [3. Companions, NPCs and reputation](#3-companions-npcs-and-reputation) | US-025 – US-034 |
| [4. Spells](#4-spells) | US-035 – US-044 |
| [5. Gear and loot](#5-gear-and-loot) | US-045 – US-054 |
| [6. The living world and factions](#6-the-living-world-and-factions) | US-055 – US-064 |
| [7. Shaping the campaign and God Mode](#7-shaping-the-campaign-and-god-mode) | US-065a – US-069a |
| [8. Saving, export and coming back](#8-saving-export-and-coming-back) | US-070 – US-075 |

---

## 1. Combat

Fights run on 5e maths — attack rolls, damage, conditions, death saves — with the dice rolled by the server rather than written by the AI. Turn order is something the GM keeps, not a lock the software enforces.

| ID | What you get |
|----|--------------|
| US-001 | The GM tracks initiative and takes each combatant in turn. *An instruction the GM follows, not a server-enforced lock.* |
| US-002 | Every roll comes from the server's random number generator. |
| US-003 | The fight pauses to offer you a reaction — Shield, Counterspell, Absorb Elements, a parry — when one is triggered. |
| US-004 | Movement, action, bonus action and reaction are tracked, so you cannot slip two spells above cantrip level into one turn. *Long multi-message turns and strict one-action turns are both in play; the GM's reading can vary.* |
| US-005 | Damage lands on hit points, and everyone's HP is visible, so you can judge when to press or retreat. |
| US-006 | Conditions bite: being frightened, prone or poisoned changes your rolls, not just the narration. See [AdvantageDisadvantage](../concepts/AdvantageDisadvantage.md). |
| US-007 | A natural 20 doubles your damage dice; a natural 1 misses outright. |
| US-008 | An area spell is rolled against every target it catches, and you see what each one took. See [Combat](../concepts/Combat.md), [Dice](../concepts/Dice.md). |
| US-009 | Where you stand feeds into the difficulty the GM sets. *There is no battle grid and no automatic flanking advantage in personal combat — armies get a Flanking Order ability in the faction game (US-059).* |
| US-010 | One concentration spell at a time, and a CON save whenever you take damage while it is up, so your strongest ongoing spell is something an enemy can break. See [Spellcasting](../concepts/Spellcasting.md). |
| US-011 | At 0 HP you roll death saves each turn — three successes stabilise you, three failures kill you. See [RestAndDeath](../concepts/RestAndDeath.md). |
| US-012 | Short rest (1 hour, spend Hit Dice) and long rest (8 hours, full recovery) restore HP, slots and class features. See [RestAndDeath](../concepts/RestAndDeath.md). |
| US-013 | Winning a fight pays: loot and gold are awarded without you asking. See [LootAndRewards](../concepts/LootAndRewards.md). |
| US-014 | Jump someone and you get a surprise round before initiative. See [Initiative](../concepts/Initiative.md). |
| US-014a | Every turn ends with a short list of suggested next moves, each one a button — and a Custom Action button for doing something nobody suggested. |

### US-002: Dice Rolls Are Real, Not Made Up

**As a** player rolling an attack, a check, or a saving throw,
**I want** the result to come from the server's random number generator instead of being written by the AI,
**So that** a bad roll is genuinely bad luck and a good one is genuinely earned.

See [Dice](../concepts/Dice.md), [DiceAuthenticity](../concepts/DiceAuthenticity.md).

### US-003: The Fight Stops to Let You React

**As a** player who is about to be hit, or who sees an enemy start casting,
**I want** the fight to pause and offer me the reaction I actually have — Shield, Counterspell, Absorb Elements, a parry,
**So that** I can spend a reaction on the moment it matters instead of hearing about it afterwards.

See [Combat](../concepts/Combat.md).

### US-014a: Suggested Next Moves, Never Forced

**As a** player deciding what to do next,
**I want** the moves I could plausibly make offered as buttons under the turn I just read,
**So that** I can take an obvious option in one tap without losing the ability to type something nobody suggested.

They appear on every story turn, not only at dramatic moments. In ordinary play you get four of them, each with a **Show pros and cons** toggle that spells out the trade-off before you commit; in God Mode you get three, without the pros and cons. Character creation and level-up offer their own shorter menus instead. A final **Custom Action** button always sits at the end of the list, and the free-text box never stops accepting anything you type.

---

## 2. Levelling up

The big difference from tabletop: nothing stops to make you fill in a form. When you cross an XP threshold the whole level lands on the same turn, and you can revise the game's choices afterwards.

| ID | What you get |
|----|--------------|
| US-015 | The new level applies itself the moment you earn it, with an optional review window afterwards. |
| US-016 | Your level-up is checked against 5e — hit points, ASI, spells known, subclass timing — before it sticks. See [LevelUp](../concepts/LevelUp.md). |
| US-017 | HP gain is your class hit die plus your CON modifier. See [LevelUp](../concepts/LevelUp.md). |
| US-018 | Subclass or archetype is offered at your class's own trigger level — Cleric 1, Wizard 2, Fighter 3. See [Subclass](../concepts/Subclass.md). |
| US-019 | At 4, 8, 12, 16 and 19 you take an ASI (+2, or +1/+1) or a feat. See [ASI](../concepts/ASI.md). |
| US-020 | Casters learn new spells and reshuffle what is prepared. See [Spellcasting](../concepts/Spellcasting.md). |
| US-021 | Class features unlock on schedule — Second Wind, Action Surge, Extra Attack and the rest. See [LevelUpProgression](../concepts/LevelUpProgression.md). |
| US-022 | Level 20 is where ordinary levelling stops. A campaign running divine progression carries on past it, onto a tier ladder with its own costs. See [LevelUpProgression](../concepts/LevelUpProgression.md). |
| US-023 | A multiclass concept like "Wizard/Cleric" is accepted. *Partial: the game uses your first class for hit dice and spell lists, and does not enforce the 5e ability-score prerequisites.* |
| US-024 | Hit points, slots, features and ability scores show up on your sheet immediately, not next session. See [LevelUp](../concepts/LevelUp.md). |

### US-015: The Level Applies Itself, Then You Can Adjust It

**As a** player who crosses an XP threshold,
**I want** the full new level — hit points, features, spells, proficiencies — applied on that same turn, with a review window afterwards where I can change what the game chose for me,
**So that** play never stops to make me fill in a form, and my sheet is never left half-levelled.

While a review is open the game keeps you on it: an unrelated action gets folded back into the pending step rather than resolved.

See [LevelUp](../concepts/LevelUp.md), [LevelUpProgression](../concepts/LevelUpProgression.md).

### US-022: Divine Ascension, Past Level 20

**As a** player whose character has outgrown the level 20 class tables,
**I want** an ascension ceremony that moves me onto a divine tier ladder — Demi-God and the tiers above it, with its own power scale, visibility rules and Chosen/Avatar mechanics,
**So that** the campaign keeps growing after the normal tables run out.

Level 20 is a real stop, not a doorway: reaching it does not trigger anything on its own, and ordinary XP stops there. The ceremony comes later, and only in a campaign with divine progression running — once your story has built up enough divine weight that the world already treats you as a god. Even then it is offered, not imposed; you can turn it down and stay mortal.

This replaces ordinary levelling rather than extending it, and the game does not use 5e Epic Boons.

See [LevelUpProgression](../concepts/LevelUpProgression.md) for the ceremony itself, the tier table and what each further level costs.

---

## 3. Companions, NPCs and reputation

Who you are to someone is tracked per person, not as one global score, and the people around you have opinions, memories and relationships with each other.

| ID | What you get |
|----|--------------|
| US-025 | Your standing is per-person first, faction second, public last. |
| US-026 | Companions have distinct personalities that drive how they talk, fight and react. |
| US-027 | Companions approve or disapprove of what you do, measured against their own values. See [CompanionArc](../concepts/CompanionArc.md). |
| US-028 | Public reputation follows your deeds and fades over time, so the world forgets a small offence and remembers a legendary one. See [NPCRelationships](../concepts/NPCRelationships.md). |
| US-029 | You can recruit new companions and dismiss current ones. See [CompanionArc](../concepts/CompanionArc.md). |
| US-030 | A dead companion stays dead unless you go and do something about it. See [CompanionArc](../concepts/CompanionArc.md). |
| US-031 | Romance arcs are opt-in and develop over time rather than firing on a trigger. See [CompanionArc](../concepts/CompanionArc.md). |
| US-032 | NPCs remember what you promised them and come back about it. See [NPCRelationships](../concepts/NPCRelationships.md). |
| US-033 | NPCs have friends, rivals and family, so helping one can cost you another and gossip travels between them. See [NPCRelationships](../concepts/NPCRelationships.md). |
| US-034 | As a faction leader you can negotiate alliances and declare rivalries. See [FactionSystem](../concepts/FactionSystem.md). |

### US-025: Who You Are to *This* Person Comes First

**As a** player dealing with NPCs and factions,
**I want** an individual's own history with me to outrank their faction's view of me, and both to outrank my public reputation,
**So that** an old friend still greets me warmly in a city that has turned against me.

See [NPCRelationships](../concepts/NPCRelationships.md).

### US-026: Companions Have a Personality, Not a Mood Bar

**As a** player travelling with companions,
**I want** each of them to hold a distinct personality type that shapes their dialogue, their choices in a fight, and how they take my orders,
**So that** a companion may argue with a plan, refuse an order, or leave outright.

See [CompanionPersonality](../concepts/CompanionPersonality.md), [CompanionArc](../concepts/CompanionArc.md).

---

## 4. Spells

Mostly 5e by the book. The two places it differs are custom class support and the fact that spell attack rolls and saves go through the same server dice as everything else.

| ID | What you get |
|----|--------------|
| US-035 | Known versus prepared spells are tracked, and slots are spent as you cast. See [Spellcasting](../concepts/Spellcasting.md). |
| US-036 | Slots come back on a long rest — on a short rest if you are a Warlock. |
| US-037 | Ritual spells can be cast without a slot for ten extra minutes. |
| US-039 | A spell attack rolls 1d20 plus your spell attack bonus against AC. See [Dice](../concepts/Dice.md). |
| US-040 | A spell that allows a save makes the target roll against your spell save DC. See [Dice](../concepts/Dice.md). |
| US-041 | Upcasting works — Fireball in a 4th-level slot adds a d6 per slot level. See [Spellcasting](../concepts/Spellcasting.md). |
| US-042 | Cantrips are unlimited and scale with your level (Fire Bolt 1d10 → 2d10 → 3d10 → 4d10). |
| US-043 | Non-standard builds are supported — gestalt classes, custom spell lists. See [ItachiGaiden](../entities/ItachiGaiden.md) for a gestalt example. |
| US-044 | Domain and patron spells are always prepared and never count against your limit. See [Subclass](../concepts/Subclass.md). |

---

## 5. Gear and loot

Equipment lives in named slots with a backpack behind it. What the game does *not* do is catalogue items: there is no rarity tier, no identified flag, no curse flag, and no carried-weight rule.

| ID | What you get |
|----|--------------|
| US-045 | A fixed set of named gear slots plus a backpack, with duplicates merged and attunement tracked. |
| US-046 | An attunement limit that matches your campaign's magic level — 3 items by default, 5–6 in a high-magic campaign, and no limit at all in a power-fantasy one. See [LootAndRewards](../concepts/LootAndRewards.md). |
| US-047 | Magic items are described and revealed through play, not looked up on a table. |
| US-051 | You can sell what you do not want and buy from merchants. See [LootAndRewards](../concepts/LootAndRewards.md). |
| US-054 | Loot and gold are sized to what you just beat, so a hard fight pays better than an easy one. *The GM judges the reward; it does not roll the published treasure tables by challenge rating.* See [LootAndRewards](../concepts/LootAndRewards.md). |

### US-045: Named Slots, Not a Pile

**As a** player managing my gear,
**I want** my equipment held in named slots — head, armour, cloak, hands, feet, neck, two rings, belt, shield, main hand, off hand, instrument — with a backpack for everything else, duplicate items merged, and attunement counted,
**So that** I can see what I am wearing at a glance and cannot accidentally equip the same sword twice.

See [Equipment](../concepts/Equipment.md), [LootAndRewards](../concepts/LootAndRewards.md).

### US-047: Magic Items Are Described, Not Catalogued

**As a** player who finds a magic item,
**I want** the GM to tell me what it appears to be and reveal the rest through use or investigation,
**So that** discovery stays part of play.

Items are not stored with a rarity tier, an identified/unidentified flag, or a curse flag. What an item is comes from its description and the GM's memory of it, which is also why a nasty surprise can be hiding in something you picked up three sessions ago.

---

## 6. The living world and factions

The world advances on its own clock, and once your ambitions outgrow a party you can switch into a strategic layer and run a faction.

| ID | What you get |
|----|--------------|
| US-055 | The world advances every 24 hours of game time, whether or not you were there. |
| US-056 | NPCs pursue their own agendas between your turns. See [NPCRelationships](../concepts/NPCRelationships.md). |
| US-057 | You can switch between Adventure mode and Faction mode. |
| US-058 | Scouts can be sent to gather intel on rivals before you commit. See [FactionIntel](../entities/FactionIntel.md), [FactionPower](../concepts/FactionPower.md). |
| US-059 | Faction battles are resolved by a battle simulator rather than narrated away. |
| US-060 | You can see where your faction ranks against the others. See [FactionPower](../concepts/FactionPower.md). |
| US-061 | Gold, influence, materials and members are yours to manage. See [FactionManagement](../concepts/FactionManagement.md). |
| US-062 | Territory can be taken, held and lost, and it feeds your economy. See [FactionManagement](../concepts/FactionManagement.md). |
| US-063 | You get warned before a deadline or a scheduled event runs out of time. See [LivingWorld](../concepts/LivingWorld.md). |
| US-064 | Defeated enemies and finished quests stop cluttering the world. See [LivingWorld](../concepts/LivingWorld.md). |

### US-055: The World Moves While You're Away

**As a** player exploring a sandbox,
**I want** the world to advance every 24 hours of game time — rivals acting, prices moving, plots maturing,
**So that** a week spent resting in town costs me something, and coming back to a place means finding it changed.

See [LivingWorld](../concepts/LivingWorld.md).

### US-057: Two Modes, One Campaign

**As a** player whose ambitions have outgrown a party,
**I want** to switch between Adventure mode, where time passes scene by scene, and Faction mode, where it passes in strategic turns,
**So that** I can run a realm without giving up the character who built it.

See [FactionSystem](../concepts/FactionSystem.md), [FactionManagement](../concepts/FactionManagement.md).

### US-059: Battles Are Simulated, Not Narrated Away

**As a** faction leader attacking a rival,
**I want** the battle resolved by a simulator that counts troops, elites and fortifications,
**So that** a war I planned badly is lost on the numbers rather than on the GM's mood.

See [FactionBattleSim](../entities/FactionBattleSim.md).

---

## 7. Shaping the campaign and God Mode

You set the premise when you create the campaign and steer everything else in play. The mode selector above the action box is how you get from playing your character to editing the world.

| ID | What you get |
|----|--------------|
| US-065a | Three modes above the action box: Character, Think/Plan, and God. |
| US-065 | Describe your campaign in plain English when you create it. |
| US-066 | Standing directives that the GM has to keep following. |
| US-067 | Say in your description whether you want a starting party, and the game builds one or leaves you alone. |
| US-068 | Your own history, geography and factions replace the defaults — set them in the description box, then keep steering with directives. See [CampaignWizard](../concepts/CampaignWizard.md). |
| US-069 | Hide the raw dice numbers and read a short outcome phrase instead — your own preference, and a campaign can start with it on. See [Dice](../concepts/Dice.md). |
| US-069a | A mature-content switch in the game header. |

### US-065a: Choose How You're Speaking — Character, Think/Plan, or God

**As a** player typing into the action box,
**I want** three modes on the selector above it — Character (what you type is what your character does), Think/Plan (pause the story for a breakdown of your options with pros and cons, with no time passing), and God (edit the world directly — stats, items, location — with the story paused),
**So that** I can act, plan, or fix something without any of the three bleeding into the others.

This selector is how you reach God Mode; the stories below describe what God Mode does once you are in it.

See [GodMode](../concepts/GodMode.md).

### US-065: Shaping a Campaign When You Create It

**As a** campaign creator,
**I want** to describe the campaign I want in plain English in a long free-text box,
**So that** the GM starts from my premise instead of a generic one.

The wizard's numbered fields and that description box are the whole of what you hand the GM at creation — there is nothing else to configure.

The description box is the last section of the creation form and it may be folded shut when you arrive — look for the **Expand** button beside the label. It is optional and it takes as much text as you care to write, so it is worth opening.

Everything else — house rules, lore, how the GM behaves — is steered in play through directives (US-066), not through a settings form.

See [CampaignWizard](../concepts/CampaignWizard.md), [CampaignDesign](../concepts/CampaignDesign.md).

### US-066: Directives the GM Keeps Following

**As a** player who wants the campaign to sound a particular way,
**I want** to write standing directives — tone, pacing, what is off the table, how NPCs speak,
**So that** the instruction holds for the rest of the campaign instead of fading after a turn or two.

See [GodMode](../concepts/GodMode.md), [GodModePrompting](../concepts/GodModePrompting.md).

### US-067: Starting Companions On or Off

**As a** campaign creator,
**I want** one switch that decides whether the game builds a complementary starting party for me,
**So that** I can begin alone or with a crew.

The game picks who they are from your campaign description. To constrain them — classes, levels, temperament — say so in the description box or steer it later with a directive (US-066).

See [CompanionPersonality](../concepts/CompanionPersonality.md).

### US-069a: Mature Content Toggle

**As a** player who wants adult scenes written rather than faded to black,
**I want** a Spicy switch in the game header that moves the campaign onto an uncensored model for as long as it is on,
**So that** the tone of intimate and violent scenes is my choice, per campaign, and reversible.

It is slower while it is on, and turning it off restores the model you were using before.

---

## 8. Saving, export and coming back

Your campaign is saved as you play. What it cannot do is hold every sentence of a hundred-hour story in front of the AI at once — so it keeps the facts and lets the scenes go.

| ID | What you get |
|----|--------------|
| US-070 | Come back weeks later and the campaign reopens on the same scene, still holding the facts that matter. |
| US-071 | Each finished turn is written to your campaign as it completes. *A turn that is still being written when you disconnect is the exception — see US-074.* |
| US-072 | Export the whole story as text, DOCX or PDF. |
| US-073 | One durable fact is recorded per narrated turn, and those facts outlive the scenes they came from. |
| US-074 | Reload and pick up where you left off, including the action you had half-typed. |
| US-075 | Your campaign follows you between desktop and mobile. |

### US-070: Coming Back Weeks Later

**As a** player who returns after days or weeks away,
**I want** my campaign to reopen on the same scene and still hold the facts that matter — who I am, who owes me what, what I promised,
**So that** the story continues instead of restarting.

The game does not keep every sentence of a long campaign in front of the AI. Old scenes are compacted away, and the per-turn record of durable facts carries them forward (US-073).

### US-072: Download & Share Campaign Story

**As a** player who wants to keep my adventure,
**I want** to export the campaign as text, DOCX or PDF,
**So that** I can read, print or share it outside the app.

See [ItachiGaiden](../entities/ItachiGaiden.md) for an example of an exported campaign.

### US-073: Core Memories Survive Compaction

**As a** player hundreds of entries into one campaign,
**I want** the game to record one durable fact per narrated turn, so that when old middle scenes drop out of the AI's working context those facts still steer the story,
**So that** the campaign stays coherent without carrying every scene forever.

Old scenes are dropped, not summarised. That per-turn record is what survives — which is why the game remembers *that* you swore an oath long after it has forgotten the wording of the scene where you swore it.

### US-074: Reload and Pick Up Where You Left Off

**As a** player reloading between turns,
**I want** the campaign to reopen on the latest scene with the story so far intact and my half-typed action restored,
**So that** a refresh costs me nothing.

Reloading *during* a turn is different: the page comes back showing a thinking bar that will never finish. Press Cancel to free the input — that turn's result is lost and has to be sent again.

---

## Rules the game doesn't track

Worth knowing before you plan around them:

- **No crafting system** — no materials, recipes or crafting feats. Describe the work and the GM narrates the result.
- **No carried weight.** The backpack has no capacity limit.
- **No armour don/doff timing.** Swapping gear mid-fight costs whatever the GM judges it should.
- **No rarity tiers, identified flags or curse flags** on items. What an item is comes from its description — see [US-047](#us-047-magic-items-are-described-not-catalogued).

## Where to read more

- [Player Features Reference](ExternalUserStories.md) — the app around the game: accounts, settings, saving, export.
