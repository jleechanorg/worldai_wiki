---
title: D&D 5e Rules and Roll Calculations
created: 2026-06-19
updated: 2026-10-18
type: concept
tags: [wa-mechanic, wa-system, wa-tutorial]
sources: [Dice.md, AbilityScores.md, SmartSkillChecks.md, Combat.md, Spellcasting.md, RestAndDeath.md]
---

# D&D 5e rules and roll calculations

## TL;DR

- Most uncertain actions use a twenty-sided die plus the bonuses and penalties that actually apply. Meet or exceed the target to succeed.
- An **attack** compares its total with **Armor Class (AC)**. An **ability check** or **saving throw** normally compares with **Difficulty Class (DC)**. Damage is a separate calculation.
- Your **ability modifier** comes from an ability score. **Proficiency** applies only when you have the relevant training or a feature grants it; **Expertise** doubles that proficiency contribution.
- **Advantage** keeps the higher of two d20s; **disadvantage** keeps the lower. Add modifiers once. If both apply, they cancel.
- A useful calculation names every recorded die, bonus, penalty and adjustment beside its number. A final total alone cannot explain where those numbers came from.
- This guide uses the **2014 / SRD 5.1 tabletop baseline**. WorldAI has house rules, including automatic success or failure on natural 20s or 1s for checks and saves. The revised 2024 rules and Baldur's Gate 3 must not silently replace your campaign's rules.
- The GM decides what an action means and which rules apply. Reading a calculation explains the recorded resolution; it is not a new roll or another resource expenditure.

## How to read an Outcome calculation

This is a mechanics reference for interpreting an Outcome calculation or asking the GM to explain one. The examples do not promise that every component is available in the current interface.

Read in this order: **who acted → what was rolled → each contribution → total → target → outcome → consequences**. The examples here are teaching examples, not results from your campaign. Actual details depend on what the turn recorded. Older turns may have only a total; missing components should be identified as unavailable, never guessed from your current character sheet.

### Calculation components

| Component | What the number means |
|---|---|
| Raw dice and kept die | Each rolled face; which d20 counted and why the others did not. |
| Ability modifier | The modifier from the relevant effective ability score. |
| Proficiency contribution | No proficiency, ordinary proficiency, Expertise, or a specifically granted fraction; count it once. |
| Named bonuses and penalties | Each item, spell, feature or condition that changes the total, with its signed value. |
| Bonus dice | Each applicable die's face and source, such as Bless; include it only if the resolution applied it. |
| Total | The kept die plus all applicable contributions. |
| Target | AC, DC, or an opposing total; use only the target information revealed for that action. |
| Outcome | Hit/miss or success/failure, including any natural-roll or other rule exception. |
| Consequences | Damage by type, defenses, healing, conditions and resource changes; these are separate from accuracy. |

### Worked roll examples

**Ordinary weapon attack:**

`14 (raw d20) + 3 (Strength modifier) + 2 (weapon proficiency) + 1 (magic weapon attack bonus) = 20 (attack total), versus 16 (target AC): hit.`

**Stealth with advantage:**

`7 (first d20, discarded) and 16 (second d20, kept because of advantage); 16 (kept d20) + 3 (Dexterity modifier) + 2 (Stealth proficiency) = 21 (check total), versus 15 (DC): success.`

**A bonus die must have its own explanation:**

`11 (raw d20) + 2 (Wisdom modifier) + 3 (saving-throw proficiency) + 4 (Bless d4 result) = 20 (save total), versus 18 (DC): success.`

Show a bonus die as part of a total only when the recorded resolution says it was applied. WorldAI can report feature dice separately; do not assume two nearby rolls belong to the same calculation. If an opponent's AC or a DC's ingredients were not revealed, their breakdown remains unknown. See [Dice](Dice.md), [DiceNotation](DiceNotation.md) and [DiceAuthenticity](DiceAuthenticity.md).

## Dice, ability scores and modifiers

In dice notation, `2d6 + 3` means roll two six-sided dice, add both faces, then add three. The die size is not its rolled result. A d20 usually resolves an attack, check or save; other dice commonly measure damage, healing or a feature's bonus. A specific rule can replace a roll with a fixed value. The GM need not ask for a roll for a routine action without meaningful uncertainty. [Rules: introduction](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/introduction).

