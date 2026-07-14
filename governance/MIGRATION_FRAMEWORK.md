# Foundation Zero Migration Framework

This framework governs how repositories relying on a specific version of Foundation Zero specifications are upgraded.

## 1. Upgrade Trigger
A migration is only initiated when reality dictates that a repository's current Foundation Zero spec version is deficient in providing the necessary runtime context or deterministic guarantees required for a task.

## 2. Migration Protocol
When upgrading a repository (e.g., from v1.0 to v2.0):

1. **Verify Implementation Compatibility:** Ensure the active compiler implementation (e.g., `Cornerstone/compiler`) is certified for the target specification version (v2.0).
2. **Halt Execution:** The repository MUST halt all domain-specific tasks.
3. **Canonical Refactor:** Re-align the repository's source documents (`BOOTSTRAP.md`, `Runtime_Contract.md`, etc.) to match the new `IR_SPEC.md` and `COMPILER_ORDER.json` of the target version.
4. **Isolated Compilation:** Run the compiler in the target mode.
5. **Certification Verification:** The new `BOOT_MANIFEST.json` MUST output `Conforms to Foundation Zero Compiler Specification v2.0`.
6. **Resume Execution:** The runtime boots into the new specification and resumes domain tasks.

## 3. Breaking Changes
Any change to `COMPILER_ORDER.json`, `MANIFEST_SCHEMA.json`, or canonicalization pipelines (`COMPILER_SPEC.md`) constitutes a **breaking change** and MUST increment the major version (e.g., v1.x to v2.x).
Repositories upgrading across major versions must strictly adhere to the Migration Protocol.
