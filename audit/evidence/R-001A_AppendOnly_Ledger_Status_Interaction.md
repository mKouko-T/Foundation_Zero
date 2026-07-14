---
Document ID: R-001A
Title: Append-Only Ledger Status Interaction
Status: Released
Version: 1.0
Classification: Evidence
Authority: Foundation Zero
---

# Append-Only Ledger Status Interaction

**Origin Audit:** P-001 Independent Interpretation  
**Evidence Source:** Submission X, Submission Z  
**Independent Replications:** 2  

## Question
Does the specification resolve the interaction between the Constitution's append-only mandate and the mutation of the ledger's status property?

## Observed Facts
Constitution #1 requires append-only events. `ledger.schema.json` defines a status string that transitions to 'promoted'.

## Reproduced Behavior
Implementations mutate the JSON array in place to satisfy the schema validation.

## Observed Divergence
No direct divergence in observable behavior, but universal forced non-compliance with Constitution #1.

## Competing Explanations
1. Append-only applies to ledger entries, not internal status fields. 2. The schema implicitly assumes an unstated event-sourcing log.

## Evidence Against This Interpretation
If status is mutable, cryptographic immutability of past candidate states is lost upon promotion, which contradicts the ledger's stated purpose.

## Residual Uncertainty
It is unknown if the schema or the Constitution takes precedence in this specific lifecycle event.

## Observation Confidence
High (Observed independently by 2 isolated teams).
