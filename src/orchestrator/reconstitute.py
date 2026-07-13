import os
import json
from pathlib import Path
from datetime import datetime, timezone
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from identity import ContentHashIdentityProvider

BASE_DIR = Path("C:/Users/maged.ibrahim/Desktop/my/Me/Foundation_Zero")
LEGACY_ROOTS = [
    BASE_DIR / "Research",
    BASE_DIR / "Projects",
    BASE_DIR / "Governance",
    BASE_DIR / "Archive",
    BASE_DIR / "Cemetery"
]

MANIFEST_OUTPUT = BASE_DIR / "docs" / "migration" / "reconstitution_manifest.json"
SUMMARY_OUTPUT = BASE_DIR / "docs" / "migration" / "Reconstitution_Summary.md"

def generate_inventory():
    """
    Phase 1-4 of Reconstitution: Discover -> Fingerprint -> Identity -> Inventory
    Note: Classification happens post-migration.
    """
    provider = ContentHashIdentityProvider()
    manifest = []
    stats = {
        "files_scanned": 0,
        "hash_duplicates": 0,
        "unknown_ontology": 0
    }
    seen_hashes = set()
    
    for root in LEGACY_ROOTS:
        if not root.exists():
            continue
            
        for filepath in root.rglob("*"):
            if filepath.is_file():
                stats["files_scanned"] += 1
                
                # Phase 2 & 3: Fingerprint & Identity Assignment
                identity = provider.generate_identity(filepath)
                
                # Detect duplicates (based on identity, which is derived from content hash)
                if identity in seen_hashes:
                    stats["hash_duplicates"] += 1
                seen_hashes.add(identity)
                
                # Phase 4: Inventory
                # We place all raw legacy files in a holding pattern (UNMAPPED) 
                # because Migration is Physical. Classification happens later.
                rel_path = filepath.relative_to(BASE_DIR)
                target_path = BASE_DIR / "archive" / "UNMAPPED" / rel_path
                
                stats["unknown_ontology"] += 1
                
                record = {
                    "identity": identity,
                    "original_locator": str(rel_path).replace("\\", "/"),
                    "target_locator": str(target_path.relative_to(BASE_DIR)).replace("\\", "/"),
                    "epistemic_facet": "UNKNOWN",
                    "operational_facet": "UNKNOWN",
                    "status": "PLANNED",
                    "justification": {
                        "reason": "Physical discovery. Ontology classification deferred.",
                        "matched_rule": "Fallback_Inventory",
                        "confidence": 1.0,
                        "classifier_version": "v1.0"
                    },
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
                manifest.append(record)
                
    MANIFEST_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
        
    # Generate Statistics
    with open(SUMMARY_OUTPUT, "w") as f:
        f.write("# Reconstitution Summary\n\n")
        f.write(f"- **Files Scanned**: {stats['files_scanned']}\n")
        f.write(f"- **Hash Duplicates**: {stats['hash_duplicates']}\n")
        f.write(f"- **Unknown Ontology**: {stats['unknown_ontology']}\n")
        f.write(f"\nManifest written to: `{MANIFEST_OUTPUT.relative_to(BASE_DIR)}`\n")
        
    print(f"Inventory complete. Scanned {stats['files_scanned']} files.")

import shutil

def execute_reconstitution():
    """
    Phase 5 & 6 of Reconstitution: Copy -> Verify
    """
    if not MANIFEST_OUTPUT.exists():
        print("No manifest found to execute.")
        return
        
    with open(MANIFEST_OUTPUT, "r") as f:
        manifest = json.load(f)
        
    execution_events = []
    executed_count = 0
    
    for record in manifest:
        if record.get("status") == "PLANNED":
            orig_path = BASE_DIR / record["original_locator"]
            targ_path = BASE_DIR / record["target_locator"]
            
            if orig_path.exists():
                # Phase 5: Copy (Physical Migration)
                targ_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(orig_path, targ_path)
                
                # Phase 6: Verify (Hashing target to ensure Information Conservation)
                provider = ContentHashIdentityProvider()
                orig_id = provider.generate_identity(orig_path)
                targ_id = provider.generate_identity(targ_path)
                
                if orig_id == targ_id:
                    # Append-Only execution record
                    executed_event = record.copy()
                    executed_event["status"] = "EXECUTED"
                    executed_event["timestamp"] = datetime.now(timezone.utc).isoformat()
                    executed_event["justification"] = {
                        "reason": "Physical copy verified against cryptographic hash.",
                        "matched_rule": "Information_Conservation",
                        "confidence": 1.0,
                        "classifier_version": "v1.0"
                    }
                    execution_events.append(executed_event)
                    executed_count += 1
                else:
                    print(f"Verification failed for {orig_path}")
                    
    # Append execution events to manifest
    manifest.extend(execution_events)
    with open(MANIFEST_OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
        
    # Freeze legacy directories
    frozen_dir = BASE_DIR / "legacy_frozen"
    frozen_dir.mkdir(parents=True, exist_ok=True)
    for root in LEGACY_ROOTS:
        if root.exists():
            shutil.move(str(root), str(frozen_dir / root.name))
            
    print(f"Execution complete. Successfully migrated and verified {executed_count} files. Legacy directories frozen.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        execute_reconstitution()
    else:
        generate_inventory()

