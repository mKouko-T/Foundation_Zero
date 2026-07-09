import subprocess
import sys
import os
import json

def run_doctor():
    print("Foundation Zero Doctor")
    print("----------------------")
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # Check Schemas
    schema_dir = os.path.join(repo_dir, "schemas")
    schemas_pass = os.path.exists(schema_dir) and any(f.endswith(".schema.json") for f in os.listdir(schema_dir))
    print(f"[{'PASS' if schemas_pass else 'FAIL'}] Schemas Validation")
    
    # Check Manifest
    manifest_path = os.path.join(repo_dir, "REPOSITORY_MANIFEST.json")
    manifest_pass = os.path.exists(manifest_path)
    print(f"[{'PASS' if manifest_pass else 'FAIL'}] Manifest Verification")
    
    # Check Invariants using pytest
    try:
        subprocess.check_output([sys.executable, "-m", "pytest", os.path.join(repo_dir, "tests", "test_repository_invariants.py")])
        invariants_pass = True
    except subprocess.CalledProcessError:
        invariants_pass = False
    except FileNotFoundError:
        invariants_pass = False
        
    print(f"[{'PASS' if invariants_pass else 'FAIL'}] Repository Invariants")
    
    if schemas_pass and manifest_pass and invariants_pass:
        print("\nResult: Repository Healthy")
        return 0
    else:
        print("\nResult: Repository Unhealthy")
        return 1

if __name__ == "__main__":
    sys.exit(run_doctor())
