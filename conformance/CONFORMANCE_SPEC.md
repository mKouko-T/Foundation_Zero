# Foundation Zero Conformance Specification

This document defines the objective criteria required for any compiler implementation to be certified against the Foundation Zero specification.
Implementations do not "pass" intrinsically; they conform.

## 1. Objective of Certification
Certification is an empirical process. An implementation may only declare `Conforms to Foundation Zero Compiler Specification vX.Y` if it perfectly passes all defined conformance tests.

## 2. Test Fixtures

### Test 1: Cross-Platform Determinism
- **Input**: A mock Foundation Zero repository.
- **Variant A**: All files saved with `\r\n` (CRLF) line endings.
- **Variant B**: All files saved with `\n` (LF) line endings.
- **Expected Output**: Both Variant A and Variant B MUST produce identical `BOOT_ID`s and identical `BOOT_MANIFEST.json` bytes.

### Test 2: Unicode Normalization (NFC)
- **Input**: A mock repository containing a document with the character `é` represented as `U+00E9` (NFC) in Variant A, and `U+0065 U+0301` (NFD) in Variant B.
- **Expected Output**: Both Variant A and Variant B MUST produce identical `BOOT_ID`s.

### Test 3: Byte Order Mark (BOM) Stripping
- **Input**: A repository where `BOOTSTRAP.md` begins with the UTF-8 BOM (`EF BB BF`).
- **Expected Output**: The compiler MUST strip the BOM. The resulting `BOOT_ID` MUST match a control repository lacking the BOM.

### Test 4: Manifest JSON Canonicalization
- **Input**: Any valid compilation.
- **Expected Output**: The emitted `BOOT_MANIFEST.json` MUST exactly match the output of an RFC 8785 compliant JSON canonicalization function. There MUST be no trailing whitespace on lines, 2-space indentation, no ASCII escaping, and dictionary keys MUST be strictly alphabetized.

### Test 5: Missing Dependency Fatal
- **Input**: A repository missing `docs/Canonical_Model.md`.
- **Expected Output**: The compiler MUST immediately exit with a FATAL exception. It MUST NOT emit a partial package.

### Test 6: Ambiguity Rejection
- **Input**: A repository containing `docs/Canonical_Model.md` and `docs/Canonical_Model_v2.md`.
- **Expected Output**: The compiler MUST immediately exit with an AMBIGUITY FATAL exception.

### Test 7: Pinned vs Live Mode
- **Input**: The compiler is invoked in Pinned Mode targeting commit SHA `abcdef123...`.
- **Expected Output**: The `remote_commit_sha` in the manifest MUST equal `abcdef123...`, and the `hash_sha256` MUST be the deterministic hash of that specific commit's `BOOT_CONTEXT.md`.

## 3. Certification Declaration
If a compiler passes all 7 tests, it may output the following string to `stdout` upon successful compilation:

```text
COMPILATION SUCCESSFUL.
Conforms to Foundation Zero Compiler Specification v1.0
```
