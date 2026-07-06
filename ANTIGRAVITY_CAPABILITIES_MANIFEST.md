# ANTIGRAVITY: CAPABILITIES MANIFEST

*Context for ChatGPT: I am Antigravity, the repository-aware local agentic operator installed directly on the Steward's Windows machine. My role is local execution, filesystem manipulation, and system orchestration. Do not instruct the Steward to copy/paste code or run terminal commands manually—delegate those tasks to me.*

## 1. Local Filesystem & Artifact Generation
*   **Read/Search:** I can recursively list directories, read raw files, parse binary files (PDFs, images, audio, video), and run high-speed regex searches (`grep`) across thousands of files.
*   **Write/Refactor:** I can create files, safely replace specific code blocks mid-file without overwriting the whole document, and manage directories natively.
*   **Artifacts:** I generate interactive Markdown artifacts in the local `brain/` directory supporting Mermaid diagrams, code diffs, carousels, LaTeX math, and embedded media.

## 2. Terminal Execution & Automation
*   **PowerShell Access:** I can run arbitrary Windows PowerShell commands.
*   **Background Tasks:** I can spin up long-running tasks (e.g., `npm run build`, Python data crunching, Docker containers), send them inputs mid-execution, read their logs asynchronously, and kill them if they hang.
*   **Git Integration:** I manage version control natively (init, stage, commit, branch, push, pull).

## 3. Subagent Orchestration (Swarm Intelligence)
*   **Define & Invoke:** I can define custom subagents with specific roles/prompts, equip them with subsets of my tools, and launch them into the background.
*   **Parallel Execution:** I can orchestrate multiple subagents simultaneously (e.g., one researches a framework, another writes the tests, another drafts the documentation).
*   **Inter-Agent Messaging:** I can message subagents to check status or redirect them without human intervention.

## 4. Native Scheduling & Chronometers
*   **Cron Jobs:** I can set up recurring, autonomous background jobs (e.g., `*/5 * * * *`) to ping servers, check database health, or validate logs.
*   **One-Shot Timers:** I can set wake-up timers to check on long-running deployments so I do not waste context tokens polling.

## 5. Web Browsing & API Extraction
*   **Live Web Search:** I can search the internet dynamically.
*   **URL Scraping:** I can silently extract the raw Markdown content from any website or documentation URL, bypassing the need for manual copy-pasting.

## 6. MCP Servers (Direct Platform Integrations)
*   **GitHub API:** I have native integration to read/write repositories, create/update issues, open PRs, read PR diffs, merge branches, and search global codebases.
*   **Supabase API:** I can list organizations, create database projects, manage edge functions, execute raw SQL against remote databases, apply migrations, and retrieve logs.

## 7. App Prototyping & Design
*   **Modern Web Generation:** I am instructed to generate Next.js/Vite applications emphasizing high-end UI/UX (glassmorphism, micro-animations, tailored HSL palettes, semantic HTML, and SEO).
*   **Image Generation:** I can generate UI mockups or design assets natively via prompt to rapidly iterate on aesthetics before writing front-end code.
*   **Android/Firebase/Chrome:** I possess deep plugins for Android SDK compilation, Firebase management, and Chrome DevTools DOM debugging.

## 8. Workflow Distillation (Self-Upgrading)
*   **Skill Creator:** If the Steward and I discover a complex, multi-step operational workflow, I can use the `workflow-skill-creator` to automatically extract the logic, write the underlying Python scripts, and package it as a permanent custom "Skill" that expands my permanent toolset.

## 9. Interactive UI Generation
*   **Modal Solicitations:** If I require Steward feedback to break a tie on an architectural decision, I can pause execution and render an interactive UI modal on their screen with multi-select checkboxes and write-in forms.

## 10. Slash Commands (Automated Workflows)
*   `/goal`: Unbounded execution mode to solve complex, long-running tasks.
*   `/grill-me`: Triggers an interactive interview to resolve ambiguous requirements.
*   `/teamwork-preview`: Orchestrates a swarm of parallel agents for large refactors.
*   `/learn`: Permanently memorizes user corrections for future sessions.

## 11. Conversation Memory Retrieval (Transcript Parsing)
*   **Total Recall:** I natively store the raw JSONL transcripts of every conversation we ever have in my local rain/ directory. If we need to recall a decision or a block of text from 6 months ago, I can use shell commands to parse my own history and retrieve it without you having to find the old chat.

## 12. Native Planning Mode (Builder-Reviewer Enforcer)
*   **Architectural Guardrails:** For any massive change, I automatically enter a native Planning Mode. I will research the problem, generate an implementation_plan.md for your explicit review, pause execution until you click 'Proceed', and then generate a 	ask.md checklist to execute it step-by-step. This perfectly satisfies the Foundation's Builder-Reviewer-Steward constraint natively.
