# Foundation Zero: Compiled Boot Context
**Generated:** 2026-07-13T09:02:30.262879Z
**Purpose:** This is a derived build artifact containing the complete 'Foundation Zero Lite' core. It exists solely to allow downstream AI orchestrators (like ChatGPT) to ingest the entire compiler state in a single file fetch.

---

## FILE: `FZ_VERSION.md`

```markdown
Foundation Zero Version: 1.0.0

Architecture Status:
Frozen

Current Promotion Ledger:
FOUND_IN_REALITY.md

Current Bootstrap Version:
Foundation Zero Lite v1.0

Current Canonical Branch:
main

Current Certification Status:
Certified

```

---

## FILE: `README.md`

```markdown
---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: Never
Reason Exercised: N/A

Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Foundation Zero

> **FOUNDATION ZERO v1.0**
> **ARCHITECTURE FROZEN**
> No changes are accepted because they are clever.
> Changes are accepted only because reality repeatedly demonstrated the current system is insufficient.
> **Operational Rule:** No change may be proposed directly to Foundation Zero. Every proposal must originate from friction encountered in a downstream repository and be recorded in FOUND_IN_REALITY before consideration.

Foundation Zero is a repository implementing the Foundation Method.

For all operational usage, documentation, and navigation:

➡ See [HOME.md](HOME.md)

The README intentionally contains no operational instructions.

```

---

## FILE: `REPOSITORY_CONSTITUTION.md`

```markdown
---
Authority: Constitution
Lifecycle State: Permanent
Owner: Core Maintainers
Permanence Justification: This is the highest authority in the repository; removing it destroys the system's physical and operational guarantees.
---

# Repository Constitution

This document defines what physical reality guarantees. It is mathematically immutable.

## 1. The Append-Only Ledger
**Events are append-only.** No physical record of an event or evidence may ever be overwritten, modified, or silently repaired. Mistakes must be corrected with compensating events.

## 2. Evidence Immutability
**Evidence cannot be altered by assessment.** A semantic evaluation may only occur on strictly parsed physical evidence, but it can never mutate the evidence itself.

## 3. The Presumption of Sufficiency
**Every proposal begins with the assumption that the correct abstraction already exists.** The proposal carries the burden of proving otherwise through implementation evidence. Architectural change requires implementation evidence.
```

---

## FILE: `.foundation_zero/ENGINEERING_DOCTRINE.md`

```markdown
---
Authority: Doctrine
Lifecycle State: Permanent
Owner: Core Maintainers
Permanence Justification: Removing this destroys the operational law of the repository.
---

# Engineering Doctrine

This is the engineering constitution. It contains the immutable rules for Foundation Zero execution. Every future implementation agent reads this before touching code.

## Foundational Principle
**Repositories accumulate knowledge. They should not accumulate decisions.**
Knowledge should remain. Repeated decisions should disappear into automation, contracts, or defaults.

## The 6-Layer Architectural Backbone
Foundation Zero operates on a strict, stable architectural backbone. The runtime (AI model) is explicitly the outermost layer.
* **Layer 0:** Kernel (Frozen)
* **Layer 1:** Capabilities (Requires justification to expand)
* **Layer 2:** Playbooks (Routine to expand)
* **Layer 3:** Execution State (Ephemeral data driving the current task)
* **Layer 4:** Operational Memory (Short-term context retained between execution steps)
* **Layer 5:** Runtime (The interchangeable execution engine, e.g., LLM)

## Foundational Interpretation

### Epistemic Clarity
Every repository statement must belong to exactly one category: Fact (physical reality), Observation (measurement), Assessment (evaluation), Decision (action), Prediction (hypothesis), or Principle (invariant rule). Mixing categories destroys analytical integrity.

### Business Priority Rule
Until implementation evidence demonstrates a constitutional deficiency, repository work must primarily improve business workflows rather than repository structure.

## Immutable Doctrines


1. **Never overwrite events.** [Test: `tests/governance/test_event_immutability.py`] Mistakes must be corrected with compensating events, never deletions.
2. **Evidence precedes assessment.** [Test: `tests/governance/test_evidence_first.py`] Semantic evaluation may only occur on strictly parsed physical evidence.
3. **Identity is eternal.** [Test: `tests/governance/test_identity_immutability.py`] Once an identity is minted, its meaning is permanently fixed.
4. **Projections are disposable.** [Test: `tests/governance/test_projection_rebuild.py`] The Event Ledger is truth. Any projection, graph, or database built from the ledger can and will be deleted and recomputed.
5. **Kernel earns abstractions only through repeated implementation.** [Test: `tests/governance/test_kernel_expansion.py`] A pattern becomes a capability only after it is successfully implemented at least twice in the application layer.
6. **Every irreversible operation occurs exactly once.** [Test: `tests/governance/test_idempotency.py`]
7. **Every semantic operation remains reversible.** [Test: `tests/governance/test_reversibility.py`]
8. **Repository is the source of truth.** [CI Check: `verify_no_external_state`] Not the conversation. Not external chat logs.
9. **ADR before architectural change.** [Test: `tests/governance/test_adr_coverage.py`] Code changes must be justified by published architectural decisions.
10. **No Level 0/1 expansion without implementation failure.** [Test: `tests/governance/test_architecture_freeze.py`] The foundation expands only when execution demonstrates an unsolvable flaw in the current architecture.
11. **Governance as Code.** [Test: `tests/governance/test_governance_coverage.py`] Governance documents are executable contracts whenever possible. They must eventually become tests or CI checks.
12. **The Disagreement Defect.** [Test: `tests/governance/test_documentation_drift.py`] When implementation and documentation disagree, the disagreement itself is a defect.
13. **The Verification Postcondition.** [Test: `tests/governance/test_verification_postcondition.py`] No operation may report SUCCESS without verifying the resulting external state against its postconditions.
14. **Justify Existence.** [Test: `tests/governance/test_repository_economics.py`] Every permanent file must explicitly justify its own existence with the required Metadata header.
15. **Ban "We'll Remember."** [CI Check: `verify_no_memory_assumptions`] Human memory is not infrastructure. Anything requiring memory must become evidence, a playbook, an ADR, or state.
16. **The Ultimate Test.** [Test: `tests/governance/test_decision_friction.py`] A repository should become easier to understand as it grows, not harder. Evaluates the `Decision Friction` KPI.
17. **Information Ownership.** Before creating a new artifact, identify the rightful owner of the information. If an existing artifact can own it without losing clarity, extend that artifact instead of creating a new one.
18. **Abstraction Leverage.** Every permanent abstraction must remove more future decisions than it creates. Otherwise it is accidental complexity.
19. **Complexity Types.** Distinguish strictly between Necessary Complexity (e.g., append-only ledgers) and Accidental Complexity (e.g., overlapping playbooks). Actively eradicate the latter.
20. **Earned Agent Abstractions.** [ADR-007] A Skill exists only when maintaining it costs less than repeatedly rediscovering the transformation it performs.

## Governance Freeze
No further governance changes are proposed until at least three independent business implementation projects have been completed using Foundation Zero.

```

