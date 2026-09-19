---
title: CampaignWizard
created: 2026-06-19
updated: 2026-09-18
type: concept
tags: [wa-system, wa-campaign, wa-tutorial]
sources: []
---

# Campaign Wizard

Everything between "I want to play" and your first scene happens in two screens.

```
Step 1: Choose Your Campaign  ──>  Step 2: Ready to Launch!  ──>  Scene 1: Character Review & Opening
```

The progress bar labels the two steps **Choose Type** and **Launch**; the footer counts "Step 1 of 2".

---

## Step 1 — Choose Your Campaign

Step 1 collects your world concept, protagonist, and campaign premise.

![Campaign Wizard Step 1 with Expanded Campaign Description Prompt](../assets/fresh_screenshots/02_wizard_step1_description_prompt.png)

### Campaign type

Two cards, and **Play a campaign** is selected for you:

- **Play a campaign** — build a completely custom world, universe, and story from scratch.
- **Dragon Knight Campaign** — the one ready-made module: written lore, two companions, and a calibrated opening scene.

> **What Dragon Knight locks.** Picking **Dragon Knight Campaign** makes it a fixed module: the Universe, Timeline and Plot fields disappear, and Character ("Ser Arion"), Setting and the Campaign description prompt are filled in for you and greyed out. The Title is pre-filled to "Dragon Knight" but you can still change it. Switch back to **Play a campaign** to edit the rest — anything you had already typed comes back.

### Universe and setting inputs (sections 1–6)