The six abilities are Strength, Dexterity, Constitution, Intelligence, Wisdom and Charisma. The modifier is **floor((score − 10) / 2)**: round toward the lower integer, including for negative numbers. Examples: score 8 gives −1; 10 gives +0; 16 gives +3; 20 gives +5. Use the effective score at the moment of the roll. An equipment bonus to the score is not automatically an additional bonus to the roll. See [AbilityScores](AbilityScores.md).

**Proficiency bonus by total character level:** levels 1–4: +2; 5–8: +3; 9–12: +4; 13–16: +5; 17–20: +6. Multiclass characters use total character level for this bonus. A creature's stat block can already include it. Do not add it again. [Rules: character advancement](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/step-by-step-characters).

Proficiency applies to an eligible skill, tool, weapon, saving throw or spell calculation, not every roll. **Expertise doubles the proficiency contribution**, not the ability modifier or the whole total. For example, show `+6 (Expertise: twice the proficiency bonus of +3)`, not another ordinary proficiency bonus on top of that six. A rule that grants half proficiency is a different feature. [Rules: proficiency](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/using-ability-scores).

## Checks, saving throws and target numbers

An **ability check** resolves an attempt such as searching or sneaking. A skill describes relevant training; it is not a separate ability score. A **saving throw** resists an effect and uses the ability specified by that effect. Skill proficiency does not also grant proficiency in that ability's saves.

The usual pattern is **d20 + relevant ability modifier + applicable proficiency + other permitted bonuses/penalties**. A tie meets the DC and succeeds. A successful save does exactly what its effect says: sometimes no damage, sometimes half damage, sometimes another consequence. It does not automatically negate every effect.

A 2014 opposed check compares both totals; a tie normally preserves the existing situation. A passive check uses a fixed baseline instead of rolling: 10 plus applicable check modifiers, with +5 for advantage or −5 for disadvantage. Neither is a normal attack against AC. [Rules: checks and saves](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/using-ability-scores).

WorldAI's DC selection and approach adjustments are described in [SmartSkillChecks](SmartSkillChecks.md). The target and its explanation belong to the original action; they should not be rewritten after seeing the roll.

## Advantage, disadvantage and rerolls

Roll two d20s and keep the higher for advantage or lower for disadvantage. The unused die is still useful evidence, but does not add to the total. Several sources of advantage do not create extra d20s. Any advantage together with any disadvantage cancels to a normal roll, regardless of how many sources each side has.

A reroll is different: it replaces a permitted die under a particular feature. Preserve the first result, replacement result, reason and which result counted. If a feature changes a die's value rather than rerolling it, say so. [Rules: advantage and rerolls](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/using-ability-scores). See [AdvantageDisadvantage](AdvantageDisadvantage.md).

## Attacks, AC and critical hits

Weapon attacks commonly use Strength for melee and Dexterity for ranged attacks; properties such as finesse or thrown, and specific features, can change that choice. Add weapon proficiency only if applicable. Spell attacks use the relevant spellcasting ability and proficiency. Meet or beat AC to hit.

AC is a target, not damage reduction. Armor, shields, Dexterity, cover and features can contribute differently; alternative base AC formulas do not simply stack. A disclosed AC of 16 is not permission to invent its armor or Dexterity components. [Rules: attack rolls and AC](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat).

Under both published tabletop baselines, a **natural 20 on an attack** hits and is a critical hit; a **natural 1 on an attack** misses. “Natural” means the kept raw die, before modifiers. A modified total of 20 is not necessarily a critical hit. An unused 20 on a disadvantage roll is not the kept result.

A critical hit normally rolls the attack's eligible damage dice twice, including eligible extra attack-damage dice, and adds flat bonuses once. It does not double the entire total. A feature may supply additional dice or change the critical range; record that source explicitly. Effects resolved only by a saving throw do not become critical hits simply because the save was very low. [Rules: attacks and critical damage](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat).

**Critical weapon damage example:**

`4 (weapon d8) + 7 (extra weapon d8 from the critical hit) + 3 (Strength damage modifier) + 1 (magic weapon damage bonus) = 15 (slashing damage before defenses).`

