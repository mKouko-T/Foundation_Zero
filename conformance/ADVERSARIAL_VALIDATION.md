# Phase Ω (Omega): Adversarial Validation

Passing all Ω-domain requirements is a prerequisite for advancing from **M3 (Reference Implementation)** to **M4 (Independent Conformance)**.

This document serves as the **Certification Contract**. It defines the required audits to demonstrate that the architecture resists failure.

---

## Domain A: Determinism Audit

**Objective:** Identical inputs produce identical outputs across supported environments.
**Threat Model:** Honest developer makes environmental mistakes (e.g., CRLF, locale).
**Success Criteria:** `BOOT_ID` matches exactly across all configurations.
**Failure Criteria:** Any configuration produces a divergent manifest or package.
**Validation Authority:** Self-testable via conformance fixtures.
**Required Tests:**
- LF vs CRLF line endings
- NFC vs NFD unicode normalization
- UTF-8 BOM presence
- Very large repositories
- Symlinks (if supported, else explicit rejection)
- Git submodules
- Unicode filenames and case-sensitive collisions
- Executable bit changes
- Varying system locales
- Detached HEAD / dirty working trees / sparse checkout

---

## Domain B: Trust Audit

**Objective:** All external dependencies are authenticated according to the strict trust model.
**Threat Model:** Malicious repository or man-in-the-middle.
**Success Criteria:** The system explicitly defines and validates all boundaries.
**Failure Criteria:** An unverified artifact is admitted into the knowledge state.
**Validation Authority:** Independent Verifier.
**Required Tests:**
- HTTPS transport validation for remote specs
- Pinned commit authenticity
- Tag mutation and branch movement
- Local cache poisoning
- Offline mode behavior

---

## Domain C: Failure Audit

**Objective:** Malformed inputs fail deterministically without emitting partial artifacts.
**Threat Model:** Malicious repository intentionally attempts to fool the compiler.
**Success Criteria:** Explicit fatal error on all invalid states. No partial `BOOT_PACKAGE.md` generated.
**Failure Criteria:** System crashes with unhandled exceptions, or partially compiles.
**Validation Authority:** Self-testable via malicious fixtures.
**Required Tests:**
- Malformed JSON in manifests or pipeline
- Duplicated specification IDs
- Missing schema version
- Incompatible runtime
- Corrupted manifest
- Invalid UTF-8
- Missing compiler identity
- Cyclic dependency graph in pipeline
- Unsupported schema version

---

## Domain D: Evolution Audit

**Objective:** Version compatibility and migration behave exactly as specified.
**Threat Model:** Honest ecosystem drift causing fragmentation.
**Success Criteria:** System gracefully handles forward and backward compatibility limits.
**Failure Criteria:** Silently accepting incompatible specs or rejecting valid legacy specs.
**Validation Authority:** Independent Verifier.
**Required Tests:**
- v1 compiler rejects v5 specs
- v5 compiler accurately compiles v1 specs
- Chaining migrations
- Repositories declaring explicit compatibility
- Preservation of old executable packages

---

## Domain E: Governance Audit

**Objective:** Specification changes follow the documented change-control process.
**Threat Model:** Social or organizational fragmentation.
**Success Criteria:** The governance model successfully resolves disputes without inventing new rules.
**Failure Criteria:** Forks due to unresolved specification ambiguity.
**Validation Authority:** Human / Organizational Audit.
**Required Tests:**
- Two conflicting proposals
- Emergency security fix
- Accidental breaking change
- Abandoned specification
- Disputed interpretation
- Multiple implementations disagree