- **Favorite Universe / TV Show / IP**: Eight one-click suggestions (Game of Thrones, Star Wars, Cyberpunk, The Witcher, Middle-earth, Stranger Things, Marvel, Dune), or type any other franchise or realm you like. These are text suggestions, not pre-built modules.
- **Timeline / Era (Optional)**: Anchor your story in a specific period (e.g. *Robert's Rebellion*, *The Clone Wars*, *Post-Cataclysm*).
- **Favourite Character / Chosen Protagonist**: Your character's name and archetype, or leave blank for a randomly generated protagonist.
- **Setting / world for your adventure**: A few lines on the physical, political, and magical environment.
- **Plot / What-If Direction**: The central conflict or departure point (e.g. *"What if Ned Stark refused to become Hand of the King?"*).
- **Campaign Title (Pick anything!)**: The name on your campaign card on the dashboard.

### Campaign description prompt (long-form world bible)

This is the **last** numbered section on Step 1 — section 7 on the **Play a campaign** path — and it starts collapsed, behind an **Expand** button. A screenshot of an untouched Step 1 shows only its heading and the Expand button — the large text box itself stays hidden until you expand it. Expand it and you can paste in a whole campaign bible, premise, or set of house rules. (Pick Dragon Knight instead and the Universe, Timeline and Plot fields disappear, so the remaining sections renumber and this one arrives read-only.)

- **Capacity**: a 70,118-character bible (~11,000–12,000 words, about 25 pages) has been tested end to end and stored intact. Length is almost never your constraint.
- **What to paste here**: setting bibles (geography, factions, pantheons, magic systems); character backstory, lineage, equipment, psychology; custom rules, tone constraints, and god-mode style instructions.
- **Short vs. long**: a 1–3 sentence prompt gives the GM room to invent. A full bible enforces strict canon, complex politics, or a custom rules system.

Click **Next** to proceed to Step 2.

---

## Step 2 — Ready to Launch!

Step 2 is your avatar, a summary to check, and the launch button.

![Campaign Wizard Step 2 Launch](../assets/fresh_screenshots/03_wizard_step2_launch.png)

### 1. Enter the World

The **Enter the World** button sits at the top of Step 2, right under the heading — you do not have to scroll to find it. The same button repeats at the bottom of the screen, beside **Previous**. Clicking either one creates your persistent campaign, sets up the rules, and opens Scene 1.

### 2. Character portrait avatar

- Drag-and-drop or click to upload an avatar image.
- JPEG, PNG, GIF, or WebP; max 5MB; 512×512 square looks best.
- It appears in the campaign header bar at the top of the game screen. It is not repeated next to each turn.
- Skipping it here is not final — you can add, replace, or remove the portrait from the game screen later. See [Your portrait in the game header](#your-portrait-in-the-game-header).

### 3. Campaign summary card & inline editing

Check your configuration before launching:
- Shows your Title, Character, Setting, and the first 50 characters of your Campaign description prompt. (Universe isn't repeated here.)
- Each row has a pencil button (**Edit title**, **Edit character**, **Edit setting**, **Edit description**) so you can fix a typo without going back to Step 1.
- Editing is inline: click the field, click outside it to save, or press **Escape** to cancel.

---

## After the wizard: Scene 1 Character Review

Character creation happens inside the story rather than on a separate form:

1. The GM introduces your character in the opening scene context.
2. The GM presents your generated character sheet (ability scores, class, starting spells, and equipment).
3. You review, request modifications, or finalize your build before your first major narrative decision.

---

## What carries into the game screen

Two parts of the wizard stay reachable once you are playing: the answers you typed, and the portrait you chose.

### Checking what you entered — the (i) button

An **info (i)** button sits in the campaign header, just left of your campaign title. Click it and a **Campaign Details** panel reads your creation inputs back to you, one per line:

- **Universe**, **Timeline**, **Character**, **Setting**, **Plot**, and **Description** — the Step 1 fields, exactly as they were stored. Fields you left blank are skipped rather than shown empty, so a quick custom campaign shows only the two or three lines you actually filled in. If nothing was recorded, the panel says so instead.
- For a **Dragon Knight** campaign there is nothing of yours to echo, so the panel shows the Dragon Knight premise — the short opening setup, not the full module text.

Use it when you are three hours into a campaign and want to check whether the world bible you pasted actually landed, or which of your what-if hooks the GM is working from. It is read-only — there is no editing here, and no way to change the premise after launch. **Close** dismisses it. On a narrow phone screen the (i) button is hidden to leave room for the campaign title.

### Your portrait in the game header

**If you skipped the avatar on Step 2**, the header shows a dashed circle with a plus and the label **Add Avatar**. Click it, pick an image, and it uploads straight away — the label switches to *Uploading…* and then your portrait takes the placeholder's spot. There is no cropping step on this quick path.

**If you already have a portrait**, click it. A character card opens over the screen with:

- the portrait at full size,
- your character's name (or the campaign title if no character name was recorded),
- their class, and
- **Level**, **HP** (current/max) and **AC**, when your campaign has recorded them. Early on, before the GM has finalised your sheet in [Scene 1](#after-the-wizard-scene-1-character-review), the stats row can be empty. See [AbilityScores](AbilityScores.md) and [LevelUp](LevelUp.md) for what those numbers mean.

The card has two buttons:

- **📷 Change Photo** — pick a new image and a full-screen crop view opens: *Drag to reposition • 512×512px recommended*. Drag the image inside the square until the framing looks right, then **✅ Use This Crop** to upload it, or **✕ Cancel** to back out. The header portrait and the card both update as soon as the upload finishes.
- **🗑 Remove** — asks you to confirm, then clears the portrait from the header. The dashed **Add Avatar** placeholder comes back the next time the campaign loads.

Close the card with its **×**, by clicking the dimmed area around it, or by pressing **Escape**.

---

## Player tips

- **Use the description prompt.** Have a homebrew world or a novel concept? Paste your notes straight into it — that is what it is for.
- **Pick one tone.** Slapstick comedy plus grimdark survival in the same prompt produces confused narration. Name a primary tone and stick to it.
- **Fix typos on Step 2.** Use the pencil buttons on the summary card instead of going back.
- **Want to customise Dragon Knight?** Only the Title and the Step 2 avatar (Ser Arion's portrait loads by default, and you can replace it). Every other field is locked — start from **Play a campaign** and describe the world you want instead.

See [CharacterCreation](CharacterCreation.md), [CampaignDesign](CampaignDesign.md), [GodModePrompting](GodModePrompting.md), and [How to Play](../queries/how-to-play-worldai.md). For the same flow on one screen, see [CampaignWizard](../entities/CampaignWizard.md).
