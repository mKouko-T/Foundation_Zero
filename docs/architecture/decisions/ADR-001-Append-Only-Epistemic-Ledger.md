# ADR-001: Append-Only Epistemic Ledger

**Status:** Accepted
**Date:** 2026-07-11

## Context
A knowledge system inherently evolves over time. If we treat concepts and assessments as mutable records in a database, we lose provenance and destroy historical context.

## Decision
Foundation Zero will use an Epistemic Event Store (an append-only ledger forming a DAG) as the absolute source of truth. Knowledge graphs, assessments, and ontologies are strictly computed projections of this ledger.

## Consequences
- State mutations are forbidden.
- Distributed implementation is inherently safer (no write-conflicts beyond sequence interleaving).
- Replayability is guaranteed mathematically.
