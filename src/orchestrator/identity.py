from abc import ABC, abstractmethod
import hashlib
import uuid
from pathlib import Path

class IdentityProvider(ABC):
    """
    Level 1 Meta-Model: Identity Provider.
    Identity is the eternal anchor. It is strictly separated from locators, hashes, or state.
    """
    @abstractmethod
    def generate_identity(self, context) -> str:
        """Generates a universal identity (e.g., FZ-0000...) independent of transient state."""
        pass

class ContentHashIdentityProvider(IdentityProvider):
    """Derives an FZ Identity based on the initial cryptographic evidence (hash)."""
    def generate_identity(self, filepath: Path) -> str:
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as f:
            hasher.update(f.read())
        
        hash_hex = hasher.hexdigest()
        # Identity is an abstract FZ string, deterministically generated from the hash,
        # but explicitly NOT the hash itself. The hash is just evidence.
        derived_uuid = uuid.uuid5(uuid.NAMESPACE_OID, hash_hex)
        return f"FZ-{derived_uuid}"

class SemanticIdentityProvider(IdentityProvider):
    """Derives an FZ Identity based on a semantic string or concept name."""
    def generate_identity(self, semantic_name: str) -> str:
        derived_uuid = uuid.uuid5(uuid.NAMESPACE_OID, semantic_name)
        return f"FZ-{derived_uuid}"
