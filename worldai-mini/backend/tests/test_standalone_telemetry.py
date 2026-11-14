"""Standalone telemetry must not rely on the full application's BigQuery sink."""

import logging

from mvp_site.mini_mcp import emit


def test_standalone_telemetry_records_metadata_without_missing_sink(caplog):
    with caplog.at_level(logging.INFO):
        emit({"source": "mini", "outcome": "ok"})
    assert any(record.message == "mini_request_outcome" for record in caplog.records)
    assert "mini_telemetry_dropped" not in caplog.text
