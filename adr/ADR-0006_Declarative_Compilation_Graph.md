# ADR-0006: Declarative Compilation Graph

**Status:** Accepted

## Context
The sequence of compilation was originally defined as a flat array. However, a flat array cannot naturally model complex dependencies, parallel execution, or optional stages without introducing implicit assumptions into the compiler's logic.

## Decision
The compilation sequence is modelled as a declarative graph in `COMPILER_PIPELINE.json`. Stages define their explicit dependencies using stable semantic IDs. The compiler must validate that the graph is acyclic and may execute any valid topological sorting.

## Alternatives Considered
1. **Flat Ordered Array:** Rejected because it assumes sequential execution and makes expressing prerequisites rigid.
2. **Dynamic Resolution:** Resolving dependencies dynamically by scanning files. Rejected because it introduces unpredictable and potentially non-deterministic build ordering.

## Consequences
- Requires compilers to implement Kahn's algorithm or similar topological sorting.
- Separates compilation prerequisites from runtime execution order.
- Provides a scalable abstraction for future feature additions like conditional stages or execution capabilities.

## Related Specifications
- `COMPILER_PIPELINE.json`

## Supersedes / Superseded By
N/A
