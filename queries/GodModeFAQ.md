---
title: GodModeFAQ
created: 2026-06-19
updated: 2026-06-19
type: query
tags: [wa-faq, wa-prompt]
sources: []
---

# God Mode FAQ

Common questions about god mode and directives.

## Q: What is god mode?

**A**: A player-supplied set of style rules that shape how the AI Game Master narrates your campaign. Two layers:
1. **God Mode header** (set at campaign creation): character + setting.
2. **god_mode_directives** (added during play): ongoing style rules.

See [GodMode](../concepts/GodMode.md).

## Q: How do I add a directive?

**A**: From the campaign's settings panel during play. Each directive is a single sentence rule.

## Q: Can I edit a directive after adding it?

**A**: Easier to add a new directive that supersedes the old one. The system treats removal as "this rule no longer applies."

## Q: How many directives can I have?

**A**: No hard limit, but more than ~10 dilutes their effect. Start with 1-3.

## Q: Can directives change plot beats?

**A**: No. Directives can shape HOW something happens, not WHETHER. You can't direct the GM to never kill your character.

## Q: Why isn't my directive being respected?

**A**: Common reasons:
1. **Too vague**: "Be cool" doesn't tell the system what to do.
2. **Contradicts other directives**: two rules pulling in opposite directions.
3. **Contradicts the rules engine**: "Don't roll dice" can't override the dice system.
4. **Buried in noise**: too many directives, this one gets lost.

**Fix**: be specific, remove contradictions, prioritize.

## Q: What's the difference between God Mode header and god_mode_directives?

**A**:
- **God Mode header**: set once at campaign creation. Describes the character + setting.
- **god_mode_directives**: added any time. Style rules that persist across scenes.

## Q: Can I see examples?

**A**: Yes. The Itachi V2 campaign has one directive that shaped 432 scenes:

> Uchiha Itachi is stoic, minimalist, and humble. He avoids grandstanding or arrogant terminology (e.g., 'math', 'laboratory', 'geometry'). He speaks with polite authority and views his power as a necessary, heavy burden for the sake of peace.

See [ItachiGaiden](../entities/ItachiGaiden.md) for the full case study.

## Q: How do I write my first directive?

**A**: Use the formula: "X is/does Y. Avoid Z. Always W." See [GodModePrompting](../concepts/GodModePrompting.md) for the full guide.

## Q: Can I share directives between campaigns?

**A**: Yes. The directive is just text — copy/paste it.

## Q: What if my directive is too long?

**A**: Shorter is usually better. One sentence is ideal. If you need multiple ideas, use multiple directives.

## Q: Does god mode affect combat?

**A**: Indirectly. Combat rules are enforced by the rules engine. God mode affects how combat is NARRATED, not its mechanical outcome.

## Q: Can I disable god mode mid-campaign?

**A**: Yes, remove all directives. The GM reverts to default tone.

## Q: Are directives per-campaign or account-wide?

**A**: Per-campaign. Each campaign has its own `custom_campaign_state.god_mode_directives` list.

See [GodMode](../concepts/GodMode.md), [GodModePrompting](../concepts/GodModePrompting.md) for full details.
