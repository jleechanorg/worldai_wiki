# WorldArchitect.AI Wiki

> The player-facing guide to [WorldArchitect.AI](https://worldarchitect.ai) — a D&D 5e game that runs in your browser. The game rolls the dice, the world remembers what you did, and the house rules are yours to write.

## Quick start: What to do

```
Dashboard  ──>  Step 1: Choose Your Campaign  ──>  Step 2: Ready to Launch  ──>  Turn loop (Character / Think/Plan / God)
```

1. **Open your dashboard**: sign in at [worldarchitect.ai](https://worldarchitect.ai) to pick up a campaign or start a new one.
2. **Fill in the 2-step wizard**:
   - **Step 1 — Choose Your Campaign**: take **Dragon Knight**, the one ready-made module, or **Play a campaign** and build your own. On the custom path, pick a universe — one-click suggestions for Game of Thrones, Star Wars, Cyberpunk, The Witcher, Middle-earth, Stranger Things, Marvel and Dune, or type any setting you like — then era, protagonist, setting, and a plot "what-if".
   - **Campaign description prompt**: the last section of step 1 (section 7 on the custom path) starts collapsed — click **Expand** to open it, then paste a full campaign bible, world lore, faction rules, or premise. A 70,000-character document has been tested and stored intact.
   - **Step 2 — Ready to Launch**: add an optional character portrait, edit anything on the summary card, and click **Enter the World**.
3. **Play turn by turn**:
   - The GM opens the scene and confirms your character sheet.
   - Pick one of the suggested actions — four in ordinary play, three after a God-mode turn — or take the **Custom Action** option and type your own. In ordinary play each suggestion has a **Show pros and cons** toggle, so you can weigh it before committing. For a longer strategy conversation with the GM, switch to **Think/Plan** first.
   - The three buttons under the message box decide how your text is read:
     - **Character** (the default): what you type is what your character does and says. The story advances.
     - **Think/Plan**: the story pauses while you weigh options with the GM. No time passes, no actions are taken.
     - **God**: administrative control — edit stats, spawn items, teleport, fix mistakes, set persistent narration rules. The world is frozen and the story does not advance.
4. **Know your limits**: playing is free, but every turn counts against a per-account allowance — **100 turns a day, and 50 in any 5-hour window**. Creating campaigns and God-mode turns draw on separate, roomier allowances. If you hit a cap, a "Rate Limit Reached" box tells you when it resets; adding your own model API key raises the ceiling to 5,000 turns a day. The **Add your key — higher limits** button in the campaign header starts that; you can close it with the **×**, and it comes back on your next visit.

---

### Visual walkthrough

#### 1. My Campaigns Dashboard
Your saved worlds. Each card shows when you last played it and a line of character, setting and premise. Click one to drop back in.

![My Campaigns Dashboard](assets/fresh_screenshots/01_dashboard_home.png)

#### 2. Campaign Wizard — Step 1, with the description prompt open
Set the universe, era and protagonist. The last section, **Campaign description prompt**, is where a long world bible goes — it is collapsed until you click **Expand**.

![Campaign Wizard Step 1 with Expanded Campaign Description Prompt](assets/fresh_screenshots/02_wizard_step1_description_prompt.png)

#### 3. Campaign Wizard — Step 2, Ready to Launch
Add a portrait, edit anything you got wrong, then **Enter the World**.

![Campaign Wizard Step 2 Launch Screen](assets/fresh_screenshots/03_wizard_step2_launch.png)

#### 4. A turn in play
The narrative log, your roll results and stats, the suggested actions, and the Character / Think/Plan / God buttons under the message box.

![Live Gameplay Turn and Action Composer](assets/fresh_screenshots/04_gameplay_turn_composer.png)

---

### Quick guides

#### How to design a campaign
The wizard asks for a universe, era, protagonist, setting and a plot "what-if" — everything else you decide in prose. Say up front how powerful your character is meant to get and what the story should feel like, and paste deep world lore into the **Campaign description prompt** field. Plan an opening scene where something is already happening, and set one to three god-mode rules early. See [CampaignDesign](concepts/CampaignDesign.md).

#### How to prompt god mode
God-mode rules are house rules you write that stay in force for the rest of the campaign, changing how the GM narrates. The ones that work name concrete traits, list specific taboos, and anchor a worldview — `X is/does Y. Avoid Z. Always W.` Type `GOD MODE: <rule>` in the composer, or click the God button first. To get rid of a rule, just ask in plain language: `GOD MODE: forget the rule about companion scaling`. See [GodModePrompting](concepts/GodModePrompting.md).

---

## What the game is

WorldArchitect.AI is a tabletop-style RPG that runs in your browser. The system runs the rules — initiative, dice, HP, spells, faction combat — and an AI narrates the world around your choices. You steer it two ways: **in-character actions**, and **God mode**, a pause menu where you edit the world directly (stats, gold, items, NPCs, the clock) and set standing rules for how the GM should narrate. Campaigns run from a few scenes to several hundred, from a village squabble to multiverse-spanning stakes, solo or with a party or at the head of a faction.

This wiki is the player manual. It assumes you've signed up at [worldarchitect.ai](https://worldarchitect.ai) and want to know what to do next. The table of contents below groups the pages by topic; [index.md](index.md) lists every page with a one-line summary.

The case studies are illustrative, not normative. Any setting, any tone, any power level works; the wiki's recommendations are patterns, so take the ones that fit your campaign.

---

## Table of contents

### Start here

| If you want to… | Read |
|---|---|
| Understand what the game is | [What is WorldArchitect.AI?](entities/WorldArchitect.md) |
| Play your first session | [How to play — first 30 minutes](queries/how-to-play-worldai.md) |
| Plan a campaign before launching | [How to design a campaign](concepts/CampaignDesign.md) |
| Start from a finished campaign bible | [House of the Dragon campaign](queries/house-of-the-dragon-campaign.md) |
| Shape how the narration sounds | [How to prompt god mode](concepts/GodModePrompting.md) |
| See what the game does, system by system | [Player user stories](queries/PlayerUserStories.md) |
| Sort out accounts, settings, saving and export | [Player features reference](queries/ExternalUserStories.md) |
| Drive the game from your own code | [Developer API](queries/DeveloperAPI.md) |

### Core systems (concepts/)

| System | What it covers |
|---|---|
| [Combat](concepts/Combat.md) | Initiative, turn order, action economy, AoE, conditions |
| [Dice](concepts/Dice.md) + [DiceAuthenticity](concepts/DiceAuthenticity.md) + [DiceNotation](concepts/DiceNotation.md) + [DiceRollMechanics](concepts/DiceRollMechanics.md) | Who rolls and when, reading `1d20+5`, and why the GM can't fake a result |
| [Spellcasting](concepts/Spellcasting.md) | Spell slots, preparation, concentration |
| [Healing](concepts/Healing.md) + [RestAndDeath](concepts/RestAndDeath.md) | HP recovery, short/long rest, death saves |
| [LootAndRewards](concepts/LootAndRewards.md) + [Equipment](concepts/Equipment.md) | Treasure and XP, gear slots, what an item actually changes |
| [LevelUp](concepts/LevelUp.md) + [LevelUpProgression](concepts/LevelUpProgression.md) + [ASI](concepts/ASI.md) + [Subclass](concepts/Subclass.md) | How leveling happens mid-scene and how to change what the AI picked, growth over a long campaign, the divine endgame past level 20, ability-score and subclass choices |
| [CharacterCreation](concepts/CharacterCreation.md) + [CharacterArchetype](concepts/CharacterArchetype.md) + [AbilityScores](concepts/AbilityScores.md) + [AdvantageDisadvantage](concepts/AdvantageDisadvantage.md) | Building a character: letting the GM build it or doing it yourself, the tabletop shorthand for what a class does in a fight (the game never asks you to pick a party role), ability scores, advantage and disadvantage |
| [CompanionArc](concepts/CompanionArc.md) + [CompanionPersonality](concepts/CompanionPersonality.md) + [NPCRelationships](concepts/NPCRelationships.md) | Companions and NPC reputation |
| [FactionSystem](concepts/FactionSystem.md) + [FactionManagement](concepts/FactionManagement.md) + [FactionPower](concepts/FactionPower.md) | The faction minigame end-to-end |
| [LivingWorld](concepts/LivingWorld.md) | The world keeps moving while you're somewhere else |
| [GodMode](concepts/GodMode.md) + [GodModePrompting](concepts/GodModePrompting.md) | The pause menu: editing the world directly, and writing rules that stick |
| [CharacterMode](concepts/CharacterMode.md) + [ThinkMode](concepts/ThinkMode.md) | The two composer buttons you use in play, and the modes the game picks for you |
| [SpicyMode](concepts/SpicyMode.md) | The 🌶️ switch in the game header, and what it changes |
| [CampaignDesign](concepts/CampaignDesign.md) + [CampaignWizard](concepts/CampaignWizard.md) | Designing a campaign, the 2-step creation flow |
| [DnD5eRules](concepts/DnD5eRules.md) | The D&D 5th Edition rule spine |
| [Initiative](concepts/Initiative.md) + [CombatVictoryProtocol](concepts/CombatVictoryProtocol.md) + [SmartSkillChecks](concepts/SmartSkillChecks.md) | Combat resolution |

### Case studies and reference (entities/)

| Page | What it is |
|---|---|
| [WorldArchitect](entities/WorldArchitect.md) | The game itself — 5-minute pitch |
| [CampaignShowcase](entities/CampaignShowcase.md) | Gallery of example campaigns |
| [ItachiGaiden](entities/ItachiGaiden.md), [AristocratReborn](entities/AristocratReborn.md), [NocturneBg3](entities/NocturneBg3.md), [ItachiUchiha](entities/ItachiUchiha.md) | Write-ups of real campaigns |
| [Daemon](entities/Daemon.md), [AegonTargaryen](entities/AegonTargaryen.md) | Character sketches from the House of the Dragon campaign template |
| [FactionBattleSim](entities/FactionBattleSim.md) + [FactionIntel](entities/FactionIntel.md) | Faction minigame subsystems |
| [GOD_MODE_RESPONSE](entities/GOD_MODE_RESPONSE.md) | What a God-mode turn sends back |
| [CampaignWizard](entities/CampaignWizard.md) | One-screen summary of the campaign creation flow |
| [WorldAI](entities/WorldAI.md) | Alias for the game's name |

### Comparisons

- [vs AI Dungeon](comparisons/WorldArchitect-vs-AIDungeon.md) — structured D&D 5e GM vs freeform LLM storytelling
- [vs Discord RPG bots](comparisons/WorldArchitect-vs-RPG-Bots.md) — dice-and-sheet bots need a human DM; this is the DM

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
4. **[How to prompt god mode](concepts/GodModePrompting.md)** — write rules that change how the narration sounds.

Once you've played one session, read [Player User Stories](queries/PlayerUserStories.md) to see what's possible, then browse [Campaign Showcase](entities/CampaignShowcase.md) for inspiration.

## Contributing

This is a public reference wiki. If you find an error or want to suggest an addition, open an issue on this repo.

The live game is the source of truth. Where this wiki and the game disagree, the game is right and the page needs fixing.

## License

MIT. See [LICENSE](LICENSE).
