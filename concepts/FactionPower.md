---
title: FactionPower
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Faction Power and Rankings

Faction Power (FP) is a single number measuring how big your faction is. It is what the rankings sort on.

## The formula

The server works FP out the same way every time, and the GM is forbidden from calculating or guessing it:

```
FP =  soldiers
    + spies          x 0.5
    + elites         x 3      (x1.1 for each elite level above 6)
    + acres          x 5
    + fortifications x 1,000
```

Five terms, and that is the whole score. Read it as a shopping list. A fortification costs 1,000gp and adds 1,000 FP, which is the best rate in the game. Ten level-11 elites are worth 45 FP rather than 30, because the level bonus applies.

Four things people expect to count and do not: **gold**, **arcana**, **citizens** and **equipment**. None of them is an input. They matter only because they buy, feed and arm the five things that are. **Intel** is not an input either — it buys a temporary combat bonus, never power ([FactionIntel](../entities/FactionIntel.md)).

Worked out on a young faction of 2,400 soldiers, 60 spies, 25 elites at average level 8, 120 acres and 3 fortifications:

```
2,400 soldiers                        = 2,400
   60 spies        x 0.5              =    30
   25 elites       x 3 x 1.2 (lvl 8)  =    90
  120 acres        x 5                =   600
    3 fortifications x 1,000          = 3,000
                                        ------
                                         6,120 FP   →  Rank #199 of 201
```

Note where half that number comes from. Three buildings, 3,000gp, outweigh 2,400 soldiers who cost 24,000gp to raise and 1,200gp a week to keep.

Your FP and rank appear on the faction status line at the top of each faction response — `[FACTION STATUS] Turn 7 | Rank #199/201 | FP: 6,120`. The status line lists your troops, land and resources but not your buildings, so the fort contribution is the part you have to remember. There is no separate faction screen anywhere in the app.

## Rankings

Rank is nothing more than every faction sorted by FP. You are measured against 200 rival factions, so ranks run from **#1** at the top down to **#201**.

Below **1,000 FP you are not ranked at all**. The game shows you as unranked and tells you how much FP you still need to get on the board; 1,000 FP puts you at #201. Ask `faction rankings` at any time and the game will also tell you the exact gap to the faction directly above you.

Expect to start at the bottom. Even the weakest of the 200 rivals opens around 5,000 FP and the strongest open near 1.5 million, so a faction that has just switched the layer on normally lands somewhere between #188 and #201. Climbing out of the low ranks is the early game.

## What rank does and does not do

- **#1 is the summit of the ladder.** Passing all 200 rivals is what the ranking is for, and the game will tell you when there is no faction left above you. It is not the only long game the faction layer has — [Apotheosis](FactionManagement.md#apotheosis) is the arcane one, and it runs on arcana rather than FP.
- **It shrinks the list of factions that can attack you.** Rivals only pick fights they expect to win — the cautious ones move only on factions well below their strength, and even the aggressive ones will not push much past an opponent a quarter stronger than themselves. Growing makes you a target for fewer of them, not more.
- **It gives you nothing else.** Rank is a scoreboard position, not a bonus. Recruiting elites depends on gold, a training ground and 100 [prestige](FactionManagement.md#prestige); income depends on citizens and buildings. Neither improves because your rank went up.

## What moves your rank

Your own FP never decays. But the 200 rivals grow their power 1–2% every turn, so a turn in which you build nothing costs you rank even though your own number has not moved.

Winning a battle only moves you insofar as it changes something in the formula — troops lost or gained, territory taken, forts captured. A glorious victory that costs you a thousand soldiers moves you *down*.

## Tips

- **Buy forts first.** 1,000gp for 1,000 FP beats 1,000gp for 100 soldiers every time.
- **Watch the gap.** The game tells you exactly how much FP stands between you and the next rank. One fortification is 1,000 of it; one elite is 3.
- **Level your elites.** Every level above 6 adds 10% to what each elite is worth.
- **Do not overextend.** More acres means more citizens to feed and more ground to defend, and territory is only 5 FP an acre.

See [FactionSystem](FactionSystem.md), [FactionManagement](FactionManagement.md), [FactionBattleSim](../entities/FactionBattleSim.md).
