---
title: CampaignDesign
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-campaign, wa-prompt, wa-tutorial]
sources: [../entities/CampaignShowcase.md]
---

# How to Design a Campaign

This page is for building your **own** world in the wizard's custom path. If you're about to play for the first time, you don't need it — take the ready-made Dragon Knight campaign in [how-to-play](../queries/how-to-play-worldai.md) and come back when you want your own setting.

The two things you write here:

- **The God Mode header** — what you type into the Campaign Wizard's title, universe, character, setting and description fields. Stored together, it's the seed of the whole campaign: it makes scene 1 a Naruto campaign rather than generic fantasy. You set it once, at creation. Steps 1-6 below are about writing it.
- **Directives** — standing rules you add later, *during* play, that change how the GM narrates. Step 7, and the full guide is [GodModePrompting](GodModePrompting.md).

## Why campaigns fall flat

Almost always one of five reasons:

1. **Vague setting** — "high fantasy" doesn't give the system anything to work with.
2. **No hook** — you start in an inn with no goal.
3. **Contradictory directives** — "be comedic" and "be grimdark" at once.
4. **No long-term arc** — interesting for 10 scenes, then it stalls.
5. **Not realising you can change the world** — the player never uses God Mode or a bold prompt.

The recommendations below are patterns from published campaigns, not rules — see [CampaignShowcase](../entities/CampaignShowcase.md). Take the ones that fit.

## Step 1 — Pick a setting

The setting is the world your story lives in. You have one ready-made module and everything else you can describe.

### The one built-in module

- **Dragon Knight** — Ser Arion, the Celestial Imperium, and the two dragons. Fully written, which also means character, setting, and premise are locked; see [CampaignWizard](CampaignWizard.md) for exactly which fields it greys out.

### Universe quick-picks (custom path)

On the **Play a campaign** path, the Universe field offers eight one-click suggestions — Game of Thrones, Star Wars, Cyberpunk, The Witcher, Middle-earth, Stranger Things, Marvel, Dune — and accepts anything else you type: Naruto, Baldur's Gate 3, plain D&D 5e fantasy, isekai, your own world. None of these are pre-written; they are hints to the GM about the world you want.

### Custom setting

Describe the world in 1-3 sentences. The more specific, the better the system can use it.

**Weak**: "A fantasy world with magic."

**Strong**: "The Shattered Coast — a continent broken into 13 island-states by a magical cataclysm 200 years ago. Each island has a different dominant magic tradition. Travel between islands is by dragon-ride. The Imperial Throne is vacant and seven claimants are at war."

### Worked examples (from published campaigns)

- **Naruto, ANBU era**: `Character: Uchiha Itachi | Setting: Naruto universe. Itachi when he was young and became member anbu. Itachi gaiden arc.` — Two lines, gives the system a canon timeline and a niche (ANBU politics).
- **Isekai, fantasy kingdom**: `Character: Sylphina | Setting: Reincarnated as the seventh daughter of Margrave Garm von Silford in the kingdom of Esfort. A magic-geek soul obsessed with mana structure, locked in her family's library.` — Two lines, sets up an isekai character-study with a niche (library-bound magic researcher).
- **BG3, faction-mode**: A custom BG3 setup running the faction minigame end-to-end with multiple rival factions and planar threats. See [NocturneBg3](../entities/NocturneBg3.md) for an example.

Both patterns work: short and setting-focused (Naruto, isekai) or long with internal-psychology detail (isekai character study). For other genre examples — a Frieren-style slow-burn fantasy, a Luke Skywalker hero's journey, a Sariel angel-themed non-human PC — see [CampaignShowcase](../entities/CampaignShowcase.md).

## Step 2 — Pick a power-level

This is the single most important decision after setting.

### Three models

