---
name: p002_specification_compression
description: Mechanically executes Audit Protocol P-002 against a given Specimen to measure Information Resilience (U-002).
---

# Skill: Specification Compression (P-002)

## Architectural Invariant
**A Skill is allowed to automate a protocol, but it is never allowed to reinterpret a protocol.**
You MUST execute the methodology exactly as written in `P-002_Specification_Compression.md`. Preserve every lineage; do not discard redundant compressions.

## Purpose
This instrument mechanically tests a Specimen for Information Resilience (U-002). It does not decide whether the protocol *should* be run.

## Inputs
- `Specimen`: The path to the specification to be compressed.
- `N`: The number of independent interpreters for verification (frozen in Audit Package).

## Execution Procedure
1. **Load Protocol**: Read the normative instructions in `P-002_Specification_Compression.md`.
2. **Execute Steps**: Mechanically perform every step of the methodology against the Specimen. 
   - Never interpret. 
   - Never optimize.
3. **Return Outputs**: Output the Fragility Curve, NID, and Evidence Package to the Laboratory Steward for archiving.
