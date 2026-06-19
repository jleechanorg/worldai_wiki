---
title: ItachiGaiden
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [wa-campaign, wa-character]
sources: [raw/Itachi V2_ZMbCnA6b.txt]
campaign_id: ZMbCnA6b
scene_count: 432
level_reached: 44
---

# Itachi Gaiden — Campaign Case Study

A 432-scene Naruto campaign that escalates from "ANBU rookie" to "Emperor of the Multiverse." It's the longest and most layered campaign in the wiki, and a masterclass in escalation, directive writing, and player-driven world-altering prompts.

## The prompt

The God Mode header was short — two lines:

> God Mode:
> Character: Uchiha Itachi | Setting: Naruto universe. Itachi when he was young and became member anbu. Itachi gaiden arc.

The system interpreted this as:
- **Race/clan**: Uchiha (Sharingan user)
- **Class**: Multi-class gestalt (Rogue Assassin + Ranger Gloom Stalker) — both stealth-and-damage classes
- **Setting**: Naruto canon timeline, ANBU era, before the Uchiha massacre
- **Tone defaults**: anime-style action, with character-driven drama

## The directive (added 2026-05-30, scene ~60)

> Uchiha Itachi is stoic, minimalist, and humble. He avoids grandstanding or arrogant terminology (e.g., 'math', 'laboratory', 'geometry'). He speaks with polite authority and views his power as a necessary, heavy burden for the sake of peace.

This single sentence shaped the next 372 scenes of prose.

## What the campaign demonstrates

### 1. AI-generated character with player refinement

The player started with "AI generated" (recommended) but then made specific requests:

> "I have 3 tomoe sharingan already and I think I should have all the progression of gestalt assassin rogue and gloomstalker"
> "Make me level 5 and show my class progression. I should have extra attack"

The system integrated these refinements into the gestalt build. By scene 10, the player had a multi-class Itachi with 3-tomoe Sharingan and starting combat power.

### 2. Player-driven meta-strategy via THINK: prompts

The player used `THINK:` as a meta-prompt prefix to plan rather than act:

> "THINK:think how can i power up quickly and get mangeykyou sharingan"
> "THINK:keep thinking about how to get mangekyou"

This pattern is reusable: it tells the GM "pause, plan, set up the next move." Useful for long-term power-progression campaigns.

### 3. World-altering prompts reshape the state

At various points the player reshaped the world directly:

> "True resurrection for my lunar vassals and give them their freedom then time skip until someone's life in danger"

This freed every vassal the player had previously mind-controlled and time-skipped to the next crisis. The system applied the change to `custom_campaign_state.core_memories` (324 entries by the end) and continued the world from the new state.

### 4. The escalation curve works

By scene 432, the PC was level 44 — "Terminal Administrator / Emperor of Eternal Stillness." The progression went:

- **Scenes 1-50**: ANBU arc. Local village politics. First Sharingan moments.
- **Scenes 50-150**: Uchiha massacre era. Clan politics. Mangekyo awakening.
- **Scenes 150-300**: post-massacre ANBU. World-shaping missions.
- **Scenes 300-432**: multiverse transcendence. Becoming the "Emperor of Eternal Stillness."

Each transition was earned. The player wasn't suddenly L20 — they grew into it.

### 5. The directive actually shaped the prose

Compare scene 1 prose to scene 432 prose. Both follow the directive.

**Scene 1**:
> Welcome to Itachi Gaiden: Path of the Shinobi. Before we begin your journey through the shadows of Konohagakure, we must establish the foundations of your character.

**Scene 432**:
> Deep Night (02:50:00) in the Year 125 DR. I remain seated by the stone lantern, the 'Bladesong' in my marrow vibrating with the final, clinical harmonization of the multiverse. I slowly lift my hand, the lavender ripples of my Rinne-Sharingan flaring with a divine, heatless intensity that reaches beyond the sky.

Both use:
- Specific timestamps and locations.
- Restraint over grandstanding.
- Precise, clinical language.
- Weight-of-duty framing.

The directive held for 432 scenes.

### 6. The end state is mythic, not game-over

The campaign didn't end with "you win." It ended with:

> You are now the singular Emperor of the Pan-Substrate. All other 999 Sovereigns have been harmonized into your hegemony.

And immediately, a new threat emerged:

> A 'Mirror' has appeared—a Rank #1 Sovereign from a parallel substrate who represents the Logic: The Void's Hunger. It is an Itachi who did not choose the garden, but the absolute deletion of all variables.

This is a "campaign continues" ending. The state is preserved; the next session picks up from the Mirror encounter.

## Key takeaways for your own campaign

1. **Short God Mode header is fine** if your directive is good. The Itachi V2 header is two lines. The directive does the heavy lifting.
2. **AI-generate the character, then refine**. Don't be shy about asking for gestalt multi-class if it fits the concept.
3. **Use THINK: for meta-strategy**. It tells the GM "plan, don't act yet."
4. **Directives can be one sentence**. The Itachi V2 directive is one sentence with 5 elements.
5. **World-altering prompts are valid**. Use them when you want to skip ahead.
6. **Escalation curves that span hundreds of scenes** are what the system is designed for.

## The end-of-campaign stats

- **Scenes**: 432
- **Final level**: 44
- **Core memories accumulated**: 324
- **God mode directives**: 1 (added scene 60, never revised)
- **Player-prompt categories used**: freeform, choice, level-up, god-return-story
- **End state**: mythic, not game-over

## Sources

- `~/llm_wiki/raw/campaigns/Itachi V2_ZMbCnA6b.txt` (1.27 MB, 432 scenes).
- `~/llm_wiki/raw/campaigns/Itachi V2_ZMbCnA6b_game_state.json` (152.8 KB game state).
- See [[concepts/GodModePrompting]] for directive-writing lessons.
- See [[concepts/CampaignDesign]] for design lessons.
