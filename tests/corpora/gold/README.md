# The Gold Decisions Corpus

This is the permanent regression testing infrastructure for Foundation Zero.

**Rule: Gold Decisions, Not Gold Outputs**
This corpus does not assert that GPT-12 will use the same wording as GPT-8. You do not want it reproducing GPT-8 wording. 

You want it reproducing:
- the same observations
- the same assessments
- the same provenance
- the same concepts

Potentially with different internal reasoning. 

Any new Evaluator version must perfectly reproduce the ledger events for these 20-30 hand-curated, peer-reviewed legacy chunks before it is permitted to process unverified ingestion campaigns.
