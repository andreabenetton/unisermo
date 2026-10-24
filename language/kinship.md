# Kinship — sibling, parent and iterative relations

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

## Confirmed parent and intergenerational lexemes

The user also expressly approved `gen/geno/gene` and `adelgen` in the **24 October 2026** historical-reconstruction conversation, confirming a previously recovered 10 August dialogue.

| Form | Meaning | Structure |
| --- | --- | --- |
| `gen` | parent (unspecified gender) | relational root |
| `geno` | father | `gen + o` |
| `gene` | mother | `gen + e` |
| `adelgen` | uncle/aunt, gender-neutral | `adel + gen` = sibling **of parent** |
| `bisjergen` | grandparent, gender-neutral | `bis + jer + gen` = two parent steps |

**Composition direction:** `A+B` means "A **of B**" in relation compounds. Thus `adelgen` is a sibling **of a parent**, not the parent of a sibling. Compounds are written without spaces or hyphens.

The preexisting general [`jer` operator](numerals.md) is used to count successive applications of a relation, **not just genealogy**. Historical user messages from **10 August 2026** already cite `bisjergen` as grandparent and `terjergen` as great-grandparent; these are transparent applications of the productive numeral + iteration mechanism. A genealogical prefix `NUMjer` specifies the number of parent links traced upward. `terjergen` thus denotes three ascendant parent links without requiring another independent lexical root.

**Open ambiguity about sex/gender scope of grandparents:** `bisjergeno` could be parsed as `bisjer + geno`, repeating the *father* relation, rather than selecting a *male individual* after two unrestricted parent links. Similarly `bisjergene` risks a maternal-line reading. The original indexed excerpts do **not** establish a binding scope rule, so neither spelling is canonized as the general "grandfather"/"grandmother". **`bisjergen` is presently the neutral canonical expression covering both**. A separate binding or gender-scoping rule is needed for exact male/female grandparent terms.

## Cousin composition: pending inverse relation

Under the rule `A+B = A relative to B`, a first cousin is a **child of a parent's sibling**, structurally `CHILD + adelgen`. If the previously proposed neutral descendant/offspring root `fil` is accepted, this gives the **candidate** `filadelgen` (child of uncle/aunt). However, **`fil` is not yet approved** as a canonical inverse to `gen`, and the compound is therefore **not canonized**. Before approving it, distinguish relational *offspring* from a young *child*, and check whether the genealogical terminology includes cousins of different degree and generation.

## Unconfirmed related designs

Earlier studies contain `par/fil/av/germ/sib` alternatives. These are **not** promoted merely by approving the `gen/adelgen` system. In particular, `fil` (offspring) and `filadelgen` (cousin) remain explicitly proposed pending approval.

`jer` remains the separately canonized general [iteration/step operator](numerals.md), not a special kinship suffix. The approved parent system validates `bisjergen` and the general iteration rule, but not every possible genealogical compound or the gender-scope of repeated relations.

See [original dialogue vs saved Git](../research/history/august-kinship-original-dialogue-versus-git.md) for the dated original user-message index, and [migration history](MIGRATION_HISTORY.md) for the original and restored states.
