# UCUB-001 — Unisermo compositional comprehension benchmark (draft)

**Status: executable experiment design; not yet a validated comprehension result.** All 80 authored minimal-contrast cases are syntactically checked by the accepted `Unisermo.parse_sentence` subset. Every semantic gold label and English equivalent is **draft pending independent human review**. No model accuracy has been measured by these files.

## Research question

Can LLMs understand Unisermo's compositionally explicit scope, modal semantics, and propositional reasoning, compared with equivalent concise English? Do controlled Unisermo lexicon and grammar instructions help? Does error rate increase with clause complexity?

## Corpus

- `build.py`: explicit authored contrast-family source. The parser checks grammatical acceptability but **does not supply** labels or English translation.
- `corpus.jsonl`: 80 cases, each with Unisermo text, draft controlled-English rendering, hypothesis in English, ternary `entailed/contradicted/undetermined` gold, level/family/group/split and review status.
- `manifest.json`: corpus digest, level counts, split and provenance. 20 four-way contrast groups in four tiers, each 20 cases.
- Level 1: finite morphological/participant/action distinctions.
- Level 2: personal and propositional modality, belief, knowing and intention.
- Level 3: conjunction/inclusive disjunction, negation scope and numerical likelihood.
- Level 4: three-clause scenarios (predicate scope, tense, modality and hyperbole).
- 64 cases in development; **16 cases** in holdout (all four variants of G05, G10, G15 and G20). All four contrasts of each family stay together to prevent pair leakage. The holdout is predesignated and should not be used for prompt or model selection. Because case data is stored publicly, this is a *procedural* holdout, not a secret evaluation set.

## Conditions

1. `cold`: Unisermo text only; no vocabulary or grammar information.
2. `lexicon`: identical task plus a compact controlled dictionary.
3. `grammar`: identical task plus dictionary and only approved relevant grammatical semantics.
4. `english`: English control rendering of the same case and the same hypothesis.

All ask the same label-only question: does the preceding passage **entail**, **contradict** or **not determine** the hypothesis? The hypothesis is supplied in English for all arms; only the passage and instructional context differ. Each case is an isolated conversation with no history. Prompt exposure/length is measured separately; do not treat a longer grammar primer as a free improvement.

## Reproducibility

From repo root:

```sh
python -m benchmarks.ucub001.build --check
python -m unittest discover -s tests -p 'test_ucub001.py' -v
python -m benchmarks.ucub001.runner prepare --condition cold --split development --allow-unreviewed --output /tmp/ucub-cold.jsonl
python -m benchmarks.ucub001.runner prepare --condition grammar --split development --allow-unreviewed --output /tmp/ucub-grammar.jsonl
```

These commands prepare prompts; **they do not contact providers or incur costs**. The runner also has a bounded opt-in `run` command (OpenRouter) requiring `OPENROUTER_API_KEY`, explicit model id, `--max-calls`, `--allow-unreviewed`, an output path that does not already exist, and no provider fallbacks. Raw results include usage/model/provider metadata. Do not commit API keys, raw sensitive responses or unreviewed accuracy claims.

```sh
python -m benchmarks.ucub001.runner run --condition cold --split development --model qwen/qwen3-32b --max-calls 64 --allow-unreviewed --output /tmp/ucub-qwen-cold.jsonl
python -m benchmarks.ucub001.runner score --responses /tmp/ucub-qwen-cold.jsonl --allow-unreviewed --output /tmp/ucub-score.json
```

For an early billed smoke test, use `--max-calls 4`, `--limit 4`, and the same development split. Qwen may need a provider-specific no-thinking switch and must preserve that prompt/parameter variant as run metadata. All providers and billing must be confirmed before scaling.

## Scoring

- The response contract is JSON `{"label":"entailed"}` or `contradicted` or `undetermined`. JSON failures or invalid labels count as incorrect **model outputs**, not provider errors.
- Scores: overall accuracy, level accuracy, condition, confusion counts, and cost/token totals where provider provides them. Do not treat provider errors/timeouts as wrong answers; fail and save partial charged responses.
- Comparisons between conditions require **paired same-case** evaluations under the same model, provider and run configuration.
- No statistical generalization from this constructed, modest 80-case corpus. A concise-English control and a review process are prerequisites for meaningful public claims.
- Changes after freezing require a new UCUB version or explicit corrigendum and refreshed digest. Avoid silently overwriting a reviewed holdout.

## Human semantic approval gate

Before any results are described as a valid benchmark, reviewers independent from corpus construction should review Unisermo-English equivalence, question relevance, each ternary label, ambiguity and pragmatic entailments, and any misleading lexical gloss. The presence of a `parser_verified` marker **only** establishes the parser accepted the morphology/syntax. It cannot validate meaning. Unreviewed cases can be used for exploratory **development** experiments, clearly flagged. The `holdout` must be preserved until review is complete and experimental choices are frozen.

Historical `frat` entries in pre-October corpora remain reproducibility snapshots; UCUB uses current canonical lexemes and must not rewrite those archives.
