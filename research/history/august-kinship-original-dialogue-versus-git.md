# 10 August 2026: original kinship dialogue versus Git-confirmed lexicon

**Retrospective research audit: 24 October 2026.** This file distinguishes (a) original **speaker-attributed, dated conversation-index excerpts**, (b) immutable **contemporaneous Git artifacts**, and (c) a **23 October retrospective preservation note**. The whole original 10 August conversation has **not** been exported, so the dated excerpts below are **summaries**, not certified verbatim transcriptions.

## Resolution from the author (24 October 2026): **an omitted implementation, not a rejected choice**

**New firsthand testimony in the active ChatGPT conversation:** the author states (verbatim, preserving the original Italian):

> "adel e' semplicemente stata dimenticata ma va sicuramente recuperata come scelta e ssotituire frat"

The author explicitly confirms that **`adel` was forgotten in Git**, rather than abandoned, and directs its restoration **replacing `frat`**, not treating both as synonyms. Combined with the independently dated **10 August 16:11:23 UTC** user acceptance of `adel/adelo/adele`, this resolves the former *cause-of-divergence* question at the level of **retrospective author testimony**. It does **not** retroactively prove that Git had integrated these words on 10 August.

**Implementation status after this 24 October correction:** this PR updates live [`language/kinship.md`](../../language/kinship.md), `confirmed_lexicon.json`, confirmed decisions, the formalization source data, generated indexes, tests and migration history. `frat` remains a **historical 10 August choice only**, plus an `example_only` parser attestation to keep old research corpora reproducible. Parent `gen` and `adelgen` are not automatically promoted by this sibling-only correction. See the dated 10 August evidence below, which describes the historical **pre-correction Git state**.

## Parent approval and generational examples — author's confirmation on 24 October 2026

Following the direct sibling restoration, the author additionally declares: **`gen/geno/gene` and `adelgen` approved**. This confirms the neutral parent, father, mother and parent's sibling relations, independently of the earlier 10 August conversation-index excerpts. The updated canonical grammar includes `gen`, `geno`, `gene`, `adelgen` and `bisjergen`.

Original dated 10 August conversation-index messages around 16:12–16:32 also identify **`bisjergen` = grandparent (two successive parent links)**, **`terjergen` = great-grandparent (three links)** and `adelbisjergen` = a grandparent's sibling, using the already confirmed `NUMjer` step operator. Exact original wording and all intermediate alternatives still require a complete transcript.

**Not ratified here:** `fil` as inverse offspring relation or `filadelgen` as cousin. `bisjergeno` and `bisjergene` are not unambiguously grandfather/grandmother without deciding whether gender modifies the final relative or all intermediate steps. See [current kinship specification](../../language/kinship.md).

Historical pre-approval observations below are retained as evidence for the former state, **not current normative status**.

## Main finding: a conversation-level confirmation absent from the confirmed Git lexicon

