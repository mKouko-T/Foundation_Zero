# ADR-0001: Repository Philosophy

**Status**: Accepted
**Category**: Repository

## Context
Foundation Zero exists to recover knowledge. It requires an operational home that guarantees reproducibility over years.

## Decision
We establish this repository as the canonical operational home using the following design rationale:
- **Why Git**: Cryptographic history and distributed availability.
- **Why Markdown**: Platform-agnostic human readability.
- **Why JSON**: Strict machine-executable contracts.
- **Why Schemas**: To prevent structural drift and silent corruption.
- **Why Generated State**: Humans are unreliable state managers. State must be compiled.
- **Why Append-Only Logs**: Deletion destroys provenance.
- **Why Specification-First**: Method survives implementation.
- **Why Evidence-First**: Knowledge without evidence is an opinion.
- **Why No Database**: Databases hide state. Repositories expose state.

## Consequences
Engineering overhead is higher initially, but maintenance costs trend to zero over a decade.
