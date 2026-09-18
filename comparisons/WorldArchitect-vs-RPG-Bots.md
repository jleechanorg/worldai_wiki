---
title: WorldArchitect vs RPG Bots
created: 2026-06-20
updated: 2026-09-18
type: comparison
tags: [wa-comparison]
sources: []
---

# WorldArchitect.AI vs Discord RPG bots

If you already play D&D on Discord, you are probably using a bot. This page is for working out whether WorldArchitect.AI replaces it, complements it, or is simply a different hobby.

The short answer: **Discord RPG bots are tools for a table that already has a human Dungeon Master. WorldArchitect.AI is the Dungeon Master.**

> Discord bot details checked on **2026-09-18** against the projects' own documentation. Bots change; check the one you actually use. If something here is out of date, open an issue on this wiki.

## The two kinds of Discord RPG bot

**Table tools.** [Avrae](https://avrae.io/) is the best-known: a dice parser wired into D&D Beyond that imports your character sheet, generates roll macros for attacks and saves, and tracks initiative and HP for a fight. Dice Maiden and similar bots do the system-agnostic version — they roll dice and nothing else. These bots do bookkeeping. A human decides what happens.

**Grind games.** The other family (EPIC RPG, Mudae and their relatives) are idle or collection games that happen to live in a chat window: type a command, get loot, level a number, repeat with your server. There is no campaign and no story to speak of.

Neither family narrates. That is not a gap in them — it is the design.

## Side by side

| | WorldArchitect.AI | Table-tool bots (Avrae, Dice Maiden) | Grind bots |
|--|-------------------|--------------------------------------|------------|
| Who runs the story | An AI Dungeon Master | A human at your table | Nobody — it is a loop |
| Players | You, solo, any time | A group, scheduled | Your whole server |
| Dice | Rolled by code, then re-checked by the game before the result counts | Rolled by the bot, full 5e notation | Rolled, but the numbers are the game |
| Rules | 5e enforced by the game | 5e maths automated; rulings are the DM's | Custom to the bot |
| Character sheets | Built by a wizard, then maintained for you | Imported from D&D Beyond or a spreadsheet, refreshed by hand | A profile with stats |
| Combat | Initiative, action economy, conditions, death saves, narrated as it resolves | Initiative and HP tracked; the DM describes it | A damage formula |
| World memory | Full campaign state carried scene to scene | Whatever the DM wrote down | None |
| Where you play | A browser | Your Discord server | Your Discord server |
| Prep needed | None | A DM, an adventure, a session time | None |
| Cost | Free, with a turn limit | Usually free | Usually free, with paid boosts |

## What each one is actually good at

**A Discord table tool is better when you have a group and a DM.** Nothing here replaces four friends arguing about whether the rope reaches. Avrae removes the arithmetic from that night and leaves the judgement with the human, which is the right split for a real table.

**WorldArchitect.AI is better when you do not have a table.** It is built for solo play at whatever hour you are free: it invents the world, plays every NPC, enforces the rules, rolls the dice, and remembers what you did twenty sessions ago. See [How to play — first 30 minutes](../queries/how-to-play-worldai.md).

**Grind bots are a different hobby.** They are a shared idle game with RPG vocabulary. If that is what you want, WorldArchitect.AI is not it.

## Things a bot cannot do that matter here

- **Standing narration rules.** [God mode directives](../concepts/GodMode.md) let you write a style rule once — "second person", "no anachronisms", "the empire is always losing" — and every later scene obeys it.
- **A world that moves without you.** Factions scheme, NPCs remember slights, and time passes between scenes. See [FactionSystem](../concepts/FactionSystem.md) and [LivingWorld](../concepts/LivingWorld.md).
- **Dice the storyteller cannot fudge.** A bot rolls honestly because a human decides what the roll meant. Here the narrator *is* the game, so the rolls are policed: the game commits to a secret number before the turn, checks afterwards that the roll used it, redoes the arithmetic, and rejects a result the narrator invented. The record behind that check isn't shown on screen yet. See [DiceAuthenticity](../concepts/DiceAuthenticity.md).

## Things a bot does better

- **Playing with other people.** WorldArchitect.AI campaigns are single-player.
- **Sitting inside a conversation you are already having.** The bot is in the channel; this is a website in another tab.
- **Systems other than 5e.** A generic roller handles Pathfinder, Call of Cthulhu, or your friend's homebrew. WorldArchitect.AI is a D&D 5e engine.

## Using both

They do not conflict. Run your weekly group on Discord with Avrae, and run a solo campaign here between sessions — the same character concept, played out in the weeks when nobody else can make it.

## Sources

- [What is WorldArchitect.AI?](../entities/WorldArchitect.md) — game overview.
- [How to play — first 30 minutes](../queries/how-to-play-worldai.md) — what a session here looks like.
- Avrae's own documentation at [avrae.io](https://avrae.io/), plus D&D Beyond's Avrae support article. Checked 2026-09-18.
