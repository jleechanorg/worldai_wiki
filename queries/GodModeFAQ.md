---
title: GodModeFAQ
created: 2026-06-19
updated: 2026-09-18
type: query
tags: [wa-faq, wa-prompt]
sources: []
---

# God Mode FAQ

Short answers about God Mode and directives. The long versions live in [GodMode](../concepts/GodMode.md) and [GodModePrompting](../concepts/GodModePrompting.md).

## Q: What is God Mode?

**A**: The game's pause menu. The world freezes and you edit it directly — HP, gold, XP, level, equipment, spell slots, NPCs, items, locations, missions, world time — instead of playing through it. Setting persistent narration rules, called directives, is one of the things you can do there, not the whole feature. See [GodMode](../concepts/GodMode.md).

## Q: How do I get into God Mode?

**A**: Two ways, and they do the same thing:

1. Pick the **God** pill under the message box, then type your request.
2. Stay in Character mode and start the message with `GOD MODE:` — for example `GOD MODE: keep the tone grimdark`.

## Q: Does `GOD MODE:` have to be in capitals?

**A**: No. `god mode:`, `God Mode:` and `GOD MODE:` all work, and leading spaces are ignored. Same for `THINK:`. This wiki writes them in capitals only so they stand out.

## Q: How do I add a directive?

**A**: Say what you want remembered, in plain language, from God Mode: "from now on...", "stop forgetting...", "always...". The GM turns it into a stored rule and confirms it. One sentence per rule works best.

## Q: Can I edit a directive after adding it?

**A**: Adding a replacement is usually easiest — the newest rule wins outright, so it takes over immediately. To remove one, ask for it in plain language ("forget the rule about companion scaling"). Removal matches the rule's full text, so if it doesn't stick, ask the GM to list your active rules and paste the exact line back.

## Q: Why isn't my directive being respected?

**A**: Four common reasons:

1. **It was rejected and you weren't told.** Rejection is silent, and the GM may still have confirmed it. Ask `GOD MODE: list my active rules` — if the rule isn't there, it was thrown out for looking like a stat value ("my level is 10") or a one-time event ("you just killed the dragon").
2. **Too vague.** "Be cool" gives the system nothing to act on.
3. **Contradicted by another directive**, or by a newer one that supersedes it.
4. **Buried.** Too many rules at once and each one dilutes the rest.

## Q: Can directives change plot beats?

**A**: No. Directives shape how something happens, not whether. You can't tell the GM never to kill your character — but you can change your HP directly from God Mode, which is a different lever.

## Q: Does God Mode affect combat?

**A**: Two answers, depending on which part you mean.

- **God Mode itself**: yes, directly. Set your HP, restore spell slots, hand yourself a weapon, delete an enemy. What it won't do is *resolve* the fight — God Mode never rolls dice and never takes a combat turn.
- **Directives**: only indirectly. A directive shapes how a fight is written, not who wins it.

## Q: Do God Mode turns use up my normal turns?

**A**: No. God Mode has its own allowance, separate from story turns and ten times larger — 1000 a day and 500 per five hours, against 100 and 50 for normal play. Admin fixes never cost you story turns, or vice versa.

## Q: Is there a limit on how much one God Mode turn can change?

**A**: A single turn can carry up to 100 structured edits — directives added, replaced or dropped, scenes rewritten, memories changed. Past that the turn is refused. You will not hit it by hand.

## Q: How many directives can I have?

**A**: No hard limit, but more than about ten dilutes their effect. Start with one to three.

## Q: Can I turn directives off mid-campaign?

**A**: Yes — drop them all and narration reverts to the default tone. God Mode itself is always available; there's nothing to switch off.

## Q: Are directives per-campaign or account-wide?

**A**: Per-campaign. Each campaign keeps its own list.

## Q: Can I share directives between campaigns?

**A**: Yes. A directive is just text — copy and paste it.

## Q: What if my directive is too long?

**A**: Shorter is usually better; one sentence is ideal. If you need several ideas, use several directives.

## Q: Can I see a real example?

**A**: The Itachi V2 campaign ran 432 scenes on one directive:

> Uchiha Itachi is stoic, minimalist, and humble. He avoids grandstanding or arrogant terminology (e.g., 'math', 'laboratory', 'geometry'). He speaks with polite authority and views his power as a necessary, heavy burden for the sake of peace.

See [ItachiGaiden](../entities/ItachiGaiden.md) for the case study.

## Q: How do I write my first directive?

**A**: Use the formula "X is/does Y. Avoid Z. Always W." See [GodModePrompting](../concepts/GodModePrompting.md) for the full guide.

## See also

- [GodMode](../concepts/GodMode.md) — what God Mode is and what it can change.
- [GodModePrompting](../concepts/GodModePrompting.md) — writing directives.
- [ThinkMode](../concepts/ThinkMode.md) — the in-character planning mode.
