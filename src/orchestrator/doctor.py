import subprocess
import sys
import os
import json
import jsonschema

def validate_json_file(filepath, schema_path):
    if not os.path.exists(filepath) or not os.path.exists(schema_path):
        return False
    with open(filepath, 'r', encoding='utf-8') as f:
        instance = json.load(f)
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=instance, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation Error in {filepath}: {e.message}")
        return False

def run_doctor():
    print("Foundation Zero Doctor")
    print("----------------------")
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # 1. Schemas Validation (Are all instances matching their schemas?)
    validations = [
        ("REPOSITORY_CONTRACT.json", "schemas/contract.schema.json"),
        ("REPOSITORY_BIOS.json", "schemas/bios.schema.json"),
        ("docs/PROJECT_STATE.json", "schemas/project_state.schema.json")
    ]
    
    caps_dir = os.path.join(repo_dir, "capabilities")
    if os.path.exists(caps_dir):
        for f in os.listdir(caps_dir):
            if f.endswith(".json"):
                validations.append((f"capabilities/{f}", "schemas/capability.schema.json"))
                
    schemas_pass = True
    for instance, schema in validations:
        if not validate_json_file(os.path.join(repo_dir, instance), os.path.join(repo_dir, schema)):
            schemas_pass = False
            
    print(f"[{'PASS' if schemas_pass else 'FAIL'}] Schema Validations")
    
    # 2. Invariants using pytest
    try:
        subprocess.check_output([sys.executable, "-m", "pytest", os.path.join(repo_dir, "tests", "test_repository_invariants.py")])
        invariants_pass = True
    except subprocess.CalledProcessError:
        invariants_pass = False
    except FileNotFoundError:
        invariants_pass = False
        
    print(f"[{'PASS' if invariants_pass else 'FAIL'}] Repository Invariants")
    
    if schemas_pass and invariants_pass:
        print("\nResult: Repository Healthy")
        return 0
    else:
        print("\nResult: Repository Unhealthy")
        return 1

if __name__ == "__main__":
    sys.exit(run_doctor())
