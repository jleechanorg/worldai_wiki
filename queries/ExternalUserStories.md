---
title: Player Features Reference
created: 2026-06-20
updated: 2026-09-18
type: query
tags: [wa-system, wa-tutorial]
---

# Player Features Reference

Everything around the story: signing in, what happens on screen while a turn
runs, settings and AI providers, what the game saves between sessions, how the
dice stay honest, and how to get your campaign out as a file.

For the rules of play — combat, spells, levelling, companions — see
[PlayerUserStories](PlayerUserStories.md). If you want to drive the game from
your own code, see [DeveloperAPI](DeveloperAPI.md).

## Your account

**Sign in with Google.** Google is the only sign-in option — there is no Apple,
email, or password sign-in. Your campaigns, settings, and progress are tied to
that account, and every request carries your identity, so nothing is saved
anonymously. Signing out ends the session and drops your cached settings. See
[HowToPlay](how-to-play-worldai.md), Step 1.

**Settings follow you.** Provider, model, theme, and persona live in your
account rather than in the browser, so they survive reloads, a different
browser, and a different device. They load once per session, and only the
fields you change get written back.

**Your API key stays masked.** If you brought your own provider key, Settings
shows it masked with an eye icon. Clicking the eye fetches the key from the
server instead of keeping a copy in the browser, and the reveal resets when you
reload the page. Each reveal is logged as a sensitive action.

**How many turns you get.** The built-in AI gives you 100 turns a day, and no
more than 50 in any five-hour stretch. Bringing your own provider key raises
that to 5,000 a day (1,000 per five hours). God Mode turns and campaign creation
are counted in two further budgets of their own, each with ten times the
built-in allowance — 1,000 a day and 500 in any five-hour stretch — so
world-building never eats into your ordinary play. Budgets count across all your
campaigns, not per campaign. When you run out, a message tells you when your next
turn unlocks; you can dismiss it without losing your place in the story.
Operators can lift the limit for individual playtest accounts — that is not
something you can switch on yourself.

**Personal access tokens are for outside tools.** A token lets a program act as
you without your Google session. Nothing in Settings creates one today — it is
something a developer sets up from their own code, and
[DeveloperAPI](DeveloperAPI.md) covers it. The server keeps only a scrambled
copy of the token, so a lost one cannot be recovered; you replace it instead.

## While a turn runs

**The story streams in.** Text fills in word by word from the moment the server
starts generating, so you are never watching a blank screen. The page
auto-scrolls to follow it, but leaves you alone if you have scrolled back to
re-read something.

**Dice show their work.** A turn's rolls are listed above its narration under a
`🎲 Dice Rolls:` heading, one line each:

```
1d20+6 = 24 vs DC 12 - Success (Sera Quill - Shadow Surveillance & Eavesdropping)
```

That is the dice and modifier rolled, the total, the number it had to beat,
whether it landed, and who was attempting what. The list is written from the
server's record of the turn rather than from the story text — see
[DiceAuthenticity](../concepts/DiceAuthenticity.md).

**Background work shows itself.** Faction moves, reward calculations, and world
events appear as compact cards in the story flow; status notes and warnings
appear as muted rows above or below the narration. You can see what the
simulation did, not just what the narrator said about it.

**Loading messages keep you company.** While a turn is in flight the wait
message cycles through a short fixed list — "The DM is thinking…", "Rolling
dice…", "Updating the world…" and a few more. The list depends on what the app
is doing (playing a turn, creating a campaign, loading, saving), not on what is
happening in the story, so a fight and a conversation show the same messages.

**A stalled stream is called out.** If no new text arrives for a while, a
warning row appears inline so you know the pause is not your connection. It
disappears the moment text resumes.

**Reduced motion is respected.** If your operating system has reduce-motion
turned on, smooth scrolling becomes instant jumps and the animated background
falls back to a static image. Toggling the OS setting mid-session takes effect
without a reload.

