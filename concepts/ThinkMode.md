---
title: ThinkMode
created: 2026-09-18
updated: 2026-11-03
type: concept
tags: [wa-mechanic, wa-tutorial]
sources: []
---

# Think Mode

Three buttons: **Act** ([CharacterMode](CharacterMode.md)) · **Think** ([ThinkMode](ThinkMode.md)) · **God** ([GodMode](GodMode.md))

Think mode is your character stopping to think. The world freezes — the story clock is paused and nothing acts — and instead of narrating what happens next, the GM gives you your character's own strategic analysis.

## How to use it

Pick the **Think** pill under the message box (the placeholder becomes `Think mode: ask for advice, time paused…`), or start a message with `THINK:` from any mode except God — there the God pill wins over the prefix:

> THINK: how do I get into the vault?

Hovering or focusing the button explains: *"Think pauses time so you can plan: get your options with pros and cons. Nothing happens in the story."* Capitalisation doesn't matter, and leading spaces are ignored.

## Your stats decide how good the plan is

This is the part players miss. Simple recall (who is in your party, recent events, your class features) is answered with no roll at all. For a real plan, the GM makes an ability check for your character — Intelligence for tactical and logical questions, Wisdom for intuitive and social ones, whichever fits the question better — against a difficulty set by how hard the plan is. Checks start at DC 9:

| DC | What you're thinking about |
|----|---------------------------|
| 9-12 | Multi-step plans, complex social situations, coordinating a group |
| 13-16 | Heists, political manoeuvring, military tactics, long-term schemes |
| 17-20 | Anticipating counter-moves, planning contingencies, tying threads together |
| 21+ | Kingdom politics, planar schemes, reality-altering plans |

Thinking under fire or while stressed makes it harder, and so does being rushed. Relevant background or genuine expertise makes it easier.

Beat the DC and the margin sets the quality: **Competent** (up to 4 over), **Sharp** (5-9), **Brilliant** (10-14), **Masterful** (15+). Miss it and the plan degrades the same way: **Incomplete** (missed by 1-4 — a couple of good options overlooked), **Muddled** (5-9 — obvious options missed, some analysis simply wrong), **Confused** (10+ — wrong assumptions and dangerous misconceptions, delivered with total confidence).

So a low-Intelligence barbarian planning a heist really does get a worse plan than a high-Intelligence wizard, and a bad plan doesn't announce itself as bad. The GM tells you which DC it set, what you rolled, and how that shaped the answer.

## If your plan fails

A failed plan locks that topic for a while of game time, based on how hard the plan was:

| DC | Locked for |
|----|-----------|
| 9-12 | 2 hours |
| 13-16 | 4 hours |
| 17-20 | 8 hours |
| 21+ | 24 hours |

Asking again about the same topic during the lock does not reroll; the GM reminds you your mind is still stuck. You can still act, explore and think about other topics. A genuinely new approach, new information, or expert help unlocks it early.

## What you get back

Two or three tactical options for a quick question or a failed check, four to six for a solid roll on a complex problem, and as many as eight for a major decision — each with a description and its pros and cons (expand a row using its chevron to reveal them inline without submitting), plus your character's internal monologue while they work it out. A good roll widens the list and spots hidden dangers; a bad roll narrows it and sounds just as sure of itself. Tapping a suggested choice automatically switches mode to **Act**, announces `Switched to Act.`, and plays that option.

## Think mode vs God mode

Both freeze the world, and that's where the similarity ends.

| | Think mode | God mode |
|---|---|---|
| Who is speaking | Your character, in character | You, as administrator |
| Ability check | Yes — an INT or WIS check you can fail | None; no dice at all |
| Can it be wrong | Yes, and convincingly | No, what you say is true |
| What it changes | Nothing; it's analysis | Anything: stats, world, history |

Use Think mode to work out what to do. Use [GodMode](GodMode.md) to change the facts.

## See also

- [GodMode](GodMode.md) — the other frozen-world mode, for editing state rather than planning.
- [AbilityScores](AbilityScores.md) — where your Intelligence and Wisdom modifiers come from.
- [CampaignDesign](CampaignDesign.md) — using `THINK:` for long-term campaign goals.
- [ItachiGaiden](../entities/ItachiGaiden.md) — a campaign where the player planned power progression with `THINK:`.
