import uuid
from datetime import datetime, timezone
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from schemas import ObservationRecord

class ObserverWorker:
    """
    Stage A: The Observer
    Extracts purely objective spans and structural elements from chunks.
    No semantic interpretation is allowed here.
    """
    def observe_span(self, source_identity: str, start: int, end: int, text: str, obs_type: str = "QuotedSpan") -> ObservationRecord:
        return ObservationRecord(
            observation_id=f"OB-{uuid.uuid4()}",
            source_identity=source_identity,
            span_start=start,
            span_end=end,
            observed_statement=text,
            observation_type=obs_type,
            timestamp=datetime.now(timezone.utc).isoformat()
        )
