import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.constitution_reference.ledger import EventStore
from src.constitution_reference.events import EpistemicEvent, EventTime

def run_ledger_contract_suite(ledger_class):
    """
    These are the contract rules that ANY ledger must fulfill.
    """
    ledger = ledger_class()
    e1 = EpistemicEvent(event_id="EV-1", sequence_number=1, parent_event_ids=[], time=EventTime(None, "now", "now"), event_type="TestEvent", payload={"data": 1})
    e2 = EpistemicEvent(event_id="EV-2", sequence_number=2, parent_event_ids=["EV-1"], time=EventTime(None, "now", "now"), event_type="TestEvent", payload={"data": 2})
    
    # Contract 1: Valid Append
    ledger.append(e1)
    ledger.append(e2)
    
    # Contract 2: Append-Only & Immutable (No overwrites)
    with pytest.raises(Exception):
        ledger.append(e1)
        
    # Contract 3: Cursor Statefulness and Checkpointing
    cursor = ledger.cursor()
    first_event = next(cursor)
    assert first_event.sequence_number == 1
    
    checkpoint = cursor.checkpoint()
    assert checkpoint == 1
    
    # Contract 4: Seek capability
    cursor.seek(2)
    second_event = next(cursor)
    assert second_event.sequence_number == 2

def test_ledger_append_only_contract():
    run_ledger_contract_suite(EventStore)
