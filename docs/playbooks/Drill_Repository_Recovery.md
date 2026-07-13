---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: Never
Reason Exercised: N/A
Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Operational Drill: Repository Recovery

**Purpose:** To prove mathematically that the repository can reconstruct itself from its foundational ledger without hidden dependencies.

**Frequency:** Every 6 Months.

## Protocol
Execute the following scenarios in an isolated, cloned workspace. If the system fails to recover its operational state, hidden dependencies exist and MUST be eradicated.

### Scenario A: Loss of Generated Artifacts
1. **Action:** Delete the entire `artifacts/` or `.system_generated/` folders.
2. **Success Criteria:** A single compilation command re-generates all JSON projections and verification reports perfectly.

### Scenario B: Loss of Operational State
1. **Action:** Delete `state/*.json` entirely.
2. **Success Criteria:** The state engine rebuilds the current `CURRENT_PHASE.md` and runtime metrics purely from the Event Ledger.

### Scenario C: Loss of Documentation (Projections)
1. **Action:** Delete all derived Markdown reports.
2. **Success Criteria:** The orchestrator rewrites the reports precisely from the kernel logic and the physical code.

### Scenario D: Loss of CI Configuration
1. **Action:** Delete the CI YAML pipeline definitions.
2. **Success Criteria:** The `scripts/audit.py` can still be run locally without requiring pipeline magic to enforce rules.

### Scenario E: Loss of Evaluator Prompts
1. **Action:** Delete the external LLM system prompts.
2. **Success Criteria:** The repository contains the `AUDITOR_PROMPT.txt` and agent schemas within `.agents/` as explicit Code. The agent can be instantly reconstituted.

## Failure Mitigation
If any scenario fails, it proves the existence of **Operational Magic** (undocumented assumptions). Open a bug, trace the dependency, and codify it.
