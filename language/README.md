# Unisermo language specification

This directory contains the **live Markdown specification** of the language.
It is intentionally descended from the original user-provided Markdown files,
so ordinary Git history shows how each document changes as decisions are made.

The untouched source snapshot is preserved at `../legacy/original-language/`.
Quantitative studies and design evidence live under `../research/`.

## Main documents

- `alphabet_and_phonology.md` — current 21-phoneme inventory and adaptation rules
- `verb_specification.md` — `root + aspect + time + person vowel + optional N`
- `noun_number_system.md` — number-neutral nouns and optional plural `wi`
- `noun_case_system.md` — seven synthetic cases plus analytic relators such as `kun`
- `articles.md` — no obligatory articles; optional indefinite `uno`
- `derivation.md` — `-or`, `-il`, `-ia`, `-it`, `-itat`, `-al` and prefixes
- `numerals.md` — cardinal numeral system including `kin` = 5
- `kinship.md` — sibling `adel/adelo/adele`, parent `gen/geno/gene`, uncle/aunt `adelgen` and grandparent `bisjergen`; historical `frat` retired
- `questions.md` — `ka` and the wh series, including `kom` = how and `ker` = why
- `negation.md` — `si/no` and focus enclitics `-si/-no`
- `copula.md` — `es` with the current person-number system
- `comparison.md` — comparison system with `major /ma.jor/` and `ekwal /e.kwal/`
- `demonstratives.md`, `adjectives.md`, `word_order.md`, `stress.md` — supporting syntax/prosody

## Current high-level invariants

- vowels `/a e i o u/`; no schwa
- `j=/j/`, `w=/w/`
- no official `c`, unitary `sh`, or independent affricate phoneme
- person `i/u/a`; plural `/N/` after the person vowel
- finite verb order: `root + aspect + time + person vowel + optional N`
- noun number neutral by default; optional explicit plural `wi`
- synthetic cases: Ø, `-em`, `-s/-es`, `-ad`, `-de`, `-in`, `-da`; comitative is analytic `kun + NP`
- indefinite singular may be expressed by the numeral/determiner `uno`
- `-it` participial/resultative; `-itat` abstract; `-ia=/i.a/` place/institution/field/domain
