# Experiments

An **Experiment** is a first-class object in the Foundation Zero methodology. It represents a single, verifiable execution of a methodology against a target.

## The Scientific Lifecycle

To prevent the overloading of evidence folders and ensure rigorous traceability across multiple domains, Foundation Zero enforces the following conceptual model:

```
Coordinate (What we are measuring)
    ↓
Protocol (How we measure it generally)
    ↓
Experiment (One specific execution)
    ↓
Evidence (The raw outputs)
    ↓
Observation (The analyzed findings)
    ↓
Knowledge (The resulting certainty)
```

## Protocol vs. Experiment
- **Protocol:** A reusable methodology (e.g., P-001, P-002). It is domain-agnostic and target-agnostic.
- **Experiment:** The specific application of a Protocol to a specific Specimen, using specific variables (e.g., *Run P-002 against Compiler Spec A with N=4*).

Every piece of Evidence must trace back not just to a Protocol, but to a specific Experiment. This prevents the commingling of results across different execution lineages, specimens, or variable configurations.
