import subprocess
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
    commit = get_git_commit(repo_dir)
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    
    report_content = f"""# Repository Certification Report

**Repository is certified for production operations and knowledge migration.**

- **Timestamp:** {timestamp}
- **Commit:** {commit}
- **BIOS Hash:** {bios_hash}
- **State JSON Hash:** {state_json_hash}
- **Generator:** certify.py v1.0
"""
    report_path = os.path.join(repo_dir, "Repository_Certification_Report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print("CERTIFICATION SUCCESS: Repository_Certification_Report.md generated.")

if __name__ == "__main__":
    run_certify()
