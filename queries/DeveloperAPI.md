---
title: Developer API
created: 2026-09-18
updated: 2026-09-18
type: query
tags: [wa-system, wa-glossary]
---

# Developer API

This page is for developers integrating with WorldArchitect.AI over MCP or
REST. Players don't need it — see
[Player Features Reference](ExternalUserStories.md) instead.

Two surfaces drive a campaign from code: the MCP endpoint and the campaign REST
routes. The `/v1/*` routes look like the OpenAI API but do something else
entirely; read [that section](#the-v1-routes-proxy-your-own-gateway) before you
point an SDK at them.

---

## Authentication

Every campaign, MCP, and `/v1/*` route below requires a bearer token in the
`Authorization` header. (The utility routes — server time, health, and client
diagnostics — are open.) Two kinds of token work:

- **A Firebase ID token** from a signed-in browser session.
- **A personal access token**, which starts with `worldai_`.

Personal access tokens have no button in the settings UI. From a signed-in
session, call the route yourself:

```http
POST /api/settings/personal-access-token
{"action": "generate"}
→ {"success": true, "token": "worldai_…"}
```

The plaintext token is returned once and never again — only its hash is stored,
so a lost token cannot be recovered. Generating a token replaces any existing
one. `{"action": "revoke"}` deletes it.

Per-account turn budgets apply to API traffic exactly as they do in the browser:
100 turns a day on the built-in AI, 5,000 with your own provider key. Over the
limit, routes return 429.

---

## MCP endpoint

`POST /mcp` speaks JSON-RPC 2.0 and supports `tools/list`, `tools/call`,
`resources/list`, and `resources/read`. The tool list is fixed at server start.

| Tool | Required | Optional | Result |
|---|---|---|---|
| `create_campaign` | `user_id`, `title` | `character`, `setting`, `description`, `selected_prompts`, `custom_options`, `god_mode` | A new campaign in your account |
| `quick_start_campaign` | `user_id` | — | A campaign with nothing to fill in |
| `get_campaign_state` | `user_id`, `campaign_id` | — | The full game state as JSON, plus your settings block — which still contains any provider key you saved, so don't log the reply verbatim |
| `process_action` | `user_id`, `campaign_id`, `user_input` | `mode`, `idempotency_key`, `client_idempotency_key`, `request_id` | One played turn, same result as the in-app submit |
| `update_campaign` | `user_id`, `campaign_id`, `updates` | — | Patched campaign metadata |
| `export_campaign` | `user_id`, `campaign_id`, `format` | — | A JSON envelope pointing at a generated `pdf`, `docx`, or `txt` — fetch the file itself via the REST export route |
| `get_campaigns_list` | `user_id` | `limit`, `sort_by` | `{success, campaigns, has_more}` |
| `get_user_settings` | `user_id` | — | Your settings, API keys masked |
| `update_user_settings` | `user_id`, `settings` | — | Partial, validated update |

Notes on the ones with sharp edges:

- **`create_campaign`** — `god_mode` carries a pre-filled character and setting
  so the wizard can be skipped; inside it, `character` and `setting` are
  required and the character needs at least a `name`.
- **`process_action`** — `mode` is `character` or `narrator` and defaults to
  `character`. The three id fields let you retry a submission without replaying
  the turn.
- **`export_campaign`** — `format` is required and must be `pdf`, `docx`, or
  `txt`. Over MCP it returns a JSON envelope (`success`, `format`,
  `campaign_title`, and a server-side file reference), not the file bytes. To
  actually download the document — the same one the in-app Export button
  produces — call `GET /api/campaigns/{id}/export?format=…`, which streams the
  file once and then discards it. For machine-readable state, use
  `get_campaign_state` and the story route.
- **`get_campaigns_list`** — `sort_by` is `last_played` (default) or
  `created_at`. `limit` defaults to 50; that is a default, not a ceiling. The
  reply adds `next_cursor` when more pages remain and `total_count` on the
  first page.
- **`roll_dice`** is **test-only**. It appears in `tools/list` solely when the
  operator starts the server with `ENABLE_DICE_TEST_TOOL=true`. On the public
  deployment it is not listed and any call returns `roll_dice tool disabled`.
  Do not build on it; real play rolls are covered by the audit trail described
  in [DiceAuthenticity](../concepts/DiceAuthenticity.md).

A campaign that is not yours returns a not-found error rather than a permission
error — campaign reads and writes are scoped to the authenticated account.

---

## Campaign REST routes

| Route | Purpose |
|---|---|
| `GET /api/campaigns` | List your campaigns |
| `POST /api/campaigns` | Create a campaign |
| `POST /api/campaigns/quick-start` | Create one with no options |
| `GET /api/campaigns/{id}` | Campaign detail |
| `PATCH /api/campaigns/{id}` | Partial metadata update |
| `POST /api/campaigns/{id}/duplicate` | Deep copy under a new id |
| `GET /api/campaigns/{id}/story` | Story entries, paginated (below) |
| `GET /api/campaigns/{id}/equipment` | Equipment list |
| `GET /api/campaigns/{id}/stats` | Ability scores, HP, AC, saves |
| `GET /api/campaigns/{id}/spells` | Known and prepared spells with slots |
| `GET /api/campaigns/{id}/export?format=…` | The campaign as `pdf`, `docx`, or `txt` |
| `POST /api/campaigns/{id}/interaction` | Play a turn |
| `POST /api/campaigns/{id}/interaction/stream` | Play a turn, streamed |

### Paging the story

`GET /api/campaigns/{id}/story` returns the newest page of entries, ordered
oldest-first inside the page. Paging backwards gives you successively older
pages.

- `limit` — page size, default 100, clamped to 1–500.
- `before` — an ISO-8601 timestamp; `before_id` — an entry id. Either pages
  further back.
- The reply is `{story, pagination}`, where `pagination` carries `total_count`,
  `fetched_count`, `has_older`, and `oldest_timestamp`.

There is **no** scene or turn-range filter. Page by cursor instead.

### Server time

`GET /api/time` returns `{server_time_utc, server_timestamp,
server_timestamp_ms}` — an ISO-8601 UTC string plus the same instant as epoch
seconds and milliseconds. Times are always UTC; there is no timezone field. No
sign-in and no database read is needed, but the route is rate-limited to 30
requests a minute (200 an hour), so poll sparingly.

### Health

`GET /health` returns 200 with a status payload whenever the web process is
running. It is a liveness check only: it does not probe the database or the
model provider, and it never returns 503. A healthy reply means the server is
up, not that a turn will succeed. Development and preview deployments add build
and concurrency details that production omits.

### Client diagnostics

`POST /api/client_diag` accepts buffered client-side page-load events. It is
rate-limited and intended for debugging slow renders.

---

## The `/v1/*` routes proxy your own gateway

`POST /v1/chat/completions` and `GET /v1/models` are OpenAI-shaped, but they do
not play a campaign. Both forward to the OpenClaw gateway URL saved in your
settings and return that gateway's answer.

- Save a gateway URL in Settings first. Without one, both routes return **400**
  (`No gateway URL configured`); if the gateway is unreachable they return
  **502**.
- `POST /v1/chat/completions` returns the gateway's reply unchanged — JSON, or
  server-sent events when you pass `stream: true`.
- `GET /v1/models` returns your gateway's model ids, not a WorldArchitect
  catalogue. They change whenever your gateway does, so do not treat them as
  stable.
- Both routes require authentication.

To drive a campaign from code, use the MCP endpoint or the campaign REST routes
above.

---

## How a turn is routed

You cannot choose which specialist handles a submitted action, and there is no
parameter for it. The game classifies each action by meaning — not by keyword
matching — and routes it to combat, conversation, faction, level-up, or
character-creation handling.

Two consequences matter for an integration:

- **An open review flow holds a lock.** While a character-creation or level-up
  review is open, every action you submit is handled by that flow — it is not
  rejected, and it will not reach combat, conversation, or faction handling
  until the review is finished. Finishing it is also recognised from meaning, so a natural-language
  "I'm done" closes it as reliably as the UI button. Crossing an XP threshold
  does not itself open one — the level applies on that turn and the review is
  optional; see [LevelUp](../concepts/LevelUp.md).
- **Faction operations require faction mode** to be switched on in that campaign
  first; see [FactionSystem](../concepts/FactionSystem.md).

---

## Where to read more

- [Player Features Reference](ExternalUserStories.md) — the same behaviour from
  the player's side of the screen.
