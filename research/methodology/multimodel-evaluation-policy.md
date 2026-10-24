# Minimum multi-model evidence policy for Unisermo LLM evaluation

**Research process revision (2026-10-24).** This is a methodological recommendation and experiment-tracking convention, not a canonical language design decision.

The early October 2026 Unisermo program used one principal model, Qwen3 32B, for grammatical slot recognition and successive semantic extraction experiments. The author identified the limitation: performance on one architecture family cannot support a language-general conclusion. From this stage forward:

1. **At least two different model families** for substantively new LLM semantic/grammatical interpretation and language-cost tests, unless a run is explicitly designated `single_model_debug`, `smoke` or `infrastructure_probe`. Report those exclusions visibly.
2. **Same material and scoring reference** for all model arms; preserve exact input prompts, output contracts, language version, model identifiers, provider endpoint, context handling, generation controls, seed requests and actual returned model/provider metadata. Document unavoidable model-specific runtime switches and never call them equivalent when they are not.
3. **Never aggregate away individual model differences.** Report by model × condition × construction family, as well as sample-level agreement: both correct, only A, only B, neither; preserve shared failure examples.
4. **Separate accuracy from format compliance, resource usage and end-to-end communication cost.** One model's lower token count is not proof of language efficiency; tokenizer and token prices differ. Prefer cost per independently accepted meaning conveyed, including repair/clarification rounds and guide overhead.
5. **Account for dependent stimuli.** Several sentences share templates, lexical items and source rules; document clusters are the natural comparison unit. Use genuine development/test partitions, then a never-used final holdout; pre-register planned metrics.
6. **Validate meaning independently of model outputs.** Machine-generated/parser-derived `gold` is useful for development but cannot establish correct natural-language semantics by itself. Assign qualified human reviewers who do not see model errors before adjudicating. Record ambiguity and lack of licensed valency as results.
7. **Two families are a minimum, not a final proof.** For a scientific publication, aim for three families spanning distinct training approaches, plus controlled English comparator and human comprehension measurements. Model-family similarity and shared data can still create common-mode errors.
8. **Preserve historical runs unchanged.** Earlier Qwen-only results remain archived with their original boundaries. New multi-model tests add separate evidence and do not upgrade or overwrite old conclusions retroactively.

First implementation: `benchmarks/two_model_case_role.py`, Qwen3 32B vs Gemma 3 27B, source `benchmarks/corpus/case-role-dev-001.jsonl`. See `research/lexicon/two-model-case-role-protocol-2026-10-24.md` and the original preliminary Qwen study in PR #13. No modifications to Unisermo case grammar, lexicon or holdout are implied.
