---
Document ID: R-001C
Title: Provenance Model Consistency
Status: Released
Version: 1.0
Classification: Evidence
Authority: Foundation Zero
---

# Provenance Model Consistency

**Origin Audit:** P-001 Independent Interpretation  
**Evidence Source:** Submission Y, Submission W  
**Independent Replications:** 2  

## Question
Does the specification provide a consistent structural definition of the Provenance object across all normative documents?

## Observed Facts
IR_SPEC.md groups `dependency_graph` and `file_hashes` under a `Provenance` block. MANIFEST_SCHEMA.json limits provenance to a string map and hoists the other fields to the root.

## Reproduced Behavior
Implementations were forced to choose which document took precedence.

## Observed Divergence
Submission W favored the Manifest Schema. Submission Y favored the IR Spec.

## Competing Explanations
1. The IR Spec is conceptual, the Manifest Schema is literal. 2. The Manifest Schema is outdated.

## Evidence Against This Interpretation
Neither document indicates precedence over the other in this specific structural conflict.

## Residual Uncertainty
It is unknown which artifact governs the final JSON structure.

## Observation Confidence
High (Observed independently by 2 isolated teams).
