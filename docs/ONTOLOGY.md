# Foundation Zero Ontology

*This document serves as the canonical conceptual model for Foundation Zero. The repository hierarchy strictly mirrors this ontology. Structure is knowledge.*

## 1. Operational Entities
These represent the active execution engines of work.
- **Project**: A living, time-bounded operational workspace focused on a specific goal. Projects are where work happens; they are not the permanent home of extracted knowledge.
- **Session**: A continuous interaction or compute cycle within a Project.
- **Artifact**: A distinct, immutable output file produced by an operation or session.

## 2. Knowledge Graph (Epistemic Elements)
These elements represent the permanent, extracted intelligence of the system.
- **Observation**: A factual, immutable statement about reality recorded at a specific point in time.
- **Hypothesis**: A testable proposition attempting to explain observations or propose a mechanism.
- **Evidence**: Data, documents, or outputs that validate or invalidate a hypothesis.
- **Finding**: A validated piece of knowledge that has survived adversarial review and verification.
- **Candidate**: An unverified proposition or draft knowledge awaiting promotion or rejection.

## 3. Governance & Architecture
These define the rules, limits, and structures of the repository.
- **Decision**: A formal, irreversible choice made regarding architecture, governance, or protocol.
- **ADR**: Architecture Decision Record; an immutable, chronologically numbered log of a governance decision.
- **Specification**: A formal, machine-enforceable definition of an interface, format, or protocol (e.g., FZS, JSON schemas).
- **Protocol**: A strict, ordered procedural rule governing how actions must be executed (e.g., Migration Procedure).
- **Risk**: An explicitly identified potential failure mode or hazard to the Foundation.
- **Issue**: A currently active defect, violation, or required engineering task.
- **Capability**: A self-contained, validated skill or function the repository can perform autonomously.

## 4. Preservation & Transitions
These define how information flows through time.
- **Ledger**: An append-only chronological record of events, decisions, operations, or certifications.
- **Promotion**: The formal protocol governing the transition of an artifact or finding from an experimental/candidate state to a validated, trusted state.
- **Archive**: A permanent, read-only storage for retired, deprecated, or replaced records.
- **Legacy**: A frozen state for untranslated prior structures awaiting semantic extraction or archival.
