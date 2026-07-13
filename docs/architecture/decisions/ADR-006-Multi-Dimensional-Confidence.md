# ADR 006: Multi-Dimensional Confidence

## Status
Accepted

## Context
Traditional systems represent "confidence" as a single scalar value (e.g., `0.95`). This forces evaluators to conflate two completely distinct epistemic concepts:
1. **Semantic Confidence**: "How sure am I that my interpretation of this specific text is correct?"
2. **Evidence Completeness**: "How much of the total available evidence have I actually looked at before making this assertion?"

A single scalar value makes it impossible to distinguish between a highly accurate assessment of a single sentence (High Semantic, Low Completeness) and a vague assessment of an entire book (Low Semantic, High Completeness).

## Decision
Confidence in Foundation Zero must be strictly multi-dimensional. The `MultiDimensionalConfidence` object must explicitly decouple these vectors. Most importantly, it must include an `evidence_completeness` metric.

## Consequences
- **Positive**: The Projection layer can now differentiate between "True but Localized" and "True and Comprehensive."
- **Positive**: It prevents a high-confidence assessment of Chunk 1 from blocking contradictory assessments from Chunk 50, because the ledger knows the Chunk 1 assessment only had an `evidence_completeness` of ~1%.
- **Negative**: Evaluators are forced to compute and emit more complex JSON structures rather than returning a simple float.
