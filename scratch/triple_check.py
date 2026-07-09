import os
import json
import jsonschema

REPO_DIR = r"C:\Users\maged.ibrahim\Desktop\my\Me\Foundation_Zero"

def check():
    print("--- Triple Check Audit ---")
    schemas_dir = os.path.join(REPO_DIR, "schemas")
    
    missing_schemas = []
    if not os.path.exists(os.path.join(schemas_dir, "bios.schema.json")):
        missing_schemas.append("bios.schema.json")
    if not os.path.exists(os.path.join(schemas_dir, "capability.schema.json")):
        missing_schemas.append("capability.schema.json")
        
    if missing_schemas:
        print("FAIL: Missing schemas for new JSON files:", missing_schemas)
    else:
        print("PASS: All schemas exist.")

if __name__ == "__main__":
    check()
