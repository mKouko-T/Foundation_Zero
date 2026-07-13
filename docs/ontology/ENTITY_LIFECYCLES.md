# Entity Lifecycles

Foundation Zero is built around transitions. This document maps the universal lifecycles that entities must traverse to gain trust and permanence within the system.

## 1. The Epistemic Lifecycle (Knowledge)
Applies to Assertions as they are refined into canon.
1. **Raw**: Initially extracted from a Source (as an Assertion).
2. **Draft**: Classified into a Claim, Hypothesis, or Observation, but unverified.
3. **Qualified**: Backed by initial Evidence, awaiting adversarial review.
4. **Verified**: Evidence has survived adversarial review (becomes a Finding).
5. **Certified Knowledge**: Integrated into the broader Knowledge Graph with established relationships.
6. **Operational Canon**: Upgraded to a foundational truth that governs future decisions.

## 2. The Operational Lifecycle (Artifacts & Capabilities)
Applies to systemic assets and modules.
1. **Experimental**: Active development; breaking changes permitted.
2. **Supported / Pilot**: In production use; strictly versioned (SemVer).
3. **Deprecated**: Marked for removal; migration path required.
4. **Frozen**: Read-only; security patches only.
5. **Archived**: Moved out of active source.
6. **Removed**: Deleted from tree (requires ADR).

## 3. The Governance Lifecycle (Decisions & Protocols)
Applies to ADRs and architectural rulings.
1. **Proposed**: Under active debate.
2. **Accepted**: Formally ratified and adopted into the Constitution.
3. **Rejected**: Denied adoption.
4. **Superseded**: Replaced by a newer Decision (requires backward reference).

## Core Principle: Confidence
Confidence is not mere metadata; it is a structural property of the ontology. Every entity holds a Confidence score or state that dictates which lifecycle phase it currently occupies. An entity cannot skip phases without explicitly generated Evidence.
