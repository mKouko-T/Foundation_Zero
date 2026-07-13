# ADR-004: Disposable Projections

**Status:** Accepted
**Date:** 2026-07-11

## Context
Persisting the graph state implies it has authority. If the graph goes out of sync with the event log, there is an epistemic split.

## Decision
All graphs (Knowledge, Candidate, Timeline, etc.) are Ephemeral Projections computed on the fly from the Event Store. The only artifact allowed to be permanently persisted is the Event Ledger itself.

## Consequences
- Zero information loss if a projection is destroyed.
- "Schema changes" to the graph merely require recompiling the projection code over the immutable ledger.
