# ADR-0001: Repository vs Runtime

**Status:** Accepted

## Context
Traditional systems treat the repository as a passive collection of documents. The runtime environment (agents) reads these documents as contextual memory. This leads to drift between what the repository declares and how the runtime behaves, because documentation lacks execution semantics.

## Decision
The repository must be compiled into a mathematically deterministic runtime executable (`BOOT_PACKAGE.md` and `BOOT_MANIFEST.json`). The repository is the source code; the runtime is the compiled binary. 

## Alternatives Considered
1. **Dynamic Prompting:** The agent dynamically reads the repository at boot time. Rejected because it breaks determinism and allows agents to selectively ignore files.
2. **Packaging Scripts:** A simple `cat` script to merge files. Rejected because it lacks cryptographic provenance, deterministic dependency graphs, and structural validation.

## Consequences
- Requires a formal compiler architecture.
- Enforces extreme hygiene on the repository structure.
- Guarantees that two instances booting from the same commit share an identical epistemic state.

## Related Specifications
- `COMPILER_SPEC.md`
- `MANIFEST_SCHEMA.json`

## Supersedes / Superseded By
N/A
