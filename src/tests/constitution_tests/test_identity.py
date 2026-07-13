import unittest
from pathlib import Path
import tempfile
import sys
import os

# Add orchestrator to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from orchestrator.identity import ContentHashIdentityProvider, SemanticIdentityProvider

class TestIdentityPrimacy(unittest.TestCase):
    def test_identity_survives_relocation(self):
        """
        Level 0 Law: The Axiom of Identity Primacy.
        Identity survives relocation. Path is just a locator.
        """
        provider = ContentHashIdentityProvider()
        
        with tempfile.NamedTemporaryFile(delete=False) as f1, tempfile.NamedTemporaryFile(delete=False) as f2:
            f1.write(b"Immutable Knowledge State")
            f2.write(b"Immutable Knowledge State")
            f1_path = Path(f1.name)
            f2_path = Path(f2.name)
            
        id1 = provider.generate_identity(f1_path)
        id2 = provider.generate_identity(f2_path)
        
        # Identity must match despite different paths
        self.assertEqual(id1, id2, "Identity failed to survive relocation.")
        
        # Identity must be an abstract identifier, not the raw hash evidence
        self.assertTrue(id1.startswith("FZ-"), "Identity must be abstract, not raw hash.")
        
        f1_path.unlink()
        f2_path.unlink()

    def test_identity_independent_of_state(self):
        """
        Semantic Identities must remain stable even if their physical evidence is entirely abstract.
        """
        provider = SemanticIdentityProvider()
        id1 = provider.generate_identity("Concept: Universal Operating Model")
        id2 = provider.generate_identity("Concept: Universal Operating Model")
        self.assertEqual(id1, id2)
        self.assertTrue(id1.startswith("FZ-"))

if __name__ == '__main__':
    unittest.main()
