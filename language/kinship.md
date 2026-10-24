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

**Reference-parser limitation:** `bisjergen` is explicitly listed in the confirmed lexicon and can be recognized by the current Phase 1 parser. `terjergen` and further `NUMjergen` combinations are licensed by the language specification but **not yet handled by a general productive compound parser**. An illustrative form is therefore not proof of implemented parser support.

## Exact maternal and paternal relations: typed genealogical paths

The **confirmed** kinship composition rule is `A+B = A relative to B`: the rightmost component names the closest relative to the reference person (ego), and the component to its left names the next relation to follow **from that relative**. The compound is written as one word; morpheme boundaries below are displayed only for analysis.

Importantly, **`geno` (father of) and `gene` (mother of) are complete relational links**, not gender inflections over the whole compound. Thus the individual's gender and the paternal/maternal branch are separately encoded in each link, without a new scope-marking suffix.

| Canonical spelling | Decomposition (right to left) | Meaning |
| --- | --- | --- |
| `genegene` | `gene + gene` | **maternal grandmother** = mother's mother |
| `genegeno` | `gene + geno` | **paternal grandmother** = father's mother |
| `genogene` | `geno + gene` | **maternal grandfather** = mother's father |
| `genogeno` | `geno + geno` | **paternal grandfather** = father's father |

All four expressions are now listed explicitly in the confirmed lexicon and can be recognized in the **limited Phase 1 formal reference**. Their path derivation is deterministic from atomic `geno` and `gene` links; it does **not** prove that real listeners will distinguish long genealogical strings without training.

**Partial specificity:** A neutral `bisjergen` means any grandparent: two applications of unspecified `gen`. `gengene` means parent **of mother**, maternal grandparent of unspecified gender; `gengeno` means parent **of father**, paternal grandparent of unspecified gender. These last two are **productive analytical compositions**, not separate listed lexemes in the Phase 1 index.

### What `jer` repeats, precisely

`NUMjer+RELATION` applies the **whole relation lexeme** the indicated number of times. For example:

- `bisjergen` = `gen(gen(ego))`: any grandparent.
- `bisjergene` = `gene(gene(ego))`: maternal grandmother (same path as `genegene`), **not** a generic grandmother of either branch.
- `bisjergeno` = `geno(geno(ego))`: paternal grandfather (same path as `genogeno`), **not** a generic grandfather of either branch.

The `bisjer` alternatives are **semantically licensed transparent formations**, but productive `NUMjer` parsing is not implemented generally by the Phase 1 parser. Prefer the explicit four-way root-path spellings when precise ancestry is needed. This rule resolves the earlier suffix-scope ambiguity by refusing to treat final `-o/-e` as global gender markers.

### Generalization

A longer chain is interpreted by applying successive known **relational links from right to left**. For example `genegenogeno` = mother of father of father (father's father's mother). The meaning follows the same rule without inventing a special word for each ancestor. For longer or unusual paths, explicit morpheme segmentation may be shown in teaching material; the normative orthography stays fused.

## Descendant inverse and first cousin

**`fil` is ratified by the author on 24 October 2026** as the neutral relational inverse of `gen`:

| Form | Meaning | Decomposition |
| --- | --- | --- |
| `fil` | offspring; son or daughter, gender-neutral, **not restricted to children by age** | inverse relation to `gen` |
| `filadelgen` | **first cousin**, gender-neutral | `fil + adel + gen` = child of parent's sibling |

For `filadelgen`, apply `gen` to ego (parent), then `adel` to that parent (uncle/aunt), then `fil` to that relative (first cousin). The form is **confirmed as a transparent productive compound**, not a free-standing new family root.

This covers first cousins at the same genealogical generation; other degrees, removals, adoptive relations, and nonstandard genealogies may require additional disambiguation. `filo/file` were discussed as gender-marked offspring candidates in past notes, but approval of the **neutral `fil` root** does not automatically approve those derived spellings.

## Unconfirmed related designs

Earlier studies contain `par/av/germ/sib` alternatives. These remain historical proposals: the approval of `fil` does not automatically approve `filo/file` or unrelated earlier kinship roots.

`jer` remains the separately canonized general [iteration/step operator](numerals.md), not a special kinship suffix. The approved parent system validates `bisjergen` and the stated right-to-left path-composition rule. Each specified `gene/geno` link carries its own meaning; there is no global gender suffix for a whole genealogical path. The reference parser still has a limited fixed indexed vocabulary.

See [original dialogue vs saved Git](../research/history/august-kinship-original-dialogue-versus-git.md) for the dated original user-message index, and [migration history](MIGRATION_HISTORY.md) for the original and restored states.
