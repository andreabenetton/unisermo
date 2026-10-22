---
id: LDR-0009
title: Evaluate dir and konstru as lexical root replacements
status: Experimental
date: 2026-10-22
domain: lexicon
supersedes: none
---

# LDR-0009 — Evaluate dir and konstru as root replacements

## Context and problem

The owner asked to reassess `dik` = say/tell in favor of `dir`, and `stru` = build/structure in favor of source spelling `constru`, while leaving `kurar` and `sentr` unchanged. This supersedes the former owner *preference* to retain `dik`, but not the accepted canonical lexicon. `c` is excluded from Unisermo; hence `constru` cannot be an accepted spelling. Experiment on `konstru` and `kostru`.

## Alternatives

1. Retain `dik`: three letters, existing productivity, but allowed `d → t` accents risk an acoustic merger with normative demonstrative `tik` (issue #1).
2. Test `dir`: three letters; exact Catalan spelling, close to Italian/French *dire* and to Spanish *decir* / Portuguese *dizer*, but actual pronunciation and recognition vary by language. German `dir` means "to you" and is a cross-language false friend, not a Unisermo homograph.
3. Retain `stru`: compact four-letter etymological root; shares the `stru-` stem with internationally common structural word families.
4. Test `konstru`: seven letters, corresponds to Latin *construere*, Spanish *construir*, French *construire*, English *construct*, German *konstruieren*, with complex /nstr/ sequence requiring accessibility review.
5. Test `kostru`: six letters, near Italian *costruire*, with less direct overlap in Spanish/French/English.
6. Reject `constru` as a canonical candidate because `c` is outside the alphabet.
7. No new proposals for `sentr` and `kurar`; their existing canonical forms remain frozen.

## Decision or hypothesis

Research `dik → dir`, `stru → konstru`, and `stru → kostru` *counterfactually*, with no canonical lexical modification. Compare actual `tiktoken` costs across generated inflections, potential derivations and development-only corpus inputs; report exact and accent-merger collision diagnostics. Keep written and spoken recognition separate, with no population scores until independently validated.

The hypothesis favoring `dir` is stronger than that favoring `konstru`, because `dir` does not add graphemes and removes the `dik/tik` accent-merger risk. Neither hypothesis is yet accepted.

## Evaluation and evidence

- `benchmarks/root_substitution.py` produces comparable, reproducible token totals per candidate on `o200k_base` and `cl100k_base`. It evaluates 54 hypothetical finite inflections, seven nominal cases, six productive suffixes and only available *development* corpus cases; no holdout examples are used or ranked.
- The existing pilot has `dik` verb examples but **no** `stru` examples, so its evidence cannot be generalized to the construction family.
- Count changes for whole forms, not letters alone; evaluate full LLM comprehension/cost and human recognition separately.
- Before norming any change: verify word-level and derivational collisions, pronounceability of clusters, sense preservation for "build" versus "structure", and differences among major modern-language populations.
- Distinguish phonology from spelling: Eastern Catalan `dir` is often /di/ while Valencian pronunciations may retain /diɾ/. Italian/French `dire` preserve an audible rhotic in different realizations; a visual identity is not automatically an acoustic identity.

Evidence: https://ca.wiktionary.org/wiki/dir ; https://www.treccani.it/vocabolario/dire/ ; https://www.dictionnaire-academie.fr/article/A9D2606 ; https://www.littre.org/definition/construire ; https://www.etymonline.com/word/construct ; https://kaikki.org/dictionary/German/meaning/d/di/dir.html .

## Consequences and compatibility

Normative `language/` specifications, confirmed lexicon, parser, corpus and historical decisions remain untouched. A future accepted lexical migration would have to revise accepted source documents and regenerate data indexes, handle compatibility aliases, corpus provenance, morphological and derivational forms, and regression tests. A status of Experimental must not be interpreted as acceptance.

## Decision authority

The owner explicitly authorized **evaluation**, not irreversible canonical replacement. An approved adoption requires a new explicit decision after reviewing measured tokenizer, collision, semantics and recognition results.

## References

- `docs/ldr/LDR-0008-lexical-recognizability.md`
- `docs/ldr/LDR-0003-semantics-preservation.md`
- `research/lexicon/candidate-register.json`
- `benchmarks/root_substitution.py`
- `language/alphabet_and_phonology.md`
- `language/derivation.md`
- https://github.com/andreabenetton/unisermo/issues/1
