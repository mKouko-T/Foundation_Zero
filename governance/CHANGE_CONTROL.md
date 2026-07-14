# Foundation Zero Change Control

This document separates the governance authority from the implementation process, defining exactly how Foundation Zero specifications are evolved, ratified, and retired.

## 1. Specification Authority
The `Foundation_Zero` repository is the absolute authority over the language, schemas, and trust model.
Changes to the architecture MUST be merged into `Foundation_Zero` before any downstream implementation (e.g., `Cornerstone`) is allowed to execute them.

## 2. Breaking vs Non-Breaking Changes
### Breaking Changes (Major Version Increment)
- Modifying the Canonicalization Pipeline (`COMPILER_SPEC.md`).
- Altering the mathematical output of JSON serialization or Hash Domain Separation.
- Changing `MANIFEST_SCHEMA.json` required fields.
- Changing `IR_SPEC.md` abstraction layers (e.g., removing `KnowledgeState`).
- Adding, removing, or re-ordering items in `COMPILER_ORDER.json`.

### Non-Breaking Changes (Minor Version Increment)
- Adding optional fields to `MANIFEST_SCHEMA.json`.
- Refining human-readable explanations in `.md` files without altering the machine-readable specifications.

## 3. Proposal and Review Process
1. **Proposal**: A change is proposed as a Pull Request to `Foundation_Zero`. It MUST include an explanation of the *empirical reality* that necessitates the change (e.g., "The current model fails to handle X").
2. **Review**: The change is reviewed against the `EPISTEMIC_MODEL.md`. Does it increase truth, clarity, robustness, or usefulness?
3. **Ratification**: Once ratified, the machine-readable schemas (e.g., `.json`, `.yaml`) and human-readable `.md` specs are bumped to a new version tag (e.g., `v1.1`).

## 4. Retirement and Deprecation
When a specification version is deprecated:
- The ecosystem will issue a `Migration Notice`.
- Independent Certification for the deprecated version will remain available for a defined sunset period to allow implementations and repositories to migrate using the `MIGRATION_FRAMEWORK.md`.
- No new implementations will be certified against a retired specification.
