# Lossless Transition Audit

**Purpose:** To prove that a completely different executor (human, ChatGPT, Claude, Gemini, API, script, future agent) could begin from the repository tomorrow and lose **no material knowledge, rationale, decisions, constraints, hypotheses, or operational state** required for continued execution.

This audit must be performed before declaring any major session complete. The objective is not to prove the session succeeded, but to guarantee zero knowledge loss across runtime boundaries.

## I. Knowledge Loss Audit
*   Is any material reasoning trapped only in conversation?
*   Are rejected alternatives documented where they matter?
*   Are hypotheses, assumptions, and rationale preserved?
*   Are any TODOs only in conversation?
*   Is any architectural rationale missing?
*   **Goal:** Zero knowledge trapped in conversation.

## II. Repository Integrity Audit
*   Repository internally consistent.
*   Clean working tree and Remote synchronized.
*   No orphan files, stale references, or broken links.
*   `CURRENT_STATE.md` and `ACTIVE_SESSION.md` are accurate.
*   Boot succeeds cleanly.
*   No contradictory documents.

## III. Executor Independence Audit
*   No executor-specific assumptions.
*   No hidden prompt knowledge or undocumented workflow.
*   Any compliant executor can continue.
*   **ChatGPT/LLM Operational Contract:** Never assume an executor has repository access, filesystem access, Git access, terminal access, previous chats, or specific tool availability unless independently verified. Require verification for each capability.

## IV. Operational Readiness Audit
*   Current objective unambiguous (e.g., in `CURRENT_STATE.md`).
*   Next executable action defined.
*   Success criteria measurable.
*   Known risks explicit.

## V. Architectural Debt Audit
*   List every intentionally deferred hypothesis (e.g., in `ACTIVE_SESSION.md`).
*   Distinguish forgotten debt from conscious, intentional debt.

---

## The Irreversible Question
At the very end of the audit, the executor must answer this question:

> **"If this chat were permanently deleted the moment I press Enter, what would I regret not having preserved?"**

If the honest answer is anything other than "nothing material," the transition is not lossless and the session cannot close.
