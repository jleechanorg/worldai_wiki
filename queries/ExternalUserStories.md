---
title: ExternalUserStories
created: 2026-06-20
updated: 2026-06-21
type: query
tags: [wa-system, wa-tutorial]
sources:
  - raw/worldarchitect.ai-docs-user-stories-general.md
---

# External User Stories (Accounts, Streaming, Settings, API, Agents, Persistence, Dice Audit, Dev Tools)

This page is the **public-facing companion** to the internal developer spec
[`raw/worldarchitect.ai-docs-user-stories-general.md`](../raw/worldarchitect.ai-docs-user-stories-general.md).
It rewrites stories **EXT-026 through EXT-100** — the 75 stories covering accounts,
live UI, settings & providers, the MCP / OpenAI API, agent routing, persistence,
dice audit, and dev tools — for an audience of **players and external developers**
who never need to read the private backend source code.

> **Why the EXT- prefix?** This page mirrors the internal spec's US-026..US-100
> numbering but uses `EXT-NNN` to avoid colliding with the gameplay-story IDs
> US-001..US-075 already used by [PlayerUserStories](PlayerUserStories.md).
> Whenever you see `EXT-NNN` on this page, it maps 1:1 to `US-NNN` in the
> internal spec — the number is the same, the prefix is just for cross-page
> clarity.
>
> | Wiki page | ID range | Audience |
> |-----------|----------|----------|
> | [PlayerUserStories](PlayerUserStories.md) | US-001 – US-075 | Player (gameplay) |
> | ExternalUserStories (this page) | EXT-026 – EXT-100 (= US-026 – US-100) | Player + External developer (operational) |

If you are a player who just wants to know what the game can do for you, start
with the first 75 stories in [PlayerUserStories](PlayerUserStories.md) and come
back here for the operator / power-user surface.

If you are an external developer integrating with the game over API, MCP, or
OpenAI-compatible chat, **start here**. Sections 13–17 cover almost everything
you need.

> **Reading guide**
> - **Player** sections: 13 (Account), 14 (Live UI), 15 (Settings), 17 (Agents),
>   18 (Persistence), 19 (Dice Audit), 20 (Export). These describe behaviour
>   you can see or configure.
> - **Developer / integrator** sections: 16 (MCP + API), 19 (Dice Audit
>   integrity claims), 20 (Diagnostics). These describe the contract surface
>   for code that talks to the game.
> - Sections are independent; jump to the one you need.

---

## System matrix (EXT-026 – EXT-100)

| ID range | System | Audience | Count |
|----------|--------|----------|-------|
| EXT-026 – EXT-030 | Account & Sign-In | Player | 5 |
| EXT-031 – EXT-044 | Live UI & Streaming | Player | 14 |
| EXT-045 – EXT-050 | Settings & Providers | Player / Power user | 6 |
| EXT-051 – EXT-067 | API & MCP Integration | Developer / Agent | 17 |
| EXT-068 – EXT-079 | Agent Routing | Player (behaviour) / Developer (mechanism) | 12 |
| EXT-080 – EXT-090 | Persistence & World State | Player | 11 |
| EXT-091 – EXT-096 | Dice Audit & Provably-Fair | Player (integrity claims) / Developer (audit log) | 6 |
| EXT-097 – EXT-100 | Diagnostics, Telemetry, Export | Developer / Power user | 4 |

**Total: 75 external-facing stories**, mirroring the internal `docs/user-stories-general.md` matrix.

---

## 13. Account, Sign-In & Identity

These stories cover sign-in, settings persistence, API-key handling, and the
rate-limit / turn-budget envelope that protects the service.

### EXT-026: Sign In With Google or Apple

**As a** player,
**I want** to sign in with Google or Apple single sign-on,
**So that** my campaign state and progress are linked to a stable account I
control.

- Sign-in uses Firebase Identity Toolkit under the hood.
- Every server request is authenticated — your `user_id` and email are
  attached to every state write.
