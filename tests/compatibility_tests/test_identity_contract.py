import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.constitution_reference.identity import DeterministicIdentityProvider, IdentityProvider

def run_identity_contract_suite(provider: IdentityProvider):
    """
    These are the contract rules that ANY identity provider must fulfill,
    whether it is v1, v2, local, or distributed.
    """
    # Contract 1: Determinism
    id1 = provider.mint("test", {"key": "value", "a": 1})
    id2 = provider.mint("test", {"a": 1, "key": "value"})
    assert id1 == id2, "Contract Violation: Identical semantic inputs must yield identical FZ identity."

    # Contract 2: Namespace collision prevention
    id3 = provider.mint("other", {"key": "value", "a": 1})
    assert id1 != id3, "Contract Violation: Identical inputs in different namespaces must yield different FZ identities."

    # Contract 3: Opaque Prefix
    assert id1.uri.startswith("FZ-"), "Contract Violation: Identity must be prefixed with FZ- to indicate epistemic opacity."

def test_v1_identity_provider_fulfills_contract():
    provider = DeterministicIdentityProvider()
    run_identity_contract_suite(provider)

# Future: 
# def test_v2_identity_provider_fulfills_contract():
#     provider = DistributedIdentityProvider()
#     run_identity_contract_suite(provider)
