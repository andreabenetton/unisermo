# Blinded lexical recognition test — experimental (LDR-0009)

This is a reproducible **model-discrimination experiment**, separate from the 78-row tokenizer pilot, its holdout, and all independently unreviewed English translations.

## What it tests

The root `dik` currently means say/tell; `dir` is the proposed replacement. The established root `dirig` (direct/guide) is a **confusion control** because it shares the opening letters of `dir`. `tik` is a separate proximal demonstrative and is covered by the structural and accent-merger tests; it is not treated as a competing infinitive.

There are **72** single-question tasks: 12 matched grammatical patterns × 3 roots × 2 conditions. Each target root appears 12 times per condition. Every sense option is correct in position A, B, or C **exactly four times** per root and condition, avoiding a systematic correct-letter bias. Nine grammatical patterns per condition/root belong to development and three to a separately reserved evaluation subset.

Each target word is checked against the reference grammar: the official parser interprets `dik` and `dirig`, while an in-memory *experimental* grammar interprets `dir`. The test never changes the confirmed lexicon. All task prompts specify the finite suffix ordering.

Two independent conditions:

1. **Unglossed:** supplies the Unisermo finite verb morphology but *no* root-to-English dictionary. Measures limited lexical inference from the visible root in this closed-choice setting. A model can guess based on similarity or prior exposure; this is **not a direct human-recognizability result**.
2. **Explicit glossary:** supplies `dik=say/tell`, `dir=say/tell`, and `dirig=direct/guide`. Measures whether the model can correctly use declared lexical assignments despite potentially misleading root similarity. This is **not spontaneous lexical recognition**.

Each question asks only which lexical action is expressed, rather than full sentence translation. The option `build or construct` is a distractor, not a claim that these senses are identical under Unisermo grammar.

## Create the two separate files

```sh
python -m benchmarks.root_recognition build --output-dir benchmarks/reports
```

- `root-recognition-prompts-v1.jsonl`: public prompt pack with options; **does not contain answers**.
- `root-recognition-answer-key-v1.jsonl`: matching expected choices, feature controls, roots and split. **Never send it to the tested model**.

Every prompt must be sent to a model in a **new isolated conversation**, not in a sequential chat. That prevents the explicit glossary or another trial from contaminating later unglossed tasks. Keep model ID/version, provider, date, effort/sampling settings, retries and actual input/output token totals in separate execution metadata. Do not fetch the key through an agent's retrieval context.

Your independent model runner should save one response per line, with exactly these fields:

```json
{"id":"R001","answer":"A"}
```

The letter in the example is **not** the official answer. The scorer does not parse explanations, and invalid outputs count as failures rather than being silently corrected.

## Score externally obtained responses

```sh
python -m benchmarks.root_recognition score \
  --key benchmarks/reports/root-recognition-answer-key-v1.jsonl \
  --responses /path/to/actual-model-responses.jsonl \
  --model-id provider/model-version \
  --output benchmarks/reports/root-recognition-score.json
```

The result reports grouped accuracy by candidate root, condition and split, plus `dir`-only / `dik`-only paired successes for the same grammatical pattern. It **does not** publish per-item evaluation outcomes, since those could encourage tuning on the evaluation subset. Do not report inferential significance from repeated, non-independent paradigms.

**As of this change there have been ZERO real LLM evaluation trials.** Unit tests use *synthetic test answers*, which are not research observations. GitHub Actions builds the prompt pack and runs correctness tests, but does not call any paid LLM endpoint, invent comprehension results, or expose private API credentials.

## Adoption gate

Before accepting `dir` as canonical:
- Run multiple actual model families, with pinned versions, independent contexts and fixed prompts.
- Compare unglossed root recognition against `dik`; check especially confusion with `dirig`.
- Compare performance after a shared glossary; score task success and total token/retry overhead, not spelling alone.
- Independently test written *and spoken* recognition with real multilingual participants; the trial above tests neither human audio recognition nor unprompted use.
- Verify grammar structure, prefix interaction, permitted accent mergers and compatibility with documented old forms.
- Present a new explicit owner-approved language change LDR and a migration plan. Otherwise retain the current accepted root.

See `research/lexicon/root-replacement-evaluation.md` and `docs/ldr/LDR-0009-alternative-roots-dir-konstru.md`.
