# ADR-0003: Manifest Authority

**Status:** Accepted

## Context
A system must be able to prove its epistemic state to external agents. Without a deterministic signature, an agent could claim to run Foundation Zero while operating on arbitrary corrupted knowledge.

## Decision
The machine-readable JSON manifest (`BOOT_MANIFEST.json`) serves as the ultimate source of cryptographic truth. The `BOOT_ID` is the SHA-256 hash of this deterministic manifest. 

## Alternatives Considered
1. **Hashing the Repository:** Hashing the `.git` folder or working tree. Rejected because it includes non-semantic files, local configuration, and breaks easily across platforms.
2. **Hashing the Package:** Hashing `BOOT_PACKAGE.md`. Rejected because markdown is a presentation format; the manifest provides a strict mathematical data structure for independent verification.

## Consequences
- The JSON manifest must be strictly canonicalized (e.g., specific indenting, sorted keys, no trailing whitespace) before hashing.
- Every verified runtime state is mathematically unique to its `BOOT_ID`.

## Related Specifications
- `MANIFEST_SCHEMA.json`

## Supersedes / Superseded By
N/A
