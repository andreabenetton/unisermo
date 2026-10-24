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
