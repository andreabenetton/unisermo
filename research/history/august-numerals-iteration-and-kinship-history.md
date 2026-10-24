# Numerals, fused compounds, iterative relations and kinship proposals (8–10 August 2026)

**Retrospective reconstruction: 24 October 2026.** Primary sources are the dated [original `language` numeral specification](https://github.com/andreabenetton/language/blob/bacc1a7a9aaaa18596120c6ea2812c927b33b0e3/numerals.md), independently verifiable Unisermo Git commits, indexed original user messages, and a **later 23 October 2026 preservation note** about prior kinship designs. Do **not** mistake the latter retrospective note for a signed original August decision about every relationship root.

## Documented alternatives and adoption

| UTC date | Primary evidence | Observed state or action |
| --- | --- | --- |
| **8 Aug 18:31** | [Original `language` commit `bacc1a7`](https://github.com/andreabenetton/language/commit/bacc1a7a9aaaa18596120c6ea2812c927b33b0e3), `numerals.md` | `duo` = TWO; `cin` = FIVE, other three-letter numerals, powers `dek/sen/mil`. Multiplicative big-endian composition and **space-separated orthographic sequences** in examples: `dek duo` (12), `duo dek` (20), `ter sen duo dek uno` (321). After numerals, the then-current noun suffix `-en` was optional. |
| **9 Aug and 10 Aug morning** | [`d5d9ed7`](https://github.com/andreabenetton/unisermo/commit/d5d9ed7c650e0c5ace90abf6487d15ec67e033a2), prior phonology and nominal-number changes | `cin→kin` follows removal of letter `c`; bare noun becomes number-neutral, with redundant `wi` normally omitted with numerals. |
| **10 Aug ~15:55 UTC** | Indexed original **user** message | Raises/reviews changing numeral TWO `duo→bis`, including a question about the preference. The indexed snippet **does not give a reliable, exhaustive comparative justification**; do not infer that `bis` is demonstrably shorter or more universal. |
| **10 Aug ~16:10 UTC** | Indexed original **user** message | Requests single-word concatenation `dekbis`, `bisdek` without spaces. The message time is recovered at approximate minute resolution. |
| **10 Aug 16:24:59** | [`4d19263`](https://github.com/andreabenetton/unisermo/commit/4d19263da58802bd184774b3d1463714c50979dc), *Canonize bis as numeral two* | **Canonical TWO `bis`**, replacing `duo` in numeral and grammar examples. The earlier `duo` is preserved in historical docs. |
| **10 Aug ~16:30 UTC** | Indexed original **user** message | Adopts `jer` for **generic repetition, iteration or relational steps**, not merely a dedicated genealogical generation marker; example patterns include `bisjer` and a longer genealogical example of the structural type `adelbisjer...`. Do not canonize the incomplete family-specific composite on this evidence. |
| **10 Aug 16:35:31** | [`b3c473e`](https://github.com/andreabenetton/unisermo/commit/b3c473e6f86cb58734e208491a7e2ed6306623c6), *Canonize jer iteration counter* | Explicitly changes multi-component numerals into **single orthographic words** (`dekbis`, `bisdek`, `tersenbisdekuno`). Confirms `NUMjer` = numerical iteration/step and use inside larger transparent compounds. Genealogy is one application; `jer` is **not an ordinal marker**. |

The timed user messages and the Git commits are separate evidence classes. In particular, the `dekbis/bisdek` preference was documented as a user request **before** its formal 16:35 Git migration, which is not necessarily its time of first conception.

## Author's retrospective clarification of why `duo` was replaced (24 October 2026)

**New direct first-person testimony:** In the present historical-reconstruction conversation, the project's author explained (verbatim, original Italian orthography):

> "duo assona con due che in inglese significa altro, tanto vale evitare questa collisione avendo una buona alternativa"

**Meaning in context:** The author confirms that `duo` was avoided because of its **perceived phonetic resemblance to English `due`**, which has meanings such as *owed, expected or scheduled* rather than TWO. The coexistence of Italian *due* = TWO and English *due* with another meaning was considered a source of potentially misleading cross-language associations. Since `bis` was an acceptable alternative, preserving `duo` had no compelling benefit. The claim is about **author-perceived risk of association or confusion**, not a tested phonological homophone in every English variety: pronunciations and syllable counts may vary between `duo` and `due`.

**Evidence provenance, kept separate:**
- **10 Aug 2026 contemporary Git:** [commit `4d19263`](https://github.com/andreabenetton/unisermo/commit/4d19263da58802bd184774b3d1463714c50979dc) proves the change from `duo` to `bis`, with historical documentation of the former form.
- **10 Aug 2026 conversation index:** a user message at approximately 15:55 UTC discusses the option; the original full transcript was **not** recovered and the indexed extract alone **did not explicitly establish this motivation**.
- **24 Oct 2026 user testimony:** the author now explicitly identifies **avoidance of misleading similarity to English `due`** as the motivation. Direct current-message evidence for the author's historical recollection, **not** a contemporaneous verbatim 10 August quotation.
- **Empirical status:** No controlled cross-language perception, lexical retrieval, confusion, acquisition, or speaking-time study was documented. Do not report `duo` as empirically proven ambiguous or `bis` as statistically superior.

**Corrected interpretation:** The change is an example of **cross-linguistic semantic-interference avoidance** as an explicit design consideration, rather than word-length compression (both forms have three letters) or an attested statistical optimization. This case complements the dated `kom/kun`, `kur/ker`, and `un/uno` collision avoidance decisions, but unlike those local same-language collisions this is an **associative collision across languages**.

## Comparisons important to the foundational efficiency objective

1. **Information encoding versus spelling:** The 8 August numeral system was already **morphologically compositional**, but its components were separated by spaces. The 10 August single-word rule changes **orthographic token boundaries**, not the component sequence or necessarily the spoken duration of `dek+bis`. No measured speaking speed follows from this change.
2. **Root size versus recognizability:** Both `duo` and `bis` contain **three written letters**. The **author has now clarified on 24 October 2026** that the change was motivated by perceived misleading assonance with English `due`, not a length reduction. The 10 August full transcript and any empirical confusion comparison remain outstanding; see the retrospective-testimony addendum above.
3. **Deduplication of grammatical categories:** `jer` was chosen as a **general iterative operator** rather than creating a distinct counting vocabulary only for genealogy. This is a productive morphosyntactic design hypothesis; the 10 August documents do not validate that all genealogical relations are semantically transparent to human speakers.
4. **Redundancy:** `wi` and obsolete `-en` should not be retroactively fused into the same noun-number system. `duo dom` in the original is not equivalent *as a morphological structure* to current `bis dom` even when translations converge.

### Source-internal problem: “all base forms are CVC” is demonstrably false

The **original** `numerals.md` claims that all 13 numeral bases are exactly three-letter **CVC** forms. In the same table, `uno` and `oto` are **V-C-V**, while `duo` is **C-V-V**. The **current** numerals file still says that all thirteen are CVC even though `uno` and `oto` remain V-C-V. Thus:

- **Accurate:** the listed 13 bases have **three written letters**.
- **Inaccurate as stated in the source:** they are uniformly **CVC phonotactic forms**.
- The original asserts both and contradicts itself; this must be documented as a historical **specification drafting error**. It is **not** evidence of an actual three-segment CVC phonology for the entire numeral system. This history-only investigation does **not** edit the normative file.

A second descriptive tension: the original heading states *thirteen base numerals* but the list consists of **ten digits (0–9) plus three powers (10, 100, 1000)**. That use of “base” is a category label, not evidence of a base-13 numbering system. Compound structure remains decimal.

> **New source-correction (24 October 2026):** The original **10 August** user messages have now been independently located. At **16:09** the author preferred parent root `gen/geno/gene`; at **16:11** the author **expressly confirmed `adel/adelo/adele` for sibling/brother/sister**, and at **16:12** proposed `adelgen` as a compositional uncle/aunt relation. The *version-controlled* lexicon had already canonized **`frat` = brother at 15:56**, and still contains `frat` rather than `adel`. The later October preservation list is therefore **partial** and its shorthand "not independently ratified" applies to Git status, **not all historical user choices**. Do not infer that `adel` was adopted in canonical Git or that it was never accepted by the user. See [conversation-vs-Git primary-source reconciliation](august-kinship-original-dialogue-versus-git.md).

> **Resolution on 24 October 2026:** The author personally confirmed that the **10 August `adel` sibling decision was forgotten** during Git integration and **must replace `frat`**. In the subsequent restoration `adel/adelo/adele` become canonical, while `frat` is retired from current language use and retained only as history/legacy benchmark compatibility. The historical conflict described below records the state *before this correction*. Other kinship proposals remain unratified. [Canonical specification](../../language/kinship.md) and [source-critical resolution](august-kinship-original-dialogue-versus-git.md).

> **Additional confirmation (24 October 2026):** The author expressly approves `gen/geno/gene` parent/father/mother and `adelgen` uncle/aunt. Earlier indexed original messages support `bisjergen` = grandparent and `terjergen` = great-grandparent via productive `NUMjer`. Candidate `filadelgen` remains provisional because `fil` offspring is not confirmed. Gender suffix scope in repeated relations is not settled, so `bisjergeno/bisjergene` cannot yet be assigned unambiguous general meanings. [Live kinship](../../language/kinship.md).

> **24 October follow-up:** the author additionally ratifies `fil` as offspring and asks for branch-specific grandparents. The resulting canonical link-based compounds `genegene`, `genegeno`, `genogene`, `genogeno` express the four possible father/mother combinations from ego, interpreted rightmost-first; `filadelgen` denotes a first cousin. Prior notes saying `fil` is unratified are retained only as historical pre-decision snapshots. The semantic feature is **newly formalized on 24 October**, not established as a specific four-way table in original August sources. [Live kinship](../../language/kinship.md).

## Kinship: distinguish preserved earlier alternatives from accepted lexicon

The [23 October retrospective preservation note](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/kinship-and-numerals-preservation.md) records earlier discussed relational stems such as `par/paro/pare` (parent/father/mother), `fil/filo/file` (offspring/son/daughter), `av/avo/ave` (grandparent/grandfather/grandmother), and **`germ` versus `sib`** for a neutral sibling stem. In that note, **these are historical candidate analyses**, explicitly **not independently ratified canonical lexemes**. The confirmed lexicon separately contains `frat` = brother. Earlier expansion suggestions `mater/pater/infan` were withdrawn without thereby canonizing `pare/paro/fil`.

**What is verifiable now:** 10 August `jer` is a canonical *general-purpose iteration operator*; 23 October preserved previously considered gendered kinship patterns as research **proposals**, not final entries.

**What is not currently proven:** exact dates and complete original user/assistant discussions for each kinship candidate, acceptance of every compound such as `adelbisjerROOT`, or measured human ability to interpret multi-generation relational strings. Such an expression must be checked against canonical existing roots and actual attested genealogy semantics before adoption.

## Historical evidence grading and open tasks

| Type | Strongest evidence | Limit |
| --- | --- | --- |
| Original numeral/compound specification | Immutable 8 August Markdown | Descriptive **CVC** claim contradicted by own table |
| Revised number-two and `jer` rules | Immutable [16:24](https://github.com/andreabenetton/unisermo/commit/4d19263da58802bd184774b3d1463714c50979dc) and [16:35](https://github.com/andreabenetton/unisermo/commit/b3c473e6f86cb58734e208491a7e2ed6306623c6) Git | Adoption timing, not direct human comprehension verification |
| Historical user preference | Dated original-message indexed excerpts at **about** 15:55, 16:10, 16:30 UTC | Approximate index times, not exported unabridged transcript |
| Kinship options | 23 October preservation note **plus now-located user messages from 10 August at 16:09, 16:11 and 16:12** | `adel/adelo/adele` explicitly **user-approved**, `adelgen` user-proposed; neither is found in Git-confirmed lexicon, which maintains `frat`. Full dialogue and later resolution still missing. |
| User's founding goal | 24 October 2026 direct author testimony | Supports conceptual lineage, not achieving human speech efficiency |

Next: recover the full 10 August 15:55–16:35 message sequence, corroborate the now author-attested `duo`/English `due` rationale in its original context if possible, and recover the complete now-located **10 August 16:09–16:12 kinship dialogue**, including alternatives and any later replacement of `frat` with `adel`. Track accepted and withdrawn forms in **separate** columns to prevent candidate proposals being merged into canonical lexical inventory.
