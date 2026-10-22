# Unisermo

**Unisermo** is a constructed international language with Latin/international
lexical foundations, regular morphology, and an emphasis on pronounceability,
clarity and efficient communication between humans and language models.

This repository contains the **local, independently developed language project**.
Its naming and language specifications are separate from the **GlottoDelta IPA
atlas**, which continues to be maintained at
<https://github.com/andreabenetton/glottodelta>.

## Where to begin

- [`language/`](language/) — current, editable normative language specification.
- [`research/grammar/`](research/grammar/) — confirmed grammatical decisions.
- [`research/lexicon/`](research/lexicon/) — confirmed and audited lexicon.
- [`research/phonology/`](research/phonology/) — phonological evidence and candidate studies.
- [`scripts/`](scripts/) — research analyzers and regression checks.
- [`docs/ldr/`](docs/ldr/) — Language Design Records (decision history, alternatives, hypotheses and evidence).
- [`formalization/`](formalization/) — Phase 1 sourced machine-readable reference, parser, generator and tests.
- [`legacy/original-language/`](legacy/original-language/) — immutable historical source documents.
- [`language/MIGRATION_HISTORY.md`](language/MIGRATION_HISTORY.md) — migration history.

## Relationship with GlottoDelta

The `baseline/`, `public/`, `data/` and atlas-related `scripts/` files are a
**local historical snapshot** of the GlottoDelta IPA atlas. They exist solely
as input for Unisermo phonetic research and as a reproducibility aid. They are
**not** the canonical or latest version of the atlas; the GitHub repository
linked above is the source of truth for future atlas development.

Do not rename the GlottoDelta branding inside that snapshot, replace its IPA
data with Unisermo vocabulary, publish this copy as the live atlas, or push
changes from here to the atlas repository. Any future refresh of the atlas
research dataset must be an explicit, separately reviewed operation.

See [`docs/atlas-snapshot/`](docs/atlas-snapshot/) for the original atlas
README and maintainer instructions retained as reference, and
[`docs/ATLAS_SNAPSHOT.md`](docs/ATLAS_SNAPSHOT.md) for data provenance.

## Formalization and decision traceability

Design rationale is recorded as **Language Design Records (LDRs)** under
`docs/ldr/`, independently of the old confirmed-decision JSON. The proposed
weighted lexical-efficiency score is experimental and has not changed the
language canon. See [`formalization/AUDIT.md`](formalization/AUDIT.md) for
remaining work.

```sh
python3 -m formalization build --check
python3 -m formalization validate
python3 scripts/test_formalization.py
```

## Local tests

From the repository root:

```bash
for test in scripts/test_*.py; do python3 "$test"; done
```

Some tests require optional dependencies or environments. The GlottoDelta
snapshot's original browser test commands remain documented separately under
`docs/atlas-snapshot/`.

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
