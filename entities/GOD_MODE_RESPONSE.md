---
title: "GodModeResponse"
created: 2026-06-19
updated: 2026-09-18
type: entity
tags: [wa-system, wa-prompt]
sources: []
---

# God Mode Response

What a God Mode turn sends back, and how the GM decides which of your directives to follow when two of them disagree. For what God Mode is and how to use it, see [GodMode](../concepts/GodMode.md); for writing directives, see [GodModePrompting](../concepts/GodModePrompting.md).

## What a God Mode turn looks like on screen

A God Mode turn does not produce story text. It produces three things:

1. **A confirmation line** stating plainly what changed — "Set HP to 50. Done." It appears in its own block rather than in the story narration. If the GM returns nothing at all, you see the placeholder `[God Mode turn — no narrative]`.
2. **The state change itself**, applied to your character sheet or the world immediately.
3. **Three follow-up buttons**, always including **Return to story**, which switches you back to Character mode, plus the usual **Custom Action** button at the end. God Mode turns carry no **Show pros and cons** toggles.

If a God Mode turn hands you story prose, something went wrong — the world is supposed to stay frozen.

## How directives are prioritised

There is exactly one rule: **newest wins**. Your active directives are handed to the GM sorted newest-first, with an explicit instruction that the most recent rule takes precedence when two conflict. Length and specificity carry no weight of their own — a one-line rule added today overrides a detailed one added last week.

This is why superseding works. Add the corrected rule and it outranks the old one immediately, even before you drop the original.

## What directives can and can't guarantee

Directives reliably shape tone, voice, POV, pacing, themes, taboos and character register across scenes. They cannot override the rules engine — dice, HP and conditions are the server's — and they cannot promise every single sentence will honour them. A directive is a lens, not a lock.

## Example: directive-driven narration

Illustrative, not from a transcript. Given this directive:

> Uchiha Itachi is stoic, minimalist, and humble. He avoids grandstanding or arrogant terminology.

Default narration reads like this:

> I feel the immense power coursing through my veins. The calculations of geometry and mathematics have yielded the ultimate technique.

With the directive in force, the same beat reads like this:

> The gravity of the moment is heavy. I steady my breath and act with quiet resolve.

## See also

- [GodMode](../concepts/GodMode.md) — the pause menu and everything it can change.
- [GodModePrompting](../concepts/GodModePrompting.md) — writing and revising directives.
- [ItachiGaiden](ItachiGaiden.md) — the campaign the example above is modelled on.
