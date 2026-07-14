---
Document ID: R-001E
Title: JSON Canonicalization Rules
Status: Released
Version: 1.0
Classification: Evidence
Authority: Foundation Zero
---

# JSON Canonicalization Rules

**Origin Audit:** P-001 Independent Interpretation  
**Evidence Source:** Submission Z, Submission W  
**Independent Replications:** 2  

## Question
Does the specification uniquely determine the serialization rules for JSON prior to cryptographic hashing?

## Observed Facts
Hashes must be produced from JSON structures, but no canonicalization rules (RFC 8785) are referenced.

## Reproduced Behavior
Submission W used Python's default sorting. Submission Z manually defined whitespace rules.

## Observed Divergence
Identical logical states would produce differing hashes depending on the language's native JSON stringify behavior.

## Competing Explanations
1. The specification expects RFC 8785 canonicalization implicitly. 2. The specification missed the requirement.

## Evidence Against This Interpretation
There is no text suggesting canonicalization is required, meaning raw string hashes are technically compliant.

## Residual Uncertainty
It is unknown how to guarantee identical hashes across different languages.

## Observation Confidence
High (Observed independently by 2 isolated teams).
