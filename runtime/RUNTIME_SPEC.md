# Foundation Zero Runtime Specification

This specification defines the universal boot sequence and execution lifecycle for any autonomous runtime (e.g., ChatGPT, Claude, Local Agents) initializing into a Foundation Zero environment.

## 1. Boot Interface
The Runtime MUST accept exactly two inputs from the Compiler:
1. `BOOT_PACKAGE.md`: The natural-language, compiled Knowledge Operating System.
2. `BOOT_MANIFEST.json`: The machine-readable cryptographic provenance and certification block.

Runtimes MUST NOT read source files (`.md`, `.py`, etc.) directly from the repository during initialization. They MUST rely entirely on the Compiled Package.

## 2. Boot Verification (Stage 1 & 2)
Before any execution begins, the Runtime MUST perform Cryptographic Boot Verification:
1. Load `BOOT_PACKAGE.md`. Extract the `BOOT_ID`.
2. Load `BOOT_MANIFEST.json`.
3. Verify that `BOOT_ID` in the package matches the `boot_id` inside the `certification` block of the manifest EXACTLY.
4. Verify that the `certification` block contains valid entries for `compiler_identity`, `repository_commit`, and `manifest_hash`.

If verification fails, the runtime MUST halt and declare a **FATAL BOOT EXCEPTION**. The package is considered tainted.

## 3. Initialization (Stage 3 & 4)
If verification passes, the Runtime MUST:
1. Ingest the **Mission** and **Epistemic Constraints**.
2. Identify the current **Execution Phase** (e.g., genesis, development, audit).
3. Read the **Task State** to determine the immediate execution requirement.

## 4. Declaration of State
The Runtime MUST output a formal `BOOT COMPLETE` report explicitly declaring:
- The verified `BOOT_ID`.
- The Compiler Identity used.
- The Current Phase and Task.

## 5. Execution Loop
Following initialization, the Runtime enters continuous execution. Every action taken MUST adhere to the Epistemic Model (`EPISTEMIC_MODEL.md`), prioritizing Reality over Identity, and ensuring all claims are backed by verifiable Evidence.
