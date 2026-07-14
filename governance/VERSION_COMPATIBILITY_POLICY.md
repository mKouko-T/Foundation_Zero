# Foundation Zero Version Compatibility Policy

Foundation Zero separates concerns into distinct architectural streams. Each stream evolves at its own pace.

## 1. The Four Version Streams

1. **Epistemic Model** (`EPISTEMIC_MODEL.md`)
   - **Scope**: The definitions of Reality, Proof, Judgment, and Knowledge.
   - **Cadence**: Extremely conservative. Changes represent a shift in the fundamental philosophy of engineering.

2. **Compiler Specification** (`COMPILER_SPEC.md`, `COMPILER_ORDER.json`, `MANIFEST_SCHEMA.json`)
   - **Scope**: The machine rules for assembling truth into an executable artifact.
   - **Cadence**: Conservative. Evolved when cryptographic provenance, canonicalization, or manifest structure requires enhancement.

3. **Runtime Specification** (`RUNTIME_SPEC.md`)
   - **Scope**: The operational constraints for the autonomous agent executing the `BOOT_PACKAGE`.
   - **Cadence**: Moderate. Evolved to support new capabilities (e.g., dynamic context loading) without breaking compilation.

4. **Implementation** (e.g., `Cornerstone/compiler/`)
   - **Scope**: The actual code that executes the compiler specification.
   - **Cadence**: Fluid. Frequent releases for performance, bug fixes, or test coverage, provided they strictly conform to the Compiler Spec.

## 2. Compatibility Matrix

Implementations MUST explicitly declare which version of the Compiler Specification they satisfy.
For example, an implementation version `v1.4.3` may certify compliance with Compiler Specification `v1.0`.

- An Implementation MUST NOT alter its compilation logic without a corresponding change in the Compiler Specification.
- An Implementation MAY support older versions of the Compiler Specification concurrently (e.g., via flags like `--spec-version 1.0`).

## 3. The Trust Chain

The ecosystem maintains a linear trust verification sequence. No entity verifies itself:

```text
Epistemic Model
        │
        ▼
Specifications (Compiler & Runtime)
        │
        ▼
Machine Schemas (JSON/YAML)
        │
        ▼
Implementations
        │
        ▼
Independent Certification (Harness & Corpus)
        │
        ▼
Trusted Runtime (BOOT_PACKAGE execution)
```
