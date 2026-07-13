---
Authority: Constitution
Lifecycle State: Permanent
Last Exercised: 2026-07-12
Reason Exercised: Established formal architectural freeze.

Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Architecture Freeze Rule

No proposal may modify the architecture unless it is accompanied by a concrete implementation that failed because of the current architecture, along with evidence showing why the failure cannot be resolved within the existing design.

## The 5-Step Override

A kernel or architecture change is allowed **ONLY** if:
1. A production implementation fails.
2. The failure cannot be solved in Layer 2+ (Specifications, Implementations, Playbooks).
3. Two alternative implementations fail.
4. Compatibility tests demonstrate impossibility.
5. Constitutional Review Board (or Steward) approves.

If these five criteria are not met, the architecture is **Frozen** and the proposal must be rejected.

## Governance Layer Freeze

The governance structure itself is frozen with the same discipline as the architectural kernel. 

**Rule:** Every new permanent governance document must retire an existing governance responsibility or demonstrate that no existing document can legitimately own it.
