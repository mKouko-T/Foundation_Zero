---
Document ID: DOC-SPEC-001
...
---
# Compiler Specification
1. **Pipeline**: Acyclic `COMPILER_PIPELINE.json` MUST declare dependencies. NO globbing. MAY execute topologically. MAY negotiate `capabilities`. Missing non-optional files MUST cause fatal error.
2. **Layers**: MUST enforce: Parser (raw->IR), Validation (IR->hashes/deps), Emission (Verified IR->outputs).
3. **Canonicalization**: Inputs MUST sequentially: Ingest->Strip BOM->Strict UTF-8 decode (reject invalid)->CRLF/CR to LF->Unicode NFC.
4. **Hashing**: `SHA-256(UTF8_Encode(Canonical_UTF8))`. NO raw hashing.
5. **Mode**: MUST support Pinned (immutable SHA) and Live (default branch). MUST declare mode. Uncommitted = dirty/reject.
6. **Emission**: Emit `MANIFEST_SCHEMA.json` (deterministic: alphabetical keys, `ensure_ascii=false`, 2-space indent, `(",", ": ")` separators). `BOOT_ID` = SHA-256 of base JSON. Emit `BOOT_PACKAGE.md` from IR. NO nondeterministic metadata.
