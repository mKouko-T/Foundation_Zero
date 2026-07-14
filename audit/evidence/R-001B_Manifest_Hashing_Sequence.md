---
Document ID: R-001B
Title: Manifest Hashing Sequence
Status: Released
Version: 1.0
Classification: Evidence
Authority: Foundation Zero
---

# Manifest Hashing Sequence

**Origin Audit:** P-001 Independent Interpretation  
**Evidence Source:** Submission Y, Submission W  
**Independent Replications:** 2  

## Question
Does the specification define a mathematically valid sequence for calculating the boot_id hash while satisfying the manifest schema?

## Observed Facts
The spec requires hashing the base manifest to produce `boot_id`, then appending the certification block. `MANIFEST_SCHEMA.json` strictly marks `certification` as required.

## Reproduced Behavior
Implementations had to either fail schema validation during the hashing step, or inject a placeholder certification block.

## Observed Divergence
Divergent approaches to bypassing the schema validation during the intermediate hashing step.

## Competing Explanations
1. The schema validates the final output, not the intermediate state. 2. The text 'base manifest' implies a separate, undocumented schema.

## Evidence Against This Interpretation
The JSON schema explicitly sets `certification` as required, meaning any intermediate state missing it is invalid by definition.

## Residual Uncertainty
It is unknown how to deterministically represent the intermediate state before certification.

## Observation Confidence
High (Observed independently by 2 isolated teams).
