# ADR-0007: Three-Layer Compiler Architecture

**Status:** Accepted

## Context
Early compiler implementations handled file reading, canonicalization, parsing, validation, and emission across intertwined functions. This made it difficult to mathematically prove that the data being validated was exactly the same data being emitted.

## Decision
The compiler must be explicitly separated into three distinct logical layers:
1. **Parser Layer:** Exclusively responsible for reading raw source artifacts from disk or network, canonicalizing them, and writing them into the Canonical IR.
2. **Validation Layer:** Exclusively reads from the Canonical IR (never raw files). It resolves topological dependencies, generates cryptographic hashes, and asserts correctness.
3. **Emission Layer:** Exclusively reads from the verified Canonical IR. It never reads source files directly.

## Alternatives Considered
1. **Streaming Compiler:** Validating and emitting files on the fly as they are read. Rejected because it precludes holistic validations like acyclic graph checking and makes partial failure recovery dangerous.

## Consequences
- Strongly enforces the Canonical IR as the single source of truth in memory.
- Significantly simplifies the process of auditing implementations across different languages (Rust, Go, etc.) since the architectural flow is identical.

## Related Specifications
- `COMPILER_SPEC.md`
- `CanonicalIR` Struct Definition

## Supersedes / Superseded By
N/A