**Two themes.** Fantasy and Light, switched from the header menu. The theme is
applied before the first paint, so you never see a flash of the wrong one. Your
choice is remembered in the browser and synced through your account settings.

**Getting started and finding things again.** Every new campaign goes through
the same two-screen wizard — **Choose Your Campaign**, then **Ready to
Launch!** — reached from the dashboard's **Play a campaign** button. The first
screen collects your universe, era, character, setting, plot, and title; the
second shows you what you picked and hands you an **Enter the World** button.
Your character is reviewed in the opening scene, after launch, not inside the
wizard (see [CampaignWizard](../concepts/CampaignWizard.md)). Once you have a
shelf full of campaigns, the dashboard has a **Search campaigns…** box that
filters as you type, sorting by Last Played, Date Created, or Title with a
newest/oldest order switch, theme and status dropdowns, and a **Clear** button.
A counter above the list ("Showing 50 of …") tells you how much of the shelf is
on screen, and each card carries its own **Edit** and **Duplicate** buttons.

## Settings and AI providers

**Choose who runs your campaign.** Settings offers four providers as a radio
group: Gemini, OpenRouter, Cerebras, and an OpenClaw Gateway you run yourself.
Each has its own model dropdown and its own API-key field, and a switch takes
effect on your next turn.

**Your key is checked when you save it.** An empty or malformed key is rejected
with a clear message, and a successful save confirms the masked key back to you.
A bad key does not poison later turns — each turn re-validates.

**Test Connection.** If you point the game at your own gateway, the Test
Connection button on the settings page probes it and updates a status badge in
place. A failure is reported inline; it does not block the page.

**Provider errors stay readable.** When the provider rate-limits you, rejects
your key, fails transiently, or returns something malformed, you get a plain
message with retry guidance as a toast or modal. Raw stack traces never reach
the screen.

**Spicy mode.** The 🌶️ toggle sits in the game header next to the campaign
title, not on the Settings page. Its own helper text describes it: "Enables Grok
AI for uncensored content including detailed adult scenes. Slower but no content
restrictions. Your previous model will be restored when disabled." It is off by
default, and it is an account setting, so it stays where you left it in every
campaign. You are never nagged about it: while it is off, an "Enable Spicy Mode"
option appears among your suggested actions only when the scene itself has
turned intimate, and a "Disable Spicy Mode" option appears the same way when
such a scene winds down. Typing `enable spicy mode` or `disable spicy mode` in
the story box works as well as the toggle.

## What the game remembers

**Your campaigns are yours.** Every campaign is stored under your account and
every query is scoped to you. There is no path from the browser to another
player's data.

**Duplicating a campaign.** Every campaign card on the dashboard has a
**Duplicate** button. It opens a small **Duplicate Campaign** window with the
new title already filled in as "<your campaign> (copy)", which you can change
before confirming. The copy is a complete one — its own campaign with its own
history — so you can branch a story and leave the original exactly as it was.

**In-world time.** The world clock is tracked down to the second and advances
when you rest, travel, or skip ahead, so schedules and calendar events stay
coherent. Time cannot be moved backwards.

**The world keeps its own turn counter,** separate from yours and owned by the
server rather than the storyteller. Faction cycles, world events, and time
pressure all read from it — see [LivingWorld](../concepts/LivingWorld.md).

**World events are stamped** with the turn and scene they belong to, so the
story can be filtered by when something happened.

**Level-up lands as one clean entry.** The finished level-up narration replaces
any draft the storyteller started, and links to the choice you made, so you can
scroll back to it later.

**Two clocks, if you run a faction.** Adventuring is measured in minutes and
hours; faction turns are measured in weeks — one strategic turn per seven
in-game days by default. The in-game time you spend adventuring, resting, and
travelling rolls the faction clock forward. Nothing advances while you are
logged off: the faction clock follows in-game time, not real-world time. See
[FactionSystem](../concepts/FactionSystem.md).

