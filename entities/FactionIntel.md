---
title: FactionIntel
created: 2026-06-19
updated: 2026-11-03
type: entity
tags: [wa-system, wa-mechanic]
sources: []
---

# Faction Intel

Spying on a rival faction. A good operation buys you a temporary edge in the fighting that follows; a bad one gets your people caught.

## Running an operation

1. **Send spies.** `deploy spies [target] [count]`. It costs 50–200gp per spy and takes 1 to 3 turns.
2. **The result lands on one of four tiers**, decided by how many spies you sent against how well the target is defended.
3. **Separately, the target rolls to catch you.** Detection risk rises with the target's shadow networks and magical wards, and falls with more spies, a Spymaster on your council, and a higher intrigue lineage — but it never goes below 5% or above 90%.

If you are caught, your result drops one tier.

## What each tier is worth

| Tier | Combat bonus | Lasts |
|---|---:|---:|
| Failure | none | — |
| Partial | +5% | 3 turns |
| Success | +10% | 5 turns |
| Critical | +20% | 8 turns |

## Cooldown

Every intel operation locks that target for 12 strategic turns, whatever the result. Only `end turn` advances the clock; ordinary story actions do not.

Higher tiers also widen how far you can see into the target's territory. Note that the bonus is a stated advantage the GM applies to how a battle plays out — the [battle simulator](FactionBattleSim.md) itself resolves from troops and fortifications, so declare that you are acting on your intel when you order the attack.

Intel never raises your [Faction Power](../concepts/FactionPower.md).

## The other spy commands

- `intel report` — what you currently know, and which targets are on cooldown.
- `recall spies` — bring your spies home from a target.
- `counter-intel` — spend to defend against rival spies. Shadow networks and wards do the same job permanently.

## Tips

- **Spy before a major assault, not before every skirmish.** The bill is 50–200gp a spy plus one to three turns, the ceiling is +20% for 8 turns, and the target is then closed to your spies for 12 turns. Worth it for a war, not for a raid.
- **Send more spies than you think you need.** A bigger team both raises your tier and lowers the chance of being spotted.
- **Appoint a Spymaster.** A Dexterity-based officer improves every operation and cuts your detection risk. See [FactionManagement](../concepts/FactionManagement.md).
- **Attack while it is live.** A Critical result that expires unused bought you nothing.

See [FactionSystem](../concepts/FactionSystem.md), [FactionBattleSim](FactionBattleSim.md).
