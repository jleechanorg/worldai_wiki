---
title: FactionFAQ
created: 2026-06-19
updated: 2026-06-19
type: query
tags: [wa-faq, wa-system]
sources: []
---

# Faction FAQ

Common questions about the faction minigame.

## Q: What is faction mode?

**A**: An opt-in game mode where you lead a faction. You manage resources, gather intel, fight rivals, climb rankings. See [[concepts/FactionSystem]].

## Q: When should I enable faction mode?

**A**: At campaign creation. Toggle it on in the [[concepts/CampaignWizard]] step 1.

## Q: Can I disable it later?

**A**: Not easily. Faction-mode campaigns have persistent faction state. Switching off mid-game breaks the state.

## Q: How do I gain power?

**A**: Through:
- Recruiting named NPCs (each contributes their level + class power).
- Acquiring territory (economic output).
- Defeating rival factions (their resources become yours).
- Buying better equipment.

See [[concepts/FactionPower]].

## Q: How does intel work?

**A**: Send scouts to gather intel on a rival. Intel gives you combat bonuses when you attack that rival. Without intel, you fight blind. See [[entities/FactionIntel]].

## Q: How do rankings work?

**A**: Factions are ranked by power. Higher rank = more visibility = more rivals attacking you. Climbing is good but risky.

## Q: Can I ally with other factions?

**A**: Yes. Diplomacy is a faction turn action. Alliances share intel and coordinate attacks.

## Q: What if I ignore my faction for a while?

**A**: After 3 turns, the system raises a reminder. After 5 turns, a warning. After 10 turns, your faction starts to suffer (members leave, rivals attack). See [[queries/PlayerUserStories#US-057|US-057]].

## Q: Can I lead multiple factions?

**A**: No. One character, one faction.

## Q: How is faction combat different from personal combat?

**A**: Faction combat is automated by the [[entities/FactionBattleSim]]. You declare strategy; the simulator resolves. Personal combat is turn-by-turn with initiative.

## Q: What resources do I need to manage?

**A**: Gold, influence, materials, members, territory. See [[concepts/FactionManagement]].

## Q: Can my faction be destroyed?

**A**: Yes. If your power drops to 0 (members killed, territory lost), your faction is destroyed. Some campaigns allow rebuilding.

## Q: Can I play faction mode without enabling it at creation?

**A**: No. It's a campaign-creation toggle.

## Q: What's the best strategy?

**A**: From the Nocturne BG3 V3 case study: intel → combat → power is the core loop. Diversify resources, recruit named NPCs, and watch your ranking.

See [[entities/NocturneBg3]] for the full case study.