| Timestamp (UTC) | Evidence | What can be established |
| --- | --- | --- |
| **10 Aug 15:56:43** | [Git commit `a1df1425`](https://github.com/andreabenetton/unisermo/commit/a1df1425bddf6e8636074ffb50309b1fd9476c1f), `research/lexicon/confirmed_lexicon.json` | The application explicitly **canonized `frat` = brother** (from international/Latin `frater`). This is an actual saved primary Git decision and a test assertion. |
| **10 Aug 16:09:15** | Original **user** conversation-index entry | User objects to `par` **as a sibling label** because of ambiguity; states preference for `gen` = parent, with `geno` = father and `gene` = mother. Do not extrapolate that every earlier use of `par` as *parent* was independently rejected. |
| **10 Aug 16:09:17** | Original **assistant** conversation-index entry | Sibling alternatives considered: `sor`, `germ`, `sib`, `frer`, `adel`. Assistant proposes `adel`. **A proposal from the assistant is not automatically an author-confirmed decision.** |
| **10 Aug 16:11:23** | Original **user** conversation-index entry | User **explicitly confirms `adel` = brother/sister (gender-neutral sibling relation), `adelo` = male sibling, `adele` = female sibling**. This is **accepted in the dialogue at this timestamp**, even though it is **not present in today's Git-confirmed lexicon**. |
| **10 Aug 16:12:33** | Original **user** conversation-index entry | User proposes `adelgen` = sibling of parent (uncle/aunt) and asks for **single-word compound kinship forms** with the relation-composition interpretation **`A+B` = A relative to B**. An assistant index later accepts/illustrates `adelgen` and proposed gender-marked `adelgeno/adelgene`; **full exchange and canonical Git adoption not established**. |
| **10 Aug 16:31:20** | Original **user** conversation-index entry | Clarifies `bisjer` is a general number of **times/iterations/steps**, not exclusively a genealogical distance marker. |
| **10 Aug 16:35:31** | [Git `b3c473e`](https://github.com/andreabenetton/unisermo/commit/b3c473e6f86cb58734e208491a7e2ed6306623c6) | Canonizes general `jer` and fused numeric/iterative compounds. `language/numerals.md` explicitly gives an **illustrative structural shape `adelbisjerROOT`**, but does not thereby establish each `adel`-family form as a confirmed lexical entry. |
| **23 Oct 2026** | [Kinship and numerals preservation note](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/kinship-and-numerals-preservation.md) | Later note preserves historical proposals `par/paro/pare`, `fil/filo/file`, `av/avo/ave`, and alternatives `germ/sib`, **explicitly as noncanonical candidates**. It does **not** fully reproduce the newly recovered `gen/adel/adelgen` conversation. |

### Evidence-level distinction that must not be lost in the paper

- **Dialogue-level confirmation (original user):** `adel`, `adelo`, `adele` at **16:11:23**, along with `gen/geno/gene` in the **16:09:15** context. These are *historical accepted choices in conversation*.
- **Dialogue-level proposal:** `adelgen` at **16:12:33**; assistant later accepts/illustrates it, but the user's exact final sign-off and competing interpretations require the complete exchange.
- **Git-canonized current lexicon:** `frat` = brother from **15:56:43** remains in `research/lexicon/confirmed_lexicon.json` and associated tests. In the current confirmed lexicon, no independent `adel`, `adelo`, `adele`, `gen`, `geno`, `gene`, `adelgen` entries were found by direct JSON inspection.
- **Git-canonized generic morphology:** `NUMjer` *was* committed. It may be illustrated with kinship compounds in normative numerals without ratifying their base roots.
- **23 October historical preservation note:** names **different historical candidates**. It cannot override either the user-confirmed **10 August dialogue** or the earlier canonical `frat` Git entry. Conversely, the retrieved 10 August dialogue does not automatically supersede the versioned lexicon or establish a subsequent accepted resolution.

**Potentially unresolved historical conflict:** The user accepted neutral sibling `adel` about **15 minutes after** `frat` = brother was committed, yet no corresponding revision appears in the present confirmed-lexicon file. **Later resolved by the author on 24 October 2026 as a forgotten integration**, not a subsequent intentional rejection. That statement is retrospective testimony and separately documented above. In particular, the later preservation note's mention of `germ/sib` as sibling alternatives is compatible with brainstorming before `adel` but not a complete account of the August user decision.

## Why this matters for Unisermo's founding objective

The author-confirmed founding idea (July 2025) was conveying more information in less time. The **August 10 kinship dialogue** addresses that goal by proposing compositional relationship roots, optional gender markers and the reusable iterative operator `jer`, rather than independently memorizing every family-relation form.

This is an **explicit morphological/semantic design hypothesis**. It is **not** evidence that `adelgen` is understood without teaching, that relational composition works on every genealogical path, that gender can be applied to every relation, or that longer fused compounds are faster to say or correctly comprehend. No such controlled human study is documented.

Two important competing design choices remain simultaneously attested:
1. **`frat`**: internationally recognizable independent lexical root, historically **canonized** at 15:56.
2. **`adel`**: a neutral productive relation permitting `adelo/adele`, **explicitly user-approved in dialogue** at 16:11, but not found in canonical confirmed-lexicon JSON.

The two embody a tension between **root recognizability** and **productive neutrality/compositionality**. The paper should preserve this unresolved tension, not silently rewrite history as though one design unambiguously replaced the other.

## Open questions requiring original transcript or later formal acceptance

1. **Resolved by author testimony on 24 October:** `adel` was omitted inadvertently and **must replace** `frat`; the Git change is being implemented in this PR. The original full August chat remains unexported.
2. What precisely was `gen` intended to cover, and why was `par` judged equivocal for the particular sibling candidate? The 16:09 index provides only a partial context.
3. Neutral `adelgen` was expressly approved on 24 October; sex/gender scope of longer `adelgeno`/`adelgene` remains unresolved. The original 10 August transcript is still to be exported.
4. Was a full `A+B` genealogical direction/semantic semantics formally defined and consistency-tested for kinship trees? No complete proof or human evaluation found.
5. How did the 23 October `par/fil/av/germ/sib` preservation note come to emphasize different roots from the **16:09–16:12 original conversation**? The note was compiled retrospectively and may be incomplete; the chronology must not be normalized by fiat.

**Documentation action:** preserve this as a Git-independent historical finding. **Do not change canonical lexicon, normative grammar or testing assertions** without a separate explicit language-design decision. Current investigation is historical only.

## Primary sources

- [Git-confirmed `frat`, 10 Aug 15:56:43](https://github.com/andreabenetton/unisermo/commit/a1df1425bddf6e8636074ffb50309b1fd9476c1f)
- [Git-confirmed `jer`, 10 Aug 16:35:31](https://github.com/andreabenetton/unisermo/commit/b3c473e6f86cb58734e208491a7e2ed6306623c6)
- [Current `confirmed_lexicon.json`](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/confirmed_lexicon.json)
- [Current `language/numerals.md`](https://github.com/andreabenetton/unisermo/blob/main/language/numerals.md)
- [23 October preservation note](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/kinship-and-numerals-preservation.md)
- Dated **10 Aug 2026 16:09:15, 16:09:17, 16:11:23, 16:12:33, 16:31:20 UTC** speaker-attributed original conversation-index retrieval. No persistent public chat URL or full export yet.
