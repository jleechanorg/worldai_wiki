---
title: GodModePrompting
created: 2026-06-19
updated: 2026-06-20
type: concept
tags: [wa-prompt, wa-system, wa-tutorial]
sources: [concepts/GodMode.md]
---

# How to Prompt God Mode

A practical guide to writing god-mode directives that actually shape narration. By the end you'll be able to write, test, and revise directives that take a campaign from "generic D&D" to "the tone I want."

## What god-mode directives are

A directive is a single rule stored in `custom_campaign_state.god_mode_directives`. Each entry has two fields:

```json
{
  "added": "2026-05-30T23:00:00Z",
  "rule": "<the directive text>"
}
```

The system reads these rules when generating narration. They're persistent across scenes. You can add directives mid-campaign.

## How a directive actually works

A directive is a one-sentence instruction that pins a stylistic choice. The system uses the directive as a lens for every scene it generates after the directive is added. The directive doesn't control *what happens* — it controls *how the narration sounds when it happens*.

Three things make a directive land:

1. **It states a concept in concrete terms.** "Stoic, minimalist, humble" beats "interesting."
2. **It lists taboos.** "Avoid grandstanding" beats "don't be too flashy."
3. **It anchors the worldview.** "Views power as a heavy burden" beats "cares about peace."

The system can apply the lens to many different scenes — combat, romance, politics, exposition — as long as the directive is concrete enough to translate into prose choices.

## The 9 directive categories

There are 9 categories of directives that actually work. Use them as a checklist.

### 1. Tone

How the narration feels emotionally.

| Directive | Effect |
|-----------|--------|
| "The narration has a stoic, minimalist tone. Restraint over expression." | Stoic anti-hero |
| "Lean dramatic. Big emotions, big gestures, cinematic scale." | Shonen-anime |
| "Comedic tone. Banter and irony. NPC dialogue should be witty." | Sitcom-style |
| "Grimdark tone. Moral compromise. No clean wins." | Dark fantasy |
| "Hopeful tone. Found family. Earnest connection." | Cozy fantasy |

### 2. Voice

The character or narrator's voice.

| Directive | Effect |
|-----------|--------|
| "First-person narration ('I do X'). Internal monologue is encouraged." | Diary-style |
| "Second-person narration ('You do X'). Closer to the player." | Choose-your-own-adventure |
| "Third-person limited. The narration follows the PC's perspective." | Novelistic |
| "Omniscient narrator. The narration knows more than the PC." | Epistolary |

### 3. POV

Point of view. (Often overlaps with Voice but distinct.)

| Directive | Effect |
|-----------|--------|
| "Stick to the PC's POV. The narration never reveals hidden information." | Tight POV |
| "Allow scene cuts to other characters when narrating world events." | Multi-POV |
| "Use deep POV: the narration shares the PC's thoughts and feelings." | Lyrical |

### 4. Pacing

How fast scenes move.

| Directive | Effect |
|-----------|--------|
| "Fast pacing. Skip montages. Each scene is a key beat." | Cinematic |
| "Slow burn. Linger on sensory detail. Build atmosphere." | Literary |
| "Scene-by-scene. Each turn is a discrete scene with a clear location change." | Theatrical |

### 5. Themes

Recurring motifs.

| Directive | Effect |
|-----------|--------|
| "Recurring theme: the weight of duty vs personal desire." | Stoic drama |
| "Recurring theme: redemption through sacrifice." | Epic |
| "Recurring theme: hubris and its consequences." | Tragedy |
| "Recurring theme: discovery and wonder." | Adventure |
| "Recurring theme: identity and self-knowledge." | Character study |

### 6. Taboos

Things the system should NOT do.

| Directive | Effect |
|-----------|--------|
| "Never break character to explain game mechanics." | Immersive |
| "Avoid 'puzzle game' framing. NPCs have motivations, not keys." | Character-driven |
| "Do not narrate romance unless the PC initiates." | Player agency |
| "Avoid meta-commentary about the AI or the game." | In-fiction |

### 7. Power-level

