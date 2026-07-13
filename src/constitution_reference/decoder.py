from abc import ABC, abstractmethod
from typing import List, Dict

class DocumentModel:
    """A purely structural representation of a decoded artifact."""
    def __init__(self, raw_bytes: bytes, elements: List[Dict]):
        self.raw_bytes = raw_bytes
        self.elements = elements

class ArtifactDecoder(ABC):
    """Parses raw physical bytes into a structural DocumentModel. Knows PDF/Markdown."""
    @abstractmethod
    def decode(self, payload: bytes) -> DocumentModel:
        pass

class MarkdownDecoder(ArtifactDecoder):
    def decode(self, payload: bytes) -> DocumentModel:
        text = payload.decode('utf-8')
        elements = [{"type": "Paragraph", "text": text.split('\n\n')[0]}] if text else []
        return DocumentModel(payload, elements)

class ObserverInterface(ABC):
    """Extracts purely physical structures from a DocumentModel. Knows nothing about PDF/Markdown."""
    @abstractmethod
    def observe(self, artifact_identity: str, document: DocumentModel) -> List[Dict]:
        pass

class GenericObserver(ObserverInterface):
    def observe(self, artifact_identity: str, document: DocumentModel) -> List[Dict]:
        import hashlib
        observations = []
        for elem in document.elements:
            content = elem.get("text", "")
            hash_digest = hashlib.sha256(content.encode('utf-8')).hexdigest()
            observations.append({
                "type": elem["type"],
                "byte_offset": 0,
                "length": len(content),
                "content_hash": hash_digest
            })
        return observations
