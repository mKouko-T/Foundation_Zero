import subprocess
import sys
import os
import json
import jsonschema

def validate_json_file(filepath, schema_path):
    if not os.path.exists(filepath) or not os.path.exists(schema_path):
        return False
    with open(filepath, 'r') as f:
        instance = json.load(f)
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=instance, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False

def run_doctor():
    print("Foundation Zero Doctor")
    print("----------------------")
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # 1. Schemas Validation
    schema_dir = os.path.join(repo_dir, "schemas")
    schemas_pass = os.path.exists(schema_dir) and any(f.endswith(".schema.json") for f in os.listdir(schema_dir))
    print(f"[{'PASS' if schemas_pass else 'FAIL'}] Schemas Integrity")
    
    # 2. BIOS Verification
    manifest_path = os.path.join(repo_dir, "REPOSITORY_BIOS.json")
    manifest_pass = os.path.exists(manifest_path)
    print(f"[{'PASS' if manifest_pass else 'FAIL'}] BIOS Verification")
    
    # 3. Repository Contract Validation
    contract_pass = validate_json_file(
        os.path.join(repo_dir, "REPOSITORY_CONTRACT.json"),
        os.path.join(repo_dir, "schemas", "contract.schema.json")
    )
    print(f"[{'PASS' if contract_pass else 'FAIL'}] Repository Contract Validation")

    # 4. Invariants using pytest
    try:
        subprocess.check_output([sys.executable, "-m", "pytest", os.path.join(repo_dir, "tests", "test_repository_invariants.py")])
        invariants_pass = True
    except subprocess.CalledProcessError:
        invariants_pass = False
    except FileNotFoundError:
        invariants_pass = False
        
    print(f"[{'PASS' if invariants_pass else 'FAIL'}] Repository Invariants")
    
    if schemas_pass and manifest_pass and invariants_pass and contract_pass:
        print("\nResult: Repository Healthy")
        return 0
    else:
        print("\nResult: Repository Unhealthy")
        return 1

if __name__ == "__main__":
    sys.exit(run_doctor())
