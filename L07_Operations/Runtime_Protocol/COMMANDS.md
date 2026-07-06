# OPERATIONAL VOCABULARY
**Version:** 1.0

This document defines the mutually exclusive operating states shared by every runtime (Cloud and Local) across the Foundation. 
It establishes behavioral definitions, not technical implementation.

---

### 1. INIT
**Purpose:** Create a new project.
*   **Local Runtime:** Generates project directory structure, creates `PROJECT.md`, creates `SESSION_001.md`, and prepares the environment.
*   **Cloud Runtime:** Acknowledges the new project boundary and awaits the first Session payload.

### 2. BEGIN
**Purpose:** Start the next sequential session inside an existing project.
*   **Local Runtime:** Creates `SESSION_00X.md`, updates `ACTIVE_SESSION.md`, and prepares the Context Payload for the Cloud Runtime (including the automatically generated **Repository Reality Snapshot** containing Git deltas).
*   **Cloud Runtime:** Initializes the reasoning context strictly bounded by the provided payload.

### 3. RESUME
**Purpose:** Continue an active session after a break or context wipe.
*   **Local Runtime:** Reads the `ACTIVE_SESSION.md`, gathers outstanding work/deliverables, and rebuilds the Context Payload (including the **Repository Reality Snapshot**).
*   **Cloud Runtime:** Accepts the payload and continues reasoning without hallucinating prior turns.

### 4. CHECKPOINT
**Purpose:** Mid-session audit (No execution allowed).
*   **Local Runtime:** Pauses execution. Does NOT modify the repository.
*   **Cloud Runtime:** Audits current work. Reports contradictions, scope drift, missing decisions, unknown risks. Recommends corrections and waits for Steward approval.

### 5. CLOSE
**Purpose:** Finalize and export the current session.
*   **Cloud Runtime:** Produces the final "Repository Export" containing a unique **Export ID**.
*   **Local Runtime:** Implements the export, generates closing reports, updates logs, runs Git commits, issues the structured **Export Acknowledgement**, and archives the session.

### 6. AUDIT
**Purpose:** Independent repository or project health inspection.
*   **Local / Cloud Runtime:** Scans for duplicate files, obsolete files, broken references, unused folders, Canon drift, and technical debt. Produces recommendations. No execution until approved.

---
**Invariant:** Commands execute work. They do not modify Foundation. Only repeated reality may justify Foundation evolution.
