---
title: NPCRelationships
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-mechanic, wa-system, wa-persona]
sources: []
---

# NPC Relationships

Every recurring NPC keeps a running opinion of you. So does every faction. So does the world at large. Those are three different scores, they can disagree with each other, and you are never shown any of them.

## Three separate scores

**1. Personal trust — one per NPC, -10 to +10.**

| Trust | Label | What the NPC does |
|---|---|---|
| -10 to -7 | Hostile | Works against you, may attack on sight, spreads harmful rumors |
| -6 to -4 | Antagonistic | Refuses requests, charges 25-50% extra, feeds you bad information |
| -3 to -1 | Cold | Curt, minimal help, social checks get harder |
| 0 | Neutral | Standard prices, standard responses |
| +1 to +3 | Friendly | Small favors, shares rumors and warnings |
| +4 to +6 | Trusted | 10-20% discounts, proactive warnings, vouches for you |
| +7 to +9 | Devoted | Free help, shares secrets, may step into a fight for you |
| +10 | Bonded | Treats you as family, will defy orders on your behalf |

**2. Faction standing — one per faction, -10 to +10.** Enemy, Hostile, Unfriendly, Neutral, Friendly, Trusted, Ally, Champion. Trusted gets you full access and faction secrets; Champion means the faction will go to war for you. See [FactionSystem](FactionSystem.md).

**3. Public reputation — one number for the whole world, -100 to +100.** Infamous, Notorious, Unknown, Neutral, Respected, Renowned, Legendary. This one moves prices everywhere at once: Notorious costs you 25-50% extra, Respected saves 10%, Renowned saves 25%, Legendary saves 50% and gets you an audience with rulers. Individual NPC trust adjusts prices on top of that, merchant by merchant.

## You never see any of these numbers

The game does not display trust, faction standing, or reputation anywhere — no character sheet entry, no party panel, no relationship screen. You read your standing off how NPCs talk to you, what they charge, what they volunteer, and whether they take risks for you.

## What moves trust

Trust moves in whole points, roughly these amounts:

| What you did | Trust change |
|---|---|
| Saved their life | +3 to +5 |
| Helped with their personal goal | +2 to +4 |
| Kept a promise, gave a real gift, defended their name | +1 to +2 |
| Ignored their request for help | -1 to -2 |
| Insulted or threatened them | -1 to -3 |
| Broke a promise | -2 to -3 |
| Stole from them | -2 to -4 |
| Killed their friend or ally | -3 to -6 |
| Betrayed them | -4 to -6 |

It spreads, too. Harming an NPC costs you 1-3 points with each of their allies; helping one gains you a point or so with each.

## Talking someone important around

Persuading a significant NPC is not one roll — it is a contest that runs across several turns, and it is the one relationship mechanic the game does put on screen. While it is live, every turn of the story carries a box like this:

```
[SOCIAL SKILL CHALLENGE: King Valdris]
Objective: Pardon the captured smugglers
Social HP: 10/10 | Status: RESISTING
```

That "Social HP" is their resolve — how much argument they can absorb before they give in. How much they start with depends on who they are:

| Who you are arguing with | Resolve |
|---|---|
| Commoner, peasant | 1-2 |
| Merchant, guard | 1-3 |
| Noble, knight | 2-4 |
| Lord, general | 3-5 |
| King, ancient ruler | 4-7 |
| God, primordial | 8-10 |

What you are asking for scales that pool as well. A minor favour — information, an audience — sits at the easy end; a standard request costs more; asking someone to betray an ally, break an oath, or submit to you outright pushes them toward the top of their range. Nobody ever ends up above 10, and the game enforces that ceiling itself, so even "kneel to me" aimed at a god is near-impossible rather than impossible.

Each turn you state your approach and the game rolls one of **Persuasion, Deception, Intimidation, or Insight** against a DC — see [SmartSkillChecks](SmartSkillChecks.md) for how that target number is set, and [Dice](Dice.md) for the roll itself. A success takes 1 point off their resolve, or 2 if you clear the DC by 5 or more. A failure takes nothing off. The box also tracks successes toward the target (usually 5) and failures toward a threshold (usually 3), and hitting that threshold ends the attempt with the NPC closed off or hostile.

Their `Status` line is your progress bar: **RESISTING** → **WAVERING** → **YIELDING** → **SURRENDERED**. Expect flat refusal on the first attempt even when you rolled well — an NPC who folds instantly is a bug, not a win.

Grinding does not work. Every resolved attempt at the same objective, success *or* failure, makes the next check 2 harder; prior successes hand some of that back as momentum. Keep winning and you stay roughly level. Keep losing and the hole only gets deeper.