- Signing out invalidates the session and any cached settings.

See [HowToPlay](how-to-play-worldai.md) (Step 1 — Sign up).

### EXT-027: Settings That Follow You Across Devices

**As a** signed-in player,
**I want** my settings (provider, model, theme, persona) to persist across
sessions and devices,
**So that** I do not have to reconfigure every time I log in.

- Your settings live in your user record and survive reloads, browser
  switches, and device hops.
- Settings are loaded once per session and only the fields you change are
  updated.

### EXT-028: Reveal / Hide Your API Key in the UI

**As a** player who brought their own API key,
**I want** to reveal or hide the saved key with a click-to-reveal eye icon,
**So that** I can confirm it's correct without exposing it to anyone looking
over my shoulder.

- The key is masked by default; click the eye to toggle visibility.
- Reveal state is local-only — it resets when you reload the page.
- Reveal events are snapshotted on the server for security observability.

### EXT-029: Trusted-Player Rate-Limit Exemption

**As a** trusted playtester,
**I want** long test sessions to be exempt from the public rate limit,
**So that** I can run extended play without hitting 429s.

- Exemption is keyed on your email and is set by the operator, not by the
  client.
- This is an internal/QA convenience; it does not appear in normal play.

### EXT-030: Per-User Turn Budget

**As a** player,
**I want** my turns per session to be capped fairly,
**So that** the service stays available for everyone and abuse is bounded.

- The default cap is generous; elevated caps exist for trusted accounts.
- When you hit the cap you'll see a clear modal showing when your next turn
  is allowed (see EXT-034).
- Budgets are tracked per user across all of their campaigns.

---

## 14. Live UI, Streaming & Front-End Feedback

These stories cover the in-browser experience: how the AI's response streams
in, how dice appear inline, what the loading state looks like, and the
client-side polish that makes long campaigns feel responsive.

### EXT-031: Live Token Streaming

**As a** player,
**I want** the AI's response to stream into the story as tokens arrive,
**So that** I see the world respond in real time instead of staring at a
blank screen.

- The story entry fills in token-by-token from the moment the server starts
  generating.
