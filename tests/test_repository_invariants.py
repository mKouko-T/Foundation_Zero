import os
import json

def test_invariant_001_schemas_have_versions():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    schema_dir = os.path.join(repo_root, "schemas")
    for s in os.listdir(schema_dir):
        if s.endswith(".schema.json"):
            with open(os.path.join(schema_dir, s), "r") as f:
                schema = json.load(f)
                assert "schema_version" in schema.get("properties", {}), f"{s} missing schema_version"

def test_invariant_002_project_state_exists():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    state_path = os.path.join(repo_root, "docs", "PROJECT_STATE.md")
    assert os.path.isfile(state_path), "PROJECT_STATE.md must exist in docs/"