Winning big is not free either. When a major NPC or faction surrenders, the next turn or two will bring one durable consequence — a hardline splinter that rejects the deal, a rival moving into the gap, or a concrete cost or debt. You keep what you won; you also inherit what it broke.

## Which score wins

When the three disagree, the game resolves them in this order:

1. **A faction override**, if that faction's leadership has issued one. This beats personal history outright — an old friend whose faction has turned on you will treat you as an enemy anyway.
2. **Your personal trust** with that specific NPC.
3. **That NPC's faction standing** with you.
4. **Your public reputation.**
5. **Neutral**, if the game knows nothing about you.

Direct experience beats hearsay. An NPC who watched you save their child trusts you even if the public thinks you are a criminal, and an NPC you personally betrayed hates you even if the public thinks you are a hero.

## What each NPC knows about who you really are

Separate from how much an NPC likes you is how much they know about you — your true identity, your hidden powers, who you actually serve. Every NPC tracks that independently, on a six-step ladder:

| Step | What they have |
|---|---|
| 0 | Never heard of you |
| 1 | A vague rumour |
| 2 | A specific rumour with at least one named detail |
| 3 | A credible report from a source they trust |
| 4 | Suspicion — circumstantial evidence, no confirmation |
| 5 | Certainty — they saw it themselves |

Two rules make this behave very differently from public reputation. **A rumour moves anyone at most one step**, however lurid it is or however much they trust the teller — so gossip can plant doubt but never proves anything. And **only direct observation reaches certainty**: someone who merely suspects you stays suspecting until they witness the thing for themselves.

There is deliberately no town-wide suspicion bar. Nobody pools what they know. That is why you can be openly, obviously yourself in front of an ally who has seen everything, walk across town, and still pass as an ordinary traveller with someone who has not.

The same boundary applies the moment you drop the act. Revealing a hidden power lands mechanically only on the people who actually saw it — their saves, their reaction, their faction's internal alarm. Everyone who merely hears about it afterwards shifts one rumour step at most and takes no mechanical effect at all. The game will not let a reveal quietly become "everyone knows now"; getting the word out is a separate thing you have to go and do.

Who was in the room is remembered for the rest of the campaign, and nobody is retroactively added to it. Showing the same secret to a new audience later is a fresh reveal with its own set of witnesses.

## NPC-to-NPC relationships

NPCs also carry connections to each other — a sister, a rival, a patron, a sworn enemy. These are written in plain language rather than picked from a fixed list, so any relationship the story needs can exist. Faction membership is tracked separately from personal ties, which is why a friendly NPC inside a hostile faction is a common and genuinely awkward situation.

These connections drive what NPCs do when you are not in the room — see [LivingWorld](LivingWorld.md).

## Hidden personality tags

Recurring NPCs carry a personality tag and an alignment. The tag is usually an MBTI code like INTJ, but it can equally be a phrase such as "mysterious and brooding". Together they steer how the NPC decides, how they speak, and how they react to you.

These labels are strictly behind the scenes: the game is instructed never to print "INTJ" or "Lawful Neutral" in the story text. You are meant to infer personality from behaviour. See [CompanionPersonality](CompanionPersonality.md).

## Player tips

- **NPCs do not forget.** Promises, debts, and grievances are recorded permanently, and the game is forbidden from quietly resetting a relationship. A slight from twenty turns ago can still be waiting for you.
- **Reputation travels ahead of you.** Witnesses know immediately, the local area within days, the region within weeks, distant lands within months. If you want a clean slate somewhere, get there before the news does.
- **Watch the price tag.** You cannot see your standing, but you can see what a merchant charges. A 25-50% markup means either your public reputation has turned bad or that particular merchant has turned against you — check whether other traders in town charge the same to tell which. A discount can come from either side and the size alone will not tell you which: a merchant who personally trusts you knocks off 10-20%, and a devoted one may charge nothing at all, while a strong public reputation cuts prices 10% to 50% everywhere. As with markups, compare several traders in town — a discount only you get is personal, one the whole town gives you is reputation.
- **Do not wear an argument down.** Every attempt at the same objective raises the next DC by 2 whether it landed or not, so repeated failure actively buries you. If two tries have gone nowhere, go find leverage — a favour, a witness, a threat with teeth — and come back with a different approach rather than the same one again.
- **Choose your audience before you reveal anything.** Only the people in the room are changed by it. If you need a secret to stay containable, show it to as few NPCs as you can; if you need it to spread, reveal it deliberately in front of someone who will carry it, because the story will not broadcast it for you.
- **Old scores fade slowly.** Rumors decay about one per in-game week if nothing reinforces them, and extreme public reputations drift back toward neutral by roughly a point a month. Deeds themselves are permanent.

See [CompanionPersonality](CompanionPersonality.md), [LivingWorld](LivingWorld.md), [FactionSystem](FactionSystem.md).
