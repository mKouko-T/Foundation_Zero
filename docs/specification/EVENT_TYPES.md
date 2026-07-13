# Foundation Zero Event Vocabulary

This is the formal protocol for Epistemic Events. Altering these schemas requires a formal protocol migration.

## Active Events (v1.0)
- `ObservationAppended`: An objective span or structural extract recorded from an artifact.
- `AssessmentAppended`: A semantic evaluation of an observation mapped to the Ontology.
- `CandidateConceptProposed`: An emergent concept synthesized from assessments.
- `CanonicalConceptAccepted`: A canonicalized concept securely entering the Knowledge Graph.
- `CandidateMerged`: An explicit operation merging a candidate into a canonical concept.
- `ConceptDeprecated`: A formal deprecation of a canonical concept.

## Deprecation, Versioning & Compatibility
- **Immutability:** Events are permanently immutable. You cannot change a schema retroactively.
- **Compatibility & Migration:** Schema changes must introduce a new event type (e.g., `AssessmentAppended_v2`). The Projection layer is responsible for backwards compatibility parsing and data migration. 
- **Reserved Namespaces:** All event types prefixed with `System` or `Core` are reserved for the Kernel. Applications must use their own prefixes if defining custom application-level ledger events (e.g., `App_PDF_Extracted`).
