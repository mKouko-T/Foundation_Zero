---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: 2026-07-13
Reason Exercised: Initial Creation
Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Anti-Patterns

**Definition:** An anti-pattern is a known, proven bad solution. It is an active failure mode that this repository has personally survived. When an anti-pattern is detected, it must be actively eradicated.

Unlike Smells (which are weak heuristics), Anti-Patterns are documented historical mistakes.

## 1. Architecture Inflation
**Symptoms:** In response to a critique or a bug, 3 to 10 new concepts/files are proposed instead of modifying the existing contracts.
**Root Cause:** Assuming that adding complexity solves problems faster than enforcing discipline.
**Why it's dangerous:** It exponentially increases the body of knowledge required to operate the system.
**Preferred Correction:** "Default response to criticism is subtraction. Only add something when subtraction fails."

## 2. Optimistic Completion
**Symptoms:** An agent executes a write command and immediately reports success without physically reading the resulting file back from disk to verify it.
**Root Cause:** Assuming that because a command did not throw an error, it achieved its semantic intent.
**Why it's dangerous:** Leads to empty files, truncated outputs, and silent data loss.
**Preferred Correction:** The Verification Postcondition (Doctrine 13). No operation may report SUCCESS without verifying the resulting external state against its postconditions.

## 3. Agreement Bias
**Symptoms:** An agent or engineer instantly agrees with a proposal simply because time has been spent on it, even when reality contradicts it.
**Root Cause:** Prioritizing conversational consistency over physical reality.
**Why it's dangerous:** It allows fundamentally broken paradigms to survive indefinitely.
**Preferred Correction:** Reality over Identity. Reality outranks consistency.

## 4. Prompt Dependency
**Symptoms:** Complex business logic or architectural rules are stored only in an LLM's system prompt or active context window.
**Root Cause:** "We'll Remember" (Doctrine 15). Treating human or agent memory as infrastructure.
**Why it's dangerous:** The moment the context window closes, the knowledge is permanently destroyed.
**Preferred Correction:** Governance as Code. If it matters, it must be written to the repository.

## 5. Hidden Operational Knowledge
**Symptoms:** A process requires a specific sequence of commands, but those commands are only known to one engineer or agent and are never written down.
**Root Cause:** Speed over documentation.
**Why it's dangerous:** Creates single points of failure and prevents deterministic replay.
**Preferred Correction:** Playbooks for everything.

## 6. Premature Generalization
**Symptoms:** Creating a highly abstract `AbstractManagerFactory` before even writing a single concrete implementation.
**Root Cause:** Anticipating future needs that do not yet exist in reality.
**Why it's dangerous:** Bloats the Kernel with unused capabilities.
**Preferred Correction:** The Rule of Two. Kernel earns abstractions only through repeated implementation (Doctrine 5).

## 7. Ontology Expansion
**Symptoms:** Inventing new terms, folders, or concepts (e.g., `knowledge/unknowns/`) when existing paradigms (e.g., `evidence/`) perfectly cover the use case.
**Root Cause:** The desire to organize instead of the desire to execute.
**Why it's dangerous:** Creates redundant layers that confuse the "Source of Truth."
**Preferred Correction:** The Invention Rule. Do not invent ontology without explicit necessity.

## 8. Semantic Leakage
**Symptoms:** Putting budgets into `state/` or putting dynamic execution logs into `docs/governance/`.
**Root Cause:** Failing to distinguish between frozen rules, ephemeral state, and historical evidence.
**Why it's dangerous:** Destroys the integrity of the layers, leading to automated tools mutating governance.
**Preferred Correction:** Strict adherence to the 6-Layer Architectural Backbone.

## 9. Component Proliferation
**Symptoms:** Solving a minor data parsing bug by introducing an entirely new microservice or agent sub-system.
**Root Cause:** Ignoring the highest-leverage dependency.
**Why it's dangerous:** Increases system fragility for minimal gain.
**Preferred Correction:** Fix the existing component.

## 10. Verification by Assertion
**Symptoms:** Claiming "The repository satisfies all rules" without running a mechanical test.
**Root Cause:** Optimism.
**Why it's dangerous:** It is intellectually dishonest and factually incorrect.
**Preferred Correction:** The Verification Suite.

## 11. Human Memory as Infrastructure
**Symptoms:** "I'll just remember to update this file next time."
**Root Cause:** Laziness.
**Why it's dangerous:** Memory is ephemeral. Repositories must outlive their creators.
**Preferred Correction:** Ban "We'll Remember." Build an explicit task or CI check.
