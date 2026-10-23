# Open-ended sentence understanding pilot (2026-10-23)

This pilot is distinct from the earlier 72-question multiple-choice test. Run: https://github.com/andreabenetton/unisermo/actions/runs/39902217811

## Design

- 8 finite-verb sentence structures, 3 root conditions (`dik`, experimental `dir`, and `dirig` control), 2 modes (unglossed and explicit dictionary), totaling 48 independent requests **per model**.
- Pairwise root replacement changes only the target verb and leaves the subject, question/negation marker, and object unchanged. The two reference interpreters accept exactly the expected grammatical features; canonical files remain unchanged.
- Each model returns its own basic English action as `{"verb":"..."}` **without any offered answer choices**. Controlled context vocabulary (`amik`, `fakit`, `tik`) and grammar are supplied in the prompt, so this is not wholly unsupervised language comprehension.
- Two OpenRouter models: `qwen/qwen3-32b` (nonthinking prompt variant) and `google/gemma-3-27b-it` (standard). Provider fallback disabled. Hard request ceiling is 48 per model; sequential requests use limited 429 retries and progressive persistence.
- A **diagnostic whitelist** maps obvious verb synonyms to the intended sense; unknown or unusual verbs remain in the report as requiring manual semantic assessment. It is not a human or LLM-as-judge semantic equivalence verdict.
- The final two sentence structures per root/condition are marked reserved; do not select or tune roots against them. The existing historical holdout remains untouched.
- No independently reviewed naturalistic translations, native-speaker comprehension, audio understanding, population-weighted results, or output-quality validation can be claimed from this pilot.

## Reproduce offline

```sh
python -m unittest discover -s tests -p 'test_open_inference.py' -v
```

`benchmarks/open_inference.py` builds independent prompts and reference keys. `benchmarks/open_inference_runner.py` uses the GitHub repository secret when invoked in the isolated, commit-guarded workflow. Raw OpenRouter model outputs and mechanical scoring are retained as per-model GitHub Actions artifacts, not committed as benchmark source data.

**Decision gate:** Even if one candidate performs better on two small LLM families, that does not establish that contemporary language populations can read or understand its pronunciation. Keep `dik`, `stru`, `sentr`, `kurar` canonical unless owner later approves an independently justified LDR.
