---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Owner: Core Maintainers
Exit Condition: Merged into an automated Capability Manager.
---

# Drill: Capability Review

This playbook defines the procedure for reviewing, promoting, or demoting operational capabilities (Playbooks, Skills, and Agents) within Foundation Zero. It enforces the rules laid out in `ADR-007`.

## Trigger
Execute this review at the end of every major implementation milestone or at minimum once a month.

## Execution Steps

### 1. The Evidence Audit
Analyze the execution logs (`walkthrough.md` artifacts, PR histories, `state/` modifications) and answer:
- Which business decision became easier?
- Which Playbooks/Skills were actively invoked?
- How often were they used?
- What was their permanent maintenance cost?
- Are there any recurring problems/conversations that currently lack a codified playbook?

### 2. Demotion (Accidental Complexity Eradication)
For any existing Capability (Playbook, Skill, or Agent):
- If there is **no evidence** of use or continuing value → DELETE IT.
- If it contains useful knowledge but doesn't meet the Promotion threshold → DEMOTE IT (e.g., Skill becomes a Playbook, Playbook becomes reference notes).
- If its knowledge overlaps with another → MERGE IT.

### 3. Promotion (Earning Abstractions)
Review recurring implementation patterns. Apply the **Promotion Pipeline**:

**A. Promote to Playbook if:**
- A problem has been implemented manually multiple times with success.

**B. Promote Playbook to Skill if:**
- It has been executed repeatedly.
- It removes repeated decisions.
- It has a stable, bounded interface.
- It is measurably cheaper to maintain than to rediscover.

**C. Promote Skill(s) to Agent if:**
- It repeatedly orchestrates multiple skills.
- It owns a specific objective.
- Manual skill orchestration has become a bottleneck.

### 4. Log the Decisions
Any promotions or demotions must be recorded in `walkthrough.md` with explicit physical evidence justifying the transition.
