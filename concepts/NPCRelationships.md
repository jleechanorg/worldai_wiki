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

**3. Public reputation — one number for the whole world, -100 to +100.** Infamous, Notorious, Unknown, Neutral, Respected, Renowned, Legendary. This is the one that moves prices: Notorious costs you 25-50% extra, Respected saves 10%, Renowned saves 25%, Legendary saves 50% and gets you an audience with rulers.

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

## Which score wins

When the three disagree, the game resolves them in this order:

1. **A faction override**, if that faction's leadership has issued one. This beats personal history outright — an old friend whose faction has turned on you will treat you as an enemy anyway.
2. **Your personal trust** with that specific NPC.
3. **That NPC's faction standing** with you.
4. **Your public reputation.**
5. **Neutral**, if the game knows nothing about you.

Direct experience beats hearsay. An NPC who watched you save their child trusts you even if the public thinks you are a criminal, and an NPC you personally betrayed hates you even if the public thinks you are a hero.

## NPC-to-NPC relationships

NPCs also carry connections to each other — a sister, a rival, a patron, a sworn enemy. These are written in plain language rather than picked from a fixed list, so any relationship the story needs can exist. Faction membership is tracked separately from personal ties, which is why a friendly NPC inside a hostile faction is a common and genuinely awkward situation.

These connections drive what NPCs do when you are not in the room — see [LivingWorld](LivingWorld.md).

## Hidden personality tags

Recurring NPCs carry a personality tag and an alignment. The tag is usually an MBTI code like INTJ, but it can equally be a phrase such as "mysterious and brooding". Together they steer how the NPC decides, how they speak, and how they react to you.

These labels are strictly behind the scenes: the game is instructed never to print "INTJ" or "Lawful Neutral" in the story text. You are meant to infer personality from behaviour. See [CompanionPersonality](CompanionPersonality.md).

## Player tips

- **NPCs do not forget.** Promises, debts, and grievances are recorded permanently, and the game is forbidden from quietly resetting a relationship. A slight from twenty turns ago can still be waiting for you.
- **Reputation travels ahead of you.** Witnesses know immediately, the local area within days, the region within weeks, distant lands within months. If you want a clean slate somewhere, get there before the news does.
- **Watch the price tag.** You cannot see your standing, but you can see what a merchant charges. A 25-50% markup means either your public reputation has turned bad or that particular merchant has turned against you — check whether other traders in town charge the same to tell which. A 10-20% discount means that NPC trusts you; a bigger one means the world does.
- **Old scores fade slowly.** Rumors decay about one per in-game week if nothing reinforces them, and extreme public reputations drift back toward neutral by roughly a point a month. Deeds themselves are permanent.

See [CompanionPersonality](CompanionPersonality.md), [LivingWorld](LivingWorld.md), [FactionSystem](FactionSystem.md).
