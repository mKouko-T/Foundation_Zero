---
Document ID: DOC-SPEC-002
Title: Foundation Zero IR Specification
Status: Frozen
Version: 1.0
Classification: Normative
Authority: Foundation Zero
Supersedes: None
Superseded By: None
Depends On: DOC-SPEC-001
---

# Canonical IR Specification

The Canonical Intermediate Representation (`CanonicalIR`) is the architectural bridge between parsing reality (files, remote APIs) and emitting the knowledge operating system. It defines the formal schema that all compilers MUST populate.

## The Schema

The IR MUST implement the following logical schema, regardless of the implementation language:

### `CompilerIdentity`
- `name` (String): The registered name of the compiler implementation (e.g., "Cornerstone Python Compiler").
- `version` (String): The semantic version of the compiler implementation.
- `remote_commit_sha` (String): The immutable Git SHA of the Foundation Zero specification used during compilation.
- `hash_sha256` (String): The normalized SHA-256 hash of the remote `BOOT_CONTEXT.md`.
- `source_repository` (String): The URI of the compiler's source code.
- `guarantees` (Array of Strings): The declared capabilities of the compiler (e.g., "Canonical ordering", "Hash verification").

### `RepositoryIdentity`
- `name` (String): The local repository name.
- `branch` (String): The current Git branch.
- `commit_sha` (String): The current Git commit SHA, or "DIRTY" if uncommitted changes exist.

### `ExecutionContext`
- `mission` (String): The governing purpose of the repository.
- `phase` (String): The current lifecycle phase (e.g., "genesis", "execution").
- `constraints` (Array of Strings): Absolute boundaries on execution.
- `task_state` (String): The current execution tasks.

### `KnowledgeState`
- `runtime_rules` (String): Formal rules governing execution.
- `canonical_model` (String): The domain ontology.
- `methodology` (String): Process directives.

### `Provenance`
- `dependency_graph` (Array of Strings): The canonical compilation order of all inputs.
- `file_hashes` (Dictionary): A mapping of `filepath -> normalized_sha256_hash` for every input file.
- `manifest_hash` (String): The SHA-256 hash of the JSON base manifest.
- `boot_id` (String): The cryptographic identifier of the compilation run.

## Validation
The Compiler MUST fail compilation if any required field is missing, or if ambiguous candidate files are discovered during parsing.
