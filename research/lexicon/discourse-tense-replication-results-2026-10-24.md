# Counterbalanced tense-prompt replication — 2026-10-24

Run: https://github.com/andreabenetton/unisermo/actions/runs/40064982181 (success). Artifact `tense-replication-40064982181`, ID `12548479955` (original OpenRouter responses and exact scorer output).

Six previously unused pro-drop document variants (18 events per instruction condition) derive from the parser-verified 144-clause development expansion. They reuse root/object/tense combinations from the preceding tests; they are **not independent naturalistic text**, and frozen held-out material was not accessed. Counterbalanced paired order: short/full for odd numbered documents; full/short for even numbered documents. Model Qwen3 32B through OpenRouter; 12 paid calls, capped at 256 tokens per response.

| Metric | Rule + examples | Full explanation |
|---|---:|---:|
| Exact events | 13/18 | 15/18 |
| Valid document responses | 6/6 | 6/6 |
| Input tokens | 1113 | 1623 |
| Output tokens | 703 | 702 |
| Provider-reported USD | 0.00042422 | 0.00048882 |

Per-document scores, in sequence R001–R006: short `2,3,1,3,1,3`; full `2,3,2,3,2,3`. These exact events include verb, object, tense and person. No automatic partial credit. The full explanation improves two events in this replication, but does not attain 18/18 outside the previously repeatedly used six development documents. All past-pattern documents were 3/3; present-pattern documents contained the errors.

The experiment does not establish a causal benefit attributable exclusively to instructions: texts use pro-drop unlike the previous explicit-subject examples; the new corpus is synthetically derived rather than independently sampled; fixed decoding seed and single execution per condition limit conclusions. No free-text semantic or human comprehension was tested. The price difference is from reported provider costs and should not be read as an intrinsic cost of Unisermo.

Implementation: `benchmarks/corpus/tense-replication-002.jsonl`, `benchmarks/discourse_tense_replication.py`, `benchmarks/discourse_tense_replication_runner.py`. **Recommendation:** keep the verbose explanation as the best observed reference for accuracy-sensitive extraction while expanding truly independent, varied linguistic evaluation. Do not alter grammar, canonical vocabulary, numerals, or kinship rules on these findings.
