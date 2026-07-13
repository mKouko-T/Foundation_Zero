import os
import hashlib
import json
from pathlib import Path
from datetime import datetime

# Define Root Directories
BASE_DIR = Path("C:/Users/maged.ibrahim/Desktop/my/Me/Foundation_Zero")
LEGACY_ROOTS = [
    BASE_DIR / "Research",
    BASE_DIR / "Projects",
    BASE_DIR / "Governance",
    BASE_DIR / "Archive",
    BASE_DIR / "Cemetery"
]

MANIFEST_OUTPUT = BASE_DIR / "docs" / "migration" / "migration_manifest.json"

def calculate_identity_hash(filepath: Path) -> str:
    """Calculates the cryptographic hash (WHO) of a file's contents."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def extract_facets(filepath: Path, base_root: Path):
    """
    Determines the Epistemic and Operational Facets (WHAT) based on legacy paths/names.
    This is Level 2 Ontology logic applied to Legacy artifacts.
    """
    epistemic_facet = "UNCLASSIFIED"
    operational_facet = "Legacy_Artifact"
    
    filename = filepath.stem.lower()
    parent_dir = filepath.parent.name.lower()
    
    if base_root.name == "Research":
        operational_facet = "Research_Artifact"
        if "hypothesis" in filename:
            epistemic_facet = "Hypothesis"
        elif "observation" in filename:
            epistemic_facet = "Observation"
        elif "evidence" in filename:
            epistemic_facet = "Evidence"
        elif "assertion" in filename:
            epistemic_facet = "Assertion"
        else:
            epistemic_facet = "Concept"
            
    elif base_root.name == "Projects":
        operational_facet = "Project_Artifact"
        if "spec" in filename or "plan" in filename:
            epistemic_facet = "Specification"
            
    elif base_root.name == "Governance":
        operational_facet = "Governance_Artifact"
        if "decision" in filename:
            epistemic_facet = "Decision"
        elif "protocol" in filename:
            epistemic_facet = "Protocol"
            
    return epistemic_facet, operational_facet

def determine_target_path(filepath: Path, base_root: Path) -> Path:
    """Determines the new physical location based on Level 3 Implementation constraints."""
    rel_path = filepath.relative_to(base_root)
    
    if base_root.name == "Research":
        return BASE_DIR / "knowledge" / "graph" / rel_path
    elif base_root.name == "Projects":
        return BASE_DIR / "archive" / "Legacy_Projects" / rel_path
    elif base_root.name == "Governance":
        return BASE_DIR / "archive" / "Legacy_Governance" / rel_path
    elif base_root.name in ["Archive", "Cemetery"]:
        return BASE_DIR / "archive" / base_root.name / rel_path
    
    return BASE_DIR / "archive" / "UNMAPPED" / rel_path

def generate_dry_run_manifest():
    manifest = []
    
    for root in LEGACY_ROOTS:
        if not root.exists():
            print(f"Skipping {root.name} - Directory not found.")
            continue
            
        for filepath in root.rglob("*"):
            if filepath.is_file():
                # Calculate universal identity
                identity_hash = calculate_identity_hash(filepath)
                
                # Determine semantics (Level 2)
                epistemic_facet, operational_facet = extract_facets(filepath, root)
                
                # Determine target (Level 3)
                target_path = determine_target_path(filepath, root)
                
                manifest.append({
                    "identity_hash": identity_hash,
                    "original_path": str(filepath.relative_to(BASE_DIR)).replace("\\", "/"),
                    "target_path": str(target_path.relative_to(BASE_DIR)).replace("\\", "/"),
                    "epistemic_facet": epistemic_facet,
                    "operational_facet": operational_facet,
                    "migration_action": "COPY",
                    "status": "PENDING",
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                })
                
    # Ensure output directory exists
    MANIFEST_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    with open(MANIFEST_OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"Dry run complete. Manifest generated with {len(manifest)} entries.")
    print(f"Location: {MANIFEST_OUTPUT}")

if __name__ == "__main__":
    generate_dry_run_manifest()
