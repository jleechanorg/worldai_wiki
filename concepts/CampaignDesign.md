---
title: CampaignDesign
created: 2026-06-19
updated: 2026-06-20
type: concept
tags: [wa-campaign, wa-prompt, wa-tutorial]
sources: [entities/CampaignShowcase.md]
---

# How to Design a Campaign

A practical guide to designing a campaign that holds up across many sessions. By the end you'll be able to pick a setting, write a god-mode header, design an opening scene, set up long-term arcs, and use god-mode directives to shape narration.

## Why this matters

Most campaigns that fall flat fail for the same reasons:

1. **Vague setting** — "high fantasy" doesn't give the system anything to work with.
2. **No hook** — the player starts in an inn with no goal.
3. **Conflicting directives** — "be comedic" + "be grimdark" at the same time.
4. **No long-term arc** — the campaign is interesting for 10 scenes and then stalls.
5. **Player doesn't know how to interact** — they don't realize they can change the world with their prompts.

This guide fixes all of that. The recommendations here are patterns drawn from published campaigns — see [CampaignShowcase](../entities/CampaignShowcase.md) for specific examples. Pick the patterns that fit your setting.

## Step 0 — Draft your campaign in a free chat LLM first

The fastest way to blow through your WorldAI budget is to iterate your God Mode header against live campaign runs. Every "let me try the prompt one more time" is a paid scene you didn't need. The five failure modes above all show up on prompt #2, not scene #200 — so catch them in a free chat first, then bring the polished prompt to WorldAI.

**The rule:** do not start a paid WorldAI campaign until you can paste your god-mode header into a chat LLM and have it produce a coherent 3-paragraph preview of scene one without flinching. If the preview is vague, your campaign will be vague.

### Where to draft for free

Pick whichever you already have an account on — the goal is iteration speed, not which LLM is best:

- **God Mode chat** (inside WorldArchitect.AI) — the in-game God Mode is itself a chat LLM interface you can talk to like ChatGPT before you commit to a campaign. Use it to brainstorm settings, test directive wording, and stress-test opening scenes. No campaign-budget consumption while you're just chatting.
- **ChatGPT** — paste a prompt, get a paragraph back, iterate.
- **Gemini** — same idea, free tier.
- **Claude** — same idea, free tier at claude.ai.

Talk to whichever one you pick **just like an LLM chat**. Examples of what to type:

> "I'm designing a Naruto-era Itachi campaign. Help me write a god-mode header. I want stoic tone, escalating power level, opening scene is the night of the Uchiha massacre. The character should be a member of ANBU."

> "Here's my draft god-mode header: `<paste>`. What's vague about it? What would you ask me to clarify before you'd be willing to write scene 1 from it?"

> "Here's my setting: `<paste>`. Suggest 3 alternative opening scenes that don't start in an inn."

### The v4 Campaign Bible template

If you want a structured starting point instead of freestyling, paste the **v4 Campaign Bible template** into ChatGPT / Gemini / Claude and iterate against it:

