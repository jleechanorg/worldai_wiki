---
title: FactionSystem
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-system, wa-mechanic]
sources: []
---

# Faction System

Faction mode is an optional strategic layer that runs alongside your character's story. You hold territory, tax citizens, recruit soldiers and spies, build fortifications, send spies against rivals, fight faction-scale battles, and climb a ranking of 201 factions.

It is off in every campaign until you ask for it.

## How to turn it on

Say so in play. Type **"enable the faction minigame"**, or pick the **Enable the strategic faction management system** option when the GM offers it among your suggested actions. That is the whole process — there is no faction toggle in the [CampaignWizard](CampaignWizard.md), and nothing about faction mode is decided when you create a campaign.

The GM starts offering it once your character actually commands troops: a suggestion at roughly 100 total troop strength, a strong recommendation past 500. You can also ask earlier and get it.

You do not pick starting stats. On enablement the game sorts the troops you already have into soldiers, spies and elites, then sizes your territory and treasury to the position your character has reached in the story — anywhere from **Fledgling** (a village band: 500–2,000 soldiers, 50–200 acres, a few forts) to **Dominant** (an empire: 100,000+ soldiers, 10,000+ acres, 500+ forts). Once on, it stays on unless you explicitly turn it off.

Your account settings also have an **Enable Faction Minigame** switch under **Settings → Faction Management**. It governs whether the faction layer is available to your campaigns at all; it never switches faction mode on by itself, because every campaign starts with it off and you ask for it in play. Turning the account switch off later does not roll back a campaign you have already enabled — that campaign keeps its faction layer until you say, in that campaign, that you want it off.

## Two different things called "faction combat"

| Scale | What triggers it | How it resolves |
|---|---|---|
| 1–5 units | Ordinary fights | Normal D&D 5e turn order ([Combat](Combat.md)) |
| 6–19 units | Larger brawls | Skirmish rules — identical creatures grouped into mobs that share a roll |
| 20+ units | Automatic | Mass combat: army-vs-army, with initiative, terrain and morale |

That 20-unit switch happens on its own, whether or not the minigame is enabled. The strategic minigame — resources, rankings, spies, the [battle simulator](../entities/FactionBattleSim.md) — is the separate opt-in layer described on this page.

## The faction turn

A faction turn is a strategic turn, not a scene. You give orders, the server's faction tools resolve the numbers, and the GM narrates the result.

`end turn` is what advances it. One strategic turn moves world time forward **seven days**, and that is when the weekly ledger runs: tax income, citizen growth, arcana generation, construction progress and troop upkeep are all applied at once. Short actions inside a turn cost 5–15 minutes of world time; a battle costs 30–60.

Every faction response opens with a status line rather than a separate screen:

> `[FACTION STATUS] Turn 7 | Rank #199/201 | FP: 6,120`
> `⚔️ Soldiers: 2,400 | Spies: 60 | Elites: 25 (avg lvl 8) | Territory: 120 acres | Citizens: 4,800/6,000 | Gold: 18,400 | Arcana: 900/2,000`

A young faction really does sit near the bottom of that table: the weakest of the 200 rivals starts around 5,000 power. See [FactionPower](FactionPower.md) for how the number is worked out — the three fortifications behind that 6,120 are not on the status line, because it lists troops, land and resources rather than buildings.

When something changes, a `[DELTA LOG]` follows it showing every gold, unit, territory, citizen and arcana movement with the arithmetic behind it. If a number moved and the log does not explain it, ask.

### A worked turn

> **Turn 7.** You order three things: send 20 spies against the goblin camp, recruit 200 soldiers, and start a fortification.
>
> - Spies: success. +10% combat against that camp for the next 5 turns. They were not spotted.
> - Recruitment: 200 soldiers at 10gp each — 2,000gp spent.
> - Construction: fortification started, 1,000gp, ready in 3 turns.
> - Weekly ledger: +2,400gp tax from 4,800 citizens, +100gp from your farm, −1,485gp upkeep on the 2,600 soldiers you now have, 60 spies and 25 elites. Net +1,015gp.
>
> Your Faction Power rises by exactly 200 — one per new soldier. The gold and the citizens are not in that score; the fourth fortification will be worth 1,000 once it finishes. The game tells you how much further it is to the next rank.

## Commands

| What you want | What you type |
|---|---|
| See your faction | `faction status`, `faction rankings`, `intel report`, `council report` |
| Advance the week | `end turn` |
| Build | `build [type] [qty]`, `upgrade [type]`, `demolish [type] [qty]` |
| Raise troops | `recruit [type] [qty]` |
| Spy | `deploy spies [target] [count]`, `recall spies`, `counter-intel` |
| Attack | `assault`, `skirmish`, `pillage` |
| Appoint officers | `appoint [character] as [role]`, `dismiss [role]` |
| Chase the arcane endgame | `faction research`, `cast apotheosis` |

What your faction owns, spends and builds is on [FactionManagement](FactionManagement.md). The power score and the rankings are on [FactionPower](FactionPower.md).

## Tips

- **Spy before a big attack, not before every raid.** An operation costs 50–200gp per spy and takes 1–3 turns, and pays back at most +20% combat for 8 turns. See [FactionIntel](../entities/FactionIntel.md).
- **Fortifications are the cheapest power you can buy.** One fortification costs 1,000gp and is worth 1,000 Faction Power — the same as a thousand soldiers.
- **Standing still loses rank.** The 200 rival factions grow their own power 1–2% every turn, so a turn where you do nothing costs you position.
- **Do not let the faction eat the story.** Faction turns burn seven days of world time each. Plot that is waiting on a timer keeps waiting.

See [FactionManagement](FactionManagement.md), [FactionPower](FactionPower.md), [FactionFAQ](../queries/FactionFAQ.md), and [NocturneBg3](../entities/NocturneBg3.md) for a campaign that ran the whole system across 600+ scenes.
