# Foundation Zero Risk Register

| Risk ID | Owner | Risk Description | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|---|
| RSK-001 | Chief Architect | Legacy extraction drifts from source evidence due to LLM hallucination. | High | Medium | Enforce strict Evidence-Ledger correlation; Verification Phase is read-only. | Active |
| RSK-002 | Foundation System | Repository architecture becomes too complex, slowing down knowledge recovery. | Medium | High | Freeze infrastructure after Milestone 2.6. Require ADR for structural changes. | Mitigated |
| RSK-003 | Foundation System | Contributor accidentally mutates or deletes canonical ledgers. | High | Low | Implement `DELETION_POLICY.md` and enforce immutable append-only ledgers. | Active |
| RSK-004 | Foundation System | JSON Schemas become misaligned with the Protocol Specification over time. | Medium | Low | `certify.py` and CI enforce schema compliance and compatibility validation. | Mitigated |
