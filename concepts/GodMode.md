---
title: GodMode
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-system, wa-prompt]
sources: []
---

# God Mode

God Mode is the game's pause menu. Switch to it and the world freezes — the story does not advance, NPCs do not act, no dice are rolled — and you talk to the system as an administrator instead of as your character. What you say there is simply true.

## How to enter it

Two ways, and they do the same thing:

1. Pick the **God** pill under the message box, then type your request.
2. Stay in Character mode and start the message with `GOD MODE:` — for example `GOD MODE: set my HP to 50`.

Capitalisation does not matter. `god mode:`, `God Mode:` and `GOD MODE:` all work, and leading spaces are ignored.

## What God Mode can do

**Edit your character.** HP, gold, XP, level, ability scores, equipment, spell slots.

**Edit the world.** Spawn or delete NPCs, items and locations; teleport anywhere instantly; add, complete or remove missions; change difficulty and other campaign settings.

**Rewrite history.** Replace the text of an earlier scene that went wrong, and add, change or remove the campaign memories the GM carries forward. If the log contradicts what you meant, you can correct the record instead of playing around it.

**Clear stuck state.** Combat that never ended, a level-up that never resolved, a stale banner in the session header — God Mode is where those get reset.

**Set directives.** Standing rules the GM follows in every later scene: "narrate in second person", "companions never fall more than one level behind me", "don't bring up the siege until I ask". Directives are the part players use most, and [GodModePrompting](GodModePrompting.md) is the guide to writing them.

**Move the clock, if you ask outright.** "Set time to Day 10" works. Time never passes on its own during a God Mode turn, and the clock is never wound backwards to patch a continuity slip — those corrections are stored as directives or memories instead.

## What God Mode can't do

- **Roll dice.** God Mode commands are absolute. No skill check, no attack roll, no saving throw.
- **Resolve combat.** It will set your HP to 1 or to 200, but it will not fight the round for you.
- **Advance the story.** No prose, no NPC dialogue, no new scene. Go back to Character mode for that.
- **Rewind world time to fix a timeline.** Continuity fixes become directives or memories, not a clock change.

Everything above is absolute except directives. A directive steers how the GM writes future scenes, and the GM can still miss one.

## Two layers: the header and your directives

1. **The God Mode header**, set once, when you create the campaign. What you typed in the Campaign Wizard — title, setting, character, description — becomes the campaign's seed, and that is what makes scene 1 a Naruto campaign rather than generic fantasy.
2. **Directives**, added during play. They are saved with the campaign, so they survive reloads and are still in force next session. You cannot add directives from the wizard — they only exist once a campaign is running.

Each directive is kept with the date you added it, so you can ask for one to be replaced or dropped without disturbing the rest.

## Seeing your directives

There is no settings screen for directives. To see the ones you have, switch to God mode and ask for them outright:

> GOD MODE: list my active rules

Asked directly like that, the GM reads the campaign's stored list back to you. It won't volunteer the list otherwise, and a vaguely worded question may get a partial answer, so ask for a full recap when you want to check the whole set. To change one, add a replacement or ask the GM to forget the old one — see [GodModePrompting](GodModePrompting.md#how-to-revise-and-drop-directives).

## What a God Mode turn gives back

A confirmation line instead of a scene, the state change applied immediately, and three follow-up buttons that always include **Return to story**, plus the usual **Custom Action** button. [GOD_MODE_RESPONSE](../entities/GOD_MODE_RESPONSE.md) covers that reply in detail.

## Player tips

- **One change per turn.** A God Mode turn that does five unrelated things is harder to check than five turns that each do one.
- **Directives cannot switch the rules off.** "Never roll dice" will not work; dice are rolled server-side. "Don't dwell on dice mechanics in narration" will. If you want a specific *outcome*, make it a state change, not a directive.
- **Add directives gradually.** One at a time, watch how narration changes, then add more. Fifteen at once dilute each other.
- **What directives are good for**: tone, voice, POV, pacing, themes, taboos, power level, companion behaviour and world rules. [GodModePrompting](GodModePrompting.md#what-directives-can-steer) has a worked table for each.

## See also

- [GodModePrompting](GodModePrompting.md) — how to write directives that land.
- [ThinkMode](ThinkMode.md) — the other frozen-world mode, for planning in character.
- [GodModeFAQ](../queries/GodModeFAQ.md) — short answers.
- [ItachiGaiden](../entities/ItachiGaiden.md) — a 432-scene campaign held together by one directive.
