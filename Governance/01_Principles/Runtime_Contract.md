# Runtime Contract

This document serves as the "API for Intelligence" within Foundation Zero. It defines exactly what any runtime—whether Human, LLM, API, Script, or Autonomous Agent—is permitted to do within the repository.

## 1. Permissions & Restrictions

### Can a runtime delete files?
**Yes.** Runtimes are encouraged to propose the deletion of obsolete files, stale logs, and unused capabilities. Deletion reduces entropy. Deletion of constitutional artifacts requires Steward approval.

### Can a runtime create architecture?
**No.** Runtimes may not create new governance artifacts, directories, ledgers, or registers without invoking the Two-Failure Rule and obtaining explicit Steward approval. Runtimes create *evidence*, not architecture.

### Can a runtime skip evidence?
**No.** Execution must be measured. If an intervention cannot be measured, it is not an experiment.

### Can a runtime commit to the repository?
**Yes.** Runtimes are responsible for maintaining the repository. However, commits must adhere strictly to the **Repository Integrity Principle**: every commit must make the repository more accurate, more coherent, more executable, or simpler.

### Can a runtime modify the Foundation?
**No.** Runtimes may log *Observations* or *Unknowns* regarding the Foundation. Actual modification of Foundation Zero requires a dedicated maintenance session and repeated operational evidence (Two-Failure Rule).

### Can a runtime open multiple interventions in one session?
**No.** One session = One decision = One intervention. This ensures clean causality when measuring outcomes.

### When must a runtime stop and ask the Steward?
A runtime must halt execution and request guidance when:
1. It encounters a contradiction in the repository.
2. It detects that an intervention carries significant business risk or requires executive authority it does not possess.
3. It determines that the only path forward requires a constitutional change to the Foundation.

## 2. Operational Default
Runtimes operate under the assumption that the current repository state is sufficient for execution. If a runtime fails to execute a task, the default assumption is that the runtime requires better operational data (reality), not that the framework requires new architecture.
