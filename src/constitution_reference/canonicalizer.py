from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from .events import EpistemicEvent

class CanonicalAction(str, Enum):
    MERGE = "MERGE"
    SPLIT = "SPLIT"
    NEW_CANONICAL = "NEW_CANONICAL"
    REJECT = "REJECT"

class CanonicalizationPolicy(ABC):
    @abstractmethod
    def evaluate(self, candidate_event: EpistemicEvent, existing_canonical_events: List[EpistemicEvent]) -> CanonicalAction:
        """
        Evaluates a Candidate Concept against existing Canonical Concepts.
        Returns the policy decision: CanonicalAction
        """
        pass

class StrictMergePolicy(CanonicalizationPolicy):
    def evaluate(self, candidate_event: EpistemicEvent, existing_canonical_events: List[EpistemicEvent]) -> CanonicalAction:
        # Reference implementation: if exact string matches an existing canonical name, merge. Else new.
        candidate_name = candidate_event.payload.get("canonical_name")
        for event in existing_canonical_events:
            if event.payload.get("canonical_name") == candidate_name:
                return CanonicalAction.MERGE
        return CanonicalAction.NEW_CANONICAL
