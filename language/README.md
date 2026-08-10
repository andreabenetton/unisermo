# Synthetic Language Specification

This directory contains the formal specification of the synthetic language. Each topic is documented in exactly one place; other documents reference the canonical source rather than duplicating its content.

## Specifications

| Document | Scope |
|---|---|
| [`alphabet_and_phonology.md`](alphabet_and_phonology.md) | The official alphabet, canonical IPA values, acceptable pronunciation variants, contrast rules, and the pronunciation rule for geminated consonants. |
| [`verb_specification.md`](verb_specification.md) | The verb system: root, person vowels, tense/aspect/mode grid, gerund, imperative, negation, and the morphological origin of double consonants. |
| [`noun_case_system.md`](noun_case_system.md) | The noun case system: base and extended case suffixes, attachment to the final word of the noun phrase, and the `-s` / `-es` and `-due` phonological notes. |
| [`noun_number_system.md`](noun_number_system.md) | The noun number system: number-neutral nouns, the plural suffix `-en`, when explicit plural marking is required, and the **root + plural + case** morpheme order. |
| [`numerals.md`](numerals.md) | The cardinal numerals: the 13 base forms (`nul`–`mil`), the big-endian composition rule, and the interaction of numerals with the noun phrase. |
| [`word_order.md`](word_order.md) | Default constituent order (SVO), pro-drop, and case-licensed reordering for emphasis. |
| [`articles.md`](articles.md) | The article system: no obligatory articles, with the indefinite-singular determiner `uno` (one / a, doubling as the numeral). |
| [`demonstratives.md`](demonstratives.md) | The three-grade demonstrative system: `tik` (this), `tes` (that near you), `tan` (that, far), with no gender distinction. |
| [`adjectives.md`](adjectives.md) | Adjective placement (before the noun), no agreement, and interaction with case and plural. |
| [`negation.md`](negation.md) | The particle `no` placed immediately before the verb, covering finite forms, imperatives, and reordered sentences. |
| [`questions.md`](questions.md) | Question formation: polar marker `ka` and nine `k-` wh-words (`kid`, `kis`, `kos`, `kud`, `kan`, `kom`, `kur`, `kot`, `kal`), with clause-initial placement. |
| [`copula.md`](copula.md) | The copula verb `es` (to be / exist), the zero-copula rule for the present simple, and the use of `es` for past, future, aspect, and existence. |
| [`comparison.md`](comparison.md) | Comparison and superlative: `major`, `minor`, `masim`, `minus`, `dan`, `ekual`. |
| [`derivation.md`](derivation.md) | Derivational morphology: five suffixes (`-er`, `-or`, `-ia`, `-it`, `-al`) and fifteen prefixes (`no-`, `anti-`, `de-`, `re-`, `pre-`, `pos-`, `ko-`, `auto-`, `semi-`, `multi-`, `neo-`, `super-`, `sub-`, `mikro-`, `makro-`), with the full **root + derivation + plural + case** order. |
| [`stress.md`](stress.md) | Lexical stress: root stress (first syllable of the root, fixed across all inflected and derived forms), with the rule that unstressed syllables never reduce. |
| [`vocabulary_design_rules.md`](vocabulary_design_rules.md) | The rules governing how lexical roots and high-frequency words must be shaped, including safety levels, fragile minimal pairs, and adaptation of international roots. |

## Speaker profiles

The [`speaker_profiles/`](speaker_profiles/) subdirectory contains one document per major speaker background, describing compatible features, risks, and the vocabulary-design rule that follows from each profile.

See [`speaker_profiles/README.md`](speaker_profiles/README.md) for the index and the overall difficulty ranking.

## Canonical sources

To avoid duplication, the following facts are owned by a single document:

- **Alphabet, IPA values, acceptable variants, gemination pronunciation** — `alphabet_and_phonology.md`
- **Person vowels, TAM markers, verb morphology, gerund, imperative** — `verb_specification.md`
- **Case suffixes, noun-phrase attachment rule** — `noun_case_system.md`
- **Plural suffix `-en`, root + plural + case order, when plural is required, basic quantifiers `mult` / `al`** — `noun_number_system.md`
- **Cardinal numerals and their composition** — `numerals.md`
- **Default word order (SVO), pro-drop, and reordering for emphasis** — `word_order.md`
- **No obligatory articles; optional determiner `uno`** — `articles.md`
- **Demonstratives `tik` / `tes` / `tan` (three-grade, no gender)** — `demonstratives.md`
- **Adjective-before-noun, no agreement** — `adjectives.md`
- **Negation particle `no` immediately before the verb** — `negation.md`
- **Polar marker `ka` and `k-` wh-words for content questions** — `questions.md`
- **Copula `es`, zero-copula present, existential use** — `copula.md`
- **Comparison and superlative (`major`, `minor`, `masim`, `minus`, `dan`, `ekual`)** — `comparison.md`
- **Derivational morphology (5 suffixes + 15 prefixes), root + derivation + plural + case** — `derivation.md`
- **Root stress (first syllable of the root; no reduction of unstressed syllables)** — `stress.md`
- **Vocabulary-design rules and adaptation of international roots** — `vocabulary_design_rules.md`
- **Per-language compatibility analyses and difficulty ranking** — `speaker_profiles/`

Other documents link to these sources rather than restating them.
