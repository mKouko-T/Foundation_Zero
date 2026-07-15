---
Document ID: DOC-SPEC-001
...
Depends On: None
---

# Foundation Zero Compiler Specification

Implementations MUST adhere strictly to this specification for certification.

## 1. COMPILER_PIPELINE.json
- Compilers MUST NOT use filesystem enumeration (`glob`) to discover dependencies.
- Input ordering MUST be explicit and defined in `COMPILER_PIPELINE.json`.
- `COMPILER_PIPELINE.json` defines Compilation dependencies, NOT runtime execution order.
- The compiler MUST validate the declared graph is acyclic.
- The compiler MAY execute any valid topological ordering.
- Features MAY be negotiated via `capabilities` array.
- Missing files MUST result in immediate fatal compilation error, unless marked optional.

## 1.1 Three-Layer Architecture
The compiler MUST contain three distinct logical layers:
1. **Parser Layer**: Reads raw artifacts, parses to Canonical IR.
2. **Validation Layer**: Reads ONLY Canonical IR, generating hashes and resolving dependencies.
3. **Emission Layer**: Consumes ONLY Verified Canonical IR to emit `BOOT_MANIFEST.json` and `BOOT_PACKAGE.md`.

## 2. Canonicalization Engine
All input sources MUST pass this pipeline before parsing/hashing:
1. **Raw Bytes**: Ingest byte stream.
2. **BOM Stripping**: Strip UTF-8 Byte Order Mark (`EF BB BF`) if present.
3. **UTF-8 Decode**: Decode as strict UTF-8; reject invalid encodings.
4. **LF Normalization**: Replace CRLF and CR with LF.
5. **Unicode Normalization**: Normalize to Unicode NFC.
Result = Canonical UTF-8 text.

## 3. Hash Domain Separation
All cryptographic hashes MUST be calculated over exact UTF-8 encoded bytes of Canonical UTF-8 text. Compilers MUST NOT hash raw filesystem bytes. Algorithm: `SHA-256(UTF8_Encode(Canonical_UTF8_Text))`

## 4. Trust Model & Modes
Compilers MUST support:
- **Pinned Mode**: Fetches `BOOT_CONTEXT.md` against immutable commit SHA of `Foundation_Zero`.
- **Live Mode**: Fetches against default branch.
Mode MUST be declared. Uncommitted working-tree changes MUST be flagged "dirty" or rejected.

## 5. Certification and BOOT_ID
Compiler MUST emit a JSON manifest (`MANIFEST_SCHEMA.json`). JSON serialization MUST be mathematically deterministic:
- Keys sorted alphabetically.
- No ASCII escaping (`ensure_ascii=false`).
- 2-space indentation.
- Separators: `(",", ": ")`.
`BOOT_ID` = SHA-256 hash of serialized JSON string of base manifest.

## 6. Emission
Emitter serializes validated IR into `BOOT_PACKAGE.md`. Emitter MUST NOT inject nondeterministic metadata into package or manifest.
