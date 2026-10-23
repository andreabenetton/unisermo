# Open-ended Unisermo sentence inference — measured results (2026-10-23)

**Actual model completions: 96/96.** This is a preliminary, small non-human reading experiment; no canonical vocabulary changed.

- GitHub Actions: https://github.com/andreabenetton/unisermo/actions/runs/39902217811
- Qwen model: `qwen/qwen3-32b`, actual raw output artifact `open-inference-qwen-39902217811`, GitHub artifact ID `12478374742`.
- Gemma model: `google/gemma-3-27b-it`, actual raw output artifact `open-inference-gemma-39902217811`, GitHub artifact ID `12479024435`.
- Each model performed 8 grammar-validated contexts × 3 roots (`dik`, experimental `dir`, `dirig`) × 2 modes (no glossary / explicit glossary) = **48 API calls**. First 6 contexts are development; remaining 2 reserved for checking, not selecting a root.
- Total charged cost reported by OpenRouter for these successful full executions: **$0.00175024** (Qwen $0.00092896; Gemma $0.00082128), excluding earlier pilots.
- One prompt per isolated API conversation; counterfactual grammatical meanings validated by in-memory parser substitution; no old frozen pilot or canonical lexicon changed.

## Corrected development-only scoring

A scoring issue was found: **all 48 Qwen replies were valid JSON inside a Markdown JSON fence**. The initial strict parser incorrectly counted these as invalid. A bounded fence-only JSON parser was added, and these values were computed again from the **original API responses**; no paid call repeated. Gemma used bare JSON for its 48 responses. The evaluator uses a narrow synonym whitelist and does not automatically certify semantic interpretation.

| Mode | Model | `dik` | `dir` | `dirig` |
| --- | --- | ---: | ---: | ---: |
| Unglossed | Qwen3 32B | 3/6 | 2/6 | 5/6 |
| Unglossed | Gemma 3 27B | 1/6 | 1/6 | 6/6 |
| **Unglossed combined** | **both models** | **4/12** | **3/12** | **11/12** |
| Explicit glossary | Qwen3 32B | 6/6 | 6/6 | 6/6 |
| Explicit glossary | Gemma 3 27B | 6/6 | 6/6 | 6/6 |

Mechanical verb guesses without glossary sometimes included `know`, `do`, `love`, `see` and `have`. These errors show the task is hard even for genuine roots; no one-word synonym mapping reliably represents open natural-language comprehension.

### Interpretation

- `dir` does **not** show a consistent advantage over `dik` in open-ended lexical interpretation; both are often guessed incorrectly without a dictionary.
- `dirig` is consistently easier to infer. This may reflect its international spelling resemblance, but it is not evidence of **speaker recognition**.
- With an explicit dictionary, the models consistently map all three roots in this test. This measures dictionary following, not recognition without instruction.
- The sound-level advantage of eliminating the documented possible `dik`/`tik` accent merger remains a separate design argument favoring `dir`.
- Neither this test nor the earlier MCQ test justifies accepting the canonical replacement yet. No human reading or audio trials have been conducted.

### Limitations and further work

1. Only six development sentences per root/model/condition, many correlated through the same finite morphology; no statistical claims.
2. This prompt gives structural grammar and object-word meanings, and the examples are syntactically accepted but lack independent discourse naturalness/sense-selection review.
3. Strict English lemma whitelist is a heuristic. Any real semantic evaluation requires independent qualitative review of raw outputs, without tuning on the reserved split.
4. Qwen requested non-thinking mode and a sampling seed; Gemma used a different policy. Provider behavior and determinism are not guaranteed.
5. Models can have extensive prior exposure to international cognates; multilingual speaker comprehension, phonetic availability and false friends still need human evaluation.

**Recommendation:** Keep `dik`, `stru`, `sentr` and `kurar` canonical. `dir` remains a serious proposal on phonological grounds, but no superiority on open-ended meaning comprehension is established. If adopting `dir` for its reduced phonological collision risk, document that rationale honestly in a future accepted LDR rather than relying on these scores.

Source and tests: `benchmarks/open_inference.py`, `benchmarks/open_inference_runner.py`, `tests/test_open_inference.py`, `research/lexicon/open-inference-protocol.md`.
