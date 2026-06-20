# WorldArchitect.AI Wiki

> The player-facing guide to [WorldArchitect.AI](https://worldarchitect.ai) — a structured D&D 5e game with server-side dice, persistent world state, faction play, and player-authored god-mode directives that shape narration.

## Executive summary

WorldArchitect.AI is a tabletop-style RPG that runs in your browser. The system runs the rules (initiative, dice, HP, spells, faction combat); an AI narrates the world around your choices. You steer the story two ways: **in-character actions** (what your character does) and **god-mode directives** (persistent rules you set that shape how the narration sounds). Campaigns can last a few scenes or several hundred, escalate from a single village to multiverse-spanning stakes, and support solo play, party play, or running a faction.

This wiki is the player manual. It assumes you've signed up at [worldarchitect.ai](https://worldarchitect.ai) and want to know what to do next.

**What you'll find here:**

- **How to play** — your first 30 minutes, step by step.
- **How to design a campaign** — pick a setting, write a god-mode header, plan an arc.
- **How to prompt god mode** — write directives that actually change the prose.
- **75 player user stories** — every feature in "as a player, I want…" form.
- **75 external user stories (US-026–US-100)** — accounts, live UI, settings, MCP/API, agents, persistence, dice audit, export. See [ExternalUserStories](queries/ExternalUserStories.md).
- **System reference** — combat, dice, faction minigame, level-up, spells, character creation.
- **Case studies** — a handful of published campaigns illustrating what works.

The case studies are illustrative, not normative. The system supports any setting (built-in or custom), any tone (stoic to comedic), and any power level (bounded L1-5 to sandbox god-tier). The wiki's recommendations are patterns — pick the ones that fit your campaign.

---

## Table of contents

### Start here

| If you want to… | Read |
|---|---|
| Understand what the game is | [What is WorldArchitect.AI?](entities/WorldArchitect.md) |
| Play your first session | [How to play — first 30 minutes](queries/how-to-play-worldai.md) |
| Plan a campaign before launching | [How to design a campaign](concepts/CampaignDesign.md) |
| Shape how the narration sounds | [How to prompt god mode](concepts/GodModePrompting.md) |
| See every feature in one list | [75 player user stories](queries/PlayerUserStories.md) |
| Integrate with the game over API or MCP | [External user stories (US-026–US-100)](queries/ExternalUserStories.md) |

### Core systems (concepts/)

| System | What it covers |
|---|---|
| [Combat](concepts/Combat.md) | Initiative, turn order, action economy, AoE, conditions |
| [Dice](concepts/Dice.md) + [DiceAuthenticity](concepts/DiceAuthenticity.md) + [DiceNotation](concepts/DiceNotation.md) + [DiceRollMechanics](concepts/DiceRollMechanics.md) | Server-side rolls, `1d20+5` notation, anti-fabrication |
| [Spellcasting](concepts/Spellcasting.md) | Spell slots, preparation, concentration |
| [Healing](concepts/Healing.md) + [RestAndDeath](concepts/RestAndDeath.md) | HP recovery, short/long rest, death saves |
| [LootAndRewards](concepts/LootAndRewards.md) | Treasure, XP, items |
| [LevelUp](concepts/LevelUp.md) + [LevelUpProgression](concepts/LevelUpProgression.md) + [ASI](concepts/ASI.md) + [Subclass](concepts/Subclass.md) | Level-up modal, long-term progression, ability-score-improvement choices |
| [CharacterCreation](concepts/CharacterCreation.md) + [CharacterArchetype](concepts/CharacterArchetype.md) + [CharacterMode](concepts/CharacterMode.md) + [AbilityScores](concepts/AbilityScores.md) + [AdvantageDisadvantage](concepts/AdvantageDisadvantage.md) | Building a character: AI-gen vs hand-roll, classes, ability scores, advantage/disadvantage |
| [CompanionArc](concepts/CompanionArc.md) + [CompanionPersonality](concepts/CompanionPersonality.md) + [NPCRelationships](concepts/NPCRelationships.md) | Companions and NPC reputation |
| [FactionSystem](concepts/FactionSystem.md) + [FactionPlay](concepts/FactionPlay.md) + [FactionManagement](concepts/FactionManagement.md) + [FactionPower](concepts/FactionPower.md) + [FactionCampaigns](concepts/FactionCampaigns.md) | The faction minigame end-to-end |
| [LivingWorld](concepts/LivingWorld.md) | World state evolves between player actions |
| [GodMode](concepts/GodMode.md) + [GodModePrompting](concepts/GodModePrompting.md) | Player-supplied style rules that shape narration |
| [CampaignDesign](concepts/CampaignDesign.md) + [CampaignWizard](concepts/CampaignWizard.md) | Designing a campaign, the 3-step creation flow |
| [DnD5eRules](concepts/DnD5eRules.md) | The D&D 5th Edition rule spine |
| [Initiative](concepts/Initiative.md) + [CombatVictoryProtocol](concepts/CombatVictoryProtocol.md) + [SmartSkillChecks](concepts/SmartSkillChecks.md) | Combat resolution |

### Reference (entities/)

| Page | What it is |
|---|---|
| [WorldArchitect](entities/WorldArchitect.md) | The game itself — 5-minute pitch |
| [WorldAI](entities/WorldAI.md) / [WorldArchitectAI](entities/WorldArchitectAI.md) | Alias redirects |
| [CampaignShowcase](entities/CampaignShowcase.md) | Gallery of example campaigns (case studies) |
| [ItachiGaiden](entities/ItachiGaiden.md), [AristocratReborn](entities/AristocratReborn.md), [NocturneBg3](entities/NocturneBg3.md), [PrinceDaemon](entities/PrinceDaemon.md), [Daemon](entities/Daemon.md), [AegonTargaryen](entities/AegonTargaryen.md), [ItachiUchiha](entities/ItachiUchiha.md) | Individual published-campaign case studies |
| [FrierenCampaign](entities/FrierenCampaign.md), [LukeCampaign](entities/LukeCampaign.md), [SarielCampaign](entities/SarielCampaign.md), [SarielCrossCampaign](entities/SarielCrossCampaign.md) | Additional archetype examples |
| [ChiontharWyrm](entities/ChiontharWyrm.md) | Combat encounter example |
| [FactionMinigame](entities/FactionMinigame.md) + [FactionBattleSim](entities/FactionBattleSim.md) + [FactionIntel](entities/FactionIntel.md) + [FactionRankings](entities/FactionRankings.md) | Faction minigame subsystems |
| [GOD_MODE_RESPONSE](entities/GOD_MODE_RESPONSE.md) | God mode's response shape |
| [CampaignWizard](entities/CampaignWizard.md) | The creation-flow entity |

### Comparisons

- [vs AI Dungeon](comparisons/WorldArchitect-vs-AIDungeon.md) — structured D&D 5e GM vs freeform LLM storytelling
- [vs RPG Bots](comparisons/WorldArchitect-vs-RPG-Bots.md) — vs Discord RPG bots

### FAQ

- [Dice FAQ](queries/DiceFAQ.md) — common dice questions
- [GodMode FAQ](queries/GodModeFAQ.md) — common god-mode questions
- [Faction FAQ](queries/FactionFAQ.md) — common faction questions

### Meta

- [SCHEMA.md](SCHEMA.md) — wiki conventions, frontmatter, tag taxonomy
- [log.md](log.md) — change history
- [index.md](index.md) — full page catalog

---

## Recommended reading order

If this is your first time, read these four pages in order and skip the rest:

1. **[What is WorldArchitect.AI?](entities/WorldArchitect.md)** — what the game does and doesn't do.
2. **[How to play](queries/how-to-play-worldai.md)** — sign up, run the wizard, take your first action.
3. **[How to design a campaign](concepts/CampaignDesign.md)** — pick a setting, write a god-mode header, plan your arc.
4. **[How to prompt god mode](concepts/GodModePrompting.md)** — write directives that change how the narration sounds.

Once you've played one session, read [Player User Stories](queries/PlayerUserStories.md) to see what's possible, then browse [Campaign Showcase](entities/CampaignShowcase.md) for inspiration.

## Contributing

This is a public reference wiki. If you find errors or want to suggest additions, open an issue on this repo.

The private game code (`jleechanorg/worldarchitect.ai`) is the source of truth for behavior. This wiki summarizes and explains — it does not duplicate code paths.

## Quick summaries

Three short reads if you want the gist before diving in.

### How to play — your first 30 minutes, step by step

You sign up at [worldarchitect.ai](https://worldarchitect.ai), open the Campaign Wizard, pick a setting (built-in or custom 1-3 sentence description), and choose how to build your character — AI-generated (recommended for first-timers), hand-rolled, or a preset. The system narrates an opening scene, you declare your first action, and the loop runs turn by turn: GM narrates → you act → system rolls dice if needed → GM narrates outcome. Add a god-mode directive when the narration drifts from what you want; use `THINK:` prompts to plan ahead of acting.

See [how-to-play-worldai](queries/how-to-play-worldai.md).

### How to design a campaign — pick a setting, write a god-mode header, plan an arc

Pick a **setting** (built-in like Naruto, GoT, BG3, isekai, or a custom 1-3 sentence description — specific beats vague), then a **power-level** (bounded for drama, escalating for long campaigns, sandbox for OP protagonists), then a **tone** (one primary — stoic, dramatic, comedic, grimdark, hopeful — plus an optional secondary). Write the **God Mode header** (`Character: ... | Setting: ...`), choose a character-creation mode, plan an opening scene (avoid the tavern, the dream, and excessive exposition), add 1-3 god-mode directives early, and pick an arc shape — hero's journey, power escalation, political, mystery, or character study.

See [CampaignDesign](concepts/CampaignDesign.md).

### How to prompt god mode — write directives that actually change the prose

A directive is a single-sentence rule stored in `custom_campaign_state.god_mode_directives`. The system uses it as a lens for every scene generated after the directive is added. Three things make a directive land: state the character concept in concrete terms ("stoic, minimalist, humble" not "interesting"), list taboos ("avoids grandstanding"), and anchor the worldview ("views power as a heavy burden"). Nine categories work — tone, voice, POV, pacing, themes, taboos, power-level, companion rules, world rules. Use the formula `X is/does Y. Avoid Z. Always W.` Start with 1-3 directives, add more as the campaign matures. Anti-patterns: trying to control plot beats, vague directives ("be epic"), contradictory tones, and adding 15 directives in scene 1.

See [GodModePrompting](concepts/GodModePrompting.md).

## License

MIT. See [LICENSE](LICENSE).
