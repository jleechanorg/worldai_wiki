---
title: CharacterCreation
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [wa-mechanic, wa-system]
sources: []
---

# Character Creation

When you start a campaign, you create a character. WorldArchitect.AI offers two paths: **AI-generated** (the system builds the character based on your prompt) or **hand-rolled** (you pick race, class, background, stats).

## Path 1: AI-generated

The fastest path. You describe what you want and the system builds it.

### Prompt format

> Character: <description> | Setting: <world>

Example (from the Itachi V2 campaign):
> Character: Uchiha Itachi | Setting: Naruto universe. Itachi when he was young and became member anbu. Itachi gaiden arc.

### What the AI generates

Based on your prompt, the CharacterCreation agent builds:
- **Race** (mapped to D&D 5e or world-equivalent)
- **Class** (or equivalent archetype in custom settings)
- **Subclass** (if applicable at level 1)
- **Background**
- **Ability scores** (rolled or assigned)
- **Equipment** (starting gear appropriate to the character concept)
- **Personality** (ideals, bonds, flaws — optionally)
- **Relationships** (connections to NPCs in the setting)

### When AI-generated works well

- You have a strong character concept ("I want to play Itachi").
- You want to play a setting-specific character (a Naruto character, a Game of Thrones character).
- You want to start playing quickly.

### When to hand-roll instead

- You want a specific build (e.g., "DEX paladin with GWM").
- You want to min-max.
- You want to play an unusual combination the AI might not think of.

## Path 2: Hand-rolled

Build your character step-by-step:

1. **Choose race**: Human, Elf, Dwarf, Halfling, etc. (or setting-equivalent).
2. **Choose class**: Fighter, Wizard, Cleric, Rogue, etc.
3. **Choose subclass**: at the appropriate level for your class.
4. **Choose background**: Acolyte, Criminal, Noble, Sage, Soldier, etc.
5. **Roll ability scores**: 4d6kh3, six times, assign.
6. **Choose skills**: from your class's list.
7. **Choose equipment**: from your class's starting equipment list.
8. **Set personality**: ideals, bonds, flaws (optional but adds flavor).

## Custom settings

In custom settings (Naruto, Game of Thrones, BG3, etc.), the character creation adapts:
- **Naruto**: clan, rank, kekkei genkai, jutsu list
- **Game of Thrones**: house, allegiances, reputation
- **BG3**: race, class, origin (origin-specific story hooks)

## Player tips

- **Start with AI-generated**: for your first campaign, let the system build the character. Learn the rules by playing.
- **Hand-roll for replay**: on your second or third character, try hand-rolling.
- **Don't over-optimize**: a character with strong personality plays better than a min-maxed one.
- **Write a backstory**: 2-3 sentences about who they are and what they want. The GM uses this.

See [[concepts/Subclass]], [[concepts/LevelUp]], [[concepts/CampaignWizard]].
