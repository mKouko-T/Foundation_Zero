from abc import ABC, abstractmethod
import hashlib
import uuid
from dataclasses import dataclass

@dataclass(frozen=True)
class Locator:
    """Physical location in a storage system (e.g., knowledge/theory/foo.md). Disjoint from Identity."""
    uri: str

@dataclass(frozen=True)
class Reference:
    """External system reference (e.g., doi:10.1000/182). Disjoint from Identity."""
    uri: str

@dataclass(frozen=True)
class Alias:
    """Human readable name or historical moniker. Disjoint from Identity."""
    name: str

@dataclass(frozen=True)
class Identity:
    """The fundamental epistemic identifier. Opaque to semantic content."""
    uri: str

class IdentityProvider(ABC):
    @abstractmethod
    def mint(self, namespace: str, inputs: dict) -> Identity:
        """
        Guarantees: uniqueness, namespace isolation, and collision policy.
        Only IdentityProviders may generate Identity objects.
        """
        pass

class DeterministicIdentityProvider(IdentityProvider):
    """
    Guarantees perfectly deterministic, reproducible identities based on immutable inputs.
    If the exact same evidence and configuration are provided, the exact same Identity is returned.
    """
    def mint(self, namespace: str, inputs: dict) -> Identity:
        import json
        # RFC-8785 style canonical serialization
        serialized = json.dumps(inputs, sort_keys=True, separators=(',', ':'))
        hash_digest = hashlib.sha256(f"{namespace}:{serialized}".encode("utf-8")).hexdigest()
        return Identity(f"FZ-{namespace}-{hash_digest[:16]}")

class EphemeralIdentityProvider(IdentityProvider):
    """
    For non-reproducible, purely temporal events where determinism is not possible (e.g., human overrides).
    """
    def mint(self, namespace: str, inputs: dict) -> Identity:
        return Identity(f"FZ-{namespace}-{uuid.uuid4()}")
