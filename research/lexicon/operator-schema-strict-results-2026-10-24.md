# Strict JSON schema experiment — 2026-10-24

Run: https://github.com/andreabenetton/unisermo/actions/runs/40070116590 (success); archived responses and score artifact `schema-strict-40070116590`, ID 12551225813.

Qwen3 32B, eight fresh development documents with 24 structurally parser-verified clauses. Explicit enumerated output types including grammatical number as the strings `singular`/`plural`, and a requested `events` wrapper. These document forms are new versus the prior operator-variety pack but drawn from the same limited generation grammar and root inventory.

| Measure | Correct | Total |
| --- | ---: | ---: |
| Exact eight-field events | 22 | 24 |
| Lemma | 24 | 24 |
| Object lemma | 24 | 24 |
| Tense | 24 | 24 |
| Aspect | 22 | 24 |
| Person | 24 | 24 |
| Grammatical number | 24 | 24 |
| Negation | 24 | 24 |
| Interrogative | 24 | 24 |

All eight answers parsed as JSON, and all API results ended with finish_reason `stop`. The two aspect errors occurred in documents S002 and S007, one event per document. No errors in grammatical number representation were observed.

OpenRouter usage: 2,443 prompt tokens, 1,685 completion tokens, provider-reported cost $0.00066724.

**Caution:** the earlier trial achieved 15/24 exact events and 15/24 number fields, but used different sentence combinations. Therefore the difference is not an unbiased paired estimate of the effect of the response specification. This exercise covers parser-derived grammatical slots, not meaning communicated in natural discourse, human comprehension, or a claim about model generality.

Code: `benchmarks/operator_schema_strict.py`, `benchmarks/operator_schema_strict_runner.py`; data: `benchmarks/corpus/schema-variety-002.jsonl`. No normative grammar, number system, kinship or lexicon modifications.
