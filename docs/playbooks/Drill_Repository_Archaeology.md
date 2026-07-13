---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Owner: Core Maintainers
Exit Condition: Obsolete if the repository achieves total immutability and zero technical debt.
---

# Operational Drill: Repository Archaeology

**Purpose:** To systematically reconstruct the original intent behind an obsolete, strange, or poorly understood artifact before making irreversible changes or deletions. 

**Trigger:** When encountering an artifact where the Information Owner is unknown, or the `Why does this exist?` answer is lost.

## The Archaeological Method

When investigating a mysterious artifact, execute the following steps in order. Do not skip to deletion until all steps are complete.

### 1. The Evidence Scan
1. Run `git log --follow -p <file>` to trace its entire physical mutation history.
2. Identify the original author and the PR/Commit that introduced it.

### 2. The Semantic Link
1. Search the repository (`grep`) for the file's exact name.
2. If it is referenced by an `ADR` or `PROPOSAL`, read the source decision.
3. If it is referenced by a `Playbook`, determine if the Playbook is still actively executed.

### 3. The Usage Test
1. Temporarily rename or move the file.
2. Run the Verification Suite (`scripts/audit.py`) and full system tests.
3. If tests pass, the artifact is operationally dead. If tests fail, you have found the hidden dependency.

### 4. The Final Verdict
Based on the reconstruction, apply one of the following:
- **Revive:** Update the file, attach clear Information Ownership, and fix the `Exit Condition`.
- **Absorb:** Move its knowledge into a more appropriate, central owner file, then delete the original.
- **Eradicate:** If it is operationally dead and holds no lasting knowledge, delete it.

**Final Interrogation:** *Why wasn't this deleted earlier?* (Document the organizational failure that allowed this artifact to persist).
