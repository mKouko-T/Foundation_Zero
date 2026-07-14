# ADR-0002: Canonical IR

**Status:** Accepted

## Context
Early compiler designs relied on reading markdown files line-by-line and applying regex transformations directly during validation and emission. This tightly coupled the file structure, markdown syntax, semantic rules, and final emission.

## Decision
Introduce a Canonical Intermediate Representation (IR). The compiler is split into stages where raw files are parsed into a single, purely semantic memory structure (the IR). All validation and hashing operations operate exclusively on the IR. Emission generates the final package purely from the verified IR.

## Alternatives Considered
1. **Direct Transpilation:** Transforming files directly into output text. Rejected because it intertwines validation with emission, making independent mathematical proofs difficult.
2. **AST:** Generating an Abstract Syntax Tree. Rejected as overly complex since Foundation Zero is largely declarative rather than imperative.

## Consequences
- Requires a strong dataclass schema (`CanonicalIR`).
- Disconnects the emission format from the source format.
- Significantly enables future language-agnostic implementations.

## Related Specifications
- `COMPILER_SPEC.md`

## Supersedes / Superseded By
N/A
