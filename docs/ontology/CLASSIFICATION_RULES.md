# Classification Rules

This document specifies deterministic rules for classifying raw `Assertions` into specific knowledge ontology types.

## The Assertion Pipeline
Every piece of recovered intelligence begins as an **Assertion**. The pipeline separates *extraction* from *interpretation*.

`Source -> Extraction -> Assertion -> Classification -> Ontology Node`

## Rules

### Rule 1: Observation
**If** the Assertion describes a factual, immutable occurrence or state in reality without proposing a mechanism, **Then** it classifies as an `Observation`.
*Example: "The migration script failed on file X at 14:00."*

### Rule 2: Claim
**If** the Assertion is a statement extracted from a Source that requires verification before it can be universally trusted, **Then** it classifies as a `Claim`.
*Example: "Framework Y is 50% faster than Framework Z."*

### Rule 3: Hypothesis
**If** the Assertion proposes a mechanism, explanation, or testable prediction based on Observations, **Then** it classifies as a `Hypothesis`.
*Example: "If we use cryptographic hashing during migration, data corruption will drop to zero."*

### Rule 4: Decision
**If** the Assertion represents a formal, irreversible architectural or governance choice made by the system or team, **Then** it classifies as a `Decision`.
*Example: "We will strictly use JSON for all machine-readable states."*

### Rule 5: Requirement
**If** the Assertion mandates a capability, constraint, or condition that the system must fulfill, **Then** it classifies as a `Requirement`.

### Rule 6: Risk
**If** the Assertion identifies a potential failure mode, hazard, or source of technical debt, **Then** it classifies as a `Risk`.

### Default: UNCLASSIFIED
If an Assertion does not cleanly match any of the above strict deterministic rules, it remains in the `UNCLASSIFIED` queue. **Never force classification. Unknown is a valid state. Wrong is not.**
