---
Authority: Interpretive (Not Authoritative)
Lifecycle State: Permanent
Owner: Core Maintainers
Exit Condition: Merged into Doctrine if strictly required.
---

# Repository Philosophy

*Note: This document is interpretive. It explains the "why." It does not govern. The hierarchy of authority is: Constitution (What reality guarantees) → Engineering Doctrine (How engineers behave) → Governance (How engineering changes) → Playbooks → Philosophy.*

## The Ultimate Mission
**Foundation Zero exists to preserve justified decisions and reduce the cost of making the next correct decision.**

## Decision Latency and Repository KPIs
Foundation Zero optimizes engineering decisions. Current measurements include:
1. **Decision Quality**
2. **Decision Confidence**
3. **Decision Latency**
*(Secondary metrics: Time to onboard a new engineer, time to answer a business question, time to modify a playbook, time to recover from corruption.)*

### The Falsification Condition
Foundation Zero must remain scientific, not ideological. If repeated business implementation proves another approach consistently produces better decisions with lower maintenance, Foundation Zero must be abandoned.

### Explicit Exclusion
Foundation Zero is an engineering operating system. It is not the permanent home for project knowledge, a wiki, or business artifacts.

## The Horizon of Permanence
Before adding anything to this repository, ask: **"What must now survive ten years?"**

- A ten-year artifact deserves **Permanence** (Constitution, Doctrine, Axioms).
- A one-year artifact deserves a **Playbook**.
- A one-month artifact deserves **Operational State**.
- A one-week artifact deserves a **Task**.

## Core Principles
- The repository exists to improve real-world decisions.
- Evidence outranks opinion.
- Verification outranks optimism.
- Simplicity outranks elegance.
- Architecture follows implementation.
- Human judgment remains the final authority.
- The event log is authoritative; projections are disposable.
- Every permanent artifact must justify its existence.
- When implementation and documentation disagree, the disagreement is the defect.

## Negative Principles
Foundation Zero **never**:
- hides evidence.
- silently repairs data.
- invents ontology.
- reports success without verification.
- treats projections as authoritative.
- relies on undocumented human memory.
- expands architecture before implementation failure.

## The Re-Approval Rule
Before committing any permanent addition, ask: **If this file already existed today, would we approve adding it again?**
