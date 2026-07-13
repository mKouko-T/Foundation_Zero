from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from enum import Enum

class ConceptLifecycle(str, Enum):
    CANDIDATE = "Candidate"
    ACCEPTED = "Accepted"
    DEPRECATED = "Deprecated"
    SUPERSEDED = "Superseded"
    MERGED = "Merged"
    SPLIT = "Split"
    WITHDRAWN = "Withdrawn"
    HISTORICAL = "Historical"

@dataclass(frozen=True)
class EventTime:
    observed_time: Optional[str]  # When the evidence actually occurred in the real world
    recorded_time: str            # When this event entered the ledger
    effective_time: str           # When this event's semantic claim becomes active

@dataclass(frozen=True)
class EvaluatorIdentity:
    operator: str
    model_version: Optional[str]
    prompt_hash: Optional[str]
    config_hash: Optional[str]

@dataclass(frozen=True)
class MultiDimensionalConfidence:
    value: float
    meaning: str           # e.g., "Probability of matching ontology"
    distribution: str      # e.g., "0.0-1.0"
    method: str            # e.g., "heuristic_regex", "llm_eval"
    calibration: str       # e.g., "uncalibrated", "human_aligned_v1"
    evidence_completeness: float # e.g., 0.15 (high confidence, low evidence) vs 0.95

@dataclass(frozen=True)
class EpistemicEvent:
    """
    The fundamental unit of truth in Foundation Zero.
    Everything else is computed from a sequence of these events.
    """
    event_id: str
    sequence_number: int
    parent_event_ids: List[str]
    time: EventTime
    event_type: str
    payload: Dict[str, Any]
