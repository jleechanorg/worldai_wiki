---
title: CampaignWizard
created: 2026-06-19
updated: 2026-08-31
type: concept
tags: [wa-system]
sources: []
---

# Campaign Wizard

A 2-step guided flow for creating a new campaign. The wizard walks you
through picking a campaign type, then lets you review and launch.

## Step 1 — Choose Type

The first screen shows a progress bar with two circles ("1 Choose Type" /
"2 Launch") and a "Step 1 of 2" counter. The form offers:

- **Campaign Type cards** — two large pickable cards:
  - **Dragon Knight Campaign** (the built-in preset; pre-selected by
    default — see [CampaignShowcase](../entities/CampaignShowcase.md)).
  - **Custom Campaign** — start from your own setting.
- **Campaign Title** — text input. Pre-filled with the preset's name for
  Dragon Knight, or "My Epic Adventure" for Custom.
- **Character you want to play** — text input. Left blank, the system
  generates a character mid-flow after launch.
- **Setting / world for your adventure** — multi-line text input. Left
  blank, the system generates a setting.
- **Campaign description prompt** — optional long-form prompt, behind a
  collapsible "Expand" toggle. Use it to describe tone, goals, or story
  premise.

### What changes when you switch type

Switching the type card updates the preview and the auto-seeded defaults
immediately:

| Pick             | Title auto-fill | Character/Setting auto-fill |
|------------------|-----------------|-----------------------------|
| Dragon Knight    | `Dragon Knight` | The preset's named defaults (Ser Arion / World of Assiah) |
| Custom           | `My Epic Adventure` | Placeholder text `Random character (auto-generate)` / `Random fantasy D&D world (auto-generate)` — the system auto-generates after launch if you leave the field blank |

A **Custom** character or setting you type yourself shows up verbatim in
the preview — the wizard does not silently swap in the preset's text.
Switching back to **Dragon Knight** and then to **Custom** again clears
your typed Custom values back to the auto-generate placeholders, not to
Ser Arion's text.

The **Next** button advances you to step 2.

## Step 2 — Ready to Launch

The second screen keeps the progress bar lit at the end and updates the
counter to "Step 2 of 2". It has three parts:

1. **Enter the World** — the big green launch button at the top. Click
   when you're ready. The wizard will create the campaign and route you
   into the opening scene.
2. **Character Avatar (Optional)** — upload a square JPEG / PNG / GIF /
   WebP up to 5 MB. You can always add or change it later.
3. **Campaign Summary** — a card listing what will be created, with each
   row editable via a pencil icon:
   - **Title** — click the pencil to edit in place; click outside to save.
   - **Character** — pre-fills "Auto-generated" if left blank on step 1.
   - **Description** — pre-fills the preset's narrative for Dragon Knight
     or your custom prompt if you wrote one.

Click any field's pencil icon to edit; click outside the input to save,
or press **Escape** to cancel the edit. Edits flow back to the underlying
form so launch uses the latest values.

There is **no dedicated Cancel button** in the wizard. To exit without
launching, click the persistent product wordmark in the top-left nav —
it returns to the dashboard and discards whatever you entered, with no
confirmation prompt.

## After the wizard

After you click **Enter the World**, the system creates the campaign and
the GM narrates Scene 1. For the built-in Dragon Knight preset this is
the moral dilemma scene; for Custom, the system generates the opening
from your prompt and (optionally) your character / setting fields.

## Player tips

- **Pick the preset on your first run.** Dragon Knight is pre-selected
  for a reason — the system has full lore, a named character, and a
  well-tuned opening scene. It is the easiest way to see what the engine
  can do.
- **Leave the character and setting blank to let the system generate.**
  The auto-generated output is usually as good as a typed short prompt
  and saves you typing on a first run.
- **Type a custom setting only if you have one in mind.** A 1–3 sentence
  description is enough — see
  [CampaignDesign](../concepts/CampaignDesign.md) Step 1 for what makes a
  setting "hold up."
- **Edit the preview rows on step 2, not step 1.** Step 1 is for the
  initial seeding; step 2 is where the final values land.
- **Don't fear the Exit.** The top-left wordmark is your escape hatch
  from any wizard state.

See [CampaignDesign](../concepts/CampaignDesign.md),
[CharacterCreation](../concepts/CharacterCreation.md).

## Sources

- [Dragon Knight world module](https://github.com/jleechanorg/worldarchitect.ai/blob/main/world_reference/campaign_module_dragon_knight.md)
  — the canonical built-in campaign that the wizard's preset card seeds
  from.
- [How to Play WorldArchitect.AI](../queries/how-to-play-worldai.md) —
  the player-facing walkthrough that uses these same steps.