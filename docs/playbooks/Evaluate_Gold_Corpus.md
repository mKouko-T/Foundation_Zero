---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: Never
Reason Exercised: N/A

Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Playbook: Evaluate Gold Corpus Playbook

**Capability Required**: `foundation_engineering`
**Role**: `Evaluator`

## Procedure:
1. Identify the next raw chunk from `data/raw/chat_001/`.
2. Extract physical objective spans (Observation).
3. Apply ontological constraints (Assessment).
4. Propose synthesis (CandidateConceptProposed).
5. Output strict JSON array of `EpistemicEvent`s matching `docs/specification/EVENT_TYPES.md`.
6. Save to `tests/corpora/gold/chunk_[N]_gold.json`.
7. Verify parser against `tests/corpora/gold/chunk_001_gold.json` schema.
