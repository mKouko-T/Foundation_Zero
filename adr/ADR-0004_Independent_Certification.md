# ADR-0004: Independent Certification

**Status:** Accepted

## Context
Compilers naturally run their own tests to verify their logic. However, a compiler declaring itself "certified" creates a circular trust model. If a malicious compiler alters its hashing logic, its own tests will still pass, but the emitted manifest will be cryptographically fraudulent.

## Decision
Certification must be decoupled from implementation. Implementations may include conformance tests to assist developers, but formal certification can only be granted by an independent verification harness (`Foundation_Zero_Certification`).

## Alternatives Considered
1. **Self-Signing:** The compiler signs its own output if tests pass. Rejected due to the circular trust flaw.
2. **Manual Code Review:** Relying on code reviews of compiler implementations. Rejected because it does not cryptographically guarantee runtime behaviour.

## Consequences
- Requires a separate certification repository and standard test vectors.
- A compiler must prove determinism against golden artifacts verified by a third-party engine.

## Related Specifications
- `CERTIFICATION_SPEC.md`
- `HARNESS_SPEC.md`

## Supersedes / Superseded By
N/A
