import uuid
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from schemas import AssessmentRecord, ClassifierInfo, ObservationRecord

class AssessorWorker:
    """
    Stage B: The Assessor
    Evaluates Observations against the loaded Domain Ontology.
    """
    def __init__(self, ontology_path: Path):
        with open(ontology_path, "r") as f:
            content = f.read()
            self.ontology = json.loads(content)
            import hashlib
            self.ontology_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
            self.ontology_path = str(ontology_path).replace("\\", "/")
            
    def assess(self, observation: ObservationRecord, epistemic_facet: str, confidence: float, rejected: dict) -> AssessmentRecord:
        classifier = ClassifierInfo(
            version="v1.0",
            ontology_document=self.ontology_path,
            ontology_hash=self.ontology_hash,
            ontology_version=self.ontology.get("ontology_version", "unknown"),
            confidence_method="heuristic_span_evaluation",
            confidence_scale="0.0-1.0",
            operator="AssessorWorker",
            timestamp=datetime.now(timezone.utc).isoformat()
        )
        
        return AssessmentRecord(
            assessment_id=f"AS-{uuid.uuid4()}",
            target_observation_id=observation.observation_id,
            epistemic_facet=epistemic_facet,
            operational_facet="UNKNOWN_OUTSIDE_ONTOLOGY",
            ontology_confidence=confidence,
            rejected_candidates=rejected,
            classifier=classifier
        )
