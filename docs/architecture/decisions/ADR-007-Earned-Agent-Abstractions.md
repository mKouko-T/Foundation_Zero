# ADR 007: Earned Agent Abstractions

## Status
Accepted

## Context
Initial governance designs within Foundation Zero treated "Agents" and "Skills" as proactive architecture. Directories were populated with theoretical roles (e.g., `foundation_engineering`, `foundation_governance`) acting as rules rather than capabilities.

This leads to the anti-pattern of **Skill Inflation**, where agents:
- Forget which skills to invoke.
- Drift from their intended boundaries.
- Explode maintenance costs.

## Decision
We establish the **Agent Promotion Framework**. Skills and Agents are no longer architectural folders; they are earned operational capabilities.

1. **Capability Taxonomy**
   - **Doctrine** owns constraints.
   - **Protocols** own specifications.
   - **Playbooks** own human guidance.
   - **Skills** own repeatable transformations.
   - **Agents** own objectives.
   
2. **Proactive Generation is Banned**
   No Agent or Skill may be created because it "seems useful." It must be earned through evidence.

3. **The Evidence Pipeline**
   Capabilities may move in either direction as new evidence changes their economic value.
   
   *Promotion path:*
   `Problem → Implementation → Evidence of Repeated Use → Codified Playbook → Evidence of Repeated Execution → Skill → Evidence of Repeated Orchestration → Agent`
   
   *Demotion path:*
   `Agent → Skill → Playbook → Archive → Delete`

### Promotion Properties
A capability earns **Skill** status only when there is physical evidence that it:
- Has demonstrated sufficient repeated evidence of successful execution.
- Removes repeated decisions.
- Has a stable, bounded interface.
- Has an identifiable owner.
- Is measurably cheaper to maintain than to rediscover.

A capability earns **Agent** status only when:
- It repeatedly orchestrates multiple Skills.
- It owns an objective rather than a procedure.
- Replacing it with direct Skill invocation demonstrably increases coordination cost.

## Consequences
- 7 proactive theoretical skills were demoted/deleted.
- Future capabilities must undergo a Capability Review before creation.
- Accidental complexity via "Skills pretending to be people" is eradicated.
