---
name: p001_independent_interpretation
description: Mechanically executes Audit Protocol P-001 against a given Specimen to measure Interpretive Stability (U-001).
---

# Skill: Independent Interpretation (P-001)

## Architectural Invariant
**A Skill is allowed to automate a protocol, but it is never allowed to reinterpret a protocol.**
You MUST execute the methodology exactly as written in `P-001_Independent_Interpretation.md`. Do not optimize, extend, or shortcut the required outputs.

## Purpose
This instrument mechanically tests a Specimen for Interpretive Stability (U-001). It does not decide whether the protocol *should* be run.

## Inputs
- `Specimen`: The path to the specification to be evaluated.
- `N`: The number of independent interpretations to generate (default provided by the Audit Package).

## Execution Procedure
1. **Load Protocol**: Read the normative instructions in `P-001_Independent_Interpretation.md`.
2. **Execute Steps**: Mechanically perform every step of the methodology. 
   - Never interpret. 
   - Never optimize.
3. **Return Outputs**: Output the Variance Report and Evidence Package to the Laboratory Steward for archiving.
