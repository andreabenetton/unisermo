# Conversation-to-commit correlation: phonology and the IPA atlas

Research note dated 24 October 2026. This source recovers **individual dated conversation excerpts / previous assistant reports** and connects them to Git history where independently available. A conversation-to-commit link is an **investigative hypothesis**, not proof of which chat triggered a change.

## Newly recovered conversational milestones

| UTC timestamp | Recovered conversational content | Evidence class |
| --- | --- | --- |
| 27 July 2026, 05:12:47 | User requested an IPA atlas with phoneme counts, grapheme mappings and speaker-weighted comparisons between languages. | User message recovered from conversation search |
| 27 July 2026, 09:00:52 | User focused on Georgian /ʊ/ and /ɑ/, the many-to-many phoneme/grapheme relationship, and validation of all 33 Georgian letters. | User message recovered from conversation search |
| 27 July 2026, 13:31:28 | Assistant described atlas refinement: standard IPA consonant/vowel locations, 111 IPA symbols, Georgian coverage, licensing and sound files. | Previous assistant output; implementation should be verified against source |
| 8 August 2026, 19:04:48 | User linked creation/deployment of GlottoDelta to the newly created `andreabenetton/language` repository. | User message recovered |
| 8 August 2026, 19:41:17 | Assistant described a full GlottoDelta reconstruction preserving `original.html` byte-for-byte; phoneme research on `phoneme-study`, reportedly commit `7311032`, comparing /ə/, /j/, /w/, /v/, speaker coverage and recognizable roots. | Previous assistant output; local commit ID **not found** in public `andreabenetton/glottodelta` |
| 8 August 2026, 20:10:53 | Assistant reported the phonological simplification `/ts/=/t+s/`, `/tʃ/=/t+j/`, `/dʒ/=/d+j/`, with coalesced pronunciations, restoring /j/ while /w/ remained under consideration; local commit `011247a`. | Previous assistant output; commit **not found** in public GlottoDelta |
| 9 August 2026, 14:13:20 | User required language-family analysis in **descending total speaker population**, with Abkhaz-Adyge outside that sequence. | User instruction recovered |
| 9 August 2026, 14:18:36 | Assistant described a CLDR family-by-speaker ranking and Indo-European analysis, reportedly in commit `9aa7b49`; Indo-European ranked first, Sino-Tibetan second; 140 languages / 144 source records. | Previous assistant output; commit **not found** in public GlottoDelta |
| 10 August 2026, 14:42:37 | Assistant reported 21 canonical graphemes and exclusion of `x` from lexical roots. | Previous assistant output; corroborated by `unisermo` commit `70e18f59c492` |
| 10 August 2026, 15:41:12 | Assistant described distinctions between `alt`, `bas`, `mov altad`, `mov basad`, `altmov` and `basmov`; reported a local head `8bb979b`. | Previous assistant output; investigate original branch/repository |

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

- Locate the Git repository or worktree that carried branch `phoneme-study` and local commit `7311032`; identify `011247a`, `9aa7b49` and `8bb979b` using original workspace or archived conversations.
- Recover the complete 27 July and 8–9 August dialogue rather than excerpt-level summaries; check discussion leading to /ə/ rejection, /w/ acceptance and globally weighted family comparison.
- If source branch can be recovered, build a per-phoneme before/after matrix with explicit model-derived and corpus-derived evidence.
