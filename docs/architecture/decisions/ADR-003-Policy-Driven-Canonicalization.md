# ADR-003: Policy-Driven Canonicalization

**Status:** Accepted
**Date:** 2026-07-11

## Context
There is no "universal" way to merge knowledge. Two conflicting facts may be a contradiction to one observer and a timeline progression to another. Hardcoding merge logic into the kernel forces semantic interpretation onto the OS.

## Decision
The Kernel will never merge Candidate Concepts into Canonical Concepts automatically. Merging requires explicit `CandidateMerged` events driven by an injected `CanonicalizationPolicy`.

## Consequences
- The Kernel remains strictly epistemic.
- Applications control the semantics of merging via pluggable policies.
