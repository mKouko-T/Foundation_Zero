---
Document ID: DOC-SPEC-001
...
---
# Compiler Specification
Implementations MUST adhere strictly.

1. **Pipeline**: Dependencies MUST be declared in acyclic `COMPILER_PIPELINE.json`. NO filesystem enumeration. MAY execute any topological order. Features MAY be negotiated via `capabilities`. Missing non-optional files MUST trigger fatal error.
2. **Architecture**: MUST enforce 3 layers: Parser (raw -> IR), Validation (ONLY IR -> hashes/dependencies), Emission (ONLY verified IR -> outputs).
3. **Canonicalization**: Inputs MUST process sequentially: Ingest bytes -> Strip BOM (`EF BB BF`) -> Decode strict UTF-8 (reject invalid) -> Normalize CRLF/CR to LF -> Normalize Unicode NFC. Result = Canonical UTF-8.
4. **Hashing**: Cryptographic hashes MUST target Canonical UTF-8 text (`SHA-256(UTF8_Encode(Canonical_UTF8))`). NO hashing raw bytes.
5. **Execution**: MUST support Pinned Mode (immutable SHA) and Live Mode (default branch). Mode MUST be declared. Uncommitted changes MUST be "dirty" or rejected.
6. **Emission**: MUST emit `MANIFEST_SCHEMA.json`. JSON MUST be deterministic: alphabetical keys, `ensure_ascii=false`, 2-space indent, `(",", ": ")` separators. `BOOT_ID` = SHA-256 of base manifest JSON. MUST serialize IR to `BOOT_PACKAGE.md` without nondeterministic metadata.
