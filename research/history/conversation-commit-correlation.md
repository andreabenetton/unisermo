# Conversation-to-commit correlation: phonology and the IPA atlas

Research note dated 24 October 2026. This source recovers **individual dated conversation excerpts / previous assistant reports** and connects them to Git history where independently available. A conversation-to-commit link is an **investigative hypothesis**, not proof of which chat triggered a change.

## May 2026 verified earlier message-level milestones

| UTC timestamp | Recovered original speaker's contribution | Evidence class |
| --- | --- | --- |
| 6 May 18:47–18:50 | Italian/Georgian IPA-grapheme comparison with explicit sound-based matches; no explicit conlang purpose established. | User and assistant original-message retrieval; **context only** |
| **16 May 11:50:27** | User raises five versus six vowel design for an international synthetic language; assistant recommends five core vowels. | Dated user/assistant original-message indexed excerpts; **first explicit constructed-language design found** |
| **22 May 22:28–22:29** | User disputes exclusion of /ə/ and confirms six verb-person vowels. | Dated user original-message indexed excerpts; design reversal |
| 22 May 22:52–22:55 | User asks Georgian IPA mapping and whether ძ and წ are affricates; assistant confirms affricate classification. | Dated user and assistant original-message indexed excerpts |
| **22 May 23:14:48** | User expressly removes /h/ from the proposed phoneme inventory. | Dated user original-message indexed excerpt |
| 22 May 23:40:45 | Assistant documents candidate with `sh ts c j` for /ʃ ts tʃ dʒ/ and no h/ng; 24 May user keeps contrasts f/v and l/r rather than merges. | Original-message indexed excerpts; full intervening sequence still to be archived |

For speaker-level details, provenance and caveats see [early May conversation evidence](early-may-conversation-evidence.md).

## Newly recovered conversational milestones

| UTC timestamp | Recovered conversational content | Evidence class |
| --- | --- | --- |
| 27 July 2026, 05:12:47 | User requested an IPA atlas with phoneme counts, grapheme mappings and speaker-weighted comparisons between languages. | User message recovered from conversation search |
| 27 July 2026, 09:00:52 | User focused on Georgian /ʊ/ and /ɑ/, the many-to-many phoneme/grapheme relationship, and validation of all 33 Georgian letters. | User message recovered from conversation search |
| 27 July 2026, 13:31:28 | Assistant described atlas refinement: standard IPA consonant/vowel locations, 111 IPA symbols, Georgian coverage, licensing and sound files. | Previous assistant output; implementation should be verified against source |
| 8 August 2026, 19:04:48 | User linked creation/deployment of GlottoDelta to the newly created `andreabenetton/language` repository. | User message recovered |
| 8 August 2026, 19:41:17 | Assistant described a full GlottoDelta reconstruction preserving `original.html` byte-for-byte; phoneme research on `phoneme-study`, reportedly commit `7311032`, comparing /ə/, /j/, /w/, /v/, speaker coverage and recognizable roots. | Previous assistant output; **later verified as Git object in Unisermo**, not GlottoDelta |
| 8 August 2026, 20:10:53 | Assistant reported the phonological simplification `/ts/=/t+s/`, `/tʃ/=/t+j/`, `/dʒ/=/d+j/`, with coalesced pronunciations, restoring /j/ while /w/ remained under consideration; local commit `011247a`. | Previous assistant output; **later verified in Unisermo Git history**, not GlottoDelta |
| 9 August 2026, 14:13:20 | User required language-family analysis in **descending total speaker population**, with Abkhaz-Adyge outside that sequence. | User instruction recovered |
| 9 August 2026, 14:18:36 | Assistant described a CLDR family-by-speaker ranking and Indo-European analysis, reportedly in commit `9aa7b49`; Indo-European ranked first, Sino-Tibetan second; 140 languages / 144 source records. | Previous assistant output; **later verified in Unisermo Git history**, not GlottoDelta |
| 10 August 2026, 14:42:37 | Assistant reported 21 canonical graphemes and exclusion of `x` from lexical roots. | Previous assistant output; corroborated by `unisermo` commit `70e18f59c492` |
| 10 August 2026, 15:41:12 | Assistant described distinctions between `alt`, `bas`, `mov altad`, `mov basad`, `altmov` and `basmov`; reported a local head `8bb979b`. | Previous assistant output; SHA **later verified in Unisermo**; original worktree topology unknown |

