from typing import List, Dict, Any
from dataclasses import dataclass
from .ledger import EventStore
from .events import EpistemicEvent

@dataclass(frozen=True)
class ReplayConfiguration:
    constitution_version: str
    ontology_version: str
    canonicalization_policy_id: str
    evaluator_set_id: str

class KnowledgeGraphProjection:
    """
    Computes the ephemeral state of the Knowledge Graph purely from the Immutable Ledger.
    If this projection is destroyed, no information is lost.
    """
    def __init__(self, ledger: EventStore, config: ReplayConfiguration):
        self.ledger = ledger
        self.config = config
        self.concepts: Dict[str, Dict[str, Any]] = {}

    def compute(self):
        self.concepts.clear()
        cursor = self.ledger.cursor()
        
        # Chronological fold over the DAG
        for event in cursor:
            if event.event_type == "CanonicalConceptAccepted":
                identity = event.payload["concept_identity"]
                self.concepts[identity] = {
                    "name": event.payload["canonical_name"],
                    "status": "Accepted",
                    "assessments": event.payload.get("assessments", [])
                }
            elif event.event_type == "ConceptDeprecated":
                identity = event.payload["concept_identity"]
                if identity in self.concepts:
                    self.concepts[identity]["status"] = "Deprecated"
            elif event.event_type == "CandidateMerged":
                # Candidate assessments are moved to the Canonical target
                target = event.payload["canonical_identity"]
                if target in self.concepts:
                    self.concepts[target]["assessments"].extend(event.payload.get("assessments", []))

    def get_concept(self, identity: str) -> Dict[str, Any]:
        return self.concepts.get(identity)
