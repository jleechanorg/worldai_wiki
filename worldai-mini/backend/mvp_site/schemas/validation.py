"""Load the Mini JSON schema without the full WorldAI schema subsystem."""

import json
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=None)
def load_schema(schema_name):
    schema_path = Path(__file__).parent / f"{schema_name}.schema.json"
    with schema_path.open(encoding="utf-8") as source:
        return json.load(source)
