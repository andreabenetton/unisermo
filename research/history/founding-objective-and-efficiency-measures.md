# Unisermo's founding objective: information communicated per unit time

**Historical note prepared 24 October 2026.** The project author explicitly confirmed the continuity of the **motivating objective** between an earlier 15 July 2025 conversation and the language that eventually became Unisermo. This document distinguishes the new **retrospective author testimony** from contemporaneous conversation records, Git snapshots, hypotheses and experiments.

## Author confirmation: direct testimony, recorded 24 October 2026

In the active ChatGPT conversation on the historical reconstruction, the author stated (short **verbatim excerpt**, preserving original orthography):

> "il driver iniziale era trasmettere piu informazioni in meno tempo"

The same message expressly identified the discussion **recorded in July 2025** as the **first spark**. The author instructed the historical investigation to proceed. The original message is retained in the current ChatGPT conversation; a separately archived complete conversation export and stable public message identifier are **not** available in this repository. Do not invent a timestamp more precise than **24 October 2026** for this confirmation.

**What is now established:** The author recognizes the 15 July 2025 minimal-language discussion as the **conceptual origin of the efficiency goal** guiding the eventual Unisermo project. Historical account may therefore describe 2025 as the origin of its *idea, motivating question or intellectual trajectory*, rather than only as an unrelated similarity.

**What this does NOT establish:** That the 2025 assistant-suggested phoneme list, a 100–200 word lexicon, adjective-after-noun order, or other details were accepted by the author; that a working 2025 grammar or software prototype existed; that development was continuous between July 2025 and May 2026; or that the stated goal has been empirically attained. Those claims need independent records.

Evidence labels for a scientific paper:
- **C25**: indexed, speaker-attributed original **15 July 2025** conversation messages: user considers minimizing time for equivalent communication and an efficient constructed language; assistant supplies an exploratory minimalist sketch. Dated source, but full text transcript not exported.
- **T26**: **24 October 2026 author recollection/confirmation** above, directly identifying C25 as first spark. Strong source for the author's *stated motivation and retrospective continuity*, not an independent contemporaneous 2025 implementation.
- **S26**: immutable **8 August 2026 original specification** and dated May messages: evidence of the subsequently developed concrete linguistic design.
- **E26**: later experimental outputs and research datasets: evidence of *particular metrics*, not proof of the original human speech objective.

This upgrades the prior status "**causal continuity unverified**" to "**author-attested continuity of the founding objective, corroborated by a dated earlier query**". It does not upgrade the separate hypotheses of **continuous engineering**, **acceptance of the 2025 assistant sketch**, or **human speech efficiency**.

## Evolution of the original objective