> **[v4 Campaign Bible template →](https://docs.google.com/document/d/1kWl5zkpxMFO7tQb7C9NRuyhmgRKYmBIdHoNuWF9Q1fI/edit?tab=t.oayq6yj5q57b)**

The template gives the LLM explicit instructions on tone, character architecture, faction structure, item frameworks, and progression tiers — so you get consistent, deep output instead of generic fantasy. Fill in the bracketed fields (`[Insert Tone]`, `[Insert Brief Concept]`) and the LLM will produce a full Campaign Bible you can mine for your god-mode header, directives, and opening scene.

### What to bring back to WorldAI

When your draft prompt passes the "paste-and-preview-scene-one" test, take it to WorldAI:

- A **1-3 sentence god-mode header** (Step 4) you've already stress-tested for vagueness.
- **1-3 directives** (Step 7) you've drafted and refined against the "do NOT include this" checklist.
- An **opening scene** (Step 6) you've sanity-checked against the inn/dream/exposition anti-patterns.
- A **tone** (Step 3) you've confirmed doesn't conflict with itself.

Then — and only then — start the paid campaign.

## Step 1 — Pick a setting

The setting is the world your story lives in. The system supports built-in settings plus custom:

### Built-in settings

- **Naruto** — shinobi politics, kekkei genkai, ANBU operations, clan wars
- **Game of Thrones** — noble houses, court intrigue, dragons, the Long Night
- **Baldur's Gate 3 (BG3)** — Forgotten Realms, mind flayers, the Absolute, faction play
- **D&D 5e fantasy** — default high fantasy
- **Isekai / Reincarnation** — modern person dies and wakes up in a fantasy world

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

## Step 4 — Write the God Mode header

The God Mode header is what you type when creating the campaign. It's:

> Character: \<description\> | Setting: \<description\>

Or, if you want a longer prompt:

> God Mode:
> Character: \<name and concept\> | Setting: \<world\>
> Description: \<longer character backstory\>

The longer the prompt, the more the system has to work with. But keep it focused.

### Worked examples

**Short (Naruto, ANBU era)**:
> God Mode:
> Character: Uchiha Itachi | Setting: Naruto universe. Itachi when he was young and became member anbu. Itachi gaiden arc.

The system used this to build a level-1 Itachi with Sharingan, then ran him through the ANBU arc. See [ItachiGaiden](../entities/ItachiGaiden.md) for what a 400+ scene run of this prompt looks like.

**Long (isekai character study)**:
The Aristocrat V2 prompt was ~3,100 words. It included past-life backstory, reincarnation setup, family dynamics, internal psychology, and world context. The length was worth it because the campaign is character-study heavy. See [AristocratReborn](../entities/AristocratReborn.md).

### Recommendation

**Start short (1-3 sentences)** for your first campaign. **Go long** if you're doing a character-study or reincarnation campaign where internal monologue is a major feature.

## Step 5 — Choose character creation mode

See [CharacterCreation](CharacterCreation.md) for full details. Two paths:

- **AI-generated** (recommended for first-timers): describe what you want, the system builds it.
- **Hand-rolled**: pick race, class, stats. Best for optimized builds.

The system integrates both. For published campaigns, AI-generation is the most common starting point because it produces a coherent build that fits the prompt; players can then refine via in-character requests.

## Step 6 — Plan the opening scene

The opening scene sets the tone, hooks the player, and establishes the campaign's rhythm.

### Strong opening templates

- **"Wake up" scene** — you wake up in the setting. The world unfolds around you. (Most common in isekai.)
- **"First mission" scene** — you have a job. Set the stakes. (Common in shonen, military, and political-intrigue setups.)
- **"First choice" scene** — the world offers you a choice immediately. (Character creation step, then action.)
- **"In medias res" scene** — drop into action. Recover context later. (Boss fight opener.)

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

Each transition is built on the previous one. The player grows into the new stakes.

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

### Meta-prompts (THINK:)

> "THINK:keep thinking about how to get the next milestone ability"

The "THINK:" prefix tells the system to plan/strategize instead of acting immediately. Useful for setting up long-term goals.

### Time-skip prompts

> "Back to story and resume the main plot"

Player signals "I've done the meta-strategy, now back to the world."

## Step 10 — Iterate

Your first campaign will have rough edges. After it ends:

- **What worked?** Note 3-5 things that landed.
- **What didn't?** Note 3-5 things that flopped.
- **What did the directives do?** Did they actually shape narration?
- **Where did pacing break?** Was there a slow middle? An abrupt ending?

Use these notes for your next campaign. The best play — human or AI — iterates.

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
- [CampaignWizard](CampaignWizard.md) — the 3-step creation flow.
- [CampaignShowcase](../entities/CampaignShowcase.md) — published campaigns illustrating these patterns.
