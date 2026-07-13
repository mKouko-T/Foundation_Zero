from typing import List
from .events import EpistemicEvent

class ImmutableLedgerException(Exception):
    pass

class EventStore:
    """
    The canonical truth of Foundation Zero. 
    It is append-only, forms a DAG, and absolutely prohibits state mutation or deletion.
    """
    def __init__(self):
        self._events: List[EpistemicEvent] = []
        self._event_ids: set = set()

    def append(self, event: EpistemicEvent) -> None:
        if event.event_id in self._event_ids:
            raise ImmutableLedgerException(f"Event {event.event_id} already exists.")
        
        if event.sequence_number != len(self._events) + 1:
            raise ImmutableLedgerException(f"Invalid sequence number: {event.sequence_number}. Expected {len(self._events) + 1}")
            
        for parent_id in event.parent_event_ids:
            if parent_id not in self._event_ids:
                raise ImmutableLedgerException(f"Parent event {parent_id} does not exist in ledger.")
                
        self._events.append(event)
        self._event_ids.add(event.event_id)

    def cursor(self):
        return LedgerCursor(self._events)

class LedgerCursor:
    def __init__(self, events: List[EpistemicEvent]):
        self._events = events
        self._index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self) -> EpistemicEvent:
        if self._index >= len(self._events):
            raise StopIteration
        event = self._events[self._index]
        self._index += 1
        return event

    def seek(self, sequence_number: int) -> None:
        """Seek to a specific sequence number for incremental replay or streaming."""
        for i, event in enumerate(self._events):
            if event.sequence_number == sequence_number:
                self._index = i
                return
        raise ValueError(f"Sequence number {sequence_number} not found.")

    def checkpoint(self) -> int:
        """Returns the current sequence number for incremental replay state saving."""
        if self._index == 0:
            return 0
        return self._events[self._index - 1].sequence_number
