import os
import json
import subprocess

REPO_DIR = r"C:\Users\maged.ibrahim\Desktop\my\Me\Foundation_Zero"

def write_json(path, data):
    full_path = os.path.join(REPO_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def read_json(path):
    full_path = os.path.join(REPO_DIR, path)
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 1. Update project_state.schema.json to match reality
project_state_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Project State",
  "type": "object",
  "properties": {
    "schema_version": {"type": "string"},
    "provenance": {
      "type": "object",
      "properties": {
        "generated_by": {"type": "string"},
        "timestamp": {"type": "string"},
        "bios_hash": {"type": "string"},
        "commit": {"type": "string"}
      }
    },
    "health": {
      "type": "object",
      "properties": {
        "schemas": {"type": "string"},
        "ci": {"type": "string"},
        "tests": {"type": "string"},
        "adr_compliance": {"type": "string"},
        "bios": {"type": "string"}
      }
    },
    "capabilities": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "enum": ["Stable", "Pilot", "Draft", "Planned", "Not Started"]
      }
    }
  },
  "required": ["schema_version", "provenance", "health", "capabilities"]
}
write_json("schemas/project_state.schema.json", project_state_schema)

# 2. Write bios.schema.json
bios_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Repository BIOS",
  "type": "object",
  "properties": {
    "repository_identity": {"type": "string"},
    "repository_version": {"type": "string"},
    "protocol_version": {"type": "string"},
    "specification_version": {"type": "string"},
    "compatibility": {"type": "object"},
    "generation_rules": {"type": "object"},
    "boot_rules": {"type": "object"}
  },
  "required": ["repository_identity", "repository_version", "protocol_version"]
}
write_json("schemas/bios.schema.json", bios_schema)

# 3. Write capability.schema.json
capability_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Capability Definition",
  "type": "object",
  "properties": {
    "schema_version": {"type": "string"},
    "capability": {"type": "string"},
    "status": {"type": "string"},
    "owner": {"type": "string"},
    "dependencies": {"type": "array"}
  },
  "required": ["schema_version", "capability", "status", "owner", "dependencies"]
}
write_json("schemas/capability.schema.json", capability_schema)

# 4. Fix state_compiler.py to include schema_version
compiler_path = os.path.join(REPO_DIR, "src", "orchestrator", "state_compiler.py")
with open(compiler_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('"provenance":', '"schema_version": "1.0",\n        "provenance":')
with open(compiler_path, "w", encoding="utf-8") as f:
    f.write(content)

# 5. Fix doctor.py to validate ALL instances
doctor_script = """import subprocess
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
        print("\\nResult: Repository Healthy")
        return 0
    else:
        print("\\nResult: Repository Unhealthy")
        return 1

if __name__ == "__main__":
    sys.exit(run_doctor())
"""
with open(os.path.join(REPO_DIR, "src", "orchestrator", "doctor.py"), "w", encoding="utf-8") as f:
    f.write(doctor_script)

print("Fixes applied.")
