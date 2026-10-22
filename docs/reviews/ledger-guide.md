# Corpus review ledger

- `pilot-reviews.jsonl` contains one **pending** review per pilot ID, with both original texts embedded to detect drift.
- `python -m benchmarks.review` validates coverage, status, provenance and approval requirements.
- The ledger contains **zero** independently verified translations as of 2026-10-22.
- The plan in `benchmarks/corpus/expansion-plan.json` proposes 1,000 balanced cases; these are quotas, **not** created or approved sentences.
- Do not change a pilot source sentence in place after measuring it. Create a new version, preserve original run evidence, and re-run tokenization.
- Human review examines subject number, tense/aspect, case, definiteness, polarity scope and pragmatic interpretation. A successful parse does not establish bilingual equivalence.
- Holdout sentences must not be used to optimize spellings or choose revised morphemes.

References: [review protocol](pilot-review-protocol.md), [LDR-0007](../ldr/LDR-0007-tokenization-diagnostic-baseline.md).
