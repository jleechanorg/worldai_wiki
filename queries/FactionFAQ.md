---
title: FactionFAQ
created: 2026-06-19
updated: 2026-09-18
type: query
tags: [wa-faq, wa-system]
sources: []
---

# Faction FAQ

Common questions about the faction minigame. The full system is on [FactionSystem](../concepts/FactionSystem.md).

## Q: What is faction mode?

**A**: An optional strategic layer on top of your campaign. You hold territory, tax citizens, recruit troops, send spies, fight rival factions and climb a ranking of 201 factions — all while your character's story continues.

## Q: How do I turn it on?

**A**: Any time during play, not at creation. Say "enable the faction minigame", or pick the **Enable the strategic faction management system** option when the GM offers it. Once your forces reach about 100 troops the GM starts suggesting it on its own, and strongly recommends it past 500.

Your account also has an **Enable Faction Minigame** switch under **Settings → Faction Management**. It decides whether the faction layer is available to your campaigns; it does not turn faction mode on in any of them by itself.

## Q: Can I enable it in a campaign I already started?

**A**: Yes — that is the only way it ever gets enabled. Nothing about faction mode is decided when the campaign is created, and every campaign starts with it off whatever your account settings say.

## Q: Do I choose my starting faction?

**A**: No. When you switch it on, the game sorts the troops you already have into soldiers, spies and elites, and sizes your territory and treasury to the position your character has actually reached — from a fledgling village band to a dominant empire.

## Q: Can I disable it later?

**A**: Yes, but do it in the campaign. Once faction mode is on it stays on until you say in that campaign that you want it off. Flipping the account-wide switch in Settings is not the way to do it: it stops the layer being offered, but a campaign where you already enabled faction mode keeps it.

## Q: How do I gain power?

**A**: Faction Power is a fixed five-part formula: soldiers, spies, elites (and their average level), acres of territory, and fortifications. Nothing else counts — not your gold, not your arcana, not your citizens, not your equipment, not your intel. Fortifications are the cheapest power you can buy: 1,000gp for 1,000 FP. See [FactionPower](../concepts/FactionPower.md).

## Q: How does intel work?

**A**: `deploy spies [target] [count]`. The operation lands on one of four tiers and gives you between nothing and +20% combat against that target for up to 8 turns. Afterwards that target is closed to your spies for a cooldown of 4 to 8 turns — longest after your best results, because the target is now alert. The target also rolls separately to catch you; if it does, your result drops a tier and three more turns go on the cooldown. See [FactionIntel](../entities/FactionIntel.md).

## Q: How do rankings work?

**A**: Every faction is sorted by Faction Power. You are ranked against 200 rivals, so ranks run #1 to #201, and below 1,000 FP you are unranked entirely. Expect to start near the bottom — the weakest rival opens around 5,000 power. Climbing is not risky: rivals only attack targets they outgun, so a higher rank means fewer of them can come after you. #1 is the top of the ladder, with no rival left above you.

## Q: Can I ally with other factions?

**A**: Yes. Your offer is scored on how your army compares to theirs, their opinion of you, your history as friend or rival, and what your spies know. A defensive ally reinforces you with half its strength when you are attacked.

## Q: What if I ignore my faction for a while?

**A**: Your faction sits where you left it. Nothing drains away on a schedule and no penalty fires after a set number of turns. The real cost is that the 200 rivals keep growing 1–2% every turn, so your rank drifts down even though your own power has not changed. Troops also resume costing weekly upkeep as soon as you take another turn.

## Q: How long is a faction turn?

**A**: `end turn` advances world time by seven days, and applies the whole weekly ledger at once — tax, citizen growth, arcana, construction progress and upkeep.

## Q: Can I lead multiple factions?

**A**: No. One character, one faction.

## Q: How is faction combat different from my character's fights?

**A**: Faction battles are resolved by the server's battle simulator from the troops each side commits. You give the order; the simulator fights it out over rounds of attrition until one side routs. Your character's own fights stay turn-by-turn with initiative. Separately, any scene with 20 or more units switches to tactical mass combat. See [FactionBattleSim](../entities/FactionBattleSim.md).

## Q: What resources do I manage?

**A**: Gold, territory, citizens and arcana, plus soldiers, spies and elites. Faction gold is separate from your character's own purse. See [FactionManagement](../concepts/FactionManagement.md).

## Q: What's the best opening?

**A**: Build farms and a training ground, put a Steward on your council so gold compounds, then spend everything spare on fortifications — they are worth more power per gold piece than anything else. Spy before a war, not before a raid.

See [NocturneBg3](../entities/NocturneBg3.md) for a campaign that played the system end to end.
