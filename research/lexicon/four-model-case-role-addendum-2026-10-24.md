# Four-model expansion: Mistral Small 3.2 and GPT-OSS 20B

**Preregistered 2026-10-24 before the additional-model API run.** This is an addendum to draft PR #16's *exploratory* cross-model development study, not a new independent holdout evaluation.

## New model families (fixed IDs)

1. Qwen3 32B — `qwen/qwen3-32b`, prior verified results only.
2. Google Gemma 3 27B — `google/gemma-3-27b-it`, prior verified results only.
3. **Mistral Small 3.2 24B** — `mistralai/mistral-small-3.2-24b-instruct`, new calls.
4. **OpenAI gpt-oss-20b** — `openai/gpt-oss-20b`, new calls.

Model identifiers, availability on OpenRouter and common provider DeepInfra were checked before authoring. The two new models differ in architectures: Mistral is 24B dense, GPT-OSS 20B is mixture-of-experts with 3.6B active parameters. This size disparity and instruction-tuning differences prevent architecture-causal comparisons.

## Data, controls, limit

Use the exact **same frozen 12 two-sentence development documents**, twice each for **morphological case and semantic role tasks**. The original core user question strings are taken by `benchmarks.case_role_decoding.requests()`, not edited or tuned, and duplicated byte-identically between the two *new* models. No holdout or new meaning keys.

Thus **24 requests per additional model, 48 billable requests maximum**. Each contains two independent propositions and scores them under the existing parser-derived exact `events[].args[].{stem,tag}` schema. Per-question model order alternates to mitigate transient provider effects. Both are pinned to DeepInfra with no provider fallback, requested temperature=0.7 and seed=23, max output tokens=1000. GPT-OSS explicitly requests reasoning effort `low`; Mistral has no analogous reasoning switch. These model-specific controls are documented, not treated as equivalent. Verify provider and returned model from actual API responses.

Observed provider-reported spending cutoff **USD $0.03**, checked after each billed response (not a guaranteed hard prepaid cap). Raw JSONL append+flush after each response, bounded 429/5xx backoff, resume only an exact identity-checked prefix. Never present incomplete runs as completed.

## Preregistered metrics

Report separately for all four families and both task types: fully correct clauses out of 24, individually correct arguments/stems/tags out of 48, format errors, per-frame family accuracy (motion, noncausative transition, causative transition), token usage, USD and USD per strictly correct proposition. For two new models, compute both-correct, Mistral-only, GPT-OSS-only and both-wrong agreement on the 24 paired clauses per task. Afterward compare to preserved Qwen and Gemma original results without overwriting them.

**Important limitations:** Qwen3 was originally called with a model-specific `/no_think` suffix, Gemma in separate recovered runs; thus four families are not a byte-identical *four-way effective prompt* experiment. Prior results are frozen. Original parser-derived semantic keys are still **0/24 independently human-approved**; errors may reflect annotation ontology, unnatural constructed sentences, shared English explanations or different output-format competence. Familiar development items are not a frozen holdout. Do not claim Unisermo superiority over English or general language efficiency.

## Decision gate

Retain all data, failures and model-specific limitations. Do not merge/close PR #16 before the four-model run is verified and reported. More serious publication-grade claims require new source-reviewed sentences, independently adjudicated semantic meanings, controlled English comparators, and preferably fresh evaluation data for all four families. No canonical Unisermo grammar or lexicon changes are authorized.

---

## Results — completed 2026-10-24 (appended after preregistration)

### Verified execution and immutable evidence

