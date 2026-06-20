---
title: WorldArchitect
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [wa-game, wa-system]
sources: []
---

# WorldArchitect.AI

WorldArchitect.AI is an AI-powered digital Game Master for tabletop role-playing games, primarily D&D 5th Edition. It runs as a hosted web application at [worldarchitect.ai](https://worldarchitect.ai) and ships with:

- **A multi-agent GM**: 12+ specialized LLM agents (Story, GodMode, CharacterCreation, LevelUp, Planning, Info, Combat, Rewards, Dialog, FactionManagement, etc.) collaborate to narrate, adjudicate rules, and remember your campaign.
- **D&D 5e rules enforcement**: ability scores, skill checks, saving throws, advantage/disadvantage, combat initiative, spell slots, hit dice, rests, death saves — all enforced with structural anti-cheat (no "I rolled a 20" fabrication; dice are rolled by the platform).
- **Living world simulation**: NPCs pursue agendas between your actions. Time advances. Seasons change. Factions scheme.
- **Faction minigame**: a complete side-system for running a faction — intel gathering, combat against rival factions, power rankings, resource management.
- **God Mode**: player-supplied style rules that shape how the GM narrates (tone, voice, POV, themes, taboos). See [GodMode](../concepts/GodMode.md).
- **Multi-provider LLM support**: pick from Gemini, OpenAI, Anthropic, MiniMax, and others at campaign creation time.
- **Persistent state**: every campaign's state is saved to the cloud. Pick up where you left off.

## What it's not

- **Not a chatbot**: there's no single LLM pretending to be a GM. Twelve specialized agents handle different aspects of narration and adjudication, with strict handoffs.
- **Not freeform fiction**: the rules engine constrains what can happen. If you try to "I rolled a 20 and critical-hit the moon", the dice system will compute your actual roll result.
- **Not just D&D 5e**: the system supports other rulesets (custom campaigns, BG3-style, Naruto-style, isekai fantasy) but the rule spine is 5e-derived.
- **Not local-first**: WorldArchitect.AI is a hosted service. State lives in Firestore. The private code repository is `jleechanorg/worldarchitect.ai`.

## Player-facing systems at a glance

| System | Wiki page |
|--------|-----------|
| Combat | [Combat](../concepts/Combat.md) |
| Dice rolling | [Dice](../concepts/Dice.md) |
| Level up | [LevelUp](../concepts/LevelUp.md) |
| Character creation | [CharacterCreation](../concepts/CharacterCreation.md) |
| Faction minigame | [FactionSystem](../concepts/FactionSystem.md) |
| God Mode | [GodMode](../concepts/GodMode.md) |
| Living world | [LivingWorld](../concepts/LivingWorld.md) |

## Sources

- `~/worldarchitect.ai/README.md` — private game repo, public pitch.
- `~/worldarchitect.ai/docs/design/system-architecture.md` — full architecture (private).
