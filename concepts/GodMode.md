---
title: GodMode
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-system, wa-prompt]
sources: []
---

# God Mode

God Mode is a player-supplied set of style rules that shape how the AI Game Master narrates your campaign. It's the single most powerful customization lever you have.

## What it is

When you create a campaign, you supply a "God Mode" prompt — a header that describes your character, setting, and tone. After the campaign starts, you can also add **directives** that tell the GM how to handle specific situations.

Two layers:

1. **God Mode Header** (set at campaign creation): character + setting + tone. Example:
   > Character: Uchiha Itachi | Setting: Naruto universe. Itachi when he was young and became member anbu. Itachi gaiden arc.
2. **god_mode_directives** (added during play): ongoing style rules. Stored in `custom_campaign_state.god_mode_directives` as a list of `{added, rule}` entries.

## Why it matters

Without god mode directives, the GM defaults to "balanced D&D 5e narrative" — serviceable but generic. With good directives, the same engine produces stoic poetic prose, or grimdark survival horror, or comedic buddy-cop banter.

## How to write good directives

See [GodModePrompting](GodModePrompting.md) for the full guide. Quick formula:

> X is/does Y. Avoid Z. Always W.

Example (real directive from the Itachi V2 campaign):
> Uchiha Itachi is stoic, minimalist, and humble. He avoids grandstanding or arrogant terminology (e.g., 'math', 'laboratory', 'geometry'). He speaks with polite authority and views his power as a necessary, heavy burden for the sake of peace.

## Where directives live

Directives are stored on the campaign's `custom_campaign_state` document in Firestore:

```json
{
  "custom_campaign_state": {
    "god_mode_directives": [
      {
        "added": "2026-05-30T23:00:00Z",
        "rule": "Uchiha Itachi is stoic, minimalist, and humble..."
      }
    ]
  }
}
```

You can view and edit these from the campaign's settings panel during play.

## The 9 directive categories

1. **Tone**: stoic, dramatic, comedic, grimdark, hopeful
2. **Voice**: minimalist, verbose, poetic, terse
3. **POV**: 1st person, 2nd person, 3rd person limited, omniscient
4. **Pacing**: fast action, slow burn, scene-by-scene
5. **Themes**: redemption, vengeance, discovery, duty, hubris
6. **Taboos**: things the player explicitly told the GM NOT to do
7. **Power-level**: bounded (level 1-5 only), escalating (start at L1, level freely), sandbox (any level)
8. **Companion rules**: relationship dynamics, romance allowed, party banter level
9. **World rules**: no resurrection, low magic, all-TPK-on-combat-failure, etc.

See [GodModePrompting](GodModePrompting.md) for full examples of each.

## Player tips

- **Directives apply across scenes**: once set, they affect every narration until removed.
- **Layer directives over time**: add new ones as the campaign matures.
- **Don't fight the rules engine**: "Never roll dice" doesn't work; the system enforces dice. But "Don't dwell on dice mechanics in narration" works.
- **Test small first**: add one directive, see how it affects narration, then add more.

## Sources

- `~/llm_wiki/raw/campaigns/Itachi V2_ZMbCnA6b_game_state.json` — `custom_campaign_state.god_mode_directives`.
- `~/llm_wiki/raw/campaigns/Itachi V2_ZMbCnA6b.txt` — full 432-scene campaign showing directives in action.
