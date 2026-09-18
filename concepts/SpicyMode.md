---
title: SpicyMode
created: 2026-09-18
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Spicy Mode

An opt-in setting for adult players that lets the GM write intimate scenes explicitly instead of fading to black. It is off until you turn it on.

## Where the switch is

In the **game header**, on the right-hand side of the bar that shows your campaign title: a small switch labelled **🌶️ Spicy**, with a `?` next to it. It is not on the Settings page — if you go looking there, you will not find it.

The switch remembers its state on your account, so it stays on across every campaign you play until you turn it off.

## What turning it on actually does

It swaps the AI that narrates your game. With Spicy on, your campaign runs on **Grok**, an uncensored model — the switch's own note calls it "uncensored content including detailed adult scenes". With it off, you are on whatever model you normally use.

"Uncensored" is about the model, not about the game having no rules. The GM still writes to the same instructions it always does: scenes stay consensual, characters keep their own boundaries, and you can steer or stop a scene at any point.

Three consequences worth knowing before you flip it:

- **Every turn is slower**, not just the intimate ones. The switch changes the narrator for the whole campaign, so ordinary combat and travel turns run on Grok too — and take longer to come back.
- **The prose voice changes.** A different model writes differently. Some players like the change; some find it a noticeable shift mid-campaign.
- **Turning it off restores what you had.** The game records which model and provider you were using before, and puts them back. The one exception: if you deliberately picked a *different* model in Settings while Spicy was on, the game keeps your choice and only clears the Spicy flag.

## What changes in the writing

With Spicy **off**, romance still happens — the GM writes the tension, the charged conversation, the moment of commitment, and then fades to black before anything explicit.

With Spicy **on**, those scenes are written out. The instructions the GM works from ask for literary erotic writing rather than clinical description: emotional weight, character-consistent behaviour, clear consent, and consequences that carry into the rest of the story. Relationship state still updates the same way it does in any other scene — see [CompanionArc](CompanionArc.md) and [NPCRelationships](NPCRelationships.md).

## How the game offers it

While Spicy is off, two things can prompt you — both only when a scene is actually heading somewhere romantic, never during ordinary play:

- **A choice in your options list.** When the GM reads the scene as turning intimate, an **Enable Spicy Mode** option appears alongside your other choices. Picking it flips the switch for you.
- **An occasional one-line aside.** On a romance-leaning turn, and only on every tenth turn, the GM may tack a short bracketed reminder onto the end of the narration saying Spicy Mode is available. (That reminder tells you to look in Settings. It is wrong — the switch is in the header.)

Neither one forces anything. Ignore them and the story continues with fade-to-black.

The offer runs the other way too, but only while Spicy is **on**: once an intimate scene is winding down, an **Exit Spicy Mode** option appears in your choices so you can drop back to your usual model without hunting for the header.

## Typing it instead

The switch is not the only way in. Typing any of these into the message box turns it on:

```
enable spicy mode
activate spicy mode
start spicy mode
```

And any of these turns it off:

```
exit spicy mode
disable spicy mode
stop spicy mode
return from spicy mode
```

The GM answers with a one-line confirmation — `🌶️ Spicy mode enabled.` — and the setting is saved immediately. It does not burn a story turn: nothing happens in the world, no time passes, and your next message picks up where the scene left off. The header switch itself may keep showing the old position until you reload the campaign; the setting is already in force regardless of what the switch looks like.

## Player notes

- **You can leave mid-scene.** Turning it off does not erase what has already been written; it changes how the next turn is written.
- **The switch is not your only brake.** Even with Spicy on, you can ask for a fade to black in the moment — say so in your action, and the GM is instructed to give you a graceful exit from the scene without you touching the toggle at all.
- **If you want romance but not explicitness, leave it off.** Fade-to-black is the default behaviour, not a degraded one — companion arcs, including the forbidden-love arc, play start to finish without it.
- **It is all-or-nothing per account, not per campaign.** There is currently no way to have it on in one campaign and off in another; the switch you flip in one game applies to the next one you open.

See [CharacterMode](CharacterMode.md), [CompanionArc](CompanionArc.md), [NPCRelationships](NPCRelationships.md).
