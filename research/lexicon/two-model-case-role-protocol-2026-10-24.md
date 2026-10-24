# Two-model replication: Qwen3 32B × Gemma 3 27B (protocol, 2026-10-24)

**Prerecorded before the paired paid API execution.** The prior case/role test (PR #13) was Qwen-only, so no model-family generalization is justified from its 16/24 case and 15/24 role outcomes. Following the author's request for at least two models, this study runs a *new paired execution* with two different architecture families.

## Model selection

- **Qwen:** `qwen/qwen3-32b` (32.8B dense), already studied as a one-model preliminary.
- **Google Gemma:** `google/gemma-3-27b-it` (27B), already listed in the repository's `benchmarks.openrouter_runner.MODELS` as an approved alternative.
- Source pricing and availability checked on OpenRouter before registration; both published endpoints available as of 2026-10-24.
- Prefer **one common inference service**, OpenRouter provider `DeepInfra` explicitly pinned, `allow_fallbacks=false`, `data_collection=deny`. Pinning provider helps reduce deployment differences but does not equalize architectures, quantization, sampling implementation, tokenizer or training.

## Locked stimuli and procedure

Exactly the **same development-only 12 two-clause documents** from `benchmarks/corpus/case-role-dev-001.jsonl` and **the same existing 24 base questions** (12 documents × case and role tasks); no new gold key and no holdout. For each document/condition, both model families are prompted with **byte-identical user message content**, with the same JSON contract and guide. The questions, subject and suffix morphology, grammatical roles and research-derived labels are unchanged.

Unlike the original Qwen-only caller, the cross-model caller avoids a hidden `/no_think` suffix in the user message, because that suffix would create unequal effective prompts across families. **This is a new run**, and its Qwen results must not be silently conflated with the previous Qwen run: the latter had an extra `/no_think` token and may have used different provider routing/temperature handling.

Common requested decoding controls: **temperature 0.7, seed 23, maximum output 340 tokens, no streaming, provider DeepInfra**. Qwen receives `reasoning.enabled=false` (no analogous Gemma switch). Provider honoring of seed and reasoning settings cannot be presumed. Actual model and provider identifiers, response IDs, token use and cost are saved for every call. Within-document model request order is alternated; case/role order is also balanced. Each call is isolated.

Total **48 billable calls** (24 per model), with a cumulative **USD 0.03 *observed cost* cutoff** checked after each response. It is *not* a hard pre-billing budget. A failed or truncated trial retains raw completed responses but is not scored as a complete experiment. No retry except limited 429 backoff.

## Scores specified before execution

For each model and each task, report:

- Primary: clauses with exact **verb root + two original-order argument stems and labels** (24 per condition).
- Secondary: correct individual arguments (48), exact stems (48), exact labels (48), invalid output format, label confusions, breakdown by the three licensed frame families (8 clauses each).
- Paired **model-agreement matrix** per task at the clause level: both correct, Qwen only, Gemma only, neither correct. Twelve two-sentence documents are the natural dependence groups, so individual clause counts must not be treated as independent general-population trials.
- Provider cost and input/output tokens **per model and task**, normalized USD per strictly correct clause (undefined on zero successful clauses).
- Preserve the raw responses and their SHA256, corpus SHA256, exact prompt hashes, verified machine rescoring and versioned files before analyzing the result.

No p-value or general model-families claim on 12 highly templated document clusters. A cross-model consensus failure is a higher-priority diagnostic for future **independently authored** sentences, but it can still arise from shared English glosses, annotation bias, similar training, or flawed machine-derived gold.

## Methodological rule for Unisermo experiments going forward

All subsequent **substantive LLM interpretation and comparative efficiency claims** should normally include *at least two architecture families*, use the same new stimuli and comparable decoding/response contracts, and report per-model outcomes rather than pooled accuracy alone. For final publication, two are a **minimum**, not sufficient independent validation: expand to a third model family if resources allow, independently adjudicate meaning keys, use a true frozen holdout, and include a reviewed controlled-English comparator and total communication costs. Model identifiers and dates must be fixed to avoid silent substitutions.

Existing conclusions from single-model runs remain recorded as such, not discarded or retroactively upgraded. No canonical edits, no holdout access, no human-approved semantic meanings claimed; new sentence review tally still **0/24**.

---

## Registered operational amendment — after first execution failed, before follow-up

**Run [40091590850](https://github.com/andreabenetton/unisermo/actions/runs/40091590850) did NOT complete the preregistered two-model trial.** It saved only **14/48** answers before OpenRouter/DeepInfra returned repeated **HTTP 429** on a Gemma request. More importantly, all **seven Qwen calls** among the 14 had `finish_reason=length` and **empty visible content**: disabling Qwen reasoning only via API `reasoning.enabled=false` without its prior `/no_think` prompt marker failed under this provider. These calls were billed and are **not semantically scored as evidence that Qwen cannot interpret Unisermo**. Gemma successfully returned valid content and `finish_reason=stop` on the other seven calls. The original failed artifact is `two-model-case-role-40091590850` (ID `12559033997`).

An attempted strict-prefix recovery job [40091922563](https://github.com/andreabenetton/unisermo/actions/runs/40091922563) *correctly rejected* the partial file because those Qwen completions were not successful. No new API calls were made by that job. The recovery script will not weaken this safety check or reinterpret empty Qwen responses as valid.

**Amended exploratory design (not equivalent to the preregistered identical-effective-prompt trial):** preserve the original **24 valid Qwen3 32B replies** from [run 40090842899](https://github.com/andreabenetton/unisermo/actions/runs/40090842899), which used the same frozen case/role questions and `/no_think` as a model-specific decoding control. Preserve the **seven valid Gemma replies** from run 40091590850 without rebilling, then execute just the remaining **17 Gemma requests** under the identical Gemma prompt/settings as those seven. Both model families therefore see the same task text and grammar reference, but Qwen has an additional model-specific nonthinking marker. It is **not literally the same effective prompt**. Compare per-model quality and errors descriptively; attribute no difference solely to learned linguistic competence.

The original preregistration above remains untouched and *must not* be rewritten as if the controlled trial succeeded. All conclusions from the salvaged comparison must be identified as **exploratory**, since the method was amended after observing the operational failures. Raw source artifacts, request hashes and all costs must be preserved. The existing frozen holdout and canonical language are still untouched.

New runner: `benchmarks/gemma_case_role_followup.py`; archive the resulting complete 24-answer Gemma set, original Qwen corpus and paired descriptive score as distinct, versioned evidence. Any future strong model-family conclusion requires **a newly preregistered** independent corpus with robust model-specific nonthinking controls and human-approved semantics.
