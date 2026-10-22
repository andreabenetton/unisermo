# Unisermo — repository guidance

Unisermo is the artificial international language designed here. **GlottoDelta**
is a distinct phonetic atlas maintained independently at
https://github.com/andreabenetton/glottodelta.

## Scope and source of truth

- `language/` contains the current Unisermo specification. Keep its decisions
  consistent with `research/grammar/confirmed_decisions.json`,
  `research/phonology/confirmed_decisions.json`, and
  `research/lexicon/confirmed_lexicon.json`.
- `research/` contains working evidence and studies for Unisermo, which may
  refer to the GlottoDelta snapshot as a dataset.
- `legacy/original-language/` is immutable; keep `SHA256SUMS` valid.
- `vendor/glottodelta-atlas/` holds `baseline/`, `data/`, `public/`, its own
  `scripts/`, `docs/`, and `package.json` as a frozen research reference;
  NOT the authoritative atlas. Do not edit, regenerate or publish those files.
- The up-to-date GlottoDelta atlas remains on its original GitHub repository.
  Refreshing the research snapshot is independent from Unisermo development.

## Git safety

This repository is a local, independently maintained Unisermo working copy.
Do not add a Git remote, and do not push to GitHub, unless expressly requested.
In particular, NEVER push language changes to `andreabenetton/glottodelta`.

## Decision records

Before treating a new linguistic choice or LLM-efficiency optimization as
normative, read `docs/ldr/README.md` and record an LDR with alternatives,
evidence and explicit acceptance. Unvalidated scoring formulas must remain
`Experimental`; parser/JSON formalization is a source-linked mirror of live
`language/` until a migration LDR is accepted. Avoid silently inventing
rationales for the pre-LDR confirmed decision corpus.

## Workflow

1. Read `language/CLAUDE.md` before changing grammar or vocabulary.
2. Distinguish confirmed decisions from tentative experiments; do not silently
   alter language semantics as part of a refactor or renaming.
3. Preserve the complete Git history and immutable legacy files.
4. Run tests in `tests/test_*.py` after language-related changes; `benchmarks/` is experimental and never normative. OpenAI token counts must use the official pinned `tiktoken` implementation, not text-length approximations. Do not claim results exist if a vocabulary cannot load.
5. Use the name **Unisermo** for the language, and **GlottoDelta** only when
   specifically referring to the original IPA atlas or historical citations.

For historical GlottoDelta atlas architecture, see
`vendor/glottodelta-atlas/docs/CLAUDE.md`.
