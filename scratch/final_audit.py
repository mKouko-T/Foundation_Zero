import os
import json
import jsonschema

REPO_DIR = r"C:\Users\maged.ibrahim\Desktop\my\Me\Foundation_Zero"

def audit():
    print("--- Final Audit ---")
    
    # 1. Contract
    md_contract = os.path.join(REPO_DIR, "REPOSITORY_CONTRACT.md")
    json_contract = os.path.join(REPO_DIR, "REPOSITORY_CONTRACT.json")
    if os.path.exists(md_contract) and not os.path.exists(json_contract):
        print("FAIL: REPOSITORY_CONTRACT is still purely markdown.")
    else:
        print("PASS: REPOSITORY_CONTRACT is json.")

    # 2. Hardcoded state
    compiler_path = os.path.join(REPO_DIR, "src", "orchestrator", "state_compiler.py")
    with open(compiler_path, "r") as f:
        content = f.read()
        if 'ci_pass = "PASS"' in content:
            print("FAIL: state_compiler.py has hardcoded ci_pass.")
        else:
            print("PASS: state_compiler.py does not hardcode CI.")
            
    # 3. Schema validation
    # Do we actually validate PROJECT_STATE.json against its schema anywhere?
    doctor_path = os.path.join(REPO_DIR, "src", "orchestrator", "doctor.py")
    with open(doctor_path, "r") as f:
        content = f.read()
        if "jsonschema.validate" not in content:
            print("FAIL: doctor.py does not actually use jsonschema to validate files.")
        else:
            print("PASS: doctor.py validates using jsonschema.")

if __name__ == "__main__":
    audit()
