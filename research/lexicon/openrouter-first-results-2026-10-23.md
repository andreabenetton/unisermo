# First real OpenRouter lexical recognition benchmark — 2026-10-23

Status: **completed, experimental, not independent semantic/human validation**. The canonical Unisermo vocabulary is **unchanged**.

## Provenance and execution

GitHub Actions run: https://github.com/andreabenetton/unisermo/actions/runs/39901560159 .

Each model answered **72 isolated single-choice tasks** (9 development + 3 frozen-evaluation grammatical patterns for each of 3 roots and each of 2 conditions). Outputs were compared to the deterministically generated key. No prompt contained the key. 0 malformed responses across 144 billed completions.

| Model | OpenRouter actual provider | Answered | Total tokens | Reported API cost |
| --- | --- | ---: | ---: | ---: |
| `qwen/qwen3-32b` | DeepInfra | 72/72 | 12,632 | $0.00108256 |
| `google/gemma-3-27b-it` | DeepInfra | 72/72 | 12,340 | $0.0010029 |
| **Total** | | **144/144** | **24,972** | **$0.00208546** |

Qwen3 required the model-card `/no_think` instruction and `reasoning.enabled=false`, with `temperature=0.7` and `seed=23` requested; Gemma used `temperature=0`. Thus the two models were **not** tested with identical decoding policies; seed support and determinism at the provider must not be assumed. Initial unsuccessful Qwen and Gemma smoke attempts incurred additional tiny charges; the total above includes **only the successful full run**, not smoke/diagnostic calls.

Artifact provenance:
- Qwen: `openrouter-full-qwen-39901560159`, artifact ID `12479510585`, archive SHA256 `d48be5b7a3881445793c229759b9495f3f4d394571440f8aafe5b054fb4ac2df`.
- Gemma: `openrouter-full-gemma-39901560159`, artifact ID `12479003410`, archive SHA256 `bfa5e5e448615cf218bbd6b3451ca62b3118d388d60c1bd6ec349e23c2af86bd`.

Artifacts contain actual one-letter replies, response IDs, returned model/provider and token/cost metadata, plus scorer JSON. Retention is 30 days. Repository secret values are not in the artifacts.

## Development-only results: 9 independently generated forms per root and condition

| Condition | Model | `dik` correct | `dir` correct | `dirig` correct |
| --- | --- | ---: | ---: | ---: |
| **Unglossed** | Qwen3 32B | 4/9 | 5/9 | 9/9 |
| **Unglossed** | Gemma 3 27B | 3/9 | 2/9 | 9/9 |
| **Explicit glossary** | Qwen3 32B | 8/9 | 9/9 | 6/9 |
| **Explicit glossary** | Gemma 3 27B | 9/9 | 6/9 | 9/9 |

Paired development comparisons on matching grammatical forms (each model and condition 9 pairs):

| Condition | Model | `dir` correct, `dik` wrong | `dik` correct, `dir` wrong | Both correct | Both wrong |
| --- | --- | ---: | ---: | ---: | ---: |
| Unglossed | Qwen | 3 | 2 | 2 | 2 |
| Unglossed | Gemma | 2 | 3 | 0 | 4 |
| Glossary | Qwen | 1 | 0 | 8 | 0 |
| Glossary | Gemma | 0 | 3 | 6 | 0 |

### Interpretation

Neither model provides reproducible evidence of a decisive **lexical recognizability** advantage for `dir`: one model favors it by one answer in the unglossed development subset, the other favors `dik` by one. Neither is evidence of human recognition or auditory accessibility. Explicit-glossary results differ materially: Qwen performed better on `dir`, Gemma better on `dik`, which raises an important prompt-use and model-confusion question; the groups are very small and dependent, and no root choice should be tuned against frozen-evaluation cases.

Both models answered all 9 `dirig` unglossed development forms correctly, indicating the control is easier to guess from international form, **not** proving `dir` and `dirig` would be safely disambiguated in free discourse. The 54 finite forms used earlier in the tokenizer experiment and the 221 structural parity pairs remain valid as **mechanical** evidence, but not semantic equivalence proof.

**Decision at this stage:** keep canonical `dik`, `stru`, `kurar`, `sentr` unchanged. Continue evaluation of `dir` (still a promising design option because it resolves the modeled `dik/tik` soft-merger and has three letters), but do not call the lexical-replacement superiority empirically established.

## Methodology shortcomings before a real decision

1. Only three verb roots, a limited choice set, and repeated morphology; no independent natural-language translation assessment, open-ended semantic interpretation or native-user validation.
2. Different model generation policies (Qwen explicitly non-thinking versus Gemma as served).
3. Prompts reveal the language construction and finite-morphology rules. Task can be solved/guessed via orthographic associations; this is **not** a genuinely unseen natural-language understanding test.
4. The evaluated `dirig` control is easier than both `dik` and `dir` in the unglossed condition. Better distractors and more roots are required to estimate an interpretable baseline.
5. The original small frozen-evaluation subset is not evidence of broad transfer. Do not use it to choose a root or optimize the test.
6. The model may have been previously exposed to related spellings or model-family training contamination. A real speaker sample stratified across languages is needed for written and spoken recognizability.

References: `benchmarks/root_recognition.py`, `benchmarks/openrouter_runner.py`, `research/lexicon/root-recognition-evaluation.md`, `docs/ldr/LDR-0009-alternative-roots-dir-konstru.md`.
