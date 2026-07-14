# Foundation Zero Certification Specification

This document defines the cryptographic trust model, certification semantics, and the exact derivation of `BOOT_ID`. 
All compiled Knowledge Operating Systems (`BOOT_PACKAGE.md`) must be cryptographically certified according to these rules.

## 1. Trust Model
Compilers implementing Foundation Zero MUST adhere to the following trust model:
1. **Git Object Identity**: Git commits, trees, and blobs are trusted as immutable cryptographic proofs of state.
2. **HTTPS Transport**: Remote retrieval of specifications (e.g., fetching `BOOT_CONTEXT.md` from GitHub) is trusted provided TLS is strictly enforced.
3. **Working Tree**: The local uncommitted working tree is **NOT TRUSTED** beyond the explicit hash it generates. Uncommitted changes MUST result in the repository commit being marked as "DIRTY".
4. **Timestamps**: Generation timestamps are inherently non-deterministic and MUST NOT be included in any certified hash payload.

## 2. Derivation of BOOT_ID
`BOOT_ID` is the cryptographic fingerprint of the entire compilation execution.
It MUST be derived by calculating the SHA-256 hash of the canonical JSON base manifest string (before the certification block is appended).

```text
BOOT_ID = SHA256(CanonicalManifest.json)
```

The `CanonicalManifest.json` MUST be serialized using exactly the rules defined in `COMPILER_SPEC.md` Section 5.

## 3. Certification Block Semantics
The base manifest MUST be sealed by appending a `certification` block containing exactly:
- `compiler_identity`: The string `"{compiler_name} {compiler_version}"`.
- `repository_commit`: The immutable SHA of the local repository (or "DIRTY").
- `manifest_hash`: The SHA-256 hash of the `CanonicalManifest.json`.
- `boot_id`: The cryptographic fingerprint derived in Section 2.
- `compiler_signature`: A cryptographic signature from the compiler verifying the build. If the compiler does not possess a private key, this MUST explicitly equal `"UNSIGNED"`.

## 4. Boot Verification
Runtimes initializing a BOOT_PACKAGE MUST verify that the `BOOT_ID` embedded in the package text exactly matches the `boot_id` stored inside the certification block of the accompanying `BOOT_MANIFEST.json`. If they diverge, the compilation is tainted and execution MUST abort.
