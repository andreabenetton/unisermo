# Phase 2 — tokenization pilot (experimental)

This is a **research harness**, never a source of normative language rules.
It does not change accepted Unisermo morphology, lexicon or semantics.

## What exists

- `corpus/pilot.jsonl`: 78 paired Unisermo/English short clauses.
  The Unisermo phrases are parser-verified. English counterparts are **drafts**,
  not independently human-reviewed or established semantic equivalents.
- `build_pilot.py`: deterministic pilot generation and verification.
- `tokenizers.py`: real official OpenAI `tiktoken` adapter and optional local
  SentencePiece / Hugging Face tokenizers. Token calculations always use the
  tokenizer's implementation, **never** characters, bytes or word counts.
- `requirements-openai.txt`: pinned official `tiktoken==0.14.0` dependency.
- `run.py`: per-row counts, corpus digest, development/holdout grouping.
- `reports/readiness.json`: environment/readiness snapshot, **not** measurements.
- `.github/workflows/benchmark-openai-tokenizers.yml`: an opt-in cloud runner
  which can run upon manual dispatch or relevant pushes **if Unisermo is later
  published to its own GitHub repository**. It does not contact the GlottoDelta
  atlas repository.

## Install and run with official OpenAI tokenizers

From the project root in a networked Python environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r benchmarks/requirements-openai.txt
python benchmarks/build_pilot.py --check
python -m unittest discover -s tests -p 'test_benchmarks.py' -v
python -m benchmarks measure-openai --include-draft \
  --output-dir benchmarks/reports
```

The final command produces **both**:

- `benchmarks/reports/o200k_base-pilot.json`
- `benchmarks/reports/cl100k_base-pilot.json`

Alternatively, one specific tokenizer:

```sh
python -m benchmarks measure --tiktoken o200k_base --include-draft \
  --output benchmarks/reports/o200k_base-pilot.json
```

`get_encoding("o200k_base")` / `get_encoding("cl100k_base")` use the official
OpenAI library <https://github.com/openai/tiktoken>. The first load of an
encoding may download vocabulary files to a user cache; **installing the wheel
alone does not necessarily cache the vocabularies**. For reproducible offline
re-runs, first populate and preserve the directory designated by
`TIKTOKEN_CACHE_DIR` in a networked environment. The JSON reports include the
`tiktoken` package version, encoding name, SHA-256 fingerprint of the actual
merge-rank table, and corpus SHA-256.

Other tokenizer formats (when local vocabularies have been supplied):

```sh
python -m benchmarks measure --sentencepiece /path/to/tokenizer.model --include-draft
python -m benchmarks measure --hf-json /path/to/tokenizer.json --include-draft
```

`--include-draft` is mandatory to prevent premature claims about comparative
semantic efficiency. Failures to load `tiktoken`, to download an encoding, or
to resolve an unknown encoding are fatal; **no estimated results are emitted**.

If you publish this repository independently, open **Actions → OpenAI tokenizer
pilot → Run workflow** in that repository to generate JSON artifacts. Local
execution is also supported. The workflow does not create commits or upload
results to another repository.

## Interpretation limits

- The pilot is morphology-biased: 64 of 78 examples are inflected verbs.
- Translations are not independently reviewed; possible mismatches can bias
  apparent efficiency in either direction.
- Short standalone messages are not the same as end-to-end LLM prompts.
- Token-count percentage is **not** a claim about model understanding,
  translation fidelity, inference output, task success or cost per successful
  task. No statistical significance is claimed on this constructed pilot.
- Neither tokenizer is guaranteed to match every OpenAI model; benchmark the
  encoding corresponding to each concrete model when that information is
  documented by its provider.

## Acceptance gates for the next iteration

1. Independently verify semantic equivalence for every scored pair.
2. Create a more balanced corpus and a truly untouched holdout set.
3. Compare against **controlled concise English** as well as ordinary English.
4. Preserve tokenizer versions and vocabulary hashes across reruns.
5. Conduct model-level comprehension, round-trip and task-success experiments.
6. Record an accepted LDR **before** changing a lexical or grammatical rule.

See [LDR-0006](../docs/ldr/LDR-0006-tokenizer-benchmark-protocol.md).

## Post-run diagnostic (LDR-0007)

GitHub Actions run `39832551377` supplied genuine pilot result artifacts.
The unmodified JSON reports are retained in `benchmarks/evidence/`.
To produce the diagnostic, without needing `tiktoken` installed:

```bash
python -m benchmarks.diagnostics \
  --reports benchmarks/evidence/*json \
  --output benchmarks/reports/diagnostic-pilot.json
```

To additionally inspect **real** tokenizer boundaries on a machine with
`tiktoken` and vocabularies installed, append `--segment-openai`. Without that
flag, the diagnostic makes no claims about token *pieces* or merge rules.
The analysis lists worst and best samples only for the development split;
holdout gets aggregate metrics, not ranked examples. Every pilot translation
is pending independent semantic review. LDR-0007 specifies balanced 1,000-pair
quotas; no fabricated or unreviewed 1,000-pair corpus is presented as evidence.
