---
Document ID: DOC-EVIDENCE-001
Title: Evidence Specification
Status: Released
Version: 1.0
Classification: Normative
Authority: Foundation Zero
Supersedes: None
Superseded By: None
Depends On: P-000
---

# Evidence Specification

This document defines the strict requirements for generating and submitting an Evidence Report (`R-xxx`) following the execution of an Audit Protocol (`P-xxx`).

## 1. Required Artifacts
Every Evidence Report must include:
- **Evidence ID:** A unique identifier (e.g., `R-2027-001`).
- **Timestamp:** ISO 8601 UTC timestamp of the audit conclusion.
- **Protocol Evaluated:** The exact `P-xxx` protocol executed.
- **Specification Version:** The exact commit SHA or tag of the Foundation Zero specification being audited.
- **Implementation Target:** The repository URL and commit SHA of the implementation(s) being evaluated (if applicable).
- **Environment:** The operating system, runtime, and hardware constraints where the audit was executed.

## 2. Reproducibility Guarantee
Evidence is invalid if it cannot be reproduced. 
- All scripts, source code, and mock repositories used to generate the evidence MUST be linked via permanent, immutable hashes.
- The specific terminal commands required to reproduce the evidence must be provided.

## 3. Disposition Formatting
The report must conclude with one of the mandatory dispositions defined in `P-000`:
- `[CONFIRMED]`
- `[REFUTED]`
- `[INCONCLUSIVE]`
- `[DEFERRED]`

If the disposition is `CONFIRMED` (meaning a deficiency was successfully proven), the report must explicitly cite the Normative Specification section that requires modification.
