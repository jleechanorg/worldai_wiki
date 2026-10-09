---
title: FactionManagement
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Faction Management

What your faction owns, what it spends, and who runs it. For how to switch faction mode on and what a turn looks like, see [FactionSystem](FactionSystem.md).

## Resources

Four numbers, shown on the status line every turn:

- **Gold** — pays for troops, buildings and weekly upkeep. Faction gold is a separate purse from your character's own coin; spending one does not touch the other.
- **Territory**, in acres — sets your citizen cap (acres × 50) and is worth 5 Faction Power per acre.
- **Citizens** — your population. They grow by `50 + 1.5%` of your current population each turn, up to the cap, and pay 0.5gp each in weekly tax.
- **Arcana** — a magical resource produced by mana fonts. It pays for [Apotheosis](#apotheosis) and nothing else.

There is no "influence" and no "materials" stat.

### Prestige

Prestige is your faction's standing — a fifth number, and the one that is not on the status line. It accrues slowly from the size of your realm and from lesser factions that answer to you, and a Charisma-based **Diplomat** on your council is what makes it accrue faster. Ask for a `council report` and the GM will tell you where you stand.

You need **100 prestige** before you can recruit elites at all. That is what it is for: it is a threshold you cross, not a purse you spend from, and it is not part of [Faction Power](FactionPower.md).

## Units

Your forces are tracked as three counts, not as individual character sheets:

- **Soldiers** — the line troops. 10gp each.
- **Spies** — run intel operations. 50gp each, and you need a shadow network before you can recruit any.
- **Elites** — named heroes and veterans. 500gp each, and they require a training ground plus 100 prestige. The game tracks their *average level*, and elites above level 6 are worth 10% more power per level.

Weekly upkeep runs 0.5gp per soldier, 1gp per spy, 5gp per elite. Recruit with `recruit [type] [qty]`.

## Buildings

Build with `build [type] [qty]`; `upgrade` and `demolish` work the same way. Construction finishes at the end of a turn.

| Building | Cost | Turns | What it does |
|---|---:|---:|---|
| Farms | 1,000gp | 1 | Feeds citizen growth, +100gp/week |
| Training grounds | 1,000gp | 1 | Lets you recruit elites |
| Artisans' guilds | 1,000gp | 1 | Faster building, +200gp/week |
| Arcane libraries | 1,000gp | 2 | Research and spell access |
| Mana fonts | 1,500gp | 2 | Generates arcana, +1,000 arcana capacity |
| Fortifications | 1,000gp | 3 | Defence in battle, +1,000 Faction Power |
| Wards | 1,000gp | 1 | Blocks 75% of hostile magic once they cover 2.5% of your territory, and catches spies |
| Shadow networks | 1,500gp | 2 | +2 spies a week, and catches spies |

Wards are the one building with a coverage threshold behind them: the 75% spell block is what you get once your wards cover 2.5% of your acreage. Take more land and you need more wards to keep it.

## Apotheosis

Apotheosis is the reason to build mana fonts, and the only thing arcana is ever spent on. It is the faction layer's magical endgame, run in parallel with the climb up the rankings.

It takes three things, in order:

1. **Research Lore to its maximum in five schools of magic.** Arcane libraries are what make research move; a Wisdom-based Sage on your council makes it move faster.
2. **Research the incantation itself.**
3. **Cast it seven times.** Each casting costs more arcana than the last: 1,000, then 10,000, 100,000, 500,000, 1,000,000, 5,000,000 and finally 10,000,000.

Every successful casting raises your Faction Power by 10% and destroys one of the low-ranked rival factions outright. Ask for a faction status and the GM reports where you are: seals cast out of seven, schools maxed out of five, and what the next casting will cost.

The costs climb far faster than a small realm's arcana income, so a serious run means many mana fonts and the territory to put them on. Say `cast apotheosis` when you are ready.

## Your council

Appoint named characters to six seats with `appoint [character] as [role]`, and check them with `council report`. Level-6-and-up elites and courtiers make the best officers, and each seat keys off a different ability score:

- **Marshal** (Strength) — cheaper upkeep, faster soldier growth.
- **Steward** (Intelligence) — more gold and better farm output.
- **Spymaster** (Dexterity) — better intel results and lower chance your spies are caught.
- **Diplomat** (Charisma) — builds prestige.
- **Sage** (Wisdom) — faster research.
- **Confidant** (any) — adds 50% on top of every other council bonus.

## Other factions

Other factions are allied with you or they are not; there is no friendly-to-hostile ladder in between. When you propose an alliance, the offer is scored on how your army compares to theirs, their opinion of you, whether you have treated them as a friend or a rival, and what your spies have learned about them. A defensive ally reinforces you with half its strength when you are attacked.

The 200 rival factions come in three temperaments: 60 passive ones that are easy to befriend, 80 balanced ones that attack only targets well below their strength, and 60 aggressive ones that will attack anything they are not badly outgunned by.

See [FactionSystem](FactionSystem.md), [FactionPower](FactionPower.md), [FactionIntel](../entities/FactionIntel.md).
