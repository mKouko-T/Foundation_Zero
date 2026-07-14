# Foundation Zero Compiler Specification

This document defines the mathematical and deterministic pipeline required to compile a Foundation Zero repository into an executable Knowledge Operating System (`BOOT_PACKAGE.md` and `BOOT_MANIFEST.json`). 
Any implementation across any programming language MUST adhere strictly to this specification to be certified.

## 1. Compilation Ordering
Compilers MUST NOT rely on filesystem enumeration (e.g., `glob`) to discover dependencies. The ordering of inputs MUST be explicit, deterministic, and sequenced exactly as defined in `COMPILER_ORDER.json`.
The specification explicitly separates the human-readable explanation (`COMPILER_SPEC.md`) from the machine-readable sequence (`COMPILER_ORDER.json`). Implementations MUST dynamically fetch and consume `COMPILER_ORDER.json` to derive the compilation graph.

Missing files MUST result in an immediate fatal compilation error, unless explicitly marked as optional.

## 2. Canonicalization Engine
To guarantee cross-platform bit-for-bit determinism, all input sources (local and remote) MUST be passed through the following canonicalization pipeline before any parsing or hashing occurs:
1. **Raw Bytes**: Ingest the raw byte stream.
2. **BOM Stripping**: Explicitly detect and strip the UTF-8 Byte Order Mark (`EF BB BF`) if present.
3. **UTF-8 Decode**: Decode the byte stream as strict UTF-8. Reject invalid encodings.
4. **LF Normalization**: Replace all occurrences of `\r\n` (CRLF) and `\r` (CR) with `\n` (LF).
5. **Unicode Normalization**: Normalize the string to Unicode NFC (Normalization Form C).

The resulting string is the **Canonical UTF-8 text**.

## 3. Hash Domain Separation
All cryptographic hashes (e.g., file provenance, remote identity) MUST be calculated over the exact UTF-8 encoded bytes of the **Canonical UTF-8 text**.
Compilers MUST NOT hash raw filesystem bytes.
Algorithm: `SHA-256(UTF8_Encode(Canonical_UTF8_Text))`

## 4. Trust Model & Modes
Compilers MUST support two remote fetch modes:
- **Pinned Mode (Preferred)**: Fetches `BOOT_CONTEXT.md` against a specific, immutable commit SHA of the `Foundation_Zero` repository.
- **Live Mode**: Fetches against the default branch (`main`).
The mode used MUST be declared in the execution environment or defaults. The compiler trusts HTTPS transport and Git object identities as immutable. Uncommitted working-tree changes MUST be flagged as "dirty" or rejected.

## 5. Certification and BOOT_ID
The compiler MUST emit a machine-readable JSON manifest (`MANIFEST_SCHEMA.json`).
JSON serialization MUST be mathematically deterministic:
- Keys sorted alphabetically.
- No ASCII escaping (`ensure_ascii=false`).
- 2-space indentation.
- Separators: `(",", ": ")`.

The `BOOT_ID` is the SHA-256 hash of the complete, serialized JSON string of the base manifest (prior to appending the certification block).

## 6. Emission
The Emitter serializes the validated Intermediate Representation (`IR_SPEC.md`) into a single executable artifact (`BOOT_PACKAGE.md`). The emitter MUST NOT inject nondeterministic metadata (e.g., generation timestamps, local absolute paths, hostname, Python version) into either the package or the manifest.
