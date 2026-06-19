---
title: LivingWorld
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-system, wa-mechanic]
sources: []
---

# Living World

The game world continues to evolve between player actions. NPCs pursue agendas, factions scheme, time advances, seasons change.

## What "living" means

When you take a long rest or a long time passes in-fiction, the world state advances:
- **NPCs make decisions**: based on their agendas, even when the player isn't watching.
- **Factions act**: see [[concepts/FactionPlay]].
- **Events fire**: scheduled plot events, random encounters, seasonal changes.
- **Time passes**: days turn into weeks; weeks into months.

## Why it matters

Without a living world, the game would freeze between player actions. The party goes to sleep, and nothing happens until they wake up. With a living world, the world keeps moving:
- The villain completes a ritual while you rest.
- The rival faction attacks your holdings.
- An NPC you insulted plots revenge.
- A festival happens in town.

This makes choices feel weighty and time feel real.

## How it works

The LivingWorldEngine runs background simulations:
1. **NPC agendas**: each NPC has goals. Periodically, they take steps toward their goals.
2. **Faction turns**: see [[concepts/FactionPlay]].
3. **Time events**: scheduled events tied to in-world dates.
4. **Random encounters**: low-probability events that fire when conditions are met.

When you return from a long rest, the system surfaces what changed.

## Player tips

- **Don't rest too long**: every day you rest, the world advances. Long rests in hostile territory are risky.
- **Use informants**: hire NPCs to keep you informed about world events.
- **Engage with NPC agendas**: NPCs who like you will tell you when they're planning something; NPCs who hate you will scheme against you in silence.

See [[concepts/FactionSystem]], [[concepts/NPCRelationships]], [[concepts/CampaignDesign]].
