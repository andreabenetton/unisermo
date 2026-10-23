# Run the Unisermo lexical experiment through OpenRouter

The OpenRouter token is read **only** from `secrets.OPENROUTER_API_KEY` in the manual Actions workflow. Never place the key in a GitHub variable, workflow input, commit, artifact, or chat.

## Run

Open [OpenRouter lexical recognition (manual)](https://github.com/andreabenetton/unisermo/actions/workflows/openrouter-root-recognition.yml), click **Run workflow**, select `main` and:

| Input | First run | Following runs |
| --- | --- | --- |
| Model | `qwen/qwen3-32b` | `google/gemma-3-27b-it` |
| Subset | `smoke` | `smoke` |
| Max requests | `6` | `6` |
| Provider | leave blank | leave blank |

The smoke test is **six paid API calls per model** (12 total for two models), not a comprehension benchmark. Once both smoke tests have returned usable results, run `full` with `max_requests=72` per model (144 further calls total). A `development` selection runs 54 requests per model if intermediate testing is necessary; do not use the reserved evaluation cases to choose root spellings.

The job is **never triggered by pushes**. It has a repository-secret check, 30-minute job timeout, isolated independent user-only prompts, temperature 0, 48 output-token ceiling, no provider fallback, `data_collection=deny`, a per-model request cap and minimal non-secret progress logs. A blank `provider` uses OpenRouter's first eligible endpoint but does **not** pin a host; the response's provider/model metadata is saved when returned. To pin a host, supply a supported provider slug (e.g. `deepinfra`) only after confirming that provider serves the chosen model. With pinning, alternate providers cannot be used. Availability, price, zero-retention policy and model IDs should be checked before paid full runs.

Results are uploaded as an artifact retained for 14 days: `openrouter-responses.jsonl` (one actual model response per line) and, for `full` only, `openrouter-responses.score.json`. Raw results can contain model-generated text and usage metadata but no secret key. Do not assume any accuracy until a real run completes.

**Error policy:** HTTP/provider failures fail the job, not count as wrong lexical answers. Invalid *model* outputs (anything other than a single A/B/C) count as incorrect when scoring. In case of a failed run, the workflow does not upload partial responses; any billable requests already made may still incur cost. Re-run explicitly only after diagnosing the failure.

**Interpretation:** The existing 72 questions are controlled morphological patterns and do not validate human spoken or written recognition. The explicit-glossary condition measures use of a supplied dictionary rather than intuitive recognition. Do not select new roots on the frozen-evaluation subset, and do not change canonical `dik` without an accepted LDR.

Relevant files: `benchmarks/openrouter_runner.py`, `benchmarks/root_recognition.py`, `research/lexicon/root-recognition-evaluation.md`, `docs/ldr/LDR-0009-alternative-roots-dir-konstru.md`.
