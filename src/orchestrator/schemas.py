from dataclasses import dataclass
from typing import List, Optional, Dict, Any

# ---------------------------------------------------------------------------
# Stage A: Observation (100% Objective Evidence)
# ---------------------------------------------------------------------------
@dataclass
class ObservationRecord:
    observation_id: str  # e.g., OB-uuid
    source_identity: str  # The FZ- identity of the chunk/document
    span_start: Optional[int]
    span_end: Optional[int]
    observed_statement: str  # The exact quote or detected structural element
    observation_type: str  # "QuotedSpan", "DetectedDefinition", "DetectedDecision"
    timestamp: str

# ---------------------------------------------------------------------------
# Stage B: Assessment (Ontological Classification)
# ---------------------------------------------------------------------------
@dataclass
class ClassifierInfo:
    version: str
    ontology_document: str
    ontology_hash: str
    ontology_version: str
    confidence_method: str  
    confidence_scale: str   
    operator: str           # "Automatic", "Human", "Consensus", "Imported"
    timestamp: str

@dataclass
class AssessmentRecord:
    assessment_id: str  # e.g., AS-uuid
    target_observation_id: str  # Points to an ObservationRecord, NOT a Concept
    epistemic_facet: str
    operational_facet: str
    ontology_confidence: float  # How confident are we this matches the ontology?
    rejected_candidates: Dict[str, float]  # E.g., {"Observation": 0.41}
    classifier: ClassifierInfo

# ---------------------------------------------------------------------------
# Stage C: Synthesis (Concept Generation)
# ---------------------------------------------------------------------------
@dataclass
class ConceptRecord:
    concept_identity: str  # e.g., FZ-uuid (The eternal anchor for this idea)
    canonical_name: str
    supporting_assessments: List[str]  # The assessments that converge on this concept
    recovery_confidence: float  # How certain are we this reflects legacy intent?
    status: str  # "Pending", "Accepted", "Rejected"
    timestamp: str

# ---------------------------------------------------------------------------
# Recovery Governance
# ---------------------------------------------------------------------------
@dataclass
class RecoveryCampaign:
    campaign_id: str  # e.g., RC-CHAT-001
    name: str
    description: str

@dataclass
class RecoveryBatch:
    batch_id: str
    campaign_id: str
    timestamp: str

@dataclass
class RecoveryRecord:
    recovery_id: str
    batch_id: str
    concept_identity: str
    basis_type: str  # "Forgotten_Knowledge", "Clarification", "Deferred_Idea"
