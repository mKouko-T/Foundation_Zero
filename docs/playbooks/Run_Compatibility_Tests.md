---
Authority: Engineering Doctrine
Lifecycle State: Permanent
Last Exercised: Never
Reason Exercised: N/A

Owner: Core Maintainers
Exit Condition: Replaced by stronger abstraction.
---

# Run Compatibility Tests Playbook

**Capability Required**: `foundation_quality`
**Role**: `Compatibility Guardian`

## Procedure:
1. Locate tests in `tests/compatibility_tests/`.
2. Ensure target environment is initialized.
3. Run `pytest tests/compatibility_tests/`.
4. If failure: REJECT the implementation change. Update `state/known_failures.json`.
5. If success: proceed to next step in execution pipeline.
