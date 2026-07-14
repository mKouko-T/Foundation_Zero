---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: Never
Reason Exercised: N/A

Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Foundation Zero

> **Foundation Zero Specification v1.0 is frozen.**
>
> Any proposed normative modification SHALL be accompanied by reproducible evidence demonstrating a deficiency in the current specification. Preference SHALL be given to clarifications over behavioral changes. Changes that alter observable behavior constitute a new specification version.

## Standards Ecosystem & Governance

Foundation Zero operates as a formal standard, not merely a compiler implementation. The ecosystem strictly separates **Normative** constraints from **Informative** guidance. 

All documentation precedence and classifications are explicitly tracked in the machine-readable `DOCUMENT_REGISTRY.json` located in the `governance/` directory.

- **Normative Specifications (`compiler/`)**: `COMPILER_SPEC.md`, `IR_SPEC.md`, `MANIFEST_SCHEMA.json`, `COMPILER_PIPELINE.json`
- **Constitutional Governance (`governance/`)**: `FOUNDATION_CONSTITUTION.md`, `CONFORMANCE_POLICY.md`, `PHILOSOPHY_OF_STANDARDIZATION.md`
- **Audit Framework (`audit/`)**: Adversarial validation protocols (`P-000` through `P-004`).

Foundation Zero is a repository implementing the Foundation Method.

For all operational usage, documentation, and navigation:

➡ See [HOME.md](HOME.md)

The README intentionally contains no operational instructions.
