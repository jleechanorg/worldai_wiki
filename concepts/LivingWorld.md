---
title: LivingWorld
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-system, wa-mechanic]
sources: []
---

# Living World

The world moves on its own schedule, not only when you are watching. Every few turns the game advances everything happening off-screen — what NPCs did, what factions gained or lost, which deadlines came due — and folds the results into your campaign's saved state.

## When the world advances

On a schedule, not when you rest. An advance becomes due on whichever comes first:

- **24 hours of in-game time** since the last advance, or
- **3 player turns** since the last advance.

The in-game clock is the trigger you can rely on: anything that burns a day — travel, downtime, a long rest — brings the next advance forward. The turn count is a backstop for scenes that take many turns without much time passing, and a run of three quick turns inside one conversation will not always produce a visible development. Resting is not itself the trigger and carries no special risk.

**[God Mode](GodMode.md) and [Think/Plan Mode](ThinkMode.md) turns are skipped by the advance schedule.** They do not advance the in-game clock and do not count toward the cadence, so a scheduled advance never fires on them. Use them as much as you like without burning world time. (A god-mode directive can still change the world directly — but that is you writing the change, not the world moving on its own.)

## What an advance produces

A single advance can move any of these:

- **Background events** — what off-screen NPCs and factions actually did.
- **Rumors** — one or two pieces of gossip NPCs may repeat. Some are true, some half true, some flatly wrong, and the rumor itself never tells you which.
- **Deadlines** — countdowns scheduled for a specific future turn come due, get pushed back, or get cancelled.
- **Faction shifts** — objectives, resources, and standing change. See [FactionSystem](FactionSystem.md).
- **One scene event** (optional) — something that reaches you directly: a messenger, a road encounter, a companion pulling you aside, a quest offer.

You are never handed a report of what changed. Hidden developments stay hidden until the story surfaces them — an NPC mentions it, a price has moved, a rumor reaches you.

## Why it matters

Between advances the world is not frozen, so the state you come back to is not the state you left. An ally makes progress on something you asked for. A caravan arrives. A repair finishes. A rival quietly gains ground.

The game is deliberately tuned *against* a pile-up of disasters. Most advances produce no major development at all — a single day is normally expected to contain none — and every background event is tagged positive, neutral, mixed, or antagonist, with positive and neutral as the default. "Time passed" is explicitly not a reason to invent a crisis.

Hostile developments are rationed by the game itself: at most **one antagonist-flagged event per 14 days of in-game time** survives into your save. Extras are discarded before the turn is written.

## Winning streaks invite trouble

The game counts your consecutive risky wins. Once that streak reaches **2**, each advance rolls to throw a complication at you, and the odds climb as the streak grows:

| Streak | Chance of a complication | Typical scale |
|---|---|---|
| 0-1 | none — cannot fire | — |
| 2 | 40% | Local: a spy burned, a minor delay |
| 3 | 50% | Regional: a network partly exposed, real resource loss |
| 4 | 60% | Regional |
| 5 | 70% | Significant: a major ally captured, an enemy gains ground |
| 6+ | 75% (the cap) | Significant |

Your streak resets to zero the moment a complication lands. Complications show up as a messenger with bad news, supplies you were counting on going missing, a rival who got there first, or a former ally who has changed sides.

## Sanctuary after a victory

When the game recognises that you finished a mission or story arc — a named enemy defeated, the threat cleared, and you taking a post-victory action like looting or resting — it grants **sanctuary**: a window in which the world will not throw a life-ending event at you.

| What you finished | Sanctuary lasts |
|---|---|
| A side quest or cleared dungeon | 8 turns (about 4-5 in-game days) |
| A quest chain finale or chapter end | 15 turns (about 10 in-game days) |
| A campaign climax or a defeated big bad | 30 turns (about 3 in-game weeks) |

Sanctuary can end early if you go looking for a fight.

## Player tips

- **Time is the clock, not rest.** There is no extra penalty for sleeping somewhere dangerous — but anything that eats a day brings the next advance closer.
- **Chase rumors.** Rumors are the main way the game tells you an off-screen event exists. Each one is marked true, partly true, or false behind the scenes, so confirm before you act.
- **Expect the counter-punch.** When a metric you are pushing — territory, faction power, a conversion campaign — crosses 25%, 50%, 75%, or 100%, the next advance must produce a named rival's counter-move, and your metric is blocked from hitting the next milestone that same turn.
- **Don't count on a quiet streak lasting.** A long run of clean wins is exactly when the complication odds are highest.

See [FactionSystem](FactionSystem.md), [NPCRelationships](NPCRelationships.md), [CompanionArc](CompanionArc.md), [CampaignDesign](CampaignDesign.md).
