# CLAUDE.md — GlottoDelta language specification

This directory is the live language specification. Historical source documents
are preserved verbatim under `../legacy/original-language/`; research evidence
and decision studies live under `../research/`.

## Canonical phoneme inventory

Vowels: `a e i o u`

Consonants/glides: `p b t d k g m n f v s z l r j w`

`j=/j/`, `w=/w/`. There is no phonemic schwa, `h`, `sh`, `c`, `ŋ`, `ɲ`, or
independent affricate phoneme. `ts`, `tj`, `dj`, `sj`, and `gn` are transparent
sequences with permitted coalescent realizations.

## Editing policy

1. Edit these Markdown files when a design decision changes the language.
2. Preserve the historical files under `legacy/original-language/` unchanged.
3. Put quantitative studies, alternatives, and evidence in `research/`.
4. Record confirmed decisions on local `main`; do not use a remote unless the
   user explicitly requests it.
5. Keep examples synchronized with the current lexicon and morphology.
6. Do not reintroduce obsolete forms from the historical snapshot merely
   because they appear in old prose.
