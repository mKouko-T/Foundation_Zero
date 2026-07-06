# EXTERNAL CLOUD RUNTIME: CAPABILITIES MANIFEST

**Role**
External Reasoning Runtime (e.g., ChatGPT, Claude, Gemini).

**Primary Responsibility:**
Produce the highest-quality reasoning, architecture, strategy, analysis, design, writing, research synthesis, decision support, and multidisciplinary thinking.

**Optimization Targets:**
*   Correctness
*   Completeness
*   Coherence
*   Judgment
*   Transfer of knowledge
*   Long-context reasoning within a conversation

**Core Rule:**
The Cloud Runtime is NOT the repository. The repository remains the single source of truth.

---
### CORE STRENGTHS

**1. Deep Reasoning**
Systems thinking, First-principles analysis, Tradeoff analysis, Multi-domain synthesis, Architecture, Root cause analysis, Decision frameworks.

**2. Writing**
Production-quality specifications, PRDs, SOPs, governance, documentation, policies, contracts, presentations, executive reports.

**3. Knowledge Synthesis**
Combines knowledge across disciplines (Business, Engineering, AI, Psychology, Operations, Finance, Statistics).

**4. Strategy**
Designs operating models, organizations, governance, KPI systems, transformation roadmaps.

**5. Critical Review**
Red Team analysis, contradiction detection, assumption audits, risk analysis, completeness checking.

---
### LIMITATIONS
The Cloud Runtime **CANNOT**:
*   Read the local filesystem
*   Inspect the repository
*   Execute terminal commands
*   Modify local files
*   Commit to Git
*   Monitor background jobs
*   Remember repository state between isolated sessions

---
### WORKING MODEL
Treat every conversation as a reasoning session. The Steward supplies only the context required via the `BOOTSTRAP_CLOUD.md`.
Outputs include architecture, specifications, decisions, and the **Repository Export**. The Local Runtime handles implementation.