| Model | When it works | Risk |
|-------|---------------|------|
| **Bounded (L1-5 only)** | Realistic drama, low-magic settings, horror | Player outgrows the campaign fast |
| **Escalating (L1 → L20)** | Long campaigns, shonen-style power growth, multiverse endings | Pacing mismatch if XP is too generous |
| **Sandbox (any level from start)** | OP protagonist, fantasy wish fulfillment, god-tier | Combat becomes trivial |

**Recommendation for new campaigns**: escalating. It gives you the full range from "village politics" to "multiverse stakes." A Naruto or isekai campaign typically uses escalating because the source material itself is escalation-driven. A political-thriller GoT-style campaign might use bounded (L1-10) because the drama comes from court intrigue, not combat power.

## Step 3 — Pick a tone

Tone is the dominant mood of the narration. The system uses your god-mode directives to set it. Pick ONE primary tone:

- **Stoic** — minimalist prose, restrained emotion, weight of duty. (Anime anti-hero, samurai drama.)
- **Dramatic** — high emotion, big gestures, cinematic. (Shonen protagonist, epic fantasy.)
- **Comedic** — banter, irony, lightheartedness. (Sitcom, parody.)
- **Grimdark** — moral compromise, bleak outcomes, no easy wins. (Dark fantasy, survival horror.)
- **Hopeful** — redemptive arcs, found family, earnest connection. (Cozy fantasy, isekai with a heart.)

Mixing two tones that conflict (e.g., comedic + grimdark) leads to confused narration. Pick one primary tone; layer one secondary tone (e.g., stoic + hopeful is fine).

## Step 4 — Write the header: wizard fields and description prompt

These fields *are* the God Mode header. You fill them in the [CampaignWizard](CampaignWizard.md) — six structured boxes plus one expandable **Campaign description prompt** for anything longer.

### Structured wizard fields

