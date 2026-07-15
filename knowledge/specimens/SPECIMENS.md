# Specimens

A **Specimen** is a first-class object in the Foundation Zero methodology. 

It represents the raw, domain-specific artifact (e.g., a compiler specification, a legal contract, a medical protocol, an API definition) that is subjected to experimental evaluation.

> **Immutability Constraint**: A Specimen is intentionally immutable during an Experiment. Any modification produces a new Specimen or a derived artifact. This prevents future protocols from editing the specimen and contaminating experiments.

## Why Separate Specimens?
By explicitly defining the object under test as a "Specimen", Foundation Zero maintains a clean separation between the methodology and the domain:

```
Specimen
  ↓
Protocol
  ↓
Evidence
  ↓
Coordinate
```

Protocols (like P-001 or P-002) measure uncertainty.
Coordinates (like U-001 or U-002) describe the underlying phenomena.
Specimens are merely the material placed under the microscope.

This separation prevents domain-specific assumptions from leaking into the core scientific methodology, enabling future protocols to evaluate entirely different kinds of specifications with equal rigor.
