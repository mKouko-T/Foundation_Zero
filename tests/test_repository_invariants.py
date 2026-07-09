import os

def test_required_directories():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    required_dirs = [
        "docs", "constitution", "schemas", 
        "knowledge", "archive", "src", "tests"
    ]
    for d in required_dirs:
        assert os.path.isdir(os.path.join(repo_root, d)), f"Missing required directory: {d}"

def test_required_schemas():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    required_schemas = [
        "ledger.schema.json", 
        "project_state.schema.json", 
        "adr.schema.json"
    ]
    for s in required_schemas:
        assert os.path.isfile(os.path.join(repo_root, "schemas", s)), f"Missing schema: {s}"

def test_project_state_exists():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    state_path = os.path.join(repo_root, "docs", "PROJECT_STATE.md")
    assert os.path.isfile(state_path), "PROJECT_STATE.md must exist in docs/"