## 9–10 August additions: original messages correlated with Git objects

| Original dated UTC item | Message-level evidence | Independent Git anchor / limitation |
| --- | --- | --- |
| **9 Aug 20:45:35** user | Individual root adaptations `cin→kin`, `doc→dots`, `fac→fak`, `dik`, `cur→kurar`; no blanket transliteration | [`16d899da`](https://github.com/andreabenetton/unisermo/commit/16d899da5e68a2328c5018f16c12ddc8bcd4f7d3), [`0beab462`](https://github.com/andreabenetton/unisermo/commit/0beab4622f235d43fb774cc8f9d98db69aa57701); original full transcript absent |
| **9 Aug 20:51:23** user | Fixed `root + TAM + person + optional N`; requests complete legacy audit | [`0b4856d5`](https://github.com/andreabenetton/unisermo/commit/0b4856d544345e7cebea023bd92006ebf76032de) 20:57; near-time correlation, not complete proof of every step |
| **9 Aug 21:03:17** user | `com→kun`, `ker` WHY, `cur→kurar`, `-ia` as /i.a/, clarify article | [`d5d9ed7c`](https://github.com/andreabenetton/unisermo/commit/d5d9ed7c650e0c5ace90abf6487d15ec67e033a2) 21:05; resolves `kom/kur/un` collisions |
| **10 Aug 07:13:38** assistant | Comparative 25/74-root phonotactic trial reported, comparing consonant clusters and vowel hiatus | [`eff48c08`](https://github.com/andreabenetton/unisermo/commit/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6) 07:18 archives simulations, does not date the very first run |
| **10 Aug 07:17:27** **user** | Confirms `root+aspect(e/o)+time(d/f)+person(i/u/a)+number(n)` | [`13a1d4fe`](https://github.com/andreabenetton/unisermo/commit/13a1d4febe0ae571cc0f63057575fac41994afd7) 07:26 adopts with hiatus protection |
| **10 Aug 07:27:08** assistant | Reports `dikedi` paradigm, hiatus, no aspect/person collapse, checks for R/R+e/o roots | Corroborated by [canonical grammar](august-tam-phonotactics-decision-history.md), user full wording unavailable |

## 10 August: semantics and Git correlated at message level

| UTC time / speaker | Evidence recovered | Independent Git source |
| --- | --- | --- |
| **13:46:04 user** | Remarks on ambiguous Italian `guarire`: spontaneous recovery versus another agent healing a patient | Contextual lead only; no direct causal proof |
| **14:06–14:07 user** | Confirms fused (unhyphenated) phase-family forms `ades/dees` | [`51be6a8`, 14:11](https://github.com/andreabenetton/unisermo/commit/51be6a882a97d4a4cc4f75458ddb1b4ec373c1c9) |
| **14:21:22 user** | Selects `traes DEST-ad SOURCE-de`, preserving simple `ades X` | [`16250c8`, 14:22](https://github.com/andreabenetton/unisermo/commit/16250c8b225daf2425112e21690ae0b2ccab2362) |
| **14:35:00 user** | Selects causative `Y traes X-em RESULT-da` | [`53df8ba`, 14:36](https://github.com/andreabenetton/unisermo/commit/53df8ba04e5d04ef9794c62c357a712567f86123) |
| **14:45:16 user** | Selects `mov` transitive/intransitive valency | [`9ce8c0c`, 14:47](https://github.com/andreabenetton/unisermo/commit/9ce8c0c4facc7df742d88ad63ee50562038e4c80) |
| **14:50:00 user** | Confirms `pel/trak` separate force verbs; pushing/pulling need not entail movement | [`141667e`, 14:57](https://github.com/andreabenetton/unisermo/commit/141667e94c198e404958ef1010df057bda553d0e) |
| **15:41 Git only** | Vertical `alt/bas` and `altmov/basmov` distinguish DIRECTION from PHASE | [`8bb979b`](https://github.com/andreabenetton/unisermo/commit/8bb979bf5e55f4a1ba713ecfe30e5b5d6c0ec1a6) |

[Detailed historical case](august-semantic-phase-motion-and-causation.md). Original index extracts are **not** a full transcript; the precise 15:41 *user* acceptance was not located.

## Independently verified Git anchors

- 27 July 2026 17:59:16 UTC — `andreabenetton/glottodelta` commit `bd25974983e3` imported an **already working** IPA atlas into Git. This postdates the 27 July **morning** conversations, establishing that the earlier conversations plausibly concerned work later captured in the imported snapshot.
- 27–28 July — source-backed improvements in population certainty (`213ba194cbc5`), PHOIBLE coverage (`9d632d9aaa2a`), allophone mapping (`24ed70978923`) and phonemic/phonetic views (`71b6c4244dd9`). Their function corresponds to the user's earlier goals, but individual-chat causality is unproven.
- 8 August 2026 18:31:07 UTC — `andreabenetton/language` initial commit `bacc1a7a9aaaa18596120c6ea2812c927b33b0e3`, preserving the original 24-unit alphabet. The 8 August 19:41 and 20:10 comments therefore **postdate** this first snapshot.
- 10 August 2026 — `andreabenetton/unisermo` recorded a new 21-letter canonical inventory and the rule excluding `x` in commits `04dad808c53f` and `70e18f59c492`.

## CORRECTION — local Git SHAs resolved in Unisermo (24 October 2026)

The previous claim below that short SHAs could not be found is **superseded**: all four have been located as verifiable objects in `andreabenetton/unisermo`, not GlottoDelta. `7311032` is the 8 August 19:41 phoneme research framework, `011247a` the 8 August 20:10 affricate study, `9aa7b49` the 9 August 14:18 family ranking, and `8bb979b` the 10 August 15:41 vertical motion study. See [August decision chain](august-phonology-decision-chain.md) and their canonical commit URLs there. The original worktree and transcript relationship are still not established.

## Critical distinction: which Git history?

**Historical note (superseded for SHA reachability):** The **public** `andreabenetton/glottodelta` only exposes branches `main` and `claude/ipa-interactive-app-analysis-ipns9g` at inspection time, and GitHub's commit lookup did **not** resolve historical abbreviated SHAs `7311032`, `011247a`, or `9aa7b49` there. Those IDs appear in previous assistant reports but may belong to a **separate local branch/worktree, agent-integrated version or another repository**, or be unreachable/orphaned history. Do **not** present them as verified public commits. The 9 August family-ranking work is especially important to recover from the original integrated workspace rather than ascribing it to the public IPA visualization.

## Scientific interpretation for the paper

This adds direct user-authored evidence for at least three distinct intellectual steps:

1. **27 July:** quantitative phoneme/orthography investigation, especially Georgian and speaker weighting.
2. **8 August:** phoneme inventory simplification (phonemic affricates replaced by sequential phonemes), with /j/ restored and /w/ still debated.
3. **9 August:** genealogical distribution weighted by total speaker count, deliberately organized from large to small families.

Hypothesis: data exploration informed the design of the language's revised phonology. This is plausible and supported by sequence/topic overlap, **not yet demonstrated by an exact transcript-to-commit mapping**.

## Priority next retrievals

- **SHA resolution completed:** `7311032`, `011247a`, `9aa7b49`, `8bb979b` all exist in the verifiable Unisermo Git object history (see [August decision history](august-phonology-decision-chain.md)). **Still open:** original branch/worktree name and whether those objects first existed on a different local topology.
- Recover the complete 27 July and 8–9 August dialogue rather than excerpt-level summaries; check discussion leading to /ə/ rejection, /w/ acceptance and globally weighted family comparison.
- If source branch can be recovered, build a per-phoneme before/after matrix with explicit model-derived and corpus-derived evidence.
