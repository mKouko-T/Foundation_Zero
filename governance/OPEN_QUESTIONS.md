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
