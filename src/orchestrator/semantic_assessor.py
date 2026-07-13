import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import sys

BASE_DIR = Path("C:/Users/maged.ibrahim/Desktop/my/Me/Foundation_Zero")
MANIFEST_PATH = BASE_DIR / "docs" / "migration" / "reconstitution_manifest.json"
ONTOLOGY_PATH = BASE_DIR / "docs" / "ontology" / "domain" / "KNOWLEDGE_ONTOLOGY.json"
SUMMARY_OUTPUT = BASE_DIR / "docs" / "migration" / "Attribution_Summary.md"

def load_ontology():
    with open(ONTOLOGY_PATH, "r") as f:
        content = f.read()
    hasher = hashlib.sha256(content.encode("utf-8"))
    return json.loads(content), hasher.hexdigest()

def assess_artifact(identity, locator, ontology, ontology_hash):
    """
    Evaluates evidence to generate an additive Assessment Record.
    """
    evidence_list = []
    
    # Evidence 1: Legacy Locator
    ev_id = f"EV-{uuid.uuid4()}"
    evidence_list.append({
        "action": "EVIDENCE_RECORD",
        "evidence_id": ev_id,
        "target_identity": identity,
        "evidence_type": "legacy_locator",
        "content": {"path": locator},
        "timestamp": datetime.now(timezone.utc).isoformat()
    })
    
    locator_lower = locator.lower()
    epistemic_facet = "UNKNOWN_INSUFFICIENT_EVIDENCE"
    operational_facet = "UNKNOWN_INSUFFICIENT_EVIDENCE"
    confidence = 0.0
    rejected = {}
    
    epistemic_types = ontology["facets"]["epistemic"]
    
    # Heuristic Rule Engine
    if "hypothesis" in locator_lower:
        epistemic_facet = "Hypothesis"
        confidence = 0.85
        rejected = {t: 0.1 for t in epistemic_types if t != "Hypothesis"}
    elif "first_principles" in locator_lower or "science_of_organizations" in locator_lower:
        epistemic_facet = "First_Principle"
        confidence = 0.90
        rejected = {t: 0.05 for t in epistemic_types if t != "First_Principle"}
    elif "glossary" in locator_lower:
        # Intentional weak mapping to trigger REVIEW_REQUIRED
        epistemic_facet = "Observation"
        confidence = 0.40
        rejected = {"Hypothesis": 0.2, "First_Principle": 0.1}
        
    if "projects" in locator_lower:
        operational_facet = "Project"
        
    # Thresholding: If we are guessing with low confidence, demand human review
    if confidence > 0.0 and confidence < 0.5:
        epistemic_facet = "REVIEW_REQUIRED"
        
    assessment_id = f"AS-{uuid.uuid4()}"
    
    classifier_info = {
        "version": "v1.0",
        "ontology_document": str(ONTOLOGY_PATH.relative_to(BASE_DIR)).replace("\\", "/"),
        "ontology_hash": ontology_hash,
        "ontology_version": ontology["ontology_version"],
        "confidence": confidence,
        "confidence_method": "heuristic_legacy_locator",
        "confidence_scale": "0.0-1.0",
        "operator": "Automatic",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
    assessment = {
        "action": "SEMANTIC_ATTRIBUTION",
        "assessment_id": assessment_id,
        "target_identity": identity,
        "epistemic_facet": epistemic_facet,
        "operational_facet": operational_facet,
        "recovery_basis": "R-001",
        "evidence_ids": [ev["evidence_id"] for ev in evidence_list],
        "rejected_candidates": rejected,
        "classifier": classifier_info
    }
    
    return evidence_list, assessment

def run_assessor():
    ontology, ontology_hash = load_ontology()
    
    if not MANIFEST_PATH.exists():
        print("Manifest not found.")
        return
        
    with open(MANIFEST_PATH, "r") as f:
        manifest = json.load(f)
        
    # Discover unassessed identities
    identities_to_assess = {}
    for record in manifest:
        if record.get("status") in ["EXECUTED", "PLANNED"]:
            identities_to_assess[record["identity"]] = record.get("original_locator", "")
            
    for record in manifest:
        if record.get("action") == "SEMANTIC_ATTRIBUTION":
            if record["target_identity"] in identities_to_assess:
                del identities_to_assess[record["target_identity"]]
                
    if not identities_to_assess:
        print("No unassessed identities found.")
        return
        
    new_records = []
    stats = {"total": 0, "facets": {}}
    
    for identity, locator in identities_to_assess.items():
        evidence, assessment = assess_artifact(identity, locator, ontology, ontology_hash)
        
        new_records.extend(evidence)
        new_records.append(assessment)
        
        stats["total"] += 1
        epi = assessment["epistemic_facet"]
        stats["facets"][epi] = stats["facets"].get(epi, 0) + 1
        
    manifest.extend(new_records)
    
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
        
    with open(SUMMARY_OUTPUT, "w") as f:
        f.write("# Semantic Attribution Summary\n\n")
        f.write(f"- **Total Assessed**: {stats['total']}\n\n")
        f.write("### Epistemic Distribution\n")
        for k, v in sorted(stats["facets"].items(), key=lambda x: x[1], reverse=True):
            f.write(f"- **{k}**: {v}\n")
            
    print(f"Assessed {stats['total']} artifacts. Manifest appended.")

if __name__ == "__main__":
    run_assessor()
