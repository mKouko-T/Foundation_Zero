---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: Never
Reason Exercised: N/A

Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Playbook: Recover Chat Playbook

**Capability Required**: `foundation_recovery`
**Role**: `Researcher / Verifier`

## Procedure:
1. Load chat transcript (raw).
2. Segment into explicit conversational chunks (C001, C002, etc.).
3. Save chunks to `data/raw/chat_XXX/`.
4. Run `Evaluate_Gold_Corpus` playbook to ingest chunks into the Ledger.
