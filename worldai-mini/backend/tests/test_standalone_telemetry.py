"""Standalone telemetry must emit bounded metadata by default."""

from unittest.mock import patch

from mvp_site.mini_mcp import emit


def test_standalone_telemetry_records_metadata_without_missing_sink():
    event = {"source": "mini", "outcome": "ok"}
    with patch("mvp_site.mini_mcp.LOG.info") as info:
        emit(event)
    assert info.call_args.args[0] == "mini_request_outcome %s"
    assert info.call_args.kwargs["extra"]["json_fields"]["mini"] == event


def test_documented_startup_emits_metadata_without_logging_overrides():
    import subprocess
    import sys
    from pathlib import Path

    backend = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import server; from mvp_site.mini_mcp import emit; emit({'source':'mini','outcome':'ok','status':200})",
        ],
        cwd=backend,
        text=True,
        capture_output=True,
        check=True,
    )
    output = result.stdout + result.stderr
    assert "mini_request_outcome" in output
    assert "outcome" in output and "200" in output
