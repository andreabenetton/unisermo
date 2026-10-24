# Sibling kinship — adel family

This document is part of the **current Unisermo language specification**. It restores a choice made in the original ChatGPT design dialogue on **10 August 2026 at 16:11:23 UTC** and omitted during the subsequent Git integration. The author expressly reconfirmed the intended replacement on **24 October 2026**.

## Confirmed sibling lexemes

| Form | Meaning | Structure |
| --- | --- | --- |
| `adel` | sibling; brother or sister without specifying sex/gender | neutral relational root |
| `adelo` | brother; male sibling | `adel + o` |
| `adele` | sister; female sibling | `adel + e` |

The `-o/-e` endings above are **explicitly confirmed for the adel sibling family**. This specification does not automatically impose noun gender or productive kinship-gender suffixes on all other roots. All three surface forms are stored explicitly in `research/lexicon/confirmed_lexicon.json` and recognized as nouns by the reference parser.

Nominal cases follow the general [seven-case system](noun_case_system.md), for example:

- `adeloem`: brother as direct object
- `adeleem`: sister as direct object
- `adelem`: sibling as direct object

These forms express sibling relations; they are not a distinct grammatical person/number marking system.

## Retired choice and documentary compatibility

`frat` previously meant **brother** in the original [10 August 2026 Git commit](https://github.com/andreabenetton/unisermo/commit/a1df1425bddf6e8636074ffb50309b1fd9476c1f). It was superseded by an author-approved dialogue choice but the lexical migration was **forgotten**. The author resolved that discrepancy on **24 October 2026**, explicitly requesting **`adel` to replace `frat`**.

Accordingly, `frat` is **not a canonical synonym or current lexical root**. It survives in immutable history, the original migration note, and historical frozen experimental corpora. The reference parser may retain it as an `example_only`/legacy attestation so old benchmarks remain interpretable, which **does not reinstate** it as current normative vocabulary. Do not create new teaching materials or research samples using `frat` as a confirmed form.

## Unconfirmed related designs

The original discussion also considered `gen/geno/gene` for parent/father/mother and `adelgen` as sibling-of-parent. Earlier studies contain `par/fil/av/germ/sib` alternatives. Their exact canonical status is **not changed here**: they need independent design approval, collision checks and clarification of how relational compounding works.

`jer` remains the separately canonized general [iteration/step operator](numerals.md), not a special kinship suffix. Nothing in this sibling lexical restoration validates all possible genealogical composites.

See [original dialogue vs saved Git](../research/history/august-kinship-original-dialogue-versus-git.md) for the dated original user-message index, and [migration history](MIGRATION_HISTORY.md) for the original and restored states.
