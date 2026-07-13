import unittest
from datetime import datetime, timezone
import sys
import os
from pathlib import Path

# Add src to path to import reference implementation
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from constitution_reference.ledger import EventStore, ImmutableLedgerException
from constitution_reference.events import EpistemicEvent, EventTime
from constitution_reference.projections import KnowledgeGraphProjection

class TestLedgerInvariants(unittest.TestCase):

    def setUp(self):
        self.ledger = EventStore()
        self.time = EventTime(
            observed_time=None,
            recorded_time=datetime.now(timezone.utc).isoformat(),
            effective_time=datetime.now(timezone.utc).isoformat()
        )

    def test_no_assessment_overwrite(self):
        """Proof: You cannot overwrite an event in the ledger."""
        event1 = EpistemicEvent(
            event_id="EV-1",
            sequence_number=1,
            parent_event_ids=[],
            time=self.time,
            event_type="AssessmentAppended",
            payload={"assessment": "Hypothesis"}
        )
        self.ledger.append(event1)

        # Attempt to overwrite EV-1
        event2 = EpistemicEvent(
            event_id="EV-1", # Same ID
            sequence_number=2,
            parent_event_ids=["EV-1"],
            time=self.time,
            event_type="AssessmentAppended",
            payload={"assessment": "Fact"}
        )
        
        with self.assertRaises(ImmutableLedgerException):
            self.ledger.append(event2)

    def test_replay_determinism(self):
        """Proof: Replaying the ledger always results in the same projection."""
        event1 = EpistemicEvent(
            event_id="EV-1",
            sequence_number=1,
            parent_event_ids=[],
            time=self.time,
            event_type="CanonicalConceptAccepted",
            payload={"concept_identity": "FZ-001", "canonical_name": "Test Concept"}
        )
        self.ledger.append(event1)

        proj1 = KnowledgeGraphProjection(self.ledger, {})
        proj1.compute()
        graph1 = proj1.get_concept("FZ-001")

        proj2 = KnowledgeGraphProjection(self.ledger, {})
        proj2.compute()
        graph2 = proj2.get_concept("FZ-001")

        self.assertEqual(graph1, graph2)
        self.assertEqual(graph1["name"], "Test Concept")

    def test_no_implicit_merge(self):
        """Proof: Merging requires an explicit event, not a projection side-effect."""
        event1 = EpistemicEvent(
            event_id="EV-1",
            sequence_number=1,
            parent_event_ids=[],
            time=self.time,
            event_type="CanonicalConceptAccepted",
            payload={"concept_identity": "FZ-001", "canonical_name": "Original"}
        )
        
        event2 = EpistemicEvent(
            event_id="EV-2",
            sequence_number=2,
            parent_event_ids=["EV-1"],
            time=self.time,
            event_type="CandidateMerged",
            payload={"candidate_identity": "FZ-CAN-002", "canonical_identity": "FZ-001", "assessments": ["AS-1"]}
        )
        
        self.ledger.append(event1)
        self.ledger.append(event2)
        
        proj = KnowledgeGraphProjection(self.ledger, {})
        proj.compute()
        
        # The merge explicitly transferred assessments to FZ-001
        concept = proj.get_concept("FZ-001")
        self.assertIn("AS-1", concept["assessments"])

if __name__ == '__main__':
    unittest.main()
