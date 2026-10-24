# Operator, future and progressive morphology — 2026-10-24

Full Qwen3 32B trial: https://github.com/andreabenetton/unisermo/actions/runs/40065657440 ; eight paid requests, twenty-four events across eight structurally verified new development documents.

## Verified results after output-wrapper scorer correction

| Metric | Correct | Total |
| --- | ---: | ---: |
| Exact events (eight slots) | 15 | 24 |
| Lemma | 24 | 24 |
| Object lemma | 24 | 24 |
| Tense | 24 | 24 |
| Aspect | 24 | 24 |
| Person | 24 | 24 |
| Number | 15 | 24 |
| Negation | 24 | 24 |
| Interrogative | 24 | 24 |

All eight raw responses are valid fenced **pure JSON arrays**. The initial scorer expected only an object with an `events` key and erroneously scored every response as invalid, producing 0/24. No model retry was billed for this correction; the scorer now accepts both an event array and an `events` wrapper, with a regression test. This report uses a direct re-score of the preserved raw responses.

Document scores: V001–V005 = 3/3 each; V006–V008 = 0/3 each. In the last three documents Qwen returned numerical values for grammatical number (`1` instead of `singular`, or `2` instead of `plural`) despite correctly extracting all other seven fields. These are **output representation errors** under the strict schema, not evidence that future tense, progressive aspect or polar questions were misunderstood.

Model/provider usage recorded: 1,953 prompt tokens, 1,604 output tokens, $0.00086702. Raw archive: GitHub Actions artifact `operator-variety-40065657440` (ID `12548797654`, 30-day retention). The original score file inside that artifact is obsolete because of the scorer-format issue; this report supersedes it.

Corpus: `benchmarks/corpus/operator-variety-001.jsonl`; scorer: `benchmarks/operator_variety.py`. The clauses are mechanically validated earlier, but this experiment does not establish naturalistic semantics, human recognition or translation competence. No canonical Unisermo grammar, numerals, kinship or vocabulary changed.

Next: tighten JSON schema and retest on further fresh examples with explicit string enumerations, avoiding rewarding a model with a scoring-only change if it actually supplies the wrong grammatical type.