How much power the PC has.

| Directive | Effect |
|-----------|--------|
| "Bounded power: the PC never exceeds level 5." | Realistic |
| "Escalating power: the PC levels freely, gains abilities, and can transcend." | Shonen |
| "Sandbox power: the PC starts at any level the player chooses." | OP protagonist |

### 8. Companion rules

How companions behave.

| Directive | Effect |
|-----------|--------|
| "Companions are competent. They don't need rescuing." | Pro party |
| "Companions have their own agendas that may conflict with the PC's." | Realistic party |
| "Romance is opt-in only. Don't force it." | Player agency |
| "Companion banter: high. They comment on everything." | Sitcom-party |

### 9. World rules

Constraints on the world itself.

| Directive | Effect |
|-----------|--------|
| "No resurrection magic. Death is permanent." | Stakes |
| "Low-magic world. Spells are rare and costly." | Gritty |
| "Total party kill on combat failure. No deus ex machina." | Hardcore |
| "All NPCs are real: NPCs have motivations and pursue them even off-screen." | Living world |

## The formula

Directives that work follow this formula:

> **X is/does Y. Avoid Z. Always W.**

Or expanded:

> **The PC is \<trait 1\>, \<trait 2\>, and \<trait 3\>. They avoid \<taboo 1\>, \<taboo 2\>. They always \<behavior\>.**

## Worked examples — one per archetype

Each example here is a single-sentence directive that was used in a published campaign. They're grouped by archetype so you can pick the one closest to your campaign's tone.

### Example 1 — Stoic anti-hero (shonen-adjacent)

> The PC is stoic, minimalist, and humble. They avoid grandstanding or arrogant terminology. They speak with polite authority and view their power as a necessary, heavy burden for the sake of peace.

**Used in**: a 432-scene Naruto campaign where the PC was an ANBU-era shinobi. The directive held for 370+ scenes without revision. See [[entities/ItachiGaiden]] for the case study.

Notice its structure:
1. **States the character concept** ("stoic, minimalist, humble").
2. **Specifies taboos** ("avoids grandstanding or arrogant terminology").
3. **Gives examples of what NOT to do** ("e.g., 'math', 'laboratory', 'geometry'").
4. **States the voice register** ("speaks with polite authority").
5. **Anchors the worldview** ("views power as a necessary, heavy burden for the sake of peace").

That's a 5-element directive in one sentence. Use this structure for your own.

### Example 2 — Obsessive specialist (isekai)

> The PC is obsessive, polite, and brilliant. Their internal monologue runs constantly on their area of expertise. They avoid social games and political maneuvering. They always treat their specialty as a system to be optimized, never as a tool to be wielded.

**Used in**: a 50-scene isekai campaign where the PC was reincarnated as a magic-obsessed noble daughter. The directive held for the full campaign. See [[entities/AristocratReborn]].

Same 5-element structure, different archetype. Works for any specialist — mage, swordsman, alchemist, scholar, engineer.

### Example 3 — Grimdark survivor

> The PC is hunted, weary, and pragmatic. They avoid heroic posturing and grand speeches. They always weigh the cost of any action, including the cost to themselves. Looting the dead feels heavy. Winning feels like a compromise.

**Use for**: dark fantasy, survival horror, morally grey campaigns. Sets a "no clean wins" frame.

### Example 4 — Sitcom party

> The narration has a comedic tone. NPCs are witty. The PC's failures are funny, not tragic. They avoid grimdark moments unless used for contrast. They always punchline after a beat of silence.

**Use for**: comedic campaigns, parody, lighthearted party play. Beats grimdark for contrast only.

### Example 5 — Heroic idealist

> The PC is earnest, courageous, and kind. They avoid cynicism and dark-edgy posturing. They always choose the harder right over the easier wrong, even when it costs them. NPCs respond to their example by being braver than they thought they could be.

**Use for**: classic hero's-journey campaigns, paladin-led parties, hopeful arcs.

### Example 6 — Slow-burn literary

