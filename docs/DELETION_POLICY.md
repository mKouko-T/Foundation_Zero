# Deletion Policy

Deletion is a governed operation. Before any artifact is deleted, it must satisfy all criteria:
- Is it derived or canonical? (Canonical artifacts cannot be deleted without an ADR).
- Is it evidence? (Evidence is permanently immutable).
- Is it generated? (If yes, safe to delete).
- Can it be regenerated deterministically?
- Does another artifact supersede it?
- Is provenance preserved?
- Does deleting it break reproducibility?