- **Favorite Universe / TV Show / IP**: pick one of the eight suggestions or type your own.
- **Timeline / Era**: the historical anchor (e.g., *Robert's Rebellion*, *The Clone Wars*).
- **Favourite Character / Chosen Protagonist**: your protagonist, or blank for an AI-generated hero.
- **Setting / world for your adventure**: 1–3 sentences on the physical and political environment.
- **Plot / What-If Direction**: your campaign's main divergence or hook.
- **Campaign Title**: what the campaign is called on your dashboard — the one box in this set you have to fill in.

### The Campaign description prompt (long-form world bible)

The last section on the custom path, collapsed behind an **Expand** button, is a big text box that takes as much as you want to give it — comfortably more than published bibles like [AristocratReborn](../entities/AristocratReborn.md) (~3,100 words) or [House of the Dragon](../queries/house-of-the-dragon-campaign.md), so length is almost never your constraint. See [CampaignWizard](CampaignWizard.md) for the tested ceiling.

Use it to paste:
1. **Full world bibles**: faction rosters, pantheons, magic systems, world history.
2. **Detailed backstory**: past lives, lineage, mental state, inventory.
3. **Narrative directives**: style rules, taboos, and tone constraints for the GM.

### Worked examples

**Short prompt (1–3 sentences in structured fields)**:
> **Character**: Uchiha Itachi
> **Setting**: Naruto universe. Young Itachi newly inducted into the ANBU Black Ops during the clan tension arc.
> **Plot / What-If**: Focus on ANBU black-ops espionage and clan loyalty dilemmas.

The system uses this to construct a level-1 Itachi with Sharingan and immediately launches the ANBU arc. See [ItachiGaiden](../entities/ItachiGaiden.md) for a 400+ scene case study.

**Long-form prompt (pasted into the Campaign description prompt)**:
> The Aristocrat V2 campaign used a ~3,100 word world bible: past-life memories, reincarnation mechanics, family genealogies, arcane mathematics, and internal psychological complexes. That depth paid off over 50+ scenes of character study. See [AristocratReborn](../entities/AristocratReborn.md).

### Recommendation

**Start short** — structured fields only — for your first campaign, and watch how the GM improvises. **Go long** when you're porting an existing tabletop campaign, adapting a specific novel or anime canon, or building an intricate political or reincarnation story.

## Step 5 — Choose character creation mode

The GM offers three ways to build your character once the campaign opens — see [CharacterCreation](CharacterCreation.md) for the full walkthrough:

- **AI Generated** (recommended for first-timers): describe who they are, the GM builds the sheet.
- **Standard D&D**: step through race, class, background and stats yourself. Best for a build you have already worked out. Starting scores come from Point Buy or the Standard Array — nothing is rolled.
- **Custom Class**: describe a class 5e doesn't have and the GM builds it to your description.

AI Generated is the most common starting point for the published campaigns because it produces a coherent build that fits the prompt; you can then refine it on the review screen or by asking in play.

## Step 6 — Plan the opening scene

The opening scene sets the tone, hooks the player, and establishes the campaign's rhythm.

### Strong opening templates

- **"Wake up" scene** — you wake up in the setting. The world unfolds around you. (Most common in isekai — stories where someone from our world wakes up in a fantasy one.)
- **"First mission" scene** — you have a job. Set the stakes. (Common in shonen, military, and political-intrigue setups.)
- **"First choice" scene** — the world offers you a choice immediately. (Character creation step, then action.)
- **"Straight into it" scene** — the fight or chase is already underway; you learn who you are as you go. (Boss-fight opener.)

### Anti-patterns

- **The inn**: "You're in a tavern. A stranger approaches." This has been done 1000 times.
- **The dream**: opening with a dream sequence delays the player engaging with the world.
- **Excessive exposition**: 3 paragraphs of lore before the player acts.

## Step 7 — Add god-mode directives early

See [GodModePrompting](GodModePrompting.md) for the full guide. Quick advice:

- Add 1-3 directives in the first 10 scenes.
- Each directive should fit on one line.
- Use the formula: "X is/does Y. Avoid Z. Always W."

**Worked example — stoic shinobi directive**:
> The PC is stoic, minimalist, and humble. They avoid grandstanding or arrogant terminology. They speak with polite authority and view their power as a necessary, heavy burden for the sake of peace.

This directive shaped every subsequent scene's prose in one published campaign for 370+ scenes. The structure is reusable: state the character concept, specify taboos, give examples of what NOT to do, anchor the worldview.

**Worked example — obsessive specialist directive**:
> The PC is obsessive, polite, and brilliant. Their internal monologue runs constantly on their area of expertise. They avoid social games and political maneuvering. They always treat their specialty as a system to be optimized, never as a tool to be wielded.

This works for any specialist archetype (mage, swordsman, alchemist, scholar).

## Step 8 — Plan the long-term arc

Long campaigns need a long-term arc. The pattern that works:

### The escalation curve

1. **Scenes 1-10** — local stakes. Village, town, single dungeon. Player learns the rules.
2. **Scenes 10-50** — regional stakes. Country-level threats. Player gains a faction or party.
3. **Scenes 50-200** — continental stakes. World-level threats. Player is a major power.
4. **Scenes 200+** — multiverse / planar stakes. Player is a god-tier entity.

Each transition should feel earned — the player should have time to grow into the new stakes.

### The arc shape

Most successful arcs follow one of these patterns:

- **Hero's Journey** — reluctant hero → chosen one → savior → legend.
- **Power escalation** — underdog → local champion → regional power → god-tier. (Naruto, isekai, most shonen-flavored campaigns.)
- **Political** — minor noble → major player → kingmaker → emperor. (GoT-style, BG3 late-game.)
- **Mystery** — small mystery → larger conspiracy → world-shaking truth.
- **Character study** — the stakes are internal. Power growth is secondary to self-understanding. (Reincarnation isekai, Frieren-style slow-burn.)

Pick ONE shape. Mixing shapes mid-campaign causes confusion.

**Example — power escalation arc** (Naruto, ANBU to multiverse):
- Scenes 1-50: local mission arc, first awakenings.
- Scenes 50-150: clan-level politics, mid-tier power.
- Scenes 150-300: regional / world-shaping missions.
- Scenes 300+: multiverse or planar transcendence.

**Example — character-study arc** (isekai specialist):
- Scenes 1-20: establishing the reincarnated PC's new life and core obsession.
- Scenes 20-50: deepening expertise, first major project.
- Scenes 50-200: the PC's mastery reshapes the world around them.
- Scenes 200+: the obsession itself becomes the campaign's central question.

## Step 9 — Player-prompt patterns that work

The player drives the world through prompts. These patterns recur across published campaigns:

### Strategic planning prompts

> "short rest or long rest before the meeting and think about how to acquire max power during the meeting"

Player takes a moment to plan, then commits to a power-acquisition goal.

### Power-progression prompts

> "Make me level 5 and show my class progression. I should have extra attack"
> "THINK:think how can i power up quickly and get the next milestone ability"

Player explicitly asks for level jumps and progression.

### World-altering prompts

> "True resurrection for my lunar vassals and give them their freedom then time skip until someone's life in danger"

Player reshapes the world: frees NPCs, time-skips, sets the next hook.

### Planning prompts (the Think/Plan button)

> "THINK:keep thinking about how to get the next milestone ability"

Starting a message with `THINK:` does the same thing as clicking the **Think/Plan** button under the message box: the GM strategises with you instead of acting, and no time passes. Useful for setting up long-term goals. See [ThinkMode](ThinkMode.md).

### Getting back to the story

> "Back to story and resume the main plot"

Signals "I'm done planning, now back to the world."

## Step 10 — Iterate

Your first campaign will have rough edges. When it ends, note what landed, what flopped, whether the directives visibly changed the prose, and where the pacing sagged. Carry that into the next one.

## Optional: draft your header in a free chat LLM first

Playing is free, but ordinary play turns count against your allowance — **100 turns a day, 50 in any 5-hour window** (your own API key raises it to 5,000 and 1,000). God Mode turns and campaign creation are metered separately and far more generously, so the cost of a re-roll lands on the scenes you play, not on the creation itself. Re-rolling a vague header against live play burns turns you didn't need to spend, and all five failure modes above show up on prompt #2, not scene #200.

So paste your draft header into ChatGPT, Gemini or Claude — whichever you already have — and ask it to write scene one. If the preview is vague, your campaign will be vague. Useful things to ask:

> "Here's my draft campaign header: `<paste>`. What's vague about it? What would you need clarified before writing scene 1?"

> "Here's my setting: `<paste>`. Suggest 3 opening scenes that don't start in an inn."

For a structured starting point, paste the community **[Campaign Bible template](https://docs.google.com/document/d/1kWl5zkpxMFO7tQb7C9NRuyhmgRKYmBIdHoNuWF9Q1fI/edit?tab=t.oayq6yj5q57b)** (hosted on Google Docs, outside this wiki) and fill in its bracketed fields. It prompts for tone, characters, factions, items and progression tiers, so you get something specific rather than generic fantasy.

## Quick-start checklist

Before launching a campaign, ask:

- [ ] Setting chosen (built-in or custom, 1-3 sentences)
- [ ] Power-level chosen (bounded / escalating / sandbox)
- [ ] Tone chosen (one primary, one secondary)
- [ ] God Mode header written
- [ ] Character creation mode chosen (AI-gen or hand-roll)
- [ ] Opening scene template chosen
- [ ] 1-3 god-mode directives ready
- [ ] Long-term arc shape picked
- [ ] First 10 scenes roughed out (optional but helpful)

## See also

- [GodModePrompting](GodModePrompting.md) — full directive-writing guide.
- [CampaignWizard](CampaignWizard.md) — the 2-step creation flow.
- [CampaignShowcase](../entities/CampaignShowcase.md) — published campaigns illustrating these patterns.
