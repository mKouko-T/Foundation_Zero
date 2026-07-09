import os
import json
import subprocess
import hashlib
import datetime

REPO_DIR = r"C:\Users\maged.ibrahim\Desktop\my\Me\Foundation_Zero"

def write_file(path, content):
    full_path = os.path.join(REPO_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

def write_json(path, data):
    full_path = os.path.join(REPO_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# 1. Update Lifecycle Policy to include SemVer
lifecycle_policy = """# Lifecycle Policy

Evolution occurs at different speeds. The following phases apply independently to the Repository, Protocol, Specification, Ledger, Schemas, and Knowledge:

## Semantic Versioning (SemVer)
All core specifications (FZS, Protocol, Schemas) strictly adhere to `MAJOR.MINOR.PATCH`:
- **MAJOR**: Incompatible or breaking structural changes (e.g., removing a required schema field). Requires a formalized Migration path.
- **MINOR**: Backwards-compatible additions (e.g., adding an optional field to a ledger).
- **PATCH**: Non-structural corrections (e.g., typos in documentation, clarifications).

## Lifecycle Phases
1. **Experimental**: Active development. Breaking changes permitted without warning.
2. **Supported / Pilot**: In production use. Bugfixes and compatible additions only.
3. **Deprecated**: Marked for removal. Migration path must be provided.
4. **Frozen**: Read-only. Security patches only.
5. **Archived**: Moved out of active source.
6. **Removed**: Deleted from tree (requires ADR).
"""
write_file("constitution/laws/LIFECYCLE_POLICY.md", lifecycle_policy)

# 2. Update PROJECT_STATE schema for SMART Health
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
        "tests_passing": {"type": "boolean"},
        "staleness_days": {"type": "integer"},
        "adrs_accumulated": {"type": "integer"},
        "maintenance_recommended": {"type": "boolean"}
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

# 3. Update state_compiler.py to actually compute SMART health
state_compiler_script = """import os
import json
import datetime
import hashlib
import subprocess

def get_git_commit(repo_dir):
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo_dir).decode('utf-8').strip()
    except Exception:
        return "Unknown"

def hash_file(filepath):
    if not os.path.exists(filepath): return "Missing"
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def compile_state(repo_dir):
    bios_path = os.path.join(repo_dir, "REPOSITORY_BIOS.json")
    bios_hash = hash_file(bios_path)
    commit = get_git_commit(repo_dir)
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    
    # Capabilities
    caps_dir = os.path.join(repo_dir, "capabilities")
    caps = {}
    if os.path.exists(caps_dir):
        for f in os.listdir(caps_dir):
            if f.endswith(".json"):
                with open(os.path.join(caps_dir, f), "r") as cf:
                    data = json.load(cf)
                    caps[data.get("capability", "Unknown")] = data.get("status", "Unknown")
    
    # SMART Repository Health / Self-Awareness
    try:
        subprocess.check_output([sys.executable, "-m", "pytest", os.path.join(repo_dir, "tests")], stderr=subprocess.STDOUT)
        tests_passing = True
    except subprocess.CalledProcessError:
        tests_passing = False
    except FileNotFoundError:
        tests_passing = False

    try:
        last_commit_date_str = subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--date=iso-strict'], cwd=repo_dir).decode('utf-8').strip()
        last_commit_date = datetime.datetime.fromisoformat(last_commit_date_str.replace('Z', '+00:00'))
        staleness_days = (datetime.datetime.now(datetime.timezone.utc) - last_commit_date).days
    except Exception:
        staleness_days = 0

    adr_dir = os.path.join(repo_dir, "constitution", "adr")
    adrs_accumulated = len([f for f in os.listdir(adr_dir) if f.endswith(".md")]) if os.path.exists(adr_dir) else 0

    maintenance_recommended = not tests_passing or staleness_days > 30 or adrs_accumulated > 20

    state_json = {
        "schema_version": "1.0",
        "provenance": {
            "generated_by": "StateCompiler v1.3",
            "timestamp": timestamp,
            "bios_hash": bios_hash,
            "commit": commit
        },
        "capabilities": caps,
        "health": {
            "tests_passing": tests_passing,
            "staleness_days": staleness_days,
            "adrs_accumulated": adrs_accumulated,
            "maintenance_recommended": maintenance_recommended
        }
    }
    
    json_path = os.path.join(repo_dir, "docs", "PROJECT_STATE.json")
    md_path = os.path.join(repo_dir, "docs", "PROJECT_STATE.md")
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(state_json, f, indent=2)
        
    md_content = f\"\"\"# Project State
*Automatically compiled by StateCompiler. Do not edit.*

## Provenance
- **Generated By:** {state_json['provenance']['generated_by']}
- **Timestamp:** {state_json['provenance']['timestamp']}
- **BIOS Hash:** {state_json['provenance']['bios_hash']}
- **Commit:** {state_json['provenance']['commit']}

## Capabilities Matrix
| Capability | Status |
|------------|--------|
\"\"\"
    for cap, status in caps.items():
        md_content += f"| {cap} | {status} |\\n"
        
    md_content += f\"\"\"
## Repository Health (SMART)
- **Tests Passing:** {'Yes' if tests_passing else 'No'}
- **Staleness:** {staleness_days} days since last commit
- **ADRs Accumulated:** {adrs_accumulated}
- **Maintenance Recommended:** {'Yes' if maintenance_recommended else 'No'}
\"\"\"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print("PROJECT_STATE.json and PROJECT_STATE.md successfully compiled.")

if __name__ == "__main__":
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    compile_state(repo_dir)
"""
write_file("src/orchestrator/state_compiler.py", state_compiler_script)

# 4. Update certify.py to hash schemas and capabilities as well
certify_script = """import subprocess
import sys
import os
import datetime
import hashlib
import json

def get_git_commit(repo_dir):
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo_dir).decode('utf-8').strip()
    except Exception:
        return "Unknown"

def hash_file(filepath):
    if not os.path.exists(filepath): return "Missing"
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def hash_directory(dirpath):
    if not os.path.exists(dirpath): return "Missing"
    hasher = hashlib.sha256()
    for root, _, files in os.walk(dirpath):
        for names in sorted(files):
            filepath = os.path.join(root, names)
            with open(filepath, 'rb') as f:
                hasher.update(f.read())
    return hasher.hexdigest()

def run_certify():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    print("Initiating Foundation Certification...")
    
    # 1. Run Doctor
    doctor_script = os.path.join(repo_dir, "src", "orchestrator", "doctor.py")
    if subprocess.call([sys.executable, doctor_script]) != 0:
        print("CERTIFICATION FAILED: Diagnostics did not pass.")
        sys.exit(1)
        
    # 2. Hash States
    bios_hash = hash_file(os.path.join(repo_dir, "REPOSITORY_BIOS.json"))
    state_json_hash = hash_file(os.path.join(repo_dir, "docs", "PROJECT_STATE.json"))
    schema_hash = hash_directory(os.path.join(repo_dir, "schemas"))
    capability_hash = hash_directory(os.path.join(repo_dir, "capabilities"))
    
    commit = get_git_commit(repo_dir)
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    
    report_content = f\"\"\"# Repository Certification Report

**Repository is certified for production operations and knowledge migration.**

- **Timestamp:** {timestamp}
- **Commit:** {commit}
- **BIOS Hash:** {bios_hash}
- **State JSON Hash:** {state_json_hash}
- **Schema Directory Hash:** {schema_hash}
- **Capability Directory Hash:** {capability_hash}
- **Generator:** certify.py v1.1
\"\"\"
    report_path = os.path.join(repo_dir, "Repository_Certification_Report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print("CERTIFICATION SUCCESS: Repository_Certification_Report.md generated.")

if __name__ == "__main__":
    run_certify()
"""
write_file("src/orchestrator/certify.py", certify_script)

print("Another round completed successfully.")