> The pacing is slow and atmospheric. The narration lingers on sensory detail — light, sound, smell, weather. The PC's internal life takes as much narrative space as events. They avoid action-movie beats and time-skip montages.

**Use for**: Frieren-style fantasy, literary fiction, character-study campaigns.

## Anti-patterns

Directives that DON'T work fall into four buckets:

### 1. Trying to control plot beats

> "Don't have the PC die. Don't let them fail the heist."

This is plot control. The system can't reliably enforce it because the rules engine can kill you. Directives can shape HOW something happens, not WHETHER it happens.

**Fix**: rewrite as a tone rule.

> "When the PC fails, narrate it as a chance to learn. Avoid fatalistic framing."

### 2. Vague directives

> "Make it cool."
> "Be epic."

These don't give the system enough to work with.

**Fix**: be specific.

> "Cinematic combat. Each blow lands with weight. The PC's finishing moves are described in slow motion."

### 3. Contradictory directives

> "Comedic tone" + "Grimdark tone" at the same time.

The system will oscillate.

**Fix**: pick one primary, one secondary.

> "Comedic primary tone with occasional grimdark beats when the PC faces a hard choice."

### 4. Too many directives at once

Adding 15 directives in scene 1 confuses the system. Each new directive dilutes the others.

**Fix**: start with 1-3. Add more as the campaign matures.

## When to add a directive

Add a directive when:

- **You see a pattern in narration you want more of.** "The PC keeps making witty comebacks. Add a directive that makes this consistent."
- **You see a pattern you want LESS of.** "The system keeps adding dark twists. Add a directive to keep the tone hopeful."
- **The campaign reaches a tonal shift.** "We're entering the multiverse arc. Add a directive for mythic register."
- **You want to test a new style.** "Try a poetic register for the next 10 scenes."

Don't add a directive just because you can. Each directive is a permanent rule.

## How to revise directives

Directives can be removed. (The system treats removal as "this rule no longer applies.") You can also supersede an old directive by adding a new one that overrides it. The pattern:

1. **Add a new directive** that supersedes the old one.
2. **Let it run for 5-10 scenes** to see if it works.
3. **Iterate**.

Published campaigns have shown that one well-written directive can hold for hundreds of scenes without revision. Don't churn directives if the first one is working.

## Worked example — directive progression in a real campaign

Hypothetical progression for a campaign starting as "adventurous" and ending as "mythic":

### Scene 1

No directives. Default tone.

### Scene 10

> Add directive 1: "Lean adventurous. Pacing is brisk. Each scene introduces a new location or challenge."

Effect: faster scene transitions, more variety.

### Scene 30

> Add directive 2: "The PC has a mentor figure (an old wizard) who dispenses cryptic advice."

Effect: recurring NPC.

### Scene 80

> Add directive 3: "As the campaign progresses, the tone shifts toward mythic. By the end, the PC is making choices that affect multiple worlds."

Effect: stakes escalate.

### Scene 150

> Add directive 4: "When narrating the PC's decisions, use weighty, considered prose. The PC feels the gravity of each choice."

Effect: gravitas.

## The 1-line sanity check

Before you commit a directive, ask:

> "If a stranger read this single sentence, would they know what tone I'm going for?"

If yes, ship it. If no, rewrite.

## Quick-start: copy this directive

If you don't know where to start, copy this and customize:

> The PC is \<insert 2-3 traits\>. They avoid \<insert 2 taboos\>. They always \<insert 1 behavior\>.

Examples:

> The PC is cautious, observant, and methodical. They avoid reckless heroics and breaking promises. They always weigh the cost of an action before committing.

> The PC is bold, witty, and impulsive. They avoid long monologues and excessive planning. They always seize the moment.

> The PC is stoic, principled, and reserved. They avoid cruelty and exploitation. They always act with quiet dignity.

## See also

- [[concepts/GodMode]] — what god mode is at the system level.
- [[concepts/CampaignDesign]] — full design guide (directives are step 7).
- [[entities/CampaignShowcase]] — published campaigns using these directive patterns.