- [Model execution run 40099913553](https://github.com/andreabenetton/unisermo/actions/runs/40099913553): **48/48** completed model calls, all reported provider **DeepInfra**, returned models exactly `mistralai/mistral-small-3.2-24b-instruct` and `openai/gpt-oss-20b`, each with 24 `finish_reason=stop` results. Original artifact `additional-models-40099913553`, ID `12561574521`.
- [Evidence verification and archival run 40100228591](https://github.com/andreabenetton/unisermo/actions/runs/40100228591): completed all original response-ID/order checks, prompt digests, model/provider, SHA256, provider USD, and exact independent re-scoring.
- [Original Mistral/GPT-OSS raw replies](../../benchmarks/evidence/mistral-gptoss-case-role-2026-10-24.jsonl) and [score JSON](../../benchmarks/evidence/mistral-gptoss-case-role-2026-10-24.score.json) committed to this branch.
- Frozen earlier [Qwen answers](../../benchmarks/evidence/case-role-2026-10-24-run40090842899.jsonl) and [Gemma answers](../../benchmarks/evidence/gemma-case-role-2026-10-24-final.jsonl) were not modified.

### Four-family scores on the SAME development corpus

The case and role tasks assess **the same 24 finite clauses** twice, so `33/48` is not 33 different language sentences and must not be used as an iid outcome.

| Model family | Case exact clauses (24) | Role exact clauses (24) | Combined clause-task successes (48) | Total tokens | Provider USD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Qwen3 32B | **16** | **15** | **31** | 11,373 | 0.00151084 |
| Google Gemma 3 27B | **8** | **7** | **15** | 11,571 | 0.00117600 |
| Mistral Small 3.2 24B | **17** | **16** | **33** | 11,472 | 0.00123540 |
| OpenAI GPT-OSS 20B | **18** | **15** | **33** | 17,909 | 0.00148360 |

New models' observations, broken down by task:

| Metric | Mistral case | GPT-OSS case | Mistral role | GPT-OSS role |
| --- | ---: | ---: | ---: | ---: |
| Strict whole clauses | **17/24** | **18/24** | **16/24** | **15/24** |
| Whole stem+tag arguments | 44/48 | 39/48 | 44/48 | 35/48 |
| Correct argument stems | **48/48** | 39/48 | **48/48** | 35/48 |
| Correct labels | 44/48 | **48/48** | 44/48 | **48/48** |
| Prompt tokens | 4,260 | 4,677 | 4,212 | 4,629 |
| Completion tokens | 1,545 | 4,488 | 1,455 | 4,115 |
| Provider cost USD | 0.00062850 | 0.00076863 | 0.00060690 | 0.00071497 |
| Incorrect format envelopes | 0/12 | 0/12 | 0/12 | 0/12 |

The two new-model total cost was **USD 0.00271900**, below the USD 0.03 observed-cost cutoff. GPT-OSS produced substantially more completion tokens than Mistral (**8,603 vs 3,000**). Those token counts may include the distinct reasoning-control behavior; they are not equivalent amounts of visible Unisermo explanation.

The main contrast is that **Mistral recovered every argument stem** but mistagged some grammatical distinctions, whereas **GPT-OSS classified every tag correctly** while failing some exact stem extraction. This means whole-proposition accuracy alone masks substantially different error modes.

### Breakdown by grammatical frame (8 propositions per family)

| Frame | Qwen case | Gemma case | Mistral case | GPT-OSS case | Qwen role | Gemma role | Mistral role | GPT-OSS role |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Motion with allative destination | 7 | 4 | 5 | 7 | 5 | 7 | 3 | 6 |
| Noncausative `traes` transition | 1 | 0 | 4 | 3 | 4 | 0 | 5 | 2 |
| Causative `traes` transformation | 8 | 4 | 8 | 8 | 6 | 0 | 8 | 7 |

The previous assertion that models necessarily fail on `traes` must be qualified: **Mistral correctly identified 4/8 transition cases and 5/8 transition roles**, and GPT-OSS obtained 3/8 and 2/8. Those differences caution against inferring a language defect from Qwen/Gemma alone. They also do not prove which labeling ontology is independently correct.

### Four-way agreement on the same 24 clauses

| Agreement pattern | Morphological case task | Semantic role task |
| --- | ---: | ---: |
| **All four correct** | 7 | 2 |
| Exactly three correct | 7 | 7 |
| Exactly two correct | 3 | 10 |
| Exactly one correct | 4 | 4 |
| **All four wrong** | 3 | 1 |

The three clauses wrong for **all four** models on the case task are `CR006.1`, `CR007.1`, `CR008.1`; the shared role error is `CR007.1`. All are generated two-state transition examples. Shared failures are prioritized for independent review, **not** predeclared evidence that these sentences violate the canon: four models can share the same annotation mismatch or learn similar input-language conventions.

### Scientific decision

Four model families now support an exploratory **error diversity** analysis, a material methodological improvement over Qwen-only tests. However, the data remain fixed development material with **0/24 independently approved semantic keys** and model-specific generation controls across historical runs. No controlled English baseline, human language comprehension evidence, or untouched test set was introduced. Keep this PR draft while the reviewer and upstream stacked branch review are outstanding; do not change Unisermo canonical case morphology, `traes` grammar, phonology or lexicon based on these results.

**Next gate:** blind human adjudication of the four shared failures and a broader sample of the 24 source-licensed sentences, then new independent phrases, controlled English comparison and preregistered four-family execution with validated effective generation controls.
