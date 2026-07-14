---
Document ID: R-001D
Title: Cryptographic Algorithm Definition
Status: Released
Version: 1.0
Classification: Evidence
Authority: Foundation Zero
---

# Cryptographic Algorithm Definition

**Origin Audit:** P-001 Independent Interpretation  
**Evidence Source:** Submission Y, Submission Z, Submission W  
**Independent Replications:** 3  

## Question
Does the specification uniquely determine the cryptographic algorithms required for hashes and signatures?

## Observed Facts
The spec mandates `bios_hash` and `compiler_signature` but lists no cryptographic standards (e.g., SHA-256, Ed25519).

## Reproduced Behavior
Implementations assumed SHA-256 based on industry defaults or inserted dummy strings.

## Observed Divergence
Signatures diverged wildly (dummy strings vs omitted). Hashes converged only because all teams guessed SHA-256.

## Competing Explanations
The specification relies on industry cultural defaults for cryptography.

## Evidence Against This Interpretation
Without explicit standards, future implementations could choose SHA-512, breaking consensus.

## Residual Uncertainty
It is unknown which signature algorithm is expected by the verification boundary.

## Observation Confidence
High (Observed independently by 3 isolated teams).
