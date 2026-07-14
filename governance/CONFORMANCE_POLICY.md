---
Document ID: DOC-GOV-004
Title: Conformance Policy
Status: Released
Version: 1.0
Classification: Normative
Authority: Foundation Zero
Supersedes: None
Superseded By: None
Depends On: DOC-GOV-001
---

# Conformance Policy

This document defines the strict semantics of conformance and certification within the Foundation Zero ecosystem.

## 1. Terminology Distinction

To maintain rigor, the following terms are strictly separated:
- **Specification Conformance:** An implementation’s ability to correctly adhere to the rules and schemas defined in the normative specifications.
- **Implementation Certification:** The formal, cryptographically reproducible evidence that an implementation achieved conformance on a specific date for a specific version.
- **Audit Completion:** The successful execution of a Phase Ω normative protocol resulting in an Evidence Report (`R-xxx`).
- **Ecosystem Maturity:** The global state of the Foundation Zero standard (e.g., M3 Reference Implementation vs M7 Proven Standard).

## 2. Levels of Conformance

Foundation Zero recognizes the following states of conformance for an implementation:

### 2.1 Full Conformance
The implementation fully satisfies all normative requirements, processes the entire pipeline graph deterministically, and produces exact cryptographic matches for all canonical tests.

### 2.2 Partial Conformance
The implementation is incomplete. It may correctly execute certain stages, but cannot produce the final verifiable Boot ID. Partial conformance is considered **Non-Conformant** for production purposes.

### 2.3 Profile Conformance
(Reserved for future use). When Foundation Zero introduces optional capabilities (e.g., embedded environments vs host environments), conformance will be evaluated against specific capability profiles. Currently, all capabilities are mandatory.

## 3. Extension & Deprecation

### Optional Capabilities
Capabilities declared under the `experimental/`, `vendor/`, or `private/` namespaces are strictly informative and non-normative. An implementation using these namespaces is still considered Fully Conformant so long as the normative outputs remain unaffected.

### Deprecated Behavior
When a feature is marked deprecated, it remains normative until formally removed in a subsequent specification version. Implementations MUST support deprecated behaviors to maintain Full Conformance.