## Damage, defenses, rounding and healing

Keep attack accuracy separate from damage. Weapon damage commonly adds the attack's ability modifier, with specific exceptions. Proficiency is not a general damage bonus. Spell damage adds only the modifiers its spell or features permit. Record each damage type separately, including extra fire, poison or other damage.

- **Resistance:** halve the applicable damage, rounding down.
- **Vulnerability:** double the applicable damage.
- **Immunity:** the protected creature takes no damage of the applicable type; immunity to a condition is a separate protection.
- Apply other damage adjustments first, then resistance, then vulnerability. Repeated sources of the same resistance do not repeatedly halve the same damage. A successful save that halves damage and resistance can both apply.

For example: `15 (rolled fire damage) ÷ 2 (successful save's half-damage rule) = 7 (damage after rounding down); 7 (post-save fire damage) ÷ 2 (fire resistance) = 3 (damage taken after rounding down).` Rounding occurs at each required step, not only at the end. [Rules: damage](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat).

Damage cannot become negative healing. Temporary HP absorbs damage before ordinary HP and is tracked separately; it is not healing and normally does not stack. Healing cannot raise current HP above its maximum. Display damage rolled, damage actually taken and HP lost separately when they differ. For example, a creature with few remaining HP can take more damage than the number of HP it loses. See [Healing](Healing.md) and [RestAndDeath](RestAndDeath.md).

## Spell attacks, spell DC and concentration

A typical **spell attack bonus** is the spellcasting ability modifier plus proficiency and any explicit spell-attack bonuses. A typical **spell save DC** is 8 plus proficiency plus the spellcasting modifier and any explicit DC bonuses. For a multiclass character, use the ability belonging to the feature or spell being used. Items and unusual features may state their own DC.

Example: `8 (spell DC base) + 3 (proficiency) + 4 (spellcasting ability modifier) = 15 (spell save DC).` The target then rolls its own save against that number. A spell does not necessarily require both an attack roll and a saving throw; follow its text. [Rules: spell attacks and saves](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/spellcasting).

**Concentration** sustains one qualifying effect. Damage normally triggers a Constitution save, with DC equal to 10 or half the damage taken rounded down, whichever is greater. In the 2014 baseline, separate damage sources require separate saves. Casting another concentration spell, becoming incapacitated or dying ends concentration. A successful save preserves it; the original spell slot is not spent again. [Rules: concentration](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/spellcasting).

The 2024 rule explicitly caps the damage-triggered concentration DC at 30; the 2014 rule does not. Record the campaign's version instead of silently importing that cap. [Revised concentration rule](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary). See [Spellcasting](Spellcasting.md).

## Initiative, turns and resources

Tabletop initiative is a **Dexterity check**, normally d20 plus Dexterity and explicit initiative features, ordered from highest to lowest. Proficiency is not automatic. Initiative determines order rather than ordinary success or failure. Its tie procedure depends on the campaign's rules; “higher Dexterity always wins” is not the universal 2014 rule. [Rules: initiative](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat).

Keep action, bonus action, reaction and movement budgets distinct. A bonus action requires a feature that permits one; Extra Attack does not automatically grant another whole action. WorldAI lets you continue using available resources until you end your turn. See [Combat](Combat.md) and [Initiative](Initiative.md).

Track spell slots by level, limited-use features, Hit Dice, ammunition, consumables, charges, concentration and conditions. A resource entry should name its source and show the recorded before/after change: `2 (slots before casting) → 1 (slot remaining after casting)`. Do not subtract it again when inspecting or replaying the log.

Recovery follows each resource's rule: a short rest does not restore everything; a long rest is not a universal reset of every item. The 2014 long-rest baseline restores spent Hit Dice up to half the character's total, minimum one; the 2024 baseline restores all spent Hit Point Dice. [2014 rest rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/adventuring), [2024 long rest](https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary).

## Zero HP and death saving throws

If reduced to zero HP without dying outright, a character normally falls unconscious. While at zero and not stable, make a death save at the start of each turn: a d20 result of 10 or more is a success; lower is a failure. Three successes stabilize; three failures mean death. Successes and failures are tracked separately and reset on regaining HP or becoming stable.

