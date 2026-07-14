# ADR-0005: Machine Readable Specifications

**Status:** Accepted

## Context
Early versions of Foundation Zero relied on human-readable Markdown to define critical execution parameters, such as the compilation order. This forced compiler implementations to parse Markdown headings to extract configuration.

## Decision
All executable configuration parameters and schemas must have a dedicated machine-readable artifact (e.g., `COMPILER_PIPELINE.json`). Markdown remains strictly for human understanding and formal definition of the protocol.

## Alternatives Considered
1. **Markdown Frontmatter:** Embedding YAML in Markdown headers. Rejected because it still tightly couples specification prose with configuration data.
2. **Regex Parsing:** Continuing to parse Markdown headings. Rejected because a trivial typo in a heading could silently alter compilation sequences.

## Consequences
- Requires explicit synchronization between Markdown specs and their JSON/YAML counterparts.
- Drastically simplifies compiler implementation.
- Eliminates presentation formatting from the attack surface.

## Related Specifications
- `COMPILER_PIPELINE.json`
- `MANIFEST_SCHEMA.json`

## Supersedes / Superseded By
N/A
