---
Document ID: DOC-GOV-003
Title: Philosophy of Standardization
Status: Released
Version: 1.0
Classification: Informative
Authority: Foundation Zero
Supersedes: None
Superseded By: None
Depends On: None
---

# Philosophy of Standardization

This document outlines the core constitutional philosophy of Foundation Zero. It defines the principles under which the standard operates and evolves.

## 1. Specifications are Products

Foundation Zero is not a compiler. It is a standard. 
- **Specifications are the product.**
- **Implementations are the consumers of that product.**

## 2. Observable Behavior

The standard dictates **observable behavior**, not internal implementation details. A compliant implementation may use any internal architecture (e.g., ASTs, interpreters, JIT) so long as the observable output perfectly matches the specification and canonical hashes.

## 3. Evidence-Based Conformance

Conformance is strictly evidence-based. No compiler is considered compliant merely by self-declaration. Conformance requires deterministic, reproducible evidence produced according to the Audit Protocols.

## 4. Independent Verification

The highest measure of a specification's quality is whether independent teams, with no shared context, can produce conforming implementations.
- **Ambiguity is a specification defect.** It is never the implementer's fault.

## 5. Extension Mechanism

Implementers may need to innovate or offer platform-specific features without waiting for the standard to evolve. To prevent forking, Foundation Zero defines specific extension namespaces:
- `experimental/`
- `vendor/`
- `private/`

Extensions must be declared inside one of these namespaces in the Manifest and the Canonical IR. Using standard fields for non-standard behavior is a fatal conformance violation.

## 6. Informative Boundaries

**Informative documents can never modify normative behavior.** This philosophy document, ADRs, walkthroughs, and tutorials exist to provide rationale and context. In any dispute between informative context and a normative specification, the normative specification wins absolutely.
