# Graph Model

Foundation Zero orchestrates six distinct, intersecting mathematical graphs.

## 1. The Reality Graph
Models physical and objective continuity.
- **Nodes**: `Source`, `Event`, `Signal`.
- **Purpose**: Anchors the computational substrate to the physical universe.

## 2. The Provenance Graph (Causality & Custody)
Models custody, time, and physical transformations.
- **Nodes**: `State`, `Transformation`.
- **Primary Edges**: `generated_from`, `transformed_by`, `derived_from`. (First-Class Edges).
- **Behavior**: Purely historical and forensic. Strictly append-only.

## 3. The Semantic Graph (Concepts & Logic)
Models meaning, representations, and uncertainty.
- **Nodes**: `Representation`, `Concept`, `Assessment`, `Evidence`.
- **Primary Edges**: `supports`, `contradicts`, `equivalent_to`. (First-Class Edges). `part_of`, `instance_of` (Structural Edges).
- **Behavior**: Evolves non-linearly based on new evidence.

## 4. The Dependency Graph (Reasoning & Justification)
Models epistemic topology and logical necessity.
- **Nodes**: `Interpretation`, `Assumption`, `Premise`, `Theorem`.
- **Primary Edges**: `requires`, `assumes`, `justifies`.
- **Behavior**: Provides the logical floor beneath a belief. Enables automated retraction downstream via Uncertainty Propagation.

## 5. The Operational Graph (System Execution)
Models execution, architecture, and constraints.
- **Nodes**: `Intent`, `Project`, `Capability`, `Protocol`, `Specification`, `Constraint`.
- **Primary Edges**: `depends_on`, `implements`, `governs`, `satisfies`.

## 6. The Value Graph (Priority & Economics)
Models importance, utility, and business value.
- **Nodes**: `Mission`, `Goal`, `Utility Metric`, `Value Assessment`.
- **Primary Edges**: `prioritizes`, `funds`, `values`.
- **Behavior**: Determines *what matters* among all equivalent possibilities. Drives decision-making allocation.