A natural 1 counts as two failures; a natural 20 restores one HP. Death saves do not normally add an ability modifier or ordinary save proficiency, though a specifically applicable feature can affect them. Damage while at zero adds failures, critical-hit damage adds two, and massive damage can cause immediate death. Stabilized does not mean conscious or healed. [Rules: zero HP and death saves](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat). See [RestAndDeath](RestAndDeath.md).

## Tabletop, WorldAI house rules and BG3

**Do not treat every d20 as an attack.** In both 2014 and 2024 tabletop rules, ordinary checks and saving throws do not automatically succeed on 20 or fail on 1. Compare their totals unless a specific exception applies. Death saves have the separate rules above. Neither an initiative 20 nor a skill-check 20 generally grants extra damage. [2014 checks](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/using-ability-scores), [2024 attack exceptions](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game).

**WorldAI's documented house rule** extends automatic success/failure to checks and saves. A displayed verdict can therefore differ from a plain total-versus-DC comparison. This is a house rule, not a statement of standard 5e. It also does not make an impossible action possible merely because a player requests a roll. WorldAI also allows a fitting social approach to add half a positive non-Charisma modifier, rounded down, and uses tier-based DCs with approach adjustments totaling at most ±4 and a ceiling of 30. These are additional house rules; see [AbilityScores](AbilityScores.md) and [SmartSkillChecks](SmartSkillChecks.md).

**2024 is a rules revision, not just new wording.** Besides concentration and rests, it changes features, spells, surprise, conditions and action details. For example, 2024 surprise gives disadvantage on initiative; 2014 surprise limits the surprised creature's first turn. Use one declared baseline and explicit exceptions. The [official SRD page](https://www.dndbeyond.com/srd) identifies SRD 5.1 and SRD 5.2.1 separately.

**Baldur's Gate 3 is a presentation reference, not this guide's rules authority.** Its video-game adaptations, difficulty options and patches must not silently become WorldAI rules. Larian, for example, has documented weighted dice and dialogue-roll changes. The useful lesson for an Outcome calculation is transparency: show what happened and why each number applied. [Larian's dice-system update](https://baldursgate3.game/news/community-update-12-patch-4-nature-s-power_21).

Custom settings and classes can add explicit exceptions. Ask the GM which rule applies when something looks unfamiliar. A missing explanation is a reason to request the recorded breakdown, not to invent a bonus. [CampaignDesign](CampaignDesign.md) covers campaign choices; [GodMode](GodMode.md) covers deliberate changes. Faction play is an original system, described in [FactionSystem](FactionSystem.md); surrendered enemies count as fully defeated for rewards, as explained in [CombatVictoryProtocol](CombatVictoryProtocol.md).

## Sources

Checked 2026-10-18. Rules explanations are paraphrased; worked examples are original. This guide is not a complete spell, class, item or condition catalog. Specific features and declared campaign rules can override general rules.

- [System Reference Document](https://dnd.wizards.com/resources/systems-reference-document): official SRD landing page.
- [SRD 5.1, Creative Commons edition](https://media.dndbeyond.com/compendium-images/srd/5.1/SRD_CC_v5.1.pdf): 2014-derived baseline.
- [SRD 5.2.1](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf) and [official version guide](https://www.dndbeyond.com/srd): revised rules, used only where labeled.
- [2014 Basic Rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014): linked chapters explain the relevant rules in context.
- [2024 Basic Rules](https://www.dndbeyond.com/sources/dnd/br-2024): linked chapters distinguish revised mechanics.
- [Larian's official dice-system update](https://baldursgate3.game/news/community-update-12-patch-4-nature-s-power_21): historical example of BG3-specific adaptation, not a claim about every current difficulty setting.
- Related WorldAI guides: [Dice](Dice.md), [AbilityScores](AbilityScores.md), [SmartSkillChecks](SmartSkillChecks.md), [Combat](Combat.md), [Spellcasting](Spellcasting.md), [RestAndDeath](RestAndDeath.md), [PlayerUserStories](../queries/PlayerUserStories.md), [index](../index.md).

### SRD attribution

This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.

This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.
