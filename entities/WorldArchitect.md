---
title: WorldArchitect
created: 2026-06-19
updated: 2026-09-18
type: entity
tags: [wa-game, wa-system]
sources: []
---

# WorldArchitect.AI

WorldArchitect.AI is an AI Game Master for tabletop role-playing, built on D&D 5th Edition rules. You describe what your character does; it narrates what happens, tracks your character sheet, rolls the dice, and remembers the campaign. It runs in a browser at [worldarchitect.ai](https://worldarchitect.ai) — nothing to install — and every campaign is saved, so you can stop mid-scene and pick up next week from any device. It is sometimes shortened to [WorldAI](WorldAI.md) — same game, no separate product.

Playing is free. You sign in with Google and get 100 story turns a day (50 in any 5-hour window). God Mode turns and starting new campaigns draw on their own, much larger allowances, so fixing your sheet never costs you story turns. Supplying your own AI provider key raises all of these.

## What you get

- **A GM that switches specialists.** Swing a sword and a combat GM answers; talk to an NPC and a dialog GM answers. You never choose — the game routes each turn to whichever specialist fits it. If you want to see which one handled a turn, switch on Debug Mode on the Settings page; it is off by default. What it means for you: a fight is run by something that knows the combat rules, not by a storyteller improvising numbers.
- **Real 5e rules.** Ability scores, skill checks, saving throws, advantage and disadvantage, initiative, spell slots, hit dice, rests, death saves. Dice are rolled for real, and the game recomputes every total and every success-or-failure verdict itself — so typing "I rolled a 20" changes nothing. See [Dice](../concepts/Dice.md).
- **A world that moves without you.** NPCs pursue their own goals between your turns, time passes, and factions act on their own plans. See [LivingWorld](../concepts/LivingWorld.md).
- **A faction layer.** Run an organization rather than just a character: gather intel, fight rival factions, climb the power rankings, manage resources. See [FactionSystem](../concepts/FactionSystem.md).
- **Three ways to type.** Three buttons sit under the message box, and they decide how your words are read. **Character** (the default) — what you type is what your character does, and the story advances. **Think/Plan** — you weigh options with the GM and no time passes. **God** — you edit the campaign directly. Everywhere this wiki says "God Mode", it means that third button.
- **God Mode.** Your out-of-character channel. Use it to fix and steer the campaign — correct a stat the GM got wrong, add or remove an item, change where you are or how an NPC feels about you — and to leave standing rules that shape how the GM narrates from then on (tone, voice, point of view, themes, things to avoid). Those standing rules are called **directives**. God Mode never advances the story; it changes the campaign around it. See [GodMode](../concepts/GodMode.md).
- **Your choice of AI.** On the Settings page you pick which AI writes your campaigns — Gemini (the default), OpenRouter, Cerebras, or a local gateway — and a specific model within it. The setting applies to all your campaigns and you can change it whenever you like.

## What it isn't

- **Not freeform fiction.** The rules constrain what can happen. Narrate intent all you like; the outcome still goes through the dice and your sheet.
- **Not 5e only.** Players have run Naruto, Baldur's Gate 3 and isekai campaigns alongside ordinary fantasy — you write the premise. The rule spine underneath stays 5e-derived; see [DnD5eRules](../concepts/DnD5eRules.md) for what that covers.
- **Not multiplayer.** Campaigns are single-player. The companions travelling with you are played by the GM, not by your friends.
- **Not offline.** It is a hosted service. Your campaigns live on the server, not on your machine, so you need a connection to play.

## Where to go next

| If you want to… | Read |
|---|---|
| Play your first session | [how-to-play-worldai](../queries/how-to-play-worldai.md) |
| Make a character | [CharacterCreation](../concepts/CharacterCreation.md) |
| Understand a fight | [Combat](../concepts/Combat.md) |
| Know how rolls work | [Dice](../concepts/Dice.md) |
| Level up | [LevelUp](../concepts/LevelUp.md) |
| Run a faction | [FactionSystem](../concepts/FactionSystem.md) |
| Steer the GM's voice | [GodMode](../concepts/GodMode.md) |
| See what other players built | [CampaignShowcase](CampaignShowcase.md) |
| Compare it with what you already use | [vs AI Dungeon](../comparisons/WorldArchitect-vs-AIDungeon.md), [vs Discord RPG bots](../comparisons/WorldArchitect-vs-RPG-Bots.md) |

## Sources

- The live product at [worldarchitect.ai](https://worldarchitect.ai), including its Settings page.