- The page auto-scrolls as new text arrives, but respects your scroll
  position (no fighting you if you've scrolled back up to re-read).

### EXT-032: Live Dice Roll Inline

**As a** player,
**I want** dice rolls to appear inline next to the narrative when a check
resolves,
**So that** I can verify the outcome and the modifiers that produced it.

- Each roll shows its notation (e.g. `1d20+5`), the base roll, the modifier,
  and the final total.
- Inline rolls reconcile against the audit log on completion — see
  [DiceAuthenticity](../concepts/DiceAuthenticity.md).

### EXT-033: Inline Tool-Result Display

**As a** player,
**I want** background tool invocations (faction moves, reward calculations,
world events) to show up inline as compact cards,
**So that** I understand what just happened in the simulation underneath the
narration.

- Faction moves appear as compact inline cards.
- Generic tool calls (rewards, world events, etc.) appear as compact inline
  cards.
- Status updates and warnings appear as muted rows above or below the
  narrative.

### EXT-034: Rate-Limit Modal With Reset Time

**As a** player,
**I want** a modal that tells me exactly when my next turn is allowed,
**So that** I know whether to wait, switch campaigns, or come back later.

- The modal shows a human-readable reset time derived from the server's
  429 response.
- It is dismissable without losing your place in the story.

### EXT-035: Loading-Message Rotation

**As a** player waiting on a long LLM call,
**I want** context-aware loading messages ("Rolling dice…", "Updating the
world…"),
**So that** I know the system is alive while thinking.

- Messages rotate on a timer while the request is in flight.
- The current context (combat, dialog, world tick) drives the message pool.

### EXT-036: Reduced-Motion Support

**As a** player who has enabled `prefers-reduced-motion` in my OS,
**I want** the UI to skip smooth scrolling and elaborate transitions,
**So that** I am not physically uncomfortable while playing.

- Smooth scrolling is replaced with instant jumps.
- Non-essential animation keyframes are skipped.
- The setting is read once at boot, not rechecked mid-flow.

### EXT-037: Theme Switcher (Default / Fantasy)

**As a** player,
**I want** to switch between the Default and Fantasy themes,
**So that** the UI matches my mood and campaign tone.

- The theme is applied before first paint to avoid a flash of the wrong theme.
- Preference persists in browser storage; cross-device sync is via your
  account settings.

### EXT-038: Campaign Wizard Onboarding

**As a** first-time player,
**I want** a guided wizard that walks me through setting, character, and
opening scene,
**So that** I can get into the game without reading docs first.

- Step indicators and a progress bar show where you are.
- Each step validates before letting you advance.
- You can skip the wizard and create a campaign directly from the dashboard.

See [CampaignWizard](../concepts/CampaignWizard.md).

### EXT-039: Enhanced Campaign Search & Filter

**As a** player with many campaigns,
**I want** debounced search plus a filter row,
**So that** I can find the campaign I want quickly.

- Search debounces input by ~200ms to avoid hammering the API.
- Filters include status, last-played, and character class.
- Empty result states show a helpful message, not a blank list.

### EXT-040: Test Connection From the Settings Page

**As a** player using a custom gateway,
**I want** a "Test connection" button on the settings page,
**So that** I can verify my setup without leaving the page.

- The button sends a probe request and updates a status badge inline.
- Failures show as a non-blocking error message.

### EXT-041: Personal Access Token (PAT) Provisioning

**As a** power user,
**I want** to generate a personal access token for CLI / MCP access,
**So that** I can drive the game from external tools.

- Tokens are issued tied to your account and shown once with a copy button.
- Tokens are stored hashed on the server; the plaintext only exists in the
  clipboard moment.

See [§ 16 — MCP, API & Integrations](#16-mcp-api--integrations).

### EXT-042: Inline Editor & Component Enhancer (Dev)

**As a** developer or QA tester,
**I want** an inline editor and component-enhancer hook in the page,
**So that** I can tweak UI text live without a redeploy.

- Only enabled in non-production builds by default.
- Lets you hot-swap component templates and edit text on selected nodes.

### EXT-043: Streaming Warning For a Stalled Stream

**As a** player,
**I want** a visible warning if the AI stream stalls,
**So that** I know it is not my connection.

- The client tracks time-since-last-token.
- After a threshold, a warning row appears inline.
- The warning disappears the moment the stream resumes.

### EXT-044: Client-Side Diagnostic Bootstrap (Dev)

**As a** QA engineer,
**I want** the client to capture page-load diagnostics,
**So that** I can debug slow renders.

- Diagnostics are queued before the diagnostic helper is loaded, so nothing
  is lost on slow pages.
- Buffered events are sent to a server endpoint with PII scrubbed.

---

## 15. Settings, Providers & Model Configuration

These stories cover the model selection surface: which LLM runs your campaign,
how your key is validated, and how errors surface when something is wrong.

### EXT-045: Provider Selection (Gemini / OpenAI / OpenClaw)

**As a** player,
**I want** to choose which LLM provider runs my campaign,
**So that** I can use my own API key, fall back to the default, or run through
my own OpenClaw gateway.

- The settings page lists available providers as a radio group.
- Switching providers takes effect immediately on your next turn.
- Provider changes are snapshotted for observability.

### EXT-046: BYOK Key Validation

**As a** player bringing my own key,
**I want** my provider key to be validated on save,
**So that** I find out immediately if it is wrong.

- Empty or malformed keys are rejected with a clear error.
- A successful save returns the masked key length for confirmation.
- A bad key does not poison subsequent turns — each turn re-validates.

### EXT-047: Model List Discovery

**As a** player,
**I want** to see the list of available models for my chosen provider,
**So that** I can pick a model without leaving the page.

- The settings page lists each model with a label and capability hints.
- External SDKs that auto-discover models use the same list via
  `GET /v1/models` — see EXT-061.

### EXT-048: Dragon Knight Campaign Description on Demand

**As a** player picking a built-in campaign,
**I want** the Dragon Knight template description fetched on demand,
**So that** the wizard can show campaign flavour text.

- The description is fetched once per session and cached.
- The wizard falls back to a default if the call fails.

See [CampaignWizard](../concepts/CampaignWizard.md).

### EXT-049: Reveal Saved API Key With Server Confirmation

**As a** player,
**I want** clicking the eye icon to fetch the key from the server,
**So that** the key never lives in client storage.

- The reveal route is auth-gated and rate-limited.
- Reveal events are logged server-side as sensitive operations.

### EXT-050: Provider Error Surfacing

**As a** player,
**I want** LLM provider errors to surface as a readable message,
**So that** I know whether to switch providers, retry, or report a bug.

- Provider exceptions map to one of: rate-limit, auth, transient, schema.
- The error shows as a toast or modal with retry guidance.
- Raw stack traces never reach the UI.

---

## 16. MCP, API & Integrations

This is the section external developers care about most. The game exposes a
JSON-RPC 2.0 MCP endpoint and an OpenAI-compatible chat surface so external
agents, CLI tools, and OpenAI SDKs can drive the game without scraping the UI.

### EXT-051: JSON-RPC 2.0 MCP Endpoint

**As an** external agent or CLI,
**I want** a single JSON-RPC 2.0 endpoint that exposes game tools,
**So that** I can drive campaigns without scraping the UI.

- The endpoint accepts `tools/call` payloads.
- The tool list is fixed and registered at server boot.
- Auth is enforced on every call (Firebase bearer or PAT).

See the per-tool stories below.

### EXT-052: `create_campaign` MCP Tool

**As an** agent,
**I want** to create a new campaign via MCP,
**So that** I can spawn sandboxed test scenarios.

- Accepts `{template, user_settings}`.
- Returns `{campaign_id, state_summary}`.
- Side effect: a new campaign document in your account.

### EXT-053: `get_campaign_state` MCP Tool

**As an** agent,
**I want** to read a campaign's current state,
**So that** I can decide what action to take next.

- Returns the full game state JSON.
- Sensitive fields (API keys) are stripped.
- A 404 is returned if the campaign does not belong to the caller.

### EXT-054: `process_action` MCP Tool

**As an** agent,
**I want** to submit a player action and get the resulting state diff,
**So that** I can chain decisions across MCP calls.

- Accepts `{input_text, mode}`.
- Returns the same shape as the in-app interaction endpoint.
- Rate limiting applies per your per-turn budget (EXT-030).

### EXT-055: `update_campaign` MCP Tool

**As an** agent,
**I want** to patch a campaign's metadata (title, character name, etc.),
**So that** I can rename or annotate campaigns without a UI flow.

- Accepts partial fields; server validates against the campaign schema.
- Audit log records the patch with caller identity.

### EXT-056: `export_campaign` MCP Tool

**As an** agent,
**I want** to export a campaign as a structured bundle,
**So that** I can run analysis or back up stories.

- Returns a serialized bundle including story entries, character state, and
  world events.
- Format matches the in-app download endpoint.

### EXT-057: `get_campaigns_list` MCP Tool

**As an** agent,
**I want** a paginated list of my campaigns,
**So that** I can pick which one to operate on.

- Returns `{items, next_cursor}`.
- Capped at 50 per page.
- Ordered by `last_played_at desc`.

### EXT-058: `get_user_settings` / `update_user_settings` MCP Tools

**As an** agent,
**I want** to read and update my own settings,
**So that** I can reconfigure from a script.

- Both tools enforce per-user isolation.
- Updates are partial and validated.
- API keys are masked in `get_user_settings`; use EXT-049 to reveal.

### EXT-059: `roll_dice` MCP Tool

**As an** agent,
**I want** to roll dice directly via MCP,
**So that** I can drive mechanical outcomes without going through the full
LLM loop.

- `roll_dice(notation)` returns a structured result.
- The roll is recorded in the audit log (EXT-095) and is private to you.

See [DiceNotation](../concepts/DiceNotation.md).

### EXT-060: OpenAI-Compatible Chat Completions

**As a** developer,
**I want** to call the API using the OpenAI client SDK,
**So that** I can use familiar tooling.

- `POST /v1/chat/completions` accepts `messages` and `model`.
- Response shape matches the OpenAI ChatCompletion schema.
- Streaming is supported via SSE on the same route.

### EXT-061: OpenAI-Compatible Model List

**As a** developer,
**I want** `GET /v1/models` to return the model catalog,
**So that** client SDKs that auto-discover models work out of the box.

- Response is `{object: "list", data: [{id, ...}]}`.
- Model IDs are stable across deploys.
- The route is auth-gated.

### EXT-062: Campaign CRUD REST API

**As a** player or agent,
**I want** REST endpoints to list, get, create, patch, and duplicate
campaigns,
**So that** I can manage my library from code.

- `GET /api/campaigns` — list.
- `GET /api/campaigns/{id}` — detail.
- `POST /api/campaigns` — create.
- `PATCH /api/campaigns/{id}` — partial update.
- `POST /api/campaigns/{id}/duplicate` — clone with a new id.

### EXT-063: Read-Only State Endpoints

**As a** player or agent,
**I want** dedicated endpoints for equipment, stats, and spells,
**So that** I can render structured views without parsing the full state
blob.

- `GET /api/campaigns/{id}/equipment` — equipment list.
- `GET /api/campaigns/{id}/stats` — ability scores, HP, AC, saves.
- `GET /api/campaigns/{id}/spells` — known and prepared spells with slots.

### EXT-064: Story Endpoint With Scene Filtering

**As a** player,
**I want** the story endpoint to return entries scoped to a scene or turn
range,
**So that** I can navigate long campaigns quickly.

- `GET /api/campaigns/{id}/story?from=N&to=M` returns the slice.
- Scene number is derived from the turn counter.
- World events are filtered to the matching scene.

### EXT-065: Server Time Endpoint

**As a** client,
**I want** `GET /api/time` to return the server's wall-clock,
**So that** I can sync timers and detect drift.

- Response is `{now: <ISO-8601>, tz: <iana>}`.
- The endpoint is cheap (no DB read) and unauthenticated.

### EXT-066: Health & Liveness Endpoints

**As an** operator,
**I want** `GET /health` to report liveness,
**So that** I can wire it to uptime monitoring.

- Endpoint returns 200 if the process is up.
- Optional checks report Firestore and provider reachability.
- 503 is returned if a critical dependency is down.

### EXT-067: Async Route Wrapper (Internal)

> Developer-internal affordance: developer-defined route handlers can run
> async coroutines so I/O-bound work does not block the worker. Players do
> not see this directly.

---

## 17. Agent Routing, Reasoning & Specialised Agents

These stories describe how the game picks the right kind of reasoning for
your action and how modal flows (level-up, character creation, campaign
upgrade) are kept atomic.

### EXT-068: Agent Selection Per Domain

**As a** player,
**I want** the right specialised reasoning to handle my action based on
what I am doing,
**So that** combat, dialog, planning, and rewards each get the right style.

- Combat routes to the combat reasoner.
- NPC conversations route to the dialog reasoner (with a heavy variant for
  long scenes — EXT-072).
- Level-up flows route to the progression reasoner ([US-015 Level-Up Modal Lock & Atomicity](PlayerUserStories.md#us-015-level-up-modal-lock-atomicity)).
- Faction management routes to the faction reasoner (EXT-074).
- Character creation and campaign-upgrade flows route to their own
  reasoners ([Campaign Wizard](../entities/CampaignWizard.md), EXT-075).

### EXT-069: Conclude-Domain Detection

**As a** player,
**I want** the system to recognize when I want to "end the session" or
"wrap up",
**So that** it shifts into the conclude domain automatically.

- Phrases like "let's stop here" or "wrap up" trigger the conclude domain.
- Conclude is only entered when no modal lock is active (EXT-078).

### EXT-070: Spicy Mode Toggle

**As a** player,
**I want** an explicit spicy mode toggle in settings,
**So that** I can opt into mature content (or out of it) per account.

- The toggle is per-user and persists with settings.
- When on, the dialog reasoner for spicy scenes is selected.
- Default is off.

### EXT-071: Prompt-Order Validation (Internal)

**As a** developer,
**I want** an agent's prompt order to be validated at boot,
**So that** misconfigured agents fail fast.

> Developer-internal; player-visible effect is "the game refuses to start if
> a prompt file is missing or out of order, rather than failing mid-scene."

### EXT-072: Heavy Dialog Mode

**As a** player in an extended NPC conversation,
**I want** the dialog reasoner to use a richer-memory variant after a while,
**So that** long conversations stay coherent.

- The transition is invisible to the player.
- The threshold is on dialog depth, not on turn count.

### EXT-073: Deferred Rewards Resolution

**As a** player,
**I want** rewards that need follow-up (e.g. a level-up choice) to be
deferred, not lost,
**So that** I can resolve them when ready.

- Deferred items appear in a "Pending Rewards" panel.
- You can resolve them from the panel at any time, even after several
  scenes have passed.

### EXT-074: Faction Turn Cycle

**As a** player,
**I want** factions to take their own turns behind the scenes,
**So that** the world evolves even when I am idle.

- Faction cycles fire every N game turns or M in-game hours.
- Outcomes are added to the world events log and visible in your campaign.
- See [FactionSystem](../concepts/FactionSystem.md).

### EXT-075: Campaign Upgrade Migration

**As a** player with an older campaign,
**I want** the system to migrate my campaign to the latest schema
automatically,
**So that** I get new features without losing progress.

- The migration runs on first load of an outdated campaign.
- A modal explains what changed and offers to continue.
- The migration is logged and reversible in tests.

### EXT-076: Planning Block Generation

**As a** player,
**I want** the reasoner to propose a multi-choice plan before risky actions,
**So that** I can pick a strategy.

- The plan appears as a clickable choice list inline.
- Your selection commits the action.

### EXT-077: System-Instruction Caching For Level-Up (Internal)

> Developer-internal. Player-visible effect: long level-up flows stay fast
> because the system-instruction text is cached per character build.

### EXT-078: Modal Lock Enforcement

**As a** player,
**I want** general navigation to be locked while a modal (level-up,
character creation, campaign upgrade) is active,
**So that** I cannot lose state mid-flow.

- Off-modal actions are rejected until the modal commits or cancels.
- The UI shows a banner explaining the lock.

### EXT-079: State-Changes Release Active Modal

**As a** player,
**I want** state changes that imply the modal is finished to release the
lock automatically,
**So that** I do not have to dismiss manually.

- The lock releases on the canonical commit.
- Releases are one-way and audit-logged.

---

## 18. Persistence, Time & World State

These stories describe what is remembered, how long-running campaigns stay
coherent, and how the world state evolves between your actions.

### EXT-080: Per-User Data Isolation

**As a** player,
**I want** my campaign state stored under my account,
**So that** I cannot see or modify other users' data.

- Every campaign document path is namespaced by user.
- Queries are scoped to the authenticated user.
- No cross-user reads or writes are possible from the client.

### EXT-081: Duplicate a Campaign

**As a** player,
**I want** to duplicate an existing campaign,
**So that** I can try a different branch without losing the original.

- The duplicate is a full deep copy with a fresh id.
- The original is untouched.

See [HowToPlay](how-to-play-worldai.md).

### EXT-082: Within-User Campaign Copy (Internal)

> Developer-internal helper used by tests and migrations. The player-facing
> behaviour is "duplicates work reliably."

### EXT-083: World Time Tracking (Y/M/D/H/M/S)

**As a** player,
**I want** the in-world time to advance during rests, travel, and time-skips,
**So that** schedules and calendar events stay coherent.

- World time is tracked at year/month/day/hour/minute/second resolution.
- The game rejects time moves that go backwards.

### EXT-084: Progressive World Time Merge (Internal)

> Developer-internal safety: partial time updates from the model only update
> known fields, so an imprecise answer cannot corrupt the calendar.

### EXT-085: Living World Turn Counter

**As a** player,
**I want** the world to track its own turn counter separately from my
turn counter,
**So that** faction cycles run on their own clock.

- The world counter is server-owned; the model cannot set it directly.
- Faction cycles, world events, and time pressure all read from it.

See [LivingWorld](../concepts/LivingWorld.md).

### EXT-086: World Event Annotation With Turn / Scene

**As a** player,
**I want** world events to be tagged with turn and scene,
**So that** I can filter the story by when things happened.

- Events are filterable by scene, turn range, or event type.

### EXT-087: Story Entry Canonicalization For Level-Up

**As a** player,
**I want** the level-up narrative to land in the story log as a clean,
atomic entry,
**So that** I can scroll back to it later.

- The canonical entry replaces any draft entries the model may have started.
- The entry links to the level-up choice that was made.

### EXT-088: Faction Minigame Dual-Mode (Real-Time + Catch-Up)

**As a** player,
**I want** the world to run faction turns both in real-time and as offline
catch-up,
**So that** the world keeps moving even if I log off for a day.

- Real-time: cycles fire while you are online.
- Catch-up: when you return, the engine computes how many cycles would have
  elapsed offline and applies them.

See [FactionSystem](../concepts/FactionSystem.md), [FactionPlay](../concepts/FactionPlay.md).

### EXT-089: World Events Cascade Cleanup

**As a** player,
**I want** old world events to be pruned automatically,
**So that** the document size stays bounded as my campaign runs for months.

- Cleanup runs inside the faction turn cycle.
- A configurable recent window is kept; older events are dropped with a
  log entry.

### EXT-090: Stale Choice Pruning

**As a** player,
**I want** stale planning choices and reward corrections to be filtered out
before commit,
**So that** they cannot override newer state.

- Superseded corrections are dropped.
- Stale level-up choices are flagged and ignored.

---

## 19. Dice Audit, Provably-Fair & Code-Execution Anti-Cheat

These stories document the integrity claims behind the dice system. As a
player you mostly experience them as "the dice are honest"; as a developer
you can read the audit trail.

### EXT-091: Code-Execution Fabrication Detection

**As a** player,
**I want** dice that come from a code-execution tool to be audited,
**So that** the model cannot launder fabricated dice through code.

- Suspicious code outputs are flagged.
- Code outputs are reconciled with the audit log.
- Violations are logged for operator review.

See [DiceAuthenticity](../concepts/DiceAuthenticity.md).

### EXT-092: Roll Tool With Structured Notation

**As a** player,
**I want** the dice reasoner to use a structured `roll_dice` tool that
accepts `NdM±K` notation,
**So that** every roll goes through the canonical tool.

- The reasoner is restricted from writing raw dice outcomes into narrative
  text.
- All rolls are requested via the structural tool, executed server-side, and
  appended to game state.

See [DiceNotation](../concepts/DiceNotation.md), [DiceRollMechanics](../concepts/DiceRollMechanics.md).

### EXT-093: Attack Roll Resolution

**As a** player attacking,
**I want** the system to compute attack roll, crit, and damage in one
server call,
**So that** the reasoner cannot split the resolution across hallucinated
steps.

- Attack, crit, and damage all go through the same audit path as plain rolls.
- Critical hits double dice (not modifiers).

See [DiceRollMechanics](../concepts/DiceRollMechanics.md).

### EXT-094: Skill Check & Saving Throw

**As a** player,
**I want** a single helper for skill checks and saving throws,
**So that** the reasoner uses the canonical signature every time.

- Skill checks and saving throws both go through the same unified entry
  point.
- The audit log records both equally.

### EXT-095: Provably-Fair Audit Trail

**As a** player who suspects cheating,
**I want** every roll to leave a server-side audit trail,
**So that** the integrity of the game is verifiable.

- Each roll produces a verifiable seed + commitment.
- Stdout and audit log are reconciled.
- Audit events ship to internal telemetry.

See [DiceAuthenticity](../concepts/DiceAuthenticity.md).

### EXT-096: Dice Anti-Fabrication Telemetry (Internal)

> Operator-facing telemetry. Player-visible effect: dice integrity issues are
> investigated and fixed; you don't see the logs directly.

---

## 20. Diagnostics, Telemetry & Export

These stories cover the developer-facing surface plus the player-facing
"download your story" feature.

### EXT-097: Server Time & Client Diagnostic Endpoints

**As a** developer,
**I want** server-time and client-diagnostic endpoints exposed,
**So that** I can debug drift and slow renders.

- `GET /api/time` returns the wall-clock (also see EXT-065).
- `POST /api/client_diag` accepts buffered client events.
- Both endpoints are cheap and rate-limited.

### EXT-098: BigQuery Telemetry Shipping (Internal)

> Operator-internal telemetry pipeline. Player-visible effect: aggregate
> integrity metrics are tracked and acted on.

### EXT-099: Context-Token Budgeting (Internal)

> Developer-internal: the LLM context is split into per-component slices
> (story, system prompt, etc.) and compacted automatically when
> utilization exceeds a threshold. Player-visible effect: very long
> campaigns keep running without stalling or failing.

### EXT-100: Document & Story Export

**As a** player,
**I want** to export my campaign story as PDF, DOCX, or TXT,
**So that** I can share or print my adventure.

- Export includes the campaign title, story entries, and world events.
- The export endpoint is auth-gated; the file is generated server-side.
- See [ItachiGaiden](../entities/ItachiGaiden.md) for an example export.

---

## Coverage by priority

| Priority | Count | Audience focus |
|----------|-------|----------------|
| P0 Critical | ~20 | Player sign-in, live streaming, MCP core tools, modal locks, per-user isolation, dice audit primitives |
| P1 High | ~38 | Settings, providers, agents, persistence, world state, dice audit ops, export |
| P2 Medium | ~17 | UI polish, theme, search, caching, dev-only diagnostics |

(See the internal `raw/worldarchitect.ai-docs-user-stories-general.md` for the
exact priority assignments per story.)

---

## Where to read more

- The **player-facing core** is in [PlayerUserStories](PlayerUserStories.md)
  (75 stories, US-001 – US-075).
- The **internal developer spec** is mirrored in
  [`raw/worldarchitect.ai-docs-user-stories-general.md`](../raw/worldarchitect.ai-docs-user-stories-general.md).
  The mirror is read-only reference material; the internal spec's own
  `file:line` references live there but are not republished in the wiki
  pages.
- **Concept deep-dives**: see [Concepts](../concepts/) for combat, dice,
  faction play, level-up, god mode, etc.
- **How-to guides**: see [HowToPlay](how-to-play-worldai.md) and
  [CampaignDesign](../concepts/CampaignDesign.md).

## Sources

- Original: `jleechanorg/worldarchitect.ai` PR
  [#7709](https://github.com/jleechanorg/worldarchitect.ai/pull/7709)
  (`docs/user-stories-general.md`, internal).
- Mirror: [`raw/worldarchitect.ai-docs-user-stories-general.md`](../raw/worldarchitect.ai-docs-user-stories-general.md).
- Audience rewrite performed 2026-06-20 to surface the operational
  system for external readers without exposing internal code paths.