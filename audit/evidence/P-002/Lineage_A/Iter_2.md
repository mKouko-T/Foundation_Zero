---
Document ID: DOC-SPEC-001
...
---
# Compiler Specification
Implementations MUST adhere strictly.

## 1. Pipeline & Architecture
- Dependencies MUST be explicitly declared in `COMPILER_PIPELINE.json` (defines compilation order). NO filesystem enumeration.
- Compiler MUST validate graph is acyclic; MAY execute any valid topological order.
- Features MAY be negotiated via `capabilities` array.
- Missing non-optional files MUST trigger immediate fatal error.
- MUST enforce 3 layers: Parser (reads raw, outputs IR), Validation (reads ONLY IR, generates hashes/dependencies), Emission (reads ONLY verified IR, emits outputs).

## 2. Canonicalization & Hashing
- Input sources MUST process sequentially: 1) Ingest bytes, 2) Strip BOM (`EF BB BF`), 3) Decode strict UTF-8 (reject invalid), 4) Normalize CRLF/CR to LF, 5) Normalize Unicode NFC. Result = Canonical UTF-8.
- Cryptographic hashes MUST target exact UTF-8 encoded bytes of Canonical UTF-8 text. NO hashing raw bytes. Algorithm: `SHA-256(UTF8_Encode(Canonical_UTF8))`.

## 3. Execution & Emission
- MUST support Pinned Mode (fetch via immutable SHA) and Live Mode (default branch). Mode MUST be declared. Uncommitted changes MUST be flagged "dirty" or rejected.
- MUST emit `MANIFEST_SCHEMA.json`. JSON MUST be deterministic: alphabetical keys, `ensure_ascii=false`, 2-space indent, `(",", ": ")` separators.
- `BOOT_ID` = SHA-256 of serialized base manifest JSON.
- Emitter MUST serialize IR to `BOOT_PACKAGE.md`. MUST NOT inject nondeterministic metadata.