**Housekeeping runs on save,** not on a faction turn. Events that have already
played out move into a world-history list, and the backlog of pending events is
capped — when it overflows, the oldest unresolved entries are folded into a
single "archived N older pending events" summary so a months-long campaign does
not bloat.

**Stale choices are dropped.** A planning choice or reward correction that a
newer turn has already superseded is discarded rather than allowed to overwrite
current state.

## When the game takes over a flow

**The game picks the specialist, you don't.** Combat, conversation, faction
management, level-up, God Mode, and character creation each get their own
handling, chosen from what you just did — there is no setting for it. You can
see which one ran: a small debug line under each turn names it, for example
"🤖 Agent: PlanningAgent". A conversation the game judges to be a substantial
scene gets more room than the usual length limit allows, and that call is made
fresh each turn rather than after a fixed number of exchanges.

**An open character-creation or level-up review holds you on it.** While either
is open, unrelated actions are folded back into it and a banner explains why, so
you cannot lose the flow halfway through. It lifts by itself once the result has
been saved to your campaign, and once lifted it stays lifted. Levelling itself
never interrupts anything: the new level lands on the turn you earn it and the
review is yours to open or skip — see [LevelUp](../concepts/LevelUp.md).

**Finishing a flow.** The visible finish button always works. Saying it in your
own words — "I'm done", "let's start the adventure" — also works, because the
game reads what you meant rather than matching a list of phrases. This applies
only to level-up and character creation; there is no general "end the session"
mode.

**Rewards that need a decision wait for you.** A reward you have to choose —
usually a level-up — is held in your campaign rather than discarded, and
surfaces as a level-up prompt in the rewards summary attached to your turns. It
stays pending until you take it. There is no separate "pending rewards" screen
to open.

**Suggested actions, every turn.** A story turn ends with four suggested
actions, each with a **Show pros and cons** button that lays out the trade-off,
plus a fifth option — **Custom Action: decide whatever you want to do** — for
anything else you had in mind. God Mode turns offer three suggestions with no
pros-and-cons button, and the same custom option. Picking one commits that
action.

**Factions act on their own.** Faction turns resolve behind the scenes and their
outcomes land in your world-events log. See
[FactionSystem](../concepts/FactionSystem.md).

**Ascending to a new tier.** When a campaign becomes eligible for divine or
multiversal play, a one-time ceremony marks the change in-story and the new
tier's rules take effect afterwards. There is no separate screen that summarises
what changed.

## Dice you can check

Every die you see was rolled by the server — the storyteller is not allowed to
write numbers into the prose. Each roll is saved to your campaign with its
notation and result, so the narration and the record cannot disagree, and an
attack's roll, critical and damage are all settled in one go rather than in
steps the storyteller could improvise between.

The game checks its own dice: it commits to a secret seed before the roll and
confirms afterwards that the roll used it. That record is kept with every turn
but is not displayed anywhere, so this is the game policing itself rather than
something you can audit by hand.
[DiceAuthenticity](../concepts/DiceAuthenticity.md) covers the guarantees in
full; [DiceNotation](../concepts/DiceNotation.md) covers the grammar.

## Exporting your campaign

Export your story as PDF, DOCX, or TXT. The file is built on the server and
includes the campaign title, the story entries, and the world events. You have
to be signed in to your own campaign to export it. See
[ItachiGaiden](../entities/ItachiGaiden.md) for an example of what an exported
story reads like.

## Where to read more

- [PlayerUserStories](PlayerUserStories.md) — how the game plays: combat,
  progression, companions, loot, the living world.
- [DeveloperAPI](DeveloperAPI.md) — MCP tools and REST routes, for integrators.
- [HowToPlay](how-to-play-worldai.md) and
  [CampaignDesign](../concepts/CampaignDesign.md) — getting started and
  designing your own campaign.
