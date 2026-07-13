---
Authority: Constitution
Lifecycle State: Permanent
Owner: Core Maintainers
Permanence Justification: This ADR enforces the transition from architectural design to business implementation.
---

# ADR 000: Architecture Frozen

## Context
Foundation Zero has reached structural maturity. Continued refinement of the repository's architecture without new implementation evidence constitutes "Governance Perfectionism" and creates accidental complexity. The architecture must now be frozen so the system can be used to solve real-world problems.

## Decision
Foundation Zero Architecture is frozen.

Future architectural proposals must satisfy:
1. implementation exists
2. implementation failed
3. failure reproduced
4. doctrine insufficient
5. constitutional review approves

Otherwise: Proposal rejected.

## Consequences
- The governance and architecture layers cannot be expanded specitatively.
- The next phase of work must be implementation of real business interventions.

*This ADR intentionally contains no successor criteria. Architecture remains frozen until implementation evidence satisfies the constitutional change process.*
