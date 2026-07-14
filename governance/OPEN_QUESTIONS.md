---
Document ID: DOC-GOV-005
Title: Open Questions Registry
Status: Active
Version: 1.0
Classification: Informative
Authority: Foundation Zero
Supersedes: None
Superseded By: None
Depends On: None
---

# Open Questions Registry

This registry tracks discovered ambiguities, unhandled edge cases, and unknowns identified during standard development and adversarial audits.

*Note: Not every question represents a specification defect. Questions must be formally dispositioned.*

## Dispositions
- **Accepted Unknown:** Acknowledge the ambiguity but decide not to specify it yet.
- **Specification Gap:** A legitimate defect requiring a normative update.
- **Deferred:** Relevant but postponed to a future version.
- **Rejected:** The question is out of scope or resolved by existing text.

---

### Q-001: Behavior of cyclic graph detection on isolated sub-graphs
- **ID:** Q-001
- **Raised by:** Phase Ω Auditors
- **Date:** 2026-07-14
- **Related Specification:** `COMPILER_SPEC.md`, `COMPILER_PIPELINE.json`
- **Current Disposition:** Deferred
- **Required Evidence:** R-001 (Hostile Implementation output proving ambiguity)
- **Resolution Reference:** TBD

### Q-002: Normative Terminology Glossary
- **ID:** Q-002
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** All Normative Docs
- **Current Disposition:** Accepted Unknown
- **Required Evidence:** Evidence of implementation divergence caused by differing interpretations of standard terminology (e.g., "Artifact", "Specification", "Requirement").

### Q-003: Stable Requirement Identities
- **ID:** Q-003
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** All Normative Docs
- **Current Disposition:** Accepted Unknown
- **Required Evidence:** Evidence of traceability failure or audit confusion due to paragraph-level references instead of unique requirement IDs (e.g., `REQ-0017`).

### Q-004: Machine-Extractable Normative Statements
- **ID:** Q-004
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** All Normative Docs
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence that manual conformance evaluation is scaling poorly and requires automated extraction of MUST/SHALL/MAY statements.

### Q-005: Requirement-Level Lifecycle States
- **ID:** Q-005
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** All Normative Docs
- **Current Disposition:** Accepted Unknown
- **Required Evidence:** Evidence that document-level versioning is insufficient for managing the deprecation and evolution of individual constraints.

### Q-006: Certification State Machine
- **ID:** Q-006
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `CONFORMANCE_POLICY.md`
- **Current Disposition:** Accepted Unknown
- **Required Evidence:** Evidence of certification ambiguity when an implementation passes some audit protocols but fails others.

### Q-007: Intra-Category Conflict Resolution
- **ID:** Q-007
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `FOUNDATION_CONSTITUTION.md`
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence of two normative specifications contradicting each other, resulting in deadlock under the current precedence hierarchy.

### Q-008: Specification Immutable Identity
- **ID:** Q-008
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `DOCUMENT_REGISTRY.json`
- **Current Disposition:** Accepted Unknown
- **Required Evidence:** Evidence of audit spoofing or version confusion due to reliance on semantic versions or git tags instead of cryptographic bundles.

### Q-009: Formal Mathematical Invariants
- **ID:** Q-009
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `COMPILER_SPEC.md`
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence of state corruption or logical invalidity inside an implementation that adhered to the pipeline graph but violated implicit invariants.

### Q-010: Governance Threat Model
- **ID:** Q-010
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `PHILOSOPHY_OF_STANDARDIZATION.md`
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence of proposal flooding, standards capture, or evidence cherry-picking actively degrading the specification.

### Q-011: Epistemic Jurisdiction Boundaries
- **ID:** Q-011
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `FOUNDATION_CONSTITUTION.md`
- **Current Disposition:** Accepted Unknown
- **Required Evidence:** Evidence of the standard suffering instability due to attempts to specify domains outside observable behavior (e.g., human cognition, business processes).

### Q-012: Evidence Admissibility Criteria
- **ID:** Q-012
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `EVIDENCE_SPEC.md`
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence of audit conflicts caused by fundamentally subjective or unverified evidence claims (e.g., simulations, AI-generated output vs independent human implementations).

### Q-013: Findings and Normative Proposals Pipeline
- **ID:** Q-013
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `FOUNDATION_CONSTITUTION.md`
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence of governance slowdown due to reviewers having to process raw Evidence Reports directly, rather than distilled "Findings" that lead to "Normative Proposals".

### Q-014: Governance Scalability & Conflicting Evidence
- **ID:** Q-014
- **Raised by:** Independent Reviewer
- **Date:** 2026-07-14
- **Related Specification:** `FOUNDATION_CONSTITUTION.md`
- **Current Disposition:** Deferred
- **Required Evidence:** Evidence of the standard's evolution stalling due to an inability to resolve conflicting but admissible evidence reports (R-xxx vs R-yyy).
