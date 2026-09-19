---
title: "WorldArchitect vs AIDungeon"
created: 2026-06-19
updated: 2026-09-18
type: comparison
tags: [wa-comparison]
sources: []
---

# WorldArchitect.AI vs AI Dungeon

Both let you play a story with an AI narrator. They are built for opposite things: WorldArchitect.AI runs a rules-enforced D&D 5e campaign, AI Dungeon runs freeform interactive fiction. This page is for deciding which one you want.

> **About the AI Dungeon column:** checked against [aidungeon.com](https://aidungeon.com) and their [pricing page](https://play.aidungeon.com/pricing) on **2026-09-18**. Their models, tiers and limits change often — check their site for current details rather than trusting this table. If something here is out of date, open an issue on this wiki.

## Quick summary

| | WorldArchitect.AI | AI Dungeon |
|--|-------------------|------------|
| What it is | A D&D 5e campaign with an AI Dungeon Master | Freeform AI storytelling |
| Rules | 5e enforced by the game | No rules engine — the story model decides |
| Dice | Rolled by code, then re-checked by the game before the result counts | No dice system; outcomes are narrated |
| Combat | Initiative, action economy, conditions, death saves | Improvised in prose |
| Memory of your world | Full campaign state: HP, spells, conditions, factions, NPC relationships, world flags | Story text plus a Memory Bank you curate; entry count scales with your tier |
| Standing style rules | God mode directives that persist for the rest of the campaign | World Info entries and a per-action Author's Note |
| Faction warfare | Yes — a full minigame with intel, battles and rankings | No |
| Model choice | Gemini by default; bring a key for OpenRouter, Cerebras, or a local gateway | Their own model list, varying by membership tier |
| Cost | Free, no paid tier. Turn limits instead | Free tier plus paid memberships |
| Best for | Rules, structure, long stateful campaigns | Creative improvisation, any genre, quick scenarios |

## Rules

**WorldArchitect.AI** enforces 5e. You cannot say "I rolled a 20" — the game rolls for you. Initiative is rolled, turns are tracked, HP is computed, and combat has a real action economy.

**AI Dungeon** has no rules engine. Whatever happens next is what the story model writes. That is the point: nothing tells you no.

## Dice

**WorldArchitect.AI** rolls come out of real random-number code, not the narrator's imagination. The game commits to a secret number before the turn and afterwards checks that the roll actually used it, redoes the arithmetic itself, and flags anything that does not line up — so a result the storyteller simply made up gets rejected rather than told to you. In play you see the dice, the modifiers, the target number and the outcome. The fairness record behind that check is kept with every turn, but nothing in the app displays it yet, so this is the game policing itself rather than something you can audit by hand. See [DiceAuthenticity](../concepts/DiceAuthenticity.md).

**AI Dungeon** has no dice system. Success and failure are narrative choices the model makes.

## Combat

**WorldArchitect.AI** runs full 5e combat — initiative order, action economy, conditions, death saves, reactions — and hands the scene to a combat specialist that narrates the mechanics as they resolve. See [Combat](../concepts/Combat.md).

**AI Dungeon** improvises. There is no turn order and no HP clock; a fight lasts as long as the prose says it does.

## What the game remembers

**WorldArchitect.AI** keeps campaign state in the cloud and carries it scene to scene: hit points, spell slots, conditions, inventory, faction standing, NPC relationships, world flags. Campaigns of hundreds of scenes are normal, and the state is still coherent at the end of them.

**AI Dungeon** keeps your story text and a Memory Bank you fill in yourself, sized by your membership tier. Long adventures drift unless you maintain those entries.

## Standing instructions to the narrator

**WorldArchitect.AI** god mode directives are style rules you write once and the game keeps. Add one in the middle of a campaign — "narrate in second person", "no modern slang", "make every noble corrupt" — and it shapes every scene after it. See [GodMode](../concepts/GodMode.md).

**AI Dungeon** uses World Info entries plus a per-action Author's Note. That is more precise turn by turn and less consistent across a long story.

## Model choice

**WorldArchitect.AI**: you pick the AI model in Settings. Google Gemini is the default and needs no setup. You can also point the game at OpenRouter, Cerebras, or a local gateway by adding your own API key for that service. The choice applies to your whole account, not to one campaign.

**AI Dungeon**: you pick from their own model list, and which models you can reach depends on your membership tier. We do not track that list.

## Who narrates

**WorldArchitect.AI** routes each scene to a specialist — combat, dialog, faction moves, level-up, lookups, character creation — so a fight is handled by something that understands fights. Which specialist handled a turn is not shown during normal play — turn on **Settings → Debug Mode** and it appears in the Debug Info panel under the narration. The trade-off is that the voice varies slightly between kinds of scene.

**AI Dungeon** uses one model for everything, which gives a more uniform voice.

## Cost

**WorldArchitect.AI** is free to play. There is no paid tier. Instead there is a turn limit — roughly 100 turns a day and 50 in any five-hour window. Add your own model API key in Settings and the limit rises sharply.

**AI Dungeon** has a free tier plus paid memberships, which buy larger context, more memory entries and access to their bigger models. Their pricing page has current numbers.

## Which one

**Pick WorldArchitect.AI if** you want rules-enforced 5e, dice the narrator cannot fudge, a campaign that stays coherent across hundreds of scenes, or the faction minigame.

**Pick AI Dungeon if** you want pure improvisation, a single consistent narrator voice, short one-off scenarios, or a genre no rules system covers.

You can also use both. Nothing stops you drafting a world in AI Dungeon and then running it here as a [custom campaign](../concepts/CampaignDesign.md).

## Sources

- [What is WorldArchitect.AI?](../entities/WorldArchitect.md) — game overview.
- [DiceAuthenticity](../concepts/DiceAuthenticity.md) — how rolls are made and checked.
- AI Dungeon's own site: [aidungeon.com](https://aidungeon.com), [pricing](https://play.aidungeon.com/pricing), [help centre](https://help.aidungeon.com). Checked 2026-09-18.
