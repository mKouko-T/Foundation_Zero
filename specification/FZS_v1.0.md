# Foundation Zero Specification (FZS)
**Version:** 1.0

## 1. Introduction
Foundation Zero is a reproducible engineering discipline for transforming unstructured human history into governed, evidence-backed institutional intelligence.

## 2. Core Concepts
- **Recovery:** Extracting propositional claims from evidence.
- **Ledger:** The immutable record of recovered propositions.
- **Promotion:** The state transition of a proposition into operational canon.
- **Verification:** Read-only audits of ledger integrity.

## 3. Conformance
A repository conforms to FZS v1.0 if and only if it satisfies the following invariants:
1. It maintains an immutable certification ledger that conforms to `ledger.schema.json`.
2. It enforces a read-only verification boundary before promotion.
3. Every architectural decision is recorded as an ADR.
4. It strictly versions its repository, protocol, and schemas independently.

## 4. Non-Goals
Foundation Zero **does not** specify:
- Programming languages
- Storage formats (e.g., Markdown vs DB)
- AI models or LLM providers
- Version control platforms
- Cloud providers
These are left to the implementation.
