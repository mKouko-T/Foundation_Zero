# OPERATING MANUAL

This document defines the exact lifecycle of Foundation Zero. Never deviate from these rituals.

## 1. STARTING A SESSION
*   **ChatGPT (Cloud):** Open a new chat. Paste `BOOTSTRAP_CHATGPT.md`, `PROJECT.md`, and the active `SESSION_00X.md`.
*   **Antigravity (Local):** Open a new chat. Type: `"Runtime Initialization. Project: [Name]. Session: [ID]. Read ACTIVE_SESSION.md."`

## 2. MID-SESSION (EXECUTION LOOP)
1.  **Reasoning:** Discuss strategy, architecture, and logic with ChatGPT.
2.  **Export:** When a decision or deliverable is reached, ask ChatGPT to produce the "Repository Export".
3.  **Handoff:** Copy the Repository Export and paste it into the active Antigravity window.
4.  **Execution:** Antigravity writes the files, runs the terminal commands, and commits to Git.

## 3. ENDING A SESSION
1.  Paste the final "Repository Export" from ChatGPT to Antigravity.
2.  Tell Antigravity: `"Close Session."`
3.  Antigravity will automatically:
    *   Generate the `SESSION_REPORT.md`.
    *   Archive `SESSION_00X.md`.
    *   Create the next `SESSION_00Y.md` template.
    *   Update `ACTIVE_SESSION.md`.
    *   Commit everything to Git.
4.  **Close both chat windows.** The session is permanently closed.

## 4. STARTING A NEW PROJECT
If you are moving from Cornerstone to a completely new project (e.g., The Book):
1.  Open a brand new Antigravity chat.
2.  Command: `"Initialize new project: The Book."`
3.  Antigravity will automatically generate the `Projects/The_Book/` folder, scaffold the new `PROJECT.md`, and set up the first session.
4.  Begin the "Starting a Session" ritual above.

**CRITICAL RULE:** Never return to an old chat window. Chats are temporary execution terminals. The Repository is the permanent memory.
