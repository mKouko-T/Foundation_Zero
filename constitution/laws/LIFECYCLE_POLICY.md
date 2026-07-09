# Lifecycle Policy

Evolution occurs at different speeds. The following phases apply independently to the Repository, Protocol, Specification, Ledger, Schemas, and Knowledge:

## Semantic Versioning (SemVer)
All core specifications (FZS, Protocol, Schemas) strictly adhere to `MAJOR.MINOR.PATCH`:
- **MAJOR**: Incompatible or breaking structural changes (e.g., removing a required schema field). Requires a formalized Migration path.
- **MINOR**: Backwards-compatible additions (e.g., adding an optional field to a ledger).
- **PATCH**: Non-structural corrections (e.g., typos in documentation, clarifications).

## Lifecycle Phases
1. **Experimental**: Active development. Breaking changes permitted without warning.
2. **Supported / Pilot**: In production use. Bugfixes and compatible additions only.
3. **Deprecated**: Marked for removal. Migration path must be provided.
4. **Frozen**: Read-only. Security patches only.
5. **Archived**: Moved out of active source.
6. **Removed**: Deleted from tree (requires ADR).