---

## FILE: `docs/playbooks/templates/BOOTSTRAP_TEMPLATE.md`

```markdown
# Project Bootstrap State

**Active Project:** [Project Name]
**Date:** [YYYY-MM-DD]

## Mission
[One-sentence description of the business problem this project solves.]

## Current Phase
[e.g., Discovery, Architecture, Implementation, Maintenance]

## Repository Map
[High-level directory structure relevant to the current work.]

## Architecture Summary
[Brief explanation of the core technical stack and design patterns.]

## How to Start
*(If using Foundation Zero Lite v1.0, ensure the minimal core is present: Constitution, Doctrine, and 3 playbooks).*
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Active Constraints
[Hard limits, API boundaries, or non-negotiables.]

## Current Decisions
[What architectural or business decisions were just made?]

## Open Risks
[What is the highest probability point of failure right now?]

## Recent ADRs
- [ADR-XXX: Description]

## How to Restore State
[If a new human or AI joins the project today, how do they recreate the local environment and mental context?]

```

---

## FILE: `docs/protocols/Protocol_Repository_Certification.md`

```markdown
# Protocol: Repository Certification

**Authority:** Doctrine
**Lifecycle State:** Permanent

This protocol defines the exact requirements to certify that a repository running under Foundation Zero is structurally and epistemically sound. It does not certify business logic; it certifies that the repository can be trusted.

A repository is officially certified when it provides verifiable, physical proof of the following five conditions:

## 1. Repository Inventory Complete
A full inventory of every file, directory, and artifact exists and has been programmatically generated. No "dark matter" files exist outside this inventory.

## 2. Universal Ownership
Every permanent artifact has a clear, documented owner. There are no orphan documents.

## 3. Universal Traceability
Every permanent artifact provides traceability. It must answer:
- Why does it exist?
- Which doctrine requires it?
- Which tests touch it?
- Which business decision does it improve?

## 4. Existential Justification
Every permanent artifact justifies its existence against the cost of rediscovery. (If it could not be justified today, it is marked for demotion or deletion).

## 5. Verification Suite Pass
The repository passes the automated structural verification suite (`pytest` invariants and `audit.py` checks) with zero errors.

```

---

## FILE: `docs/governance/PROPOSAL_TEMPLATE.md`

```markdown
---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Owner: Core Maintainers
Exit Condition: Merged into standard issue templates.
---

# Proposal Template

*Every architectural or significant operational proposal must follow this format to guarantee evidence-driven evolution.*

## 1. Information Owner
*Before proposing a new artifact, who currently owns this knowledge domain?*
- **Existing owner:** 
- **Evidence owner consulted:** 
- **Reason existing owner is insufficient:** 

## 2. Proposed Change
*What exactly will be physically altered, created, or deleted?*

## 3. Why Existing Mechanisms Are Insufficient
*What specific failure or friction in reality necessitates this change?*

## 4. Evidence Status
*Current evidence supporting this proposal: [ Established | Emerging | Hypothesis ]*

## 5. Required Evidence
*How will we mathematically or physically prove this change achieved its intent without degrading the repository?*

```

---

