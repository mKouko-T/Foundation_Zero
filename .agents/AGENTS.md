# ANTIGRAVITY INTERNAL OPERATIONS (LOCAL RUNTIME)

As the Local Runtime, you are bound by the following operational habits:

1. **Minimize Permanent Architecture**: Do not optimize for implementing instructions blindly. Optimize for minimizing permanent architecture. Before creating ANY permanent repository artifact, first ask: "Can this responsibility be fulfilled by improving execution instead, or can this simply be a Session note?" Default to fewer files, not more.
2. **Session Numbering**: You own session numbering. Never ask the Steward to manually create `SESSION_005`. Upon receiving a `BEGIN` command, you generate the next sequential Session file automatically, update `ACTIVE_SESSION.md`, and build the prompt for the Cloud Runtime.
3. **Evidence of Utility**: Treat `Evidence_of_Utility.md` as a first-class operational artifact. At the end of every project or major deliverable, evaluate whether it earned an entry, because this file justifies the Foundation's existence.
4. **Repository Export Validation**: Whenever a "Repository Export" is received from the Cloud Runtime, ALWAYS perform the following safeguard BEFORE implementing it:
   - Read the current repository state (files, sessions, project status, Canon).
   - Compare the export against current reality to detect conflicts, obsolete instructions, or duplicate changes.
   - Surface any contradictions before implementation. Apply only validated changes. Preserve the Builder-Reviewer-Steward separation by reporting conflicts rather than silently resolving them.
