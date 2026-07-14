---
Document ID: R-001H
Title: Normative/Informative Dependence
Status: Released
Version: 1.0
Classification: Evidence
Authority: Foundation Zero
---

# Normative/Informative Dependence

**Origin Audit:** P-001 Independent Interpretation  
**Evidence Source:** Submission W  
**Independent Replications:** 1  

## Question
Can the normative specification be implemented without consulting informative documentation?

## Observed Facts
Submission W (Cold Reader) received only normative documents and failed to resolve basic architectural goals like the purpose of `boot_id`.

## Reproduced Behavior
Submission W was forced to guess the semantic meaning of fields missing from the normative schemas.

## Observed Divergence
The Cold Reader produced a technically compliant but semantically useless implementation.

## Competing Explanations
The normative schemas are mechanically complete but semantically incomplete.

## Evidence Against This Interpretation
Submission Y (Rust) also received only normative docs but used standard software engineering patterns to bridge the semantic gap.

## Residual Uncertainty
It is unknown if the standard is currently self-hosting without its own history.

## Observation Confidence
Medium (Observed in the Cold Reader, partially observed in Rust).
