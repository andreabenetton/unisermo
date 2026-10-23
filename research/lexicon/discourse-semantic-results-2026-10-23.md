# Multi-clause semantic-slot pilot — 2026-10-23

Status: six controlled documents completed via OpenRouter Qwen3 32B; canonical vocabulary unchanged.

GitHub Actions: https://github.com/andreabenetton/unisermo/actions/runs/39998936447
Artifact: discourse-slots-39998936447, ID 12520997690 (raw responses + mechanical JSON scores).

## Corpus and method

Six documents, three clauses each, contrast pel=push, trak=pull, vid=see across the three objects akwa=water, frat=brother, aerplan=airplane and two tense/person patterns. Cases are derived from the 144-row grammatical draft expansion with exact source IDs. Grammar and object roles are parser-verified; no idiomatic discourse or human translation validation is asserted.

Prompt supplies root glossary, pronouns, object marker -em, and zero-present/past-d tense rule. One isolated completion per document; Qwen non-thinking requested through existing runner. Strictly scored verb, object, tense, person per event. No automatic credit for partially correct events.

## Observed results

| Document | Object | Features | Correct events |
| --- | --- | --- | ---: |
| D001 | water | present, first singular | 1/3 |
| D002 | water | past, second singular | 3/3 |
| D003 | brother | present, first singular | 1/3 |
| D004 | brother | past, second singular | 3/3 |
| D005 | airplane | present, first singular | 2/3 |
| D006 | airplane | past, second singular | 3/3 |
| **Total** | | | **13/18** |

Six of six responses were well-formed JSON (fenced JSON accepted by the deterministic scorer). All five missed events failed on **tense only**, with present incorrectly reported as past; no verb, object, or person errors were observed in this small sample. All nine past events were correct, but only four of nine present events were fully correct.

OpenRouter usage for the six successful requests: 1,074 input tokens, 720 output tokens, reported cost **$0.00028752**. Initial failure/diagnostic charges, if any, are not included.

## Important limitations and next design

1. The examples use repeated morphology and semantically unusual combinations (e.g. pushing water, pulling a brother), rather than independently reviewed pragmatic text.
2. The tense errors indicate the short morphology primer was not reliably followed; they do **not** establish a flaw in the Unisermo tense system or imply that the canonical grammar should change.
3. Semantic-slot extraction is not full translation competence; no human recognition was measured.
4. Six prompts with one model and no repeated decoding are inadequate for statistical or cross-linguistic conclusions.
5. A next controlled contrast should hold the six documents fixed, vary only the explicitness of the zero-tense explanation, and use development data rather than an unexamined frozen holdout. Preserve all raw answers and provider costs.

Code: benchmarks/build_discourse_001.py, benchmarks/discourse_semantics.py, benchmarks/discourse_semantics_runner.py. Tests: tests/test_discourse_001.py, tests/test_discourse_semantics.py.
