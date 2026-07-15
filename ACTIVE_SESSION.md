# Active Session

**Goal:** Conclude P-002 execution and prepare the project state for future empirical exploration.

**Context:** The evidentiary baseline for P-002 is secure. The project has reached an important governance milestone: improvements are now being driven by empirical results rather than design intuition. The philosophical definition of the project has sharpened: *Foundation Zero is a reproducible methodology for discovering, isolating, and experimentally reducing independent dimensions of specification uncertainty.*

**Immediate Action:**
1. Wait for reality to dictate the necessity of `P-003`. 
2. A valid candidate for `P-003` must answer the question: *"What observable disagreement could still occur even if P-001 and P-002 both succeed?"*

## Operational Observations (Not Yet Promoted)
*These discoveries have been logged from execution. They require a second independent failure/observation before being elevated to constitutional constraints (Two-Failure Rule).*

**1. Reality Confirmation Loop (Post-Intervention Verification):** Every operation that claims to modify reality should verify reality after the modification. (Observe ➡ Modify ➡ Reload ➡ Compare ➡ Resolve discrepancies ➡ Report). 

**2. The Five Truth Domains:** Rendered conversational artifacts can misinterpret the underlying repository state. The truth domains are: Reality ➡ Persistent State ➡ Runtime State ➡ Representation ➡ Interpretation. The recent duplication bug was a failure between Representation and Interpretation. Direct artifact inspection remains the authoritative verification mechanism.

**3. The Universal Claim Principle:** Capability verification and Reality verification are manifestations of the same higher-order pattern: *Every claim should identify the observation that currently justifies it.*

**4. Dependency Transparency:** Every statement has dependencies. Instead of saying "Repository is clean," the runtime should know it depends on specific hashes, audits, or Git states. This is deeper than verification; it is continuous dependency tracing.

**5. Source Authority Principle:** When representations disagree (or when evidence conflicts), the authoritative source for that claim must be directly inspected. (e.g., File contents beat diff rendering; Git status beats memory; API response beats API documentation). Repository wins over conversational evidence.

---

### Leading Explanatory Hypothesis: The Claim Ontology
*Status: Hypothesis. Must survive one complete Phase I execution cycle before promotion.*

The five observations above appear to be manifestations of a single canonical data structure: the **Claim**. However, *Claim* is inside the reality loop (Reality ➡ Observation ➡ Claim ➡ Verification ➡ Evidence ➡ Belief ➡ Decision ➡ Intervention ➡ Reality), not above it. 

If this ontology survives execution, a Claim will likely require: `[Claim ID, Purpose, Statement, Owner, Authority, Verification Method, Current Evidence, Evidence State, Freshness, Dependencies, Falsifier, Last Verified]`. 
It will also likely form a Dependency Graph rather than a flat list.

**Warning:** Do not delete existing governance (e.g., Rule 21) or workflows. Ontology describes *what is*, Governance constrains *behavior*, and Workflows describe *when*. They are orthogonal.

**6. Compression does not imply fundamentality:** A simpler explanatory model (like the Claim Ontology) is only a hypothesis until it survives repeated attempts at falsification. A beautiful compression can still be false.

**7. Governance Success Metric:** Successful governance reduces the frequency with which governance itself becomes the subject of work. If future sessions mostly discuss governance, the governance is failing. If they produce operational value, it is succeeding.

---

### Leading Explanatory Hypothesis 2: Executor Capability Contract & `EXECUTOR_PROFILE.md`
*Status: Hypothesis. Must survive operational testing in Phase I.*

An **Executor** (Human, ChatGPT, Antigravity, Claude, Script, API) is currently missing from the Foundation's ontology.
Every executor should explicitly disclose its operating envelope before work begins (Identity, Persistence, Tool Surface, Authority Surface, Visibility Surface, Mutation Surface, Verification Surface, Trust Boundary).
This could be formalized by generating a disposable `EXECUTOR_PROFILE.md` per runtime at boot.

**The ChatGPT Operational Contract:**
When collaborating with ChatGPT (or any LLM):
Never assume the executor has: repository access, filesystem access, Git access, terminal access, previous chats, previous runtime memory, same tool availability, same connectors, or same permissions.
**Instead: Require verification for each capability.**
Never assume successful execution from intended execution. Treat repository access as a capability requiring independent verification.
