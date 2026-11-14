"""Standalone Flask entry point for the Mini MCP and recovery routes."""

import json
import os
from pathlib import Path

from flask import Flask, Response, abort, jsonify, send_from_directory

from mvp_site.mini_mcp import register_routes


def firestore_store():
    """Use the deployment's configured Firebase application credentials lazily."""
    import firebase_admin
    from firebase_admin import firestore
    from mvp_site.mini_storage import FirestoreStore

    try:
        app = firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app()
    return FirestoreStore(firestore.client(app=app))


def create_app(store_factory=None):
    app = Flask(__name__)
    register_routes(app, store_factory or firestore_store)
    frontend = Path(__file__).parent / "mvp_site" / "frontend_v1"

    @app.get("/health")
    def health():
        return jsonify(
            {"service": "worldai-mini", "mini": app.extensions["mini_readiness"]()}
        )

    @app.get("/.well-known/openai-apps-challenge")
    def openai_apps_challenge():
        challenge = os.getenv("OPENAI_APPS_CHALLENGE", "")
        if not challenge:
            return Response(status=404)
        result = Response(challenge, mimetype="text/plain")
        result.headers["Cache-Control"] = "no-store"
        return result

    @app.get("/frontend_v1/firebase-config.js")
    def firebase_web_config():
        config = {
            "apiKey": os.getenv("MINI_FIREBASE_WEB_API_KEY", ""),
            "authDomain": os.getenv("MINI_FIREBASE_AUTH_DOMAIN", ""),
            "projectId": os.getenv("MINI_FIREBASE_PROJECT_ID", ""),
        }
        if not all(config.values()):
            return Response(status=503)
        result = Response(
            "window.MINI_FIREBASE_CONFIG = " + json.dumps(config) + ";\n",
            mimetype="application/javascript",
        )
        result.headers["Cache-Control"] = "no-store"
        return result

    @app.get("/frontend_v1/<path:filename>")
    def mini_frontend(filename):
        if filename not in {"mini-recovery.html", "mini-recovery.js", "auth.js"}:
            abort(404)
        return send_from_directory(frontend, filename)

    return app


app = create_app()
