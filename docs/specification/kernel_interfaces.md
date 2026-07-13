# Foundation Zero Kernel Interfaces

The Kernel API is language-agnostic. Any implementation (Python, Rust, Go) must fulfill these strict contracts.

## Compatibility Levels
Every public contract declares one of the following statuses:
- **Experimental**: May change based on initial implementation feedback.
- **Stable**: Implementation proven. Changes require deprecation.
- **Frozen**: Foundational core. Will not change without a constitutional crisis.
- **Deprecated**: Scheduled for removal.
- **Removed**: No longer part of the specification.

## 1. EventStore & Cursor
**Status**: Frozen

The EventStore is the immutable ledger of Epistemic Events.
- `append(event: EpistemicEvent) -> None`
  - **Must satisfy:** immutable, append-only, parent validity, and deterministic replay. Throws if these are violated.
- `cursor() -> LedgerCursor`: Returns a stateful cursor.
- **LedgerCursor**: `next() -> EpistemicEvent`, `seek(sequence_number) -> None`.

> **Note on Sequence Numbers:** Strict contiguous integer sequence numbers (e.g. `len(events)+1`) are **reference implementation behavior**, not a constitutional requirement. The Constitution requires only: total ordering inside one ledger, valid parent references, and deterministic replay. How ordering is achieved in distributed implementations is an implementation concern.

## 2. IdentityProvider
**Status**: Frozen

Mints `FZ-` IDs.
- `mint(namespace, inputs) -> Identity`
- **Contracts**: Must declare namespace policies, collision behavior, and guarantee determinism when required. It has ZERO knowledge of Locators, References, or Aliases.

## 3. Projection
**Status**: Stable

An ephemeral, disposable computation over the EventStore.
- `compute(cursor: LedgerCursor) -> None`: Folds chronological events into a materialized state.

> **Note on Projections:** The Kernel enforces Projection as an interface. Applications may implement `KnowledgeGraphProjection`, `TimelineProjection`, `EvidenceProjection`, `GovernanceProjection`, etc. All are equally disposable.

## 4. CanonicalizationPolicy
**Status**: Experimental

Evaluates a `CandidateConcept`.
- `evaluate(candidate, existing_canonicals) -> Action`
- Actions: `MERGE`, `SPLIT`, `NEW_CANONICAL`, `REJECT`.

## 5. Decoder & Observer
**Status**: Experimental
- **Decoder**: `decode(bytes) -> DocumentModel` (Parses physical formats like PDF/Markdown into structural models).
- **Observer**: `observe(DocumentModel) -> List[ObservationRecord]` (Extracts objective structures with byte offsets, lengths, and content checksums).
