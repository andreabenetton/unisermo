# Paired generic versus strict output schema — 2026-10-24

Completed bounded 16-call Qwen3 32B experiment: https://github.com/andreabenetton/unisermo/actions/runs/40071313036

Eight development documents, each with three parser-verified events, tested under both generic and strict response instructions with alternating condition order per document. Exact same clauses and expected eight slots in both arms. No canonical language changes.

| Measure | Generic | Strict |
| --- | ---: | ---: |
| Exact eight-slot events | 16/24 | 23/24 |
| Verb root | 24/24 | 24/24 |
| Object root | 24/24 | 24/24 |
| Tense | 19/24 | 24/24 |
| Aspect | 24/24 | 23/24 |
| Person | 21/24 | 24/24 |
| Number | 24/24 | 24/24 |
| Negation | 24/24 | 24/24 |
| Interrogative | 24/24 | 24/24 |
| Prompt tokens | 1939 | 2443 |
| Completion tokens | 1631 | 1688 |
| Provider cost USD | 0.00061180 | 0.00066808 |

All sixteen responses were parseable JSON, either arrays or `events` wrapped objects. Strict format raised exact event extraction by seven items for an additional 504 input tokens across eight requests. The generic arm's mistakes mainly affected tense (five events) and person (three events); the strict arm retained one aspect error (document S002). Both arms got all number fields right, so the earlier numeric-number output mistake was not reproduced in the generic paired condition.

Interpretation caveats: the same development documents had previously been tested with strict prompts, and the Qwen provider/seed may not produce perfectly repeatable outputs. This is a paired comparison but not an independent holdout or statistical proof. Moreover the strict condition changes multiple schema details simultaneously, so individual wording effects remain unidentified. Structurally correct extracted features do not establish idiomatic semantic understanding.

Artifacts: `paired-schema-40071313036`, ID `12551770970` (raw responses and exact scoring). Reproducible code: `benchmarks/operator_schema_paired.py`, `benchmarks/operator_schema_paired_runner.py`. No canon, numeral, or kinship changes.
