# Unisermo

**Unisermo** is a constructed international language with Latin/international
lexical foundations, regular morphology, and an emphasis on pronounceability,
clarity and efficient communication between humans and language models.

This repository contains the **local, independently developed language project**.
Its naming and language specifications are separate from the **GlottoDelta IPA
atlas**, which continues to be maintained at
<https://github.com/andreabenetton/glottodelta>.

## Repository layout

```text
unisermo/
├── language/                    Canonical human-readable language rules
├── research/                    Grammar, lexicon, phonology, candidate studies
├── formalization/
│   ├── schema/                  Data contracts and JSON Schema
│   ├── data/                    Decision indexes, morphology and lexicon metadata
│   ├── generator/               Deterministic finite and nominal generation
│   ├── parser/                  Word analyses and narrow SVO clause parser
│   ├── semantics/               Explicit semantic limitations and future model
│   └── corpus/                  312 machine-checked morphology examples
├── benchmarks/
│   ├── corpus/                  Pilot paired-language sentences
│   ├── reports/                 Readiness report; no invented token results
│   ├── requirements-openai.txt  Pinned official OpenAI tiktoken library
│   └── tokenizers.py            Audited adapters to real tokenizers
├── .github/workflows/           Opt-in tokenizer benchmark for independent repo
├── docs/ldr/                    Accepted/proposed/experimental design records
├── scripts/                     Unisermo research and linguistic analysis
├── tests/                       Regression and provenance checks
├── legacy/original-language/    Immutable original specification
└── vendor/glottodelta-atlas/    FROZEN historical atlas snapshot, not upstream
```

Main starting points: [`language/README.md`](language/README.md),
[`formalization/README.md`](formalization/README.md),
[`benchmarks/README.md`](benchmarks/README.md), and
[`docs/ldr/README.md`](docs/ldr/README.md).

## Relationship with GlottoDelta

The atlas snapshot is isolated under [`vendor/glottodelta-atlas/`](vendor/glottodelta-atlas/).
Its original `baseline/`, `data/`, `public/`, `scripts/`, `package.json`, and
original README/CLAUDE instructions remain byte-for-byte preserved (see
[`docs/ATLAS_SNAPSHOT.md`](docs/ATLAS_SNAPSHOT.md)). It is research input for
Unisermo, **not** the latest or canonical atlas. The actively maintained atlas
remains <https://github.com/andreabenetton/glottodelta>.

There is no Git remote configured. Do not update or deploy the snapshot from
this repository, and do not push this repository to the atlas upstream.

## Formalization and decision traceability

Design rationale is recorded as **Language Design Records (LDRs)** under
`docs/ldr/`, independently of the old confirmed-decision JSON. The proposed
weighted lexical-efficiency score is experimental and has not changed the
language canon. See [`formalization/AUDIT.md`](formalization/AUDIT.md) for
remaining work.

```sh
python3 -m formalization build --check
python3 -m formalization validate
python3 tests/test_formalization.py
```

## Phase 2 — tokenizer evaluation

The draft parallel corpus contains **78** short parser-verified Unisermo / English
pairs, not human-validated translations. The pilot's readiness report
(`benchmarks/reports/readiness.json`) deliberately contains **no real token
counts** until a real model tokenizer is available. A measured reduction is
*not* evidence of LLM correctness or task efficiency.

```sh
python3 benchmarks/build_pilot.py --check
python3 -m benchmarks readiness
python3 -m pip install -r benchmarks/requirements-openai.txt
python3 -m benchmarks measure-openai --include-draft --output-dir benchmarks/reports
python3 tests/test_benchmarks.py
```

The official OpenAI tokenizer source is https://github.com/openai/tiktoken; the
benchmark pins PyPI version `0.14.0`. A first vocabulary download may require
network access even after the Python package is installed. An opt-in GitHub
Actions workflow can generate real `o200k_base` and `cl100k_base` reports in a
future **separate Unisermo repository**. No tokenizer is installed or executed
in this offline archive build: existing readiness data is **not** a measurement.
Absent tokenizers fail explicitly rather than producing invented counts. The
experimental protocol is documented in LDR-0006.

## Local tests

From the repository root:

```bash
for test in tests/test_*.py; do python3 "$test"; done
```

Some test suites are compute-intensive or require optional dependencies. The GlottoDelta
snapshot's original browser test commands remain documented separately under
`vendor/glottodelta-atlas/docs/`.

## Development policy

Maintain Unisermo's own Git history locally. **No Git remote is configured**
in the distributed repository. Never configure or push to the GlottoDelta
upstream without explicit owner authorization. Preserve the immutable language
legacy snapshot and the frozen IPA research dataset.

The earlier rename to Unisermo did not alter pronunciation rules, roots
or grammatical decisions. The separate Phase 1 `formalization/` workspace
implements a reference mirror and decision traceability without introducing
new language semantics.

## Licence

This code and material retain their existing licence notices; consult
[`LICENSE`](LICENSE) and the atlas snapshot's component attribution before
redistributing or deploying anything.
