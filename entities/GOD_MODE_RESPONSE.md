---
title: "GodModeResponse"
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [wa-system, wa-prompt]
sources: []
---

# God Mode Response

Reference page for how god mode directives are read and applied by the AI Game Master.

## The contract

When generating narration, the system reads `custom_campaign_state.god_mode_directives` and incorporates them into the prompt context. The directives are persistent across scenes.

## How directives are prioritized

1. **Most recent first**: directives added later override earlier ones if they conflict.
2. **Specific beats general**: a directive about "scene tone" beats a directive about "narration style" when the system has to choose.
3. **Long-form beats short-form**: a detailed directive wins over a one-liner.

## What the system CAN do

- Apply tone, voice, POV, pacing directives consistently.
- Avoid taboos (words, phrases, plot directions).
- Emphasize themes.
- Maintain character voice.

## What the system CAN'T do

- Override the rules engine (dice, HP, conditions).
- Prevent plot events the system has decided to fire.
- Modify NPC behavior beyond the campaign's persona tags.
- Guarantee directives will be respected in every single sentence.

## Example: directive-driven narration

**Directive**:
> Uchiha Itachi is stoic, minimalist, and humble. He avoids grandstanding or arrogant terminology.

**Without directive** (default):
> I feel the immense power coursing through my veins. The calculations of geometry and mathematics have yielded the ultimate technique.

**With directive**:
> The gravity of the moment is heavy. I steady my breath and act with quiet resolve.

The directive successfully shaped the second version.

See [[concepts/GodMode]], [[concepts/GodModePrompting]], [[entities/ItachiGaiden]].
