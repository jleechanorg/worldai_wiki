# WorldAI Mini

WorldAI Mini is a player-led tabletop adventure client for ChatGPT and a small MCP backend for saved Mini campaigns, recorded dice, and player-only checkpoints. This directory contains the client package and the backend code needed to run it separately from the full WorldAI application. Mini campaigns are separate from full WorldAI campaigns.

See the wiki's [how-to-play guide](../queries/how-to-play-worldai.md) and [dice guide](../concepts/Dice.md) for general gameplay. The code is provided under the [included MIT license](LICENSE).

## Contents

- `client/` is the 1.0.3 ChatGPT plugin package, including its skill and MCP connection. Its MCP URL initially points to the WorldAI-hosted service. Change the URL in `client/mcp.json` before connecting it to your own deployment.
- `backend/` contains the Flask MCP server, Mini state and dice logic, Firestore storage, optional verified-email recovery, the Mini-only recovery page, schemas, prompts, and focused tests.

## Run the backend

Python 3.12 or newer and a Firebase project with Firestore are required. This server uses the Google application-default credentials of the process that runs it. Use a dedicated project and least-privilege service identity. Do not put credentials in this repository.

```sh
cd worldai-mini/backend
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
export GOOGLE_CLOUD_PROJECT="<your-firebase-project-id>"
# Set GOOGLE_APPLICATION_CREDENTIALS to your local credential file if needed.
gunicorn --bind 127.0.0.1:8080 server:app
```

The standalone backend writes bounded operational metadata to standard error. Configure your own log collection.

The service fails closed until Firestore document `mini_runtime_control/default` has `enabled: true`. Create that document deliberately in your own Firebase project before serving traffic. The server maintains rate-limit and session documents; configure Firestore retention and TTL policies for its `ttl_at` fields, appropriate access controls, backups, and cost limits. This setup uses a real external database; it is not an offline database.

The MCP endpoint is `/mini-mcp`. It accepts JSON-RPC POST requests and supports initialization, `tools/list`, and the eight Mini tools. `GET /health` reports Mini readiness. To enable domain verification, set `OPENAI_APPS_CHALLENGE` to the value supplied by the platform; the server serves it at `/.well-known/openai-apps-challenge`. Leave it unset to return 404. Do not log or commit the value. The served value must match the platform's expected token exactly — byte for byte, plain text, with nothing added — or verification fails. Domain verification is required before the platform will accept a submission. In the platform portal, the verification token and the Verify control are in the MCP server's Connect drawer.

The MCP endpoint is intended for server-to-server clients such as ChatGPT. Its origin allowlist rejects unapproved `Origin` headers, but it does **not** enable cross-origin browser access: it returns 405 for `OPTIONS` and does not send CORS headers. The included recovery page is served from the same origin as its API. Do not add a wildcard to the allowlist. Set `MINI_ICON_URL` to your own HTTPS-hosted 192×192 PNG if you want discovery to advertise an icon; otherwise the icon is omitted. Put the service behind HTTPS and configure suitable ingress, request limits, and monitoring for your environment. Behind a reverse proxy, configure client-IP handling carefully: an untrusted forwarded header must not become the quota identity, and a shared proxy address can cause clients to share a quota.

### Optional recovery page

The page at `/frontend_v1/mini-recovery.html` can link and recover Mini campaigns using a verified Firebase account. Enable the desired Firebase sign-in provider, authorize your domain, and set these **public Firebase web configuration** values for the backend:

- `MINI_FIREBASE_WEB_API_KEY`
- `MINI_FIREBASE_AUTH_DOMAIN`
- `MINI_FIREBASE_PROJECT_ID`

These are client-side Firebase web settings, not a service-account private key. Authentication tokens and service credentials must remain private. If any setting is missing, the page's configuration endpoint returns 503. Review Firebase security rules, permissions, allowed domains, and recovery behavior before exposing your deployment.

After recovering a campaign, save the new private capability and select **I saved my new private capability**. Until you confirm it, normal removal of recovery links is blocked. If a response is lost, keep recovery enabled and recover the campaign again. You can still explicitly remove recovery without confirming, but the page warns that doing so may permanently lose access.

## Tests and verification limits

```sh
cd worldai-mini/backend
pip install pytest
python -m pytest tests mvp_site/tests -q
node --test mvp_site/frontend_v1/tests/mini_recovery_auth_race.test.cjs
```

The included tests use synthetic data and an in-memory store; they check Mini's HTTP protocol, create/save/read/dice/export behavior, recovery logic, and browser account-change safeguards. They do **not** prove that a particular Firebase project, live ChatGPT integration, deployed service, or reviewer walkthrough is configured correctly. Test those separately in your own dedicated environment before relying on a deployment.

A resume key grants access to its Mini campaign. Treat it like a password and never include one in logs, public issues, examples, or screenshots.
