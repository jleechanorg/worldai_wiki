import server


def test_standalone_server_exposes_app_factory():
    assert callable(getattr(server, "create_app", None)), (
        "standalone app factory is required"
    )


def test_recovery_frontend_and_public_config_are_served(monkeypatch):
    monkeypatch.setenv("MINI_FIREBASE_WEB_API_KEY", "example-public-key")
    monkeypatch.setenv("MINI_FIREBASE_AUTH_DOMAIN", "example.test")
    monkeypatch.setenv("MINI_FIREBASE_PROJECT_ID", "example-project")
    client = server.create_app(lambda: None).test_client()
    assert client.get("/frontend_v1/mini-recovery.html").status_code == 200
    config = client.get("/frontend_v1/firebase-config.js")
    assert config.status_code == 200
    assert b"example-project" in config.data
    assert client.get("/frontend_v1/auth.js").status_code == 200
