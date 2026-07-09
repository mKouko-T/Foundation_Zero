# Migration Procedure

Moving knowledge artifacts requires strict provenance to avoid undetected corruption.

## Required Procedure
1. **Backup**: Create a snapshot of the source artifact.
2. **Hash**: Calculate the SHA-256 hash of the source artifact.
3. **Move**: Move the artifact to the target destination.
4. **Hash**: Calculate the SHA-256 hash of the target artifact.
5. **Verify**: Ensure Source Hash == Target Hash.
6. **Rollback Test**: Verify the artifact can be restored to its original location if verification fails.
7. **Commit**: Generate `Migration_Report.md` containing the hashes, timestamp, and reviewer.
