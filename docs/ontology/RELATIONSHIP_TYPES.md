# Relationship Types

Edges in Foundation Zero connect the Semantic Universe. They are organized into four distinct structural families.

## 1. Causal (Provenance & Transformation)
These relationships model how things come to exist through time.
- `generated_from`: Connects an output directly to the Transformation or Session that produced it.
- `derived_from`: Connects a downstream entity to its upstream origin (e.g., Assertion derived from Signal).
- `extracted_from`: Connects a Signal to its Source Origin.
- `caused_by`: Connects an Event, Issue, or State change to its trigger.
- `transformed_by`: Connects a raw Signal to the Extraction Algorithm that parsed it.

## 2. Semantic (Meaning & Reasoning)
These relationships model logic, taxonomy, and inference.
- `supports`: Connects an Assessment/Evidence to a Belief, increasing its Confidence.
- `contradicts`: Connects an Assessment/Evidence to a Belief, decreasing its Confidence.
- `explains`: Connects a Hypothesis to an Observation.
- `specializes`: Connects a narrower concept to a broader one.
- `generalizes`: Connects a broader concept to a narrower one.
- `instantiates`: Connects a specific occurrence to a general concept.
- `equivalent_to`: Declares strict semantic equality between two nodes.
- `inferred_from`: Connects an Inference to the Facts or Beliefs that justify it.

## 3. Operational (Execution & Compliance)
These relationships model how the system runs and enforces rules.
- `implements`: Connects Source Code or Capability to a Specification.
- `depends_on`: Indicates a hard architectural or functional requirement.
- `governs`: Connects a Protocol, Specification, or Decision to the entities it regulates.
- `satisfies`: Connects an Implementation or Artifact to a Requirement/Constraint.
- `certifies`: Connects an Authority or Ledger to an Operational Canon.

## 4. Temporal (Lifecycle)
These relationships model sequence and validity over time.
- `supersedes`: Connects a new Decision, Protocol, or Version to the one it replaces.
- `precedes`: Explicitly orders two events chronologically.
- `succeeds`: The inverse of precedes.
- `valid_during`: Connects a Belief or Assessment to a specific time window or epoch.