| Stage | Source | Documented problem / response | Type |
| --- | --- | --- | --- |
| **15 July 2025** | [Earlier-language-proposal record](2025-minimal-language-precursor.md) plus T26 | Transmit more information in less time; explore a deliberately minimal constructed language, with Toki Pona as an illustrative reference. | User intention, now directly confirmed as the first spark |
| **16–24 May 2026** | [Early May dialogue](early-may-conversation-evidence.md) and [May grammar history](may-august-morphology-decision-chain.md) | Choose recognizable sounds/letters, compare 5 and 6 vowels, use vowel endings for grammatical person, compact roots, fixed morpheme locations, distinguishable cases and protected core contrasts. | Linguistic proposals/decisions, **not timed speech trials** |
| **27 July 2026** | [39-snapshot IPA atlas audit](glottodelta-39-snapshot-audit.md) | Provide a phonological/evidence instrument for distribution and estimated speaker exposure; stable 111-symbol corpus with iterative demographic/orthographic interpretation. | Static attestation data and engineering, **not measured speech information rate** |
| **8–10 August 2026** | [Phoneme decision chain](august-phonology-decision-chain.md), [original-language specification](original-language-repository.md), [grammar chronology](may-august-morphology-decision-chain.md) | Reconcile compactness with pronounceability and international root recognition: drop phonemic schwa, use 3 person vowels plus nasal plural, allow sequential affricates, optional analytic noun plural, simplify cases. | Quantitative model comparisons plus design decisions; phonological population proxies are **not listener performance data** |
| **22–24 October 2026** | [Benchmark harness](https://github.com/andreabenetton/unisermo/blob/main/benchmarks/README.md) and below | Compare some tokenizer, prompt, compositionality, semantic-slot and grammar-analysis outcomes. | Reproducible **written/LLM** research; **not proof of faster oral communication** |

The 8 August [original vocabulary-design rules](https://github.com/andreabenetton/language/blob/bacc1a7a9aaaa18596120c6ea2812c927b33b0e3/vocabulary_design_rules.md) state explicit additional constraints: shortest forms for frequent words, globally recognizable roots, predictable composition, and avoiding fragile minimal pairs in the first 500–1,000 words. The existence of such constraints is strong Git-source evidence. Their effectiveness was **not** experimentally validated simply by being written.

### Important rejected/superseded design path

- **2025 assistant sketch:** 5 vowels, 8 consonants, 100–200 words and postnominal adjectives; offered as an *unaccepted proposal*, not historic Unisermo v0.
- **August 2026 original specification:** 24 official written units, 6 contrastive vowels and **prenominal** adjectives, with phonological accommodation and recognizable roots. This is a new, independently documented architecture; it should not be described as a single confirmed step-by-step revision from the 2025 assistant sketch.
- **8–10 August redesign:** 21 official written units with 5 vowels and 3 grammatical person vowels, /N/ plural, `j=/j/` and `w=/w/`. The same efficiency motive can be considered continuous **by author testimony**, but every specific causal reason for every phoneme change still requires its own contemporaneous evidence.

## Do not confuse three operational meanings of 'efficiency'

| Endpoint | Possible defensible measurement | What existing results establish |
| --- | --- | --- |
| **A. Human oral communication:** original goal | **Accurately recovered semantic propositions per minute** or **time to correct comprehension** for controlled meaning-equivalent messages; optionally acoustic duration, speech rate and error-correction time separately. | **Not yet tested** with human speakers/listeners. This remains the key outstanding outcome. |
| **B. Written linguistic economy** | Grapheme/word/syllable count for independently judged semantically equivalent messages, including disambiguating context and learned vocabulary cost. | Canonical grammar and some scripted corpus pairs exist, but independent semantic-equivalence certification remains incomplete. |
| **C. Computational token and inference economy** | Tokens billed, cost per **correctly decoded meaning**, and prompt overhead at specified model/provider, task and context. | Limited measured LLM pilots exist. Token counts are tokenizer-dependent, and experimental accuracy does not establish human spoken information efficiency. |

**Conceptual trap:** fewer *lexical items* or shorter phonological forms alone do not imply more useful information transferred per minute. Ambiguous meanings may require longer clarification, repeated explanations, repairs, or additional context. Lower input tokens may similarly degrade model interpretation. A scientific claim requires **equivalence of meaning, comprehension accuracy, and time/cost jointly**, rather than compression alone.

### Specific existing experimental anchors — narrow results, not oral validation

- [78-sentence tokenizer pilot methodology](https://github.com/andreabenetton/unisermo/blob/main/benchmarks/README.md): most pilot sentences are inflected verbs (64/78); English drafts lack independent equivalence review. Token-count differences therefore cannot establish semantic efficiency.
- [23 October Qwen productive-compound pilot](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/compound-inference-results-2026-10-23.md): 9/12 exact root splits cold versus 12/12 supplied dictionary. These are **segmentation** scores, not human comprehension or correct interpretation of intended meanings.
- [23 October context-overhead comparison](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/compound-context-results-2026-10-23.md): both tested conditions split 12/12 correctly, but repeated glossary requests cost 1,976 total billed tokens versus 6,182 with full growing message history. This is a **provider/accounting/prompt-design** result, not proof of intrinsic linguistic compression.
- [23 October selective glossary pilot](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/document-primer-results-2026-10-23.md): 8/8 correct splits under either small header; 384 vs 395 billed total tokens across two conditions. Narrow and not semantically reviewed.
- [24 October new-document tense replication](https://github.com/andreabenetton/unisermo/blob/main/research/lexicon/discourse-tense-replication-results-2026-10-24.md): 13/18 vs 15/18 events exactly extracted under different primers, a reminder that shorter prompts can lose important semantic detail.

## Recommended paper claim and empirical test

**Defensible historical formulation (paraphrase, not verbatim):**
> The initial motivation for the project later named Unisermo arose from an exploration of whether an artificial language could increase the amount of correctly communicable information per unit of speaking time. The author identified a July 2025 conversation as the first spark in retrospective testimony dated 24 October 2026. The systematic phonological and grammatical development documented in the surviving record took place from at least May 2026 onward.

**Prospective, NOT-yet-performed primary-outcome study:** Establish a set of meaning-equivalent short messages with human-verified answer keys; compare trained Unisermo speakers with appropriately trained comparison-language users in **paired, randomized message-production and message-understanding tasks**. Record actual utterance and comprehension time, transfer accuracy, repair requests and prior exposure. Recruit diverse L1 groups and track learning time; pre-register a rate/accuracy composite and analyze confounders. This is a proposed design only, not a completed experiment and not a basis for claiming language superiority.

**Open archival task:** recover full 2025 and May 2026 chats to capture exact rejected alternatives. **Author continuity is confirmed by testimony; the intervening engineering chronology is still incomplete.**
