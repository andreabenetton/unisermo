# Phoneme and grapheme design: recoverable historical stages

**Updated status (24 Oct 2026):** Message-level excerpts from **22 May 2026** document early linguistic design debates, and the **27 July 2026 ChatGPT conversation** for the first IPA atlas has been located. The complete transcripts are still not archived, and the original historical phonology specification is separately preserved in Git. Do not treat dated commit imports as dates of the first conversations.

## Earlier conversations and empirical atlas work (May–July 2026)

- **22 May 2026:** recovered conversation excerpts show the user requesting IPA mappings for Georgian, discussing sound selections across languages and considering /h/ (removed), /ŋ/ (temporarily admitted as `ng`, later removed), glides `w/y`, plus spelling decisions `c=/tʃ/`, `sh=/ʃ/`, `ts=/ts/`, and `j=/dʒ/`. This is an evolving discussion, **not** a final inventory snapshot.
- **27 July 2026 05:11–16:24 UTC:** original ChatGPT IPA atlas conversation covered counts per symbol, population weighting, source and orthography evidence, phoneme/grapheme correspondence, verification of all 33 Georgian letters, and official IPA presentation. First imported Git baseline at **17:59 UTC** that day. See `original-chatgpt-ipa-atlas-conversation.md`.
- The exact reasons for adopting or rejecting individual phonemes in the formal Unisermo inventory remain to be corroborated with full dialogue, controlled comparisons and recorded source statistics.

## Original design, composed before or by 10 Aug 2026

Source: `legacy/original-language/alphabet_and_phonology.md`, imported without subsequent edits in commit `c7b9f16f8fa7` at 2026-08-10 05:33:32 UTC.

- Official **24 written units**, **six vowels** `a e i o u ə` and **18 consonantal units** `p b t d k g m n f v s z sh ts c j l r`.
- Multi-letter `sh` represented a single underlying /ʃ/; `ts` represented /ts/; `c` represented /tʃ/ rather than /k/; `j` represented /dʒ/ rather than /j/.
- `h`, `w`, `y` excluded as official letters; no phonemic /h/ or /ŋ/. `ng` read as /n+g/ rather than an independent /ŋ/.
- High value placed on one-to-one mapping **of written units** to phonemes, auditory stability, a deliberately limited global inventory, avoidance of weak /h/, and accent variants that did not neutralize contrast.
- The six distinct vowels also encoded distinct person markers, motivating stringent vowel distinction. This is a **historical system**, not current canonical conjugation.
- The earlier system contained choices later reversed, including phonemic schwa and affricates. Their rejection or replacement is a significant historical design issue for the paper.

## Major redesign recorded on 10 Aug 2026

Git commit `04dad808c53f` (2026-08-10 05:34:20 UTC), immediately after the import, has message **Migrate live specification to current phonology and person number**.

Current specification `language/alphabet_and_phonology.md`:
- **21 letters = five vowels** `a e i o u` + **16 consonants/glides** `p b t d k g m n f v s z l r j w`.
- No phonemic schwa /ə/; no independent /ʃ/, /ts/, /tʃ/, /dʒ/, /ɲ/, /ŋ/, /h/; no `c`, `x`, or `h` as official letters.
- `j` now represents /j/ and `w` represents /w/. Pronounceable sequences `ts`, `tj`, `dj`, `sj`, `gn` may have predictable coalescent phonetic outputs without adding independent phonemes.
- Three grammar-critical personal vowel markers `i u a`; plural nasal /N/ written `n`; mid vowels `e o` carry aspect in finite verbs; optional referential specificity `-e/-o`.
- Controlled accent-tolerant mergers `b→p`, `d→t`, `g→k`, `z→s`, and sometimes `v→f/w` in unambiguous contexts. Preserve canonical lexical contrasts and avoid hazardous minimal pairs.
- Explicitly favor **population- and family-aware coverage**, root-by-root adaptation and globally recognizable modern forms, rather than mechanical letter-by-letter Latin conversion.

Subsequent dated commits:
- `13a1d4febe0a`, **10 Aug 2026 07:26:33 UTC**: *Canonize vowel aspect before tense*.
- `70e18f59c492`, **10 Aug 2026 14:42:35 UTC**: *Enforce canonical alphabet without x*.
- `8179564eddda`, **22 Oct 2026 16:12:47 UTC**: *Rename constructed language to Unisermo and isolate atlas snapshot*.

## What the original discussions likely need to establish (still unverified)

1. When and why /ə/ was first admitted as a sixth vowel, and why eventually removed.
2. Why `sh`, `ts`, `c=/tʃ/`, and `j=/dʒ/` were first selected and later turned into contextual sequences, and why glides `j,w` replaced that inventory.
3. Which international language-family and first-language population analyses actually informed the tradeoffs, versus retrospective justifications in specifications.
4. Whether the one-written-unit/phoneme ideal was revised explicitly because productive compounding and phonemic accessibility required coalescence.
5. Origin and exact dated rationale for /h/ and /ŋ/ exclusions, accent-tolerant mergers, genitive `-s/-es` and other morphology/phonotactics interactions.
6. The dates and exact arguments in original **conversations earlier than May 2026**. An available personal-history search produced no matching conversation. Additional historical chat export or another identifiable thread may be needed.

**Important distinction:** source commit dates anchor when versions entered this repository. They do not prove when ideas were first discussed. All original-specification decisions are documented as *no later than* their 10 Aug import unless verified earlier elsewhere.

## Paper significance

Unisermo's phonological design visibly underwent substantive changes: a phonemic 24-unit system with schwa and affricates gave way to a 21-letter system with glides and coalescent sequences. This is stronger documented evidence of iterative engineering than simply describing the current inventory. The research paper must preserve both the abandoned and accepted architectures, test their accessibility claims independently, and avoid inferring precise conversations from specifications.

## 24 October 2026: audit of quantitative source versus design choices

A new code-level reading of the **unaltered 27 July 2026 ChatGPT artifact** is preserved in [`glottodelta-original-baseline-audit.md`](glottodelta-original-baseline-audit.md). It identified baseline **L** values /ə/: **533** (24.5% of the source-language baseline), /h/: **1,258** (57.8%), /ŋ/: **1,424** (65.4%), /ʃ/: **782** (35.9%), /j/: **1,993** (91.5%), /w/: **1,883** (86.5%). These percentages are stored `DATA`-source language percentages, **not speaker-weighted P**, and must not be cited as the proportion of humanity able to articulate or hear the phoneme.

This comparison exposes a crucial historical counterexample to simplistic frequency optimization: the 8 August design had excluded /h/ and /ŋ/ *despite* their substantial attestation, whereas it admitted schwa /ə/ with a much lower observed source-language count. Its rationale explicitly coupled phoneme choices to orthographic ambiguity and grammatical necessity (schwa distinguished a sixth verbal person). By the 10 August specification, person morphology instead used three person vowels plus plural `n`, removing that architectural dependency on schwa; glides /j/ and /w/ were included and the formerly separate affricates were reinterpreted as transparent sequences.

These are **documented cross-snapshot facts and a mechanistic design interpretation**. No identified contemporaneous message yet shows that the July **numeric observations caused** an August selection decision. The project had already debated rejecting /h/ and /ŋ/ on 22 May, well before the dedicated IPA atlas, so even a strong correlation in July cannot be a claimed initial cause.

## Correction to 22 May source attribution and dated 9 August intermediate state

The alleged **22 May** original phoneme/grapheme dialogue is still a useful recovery target, but targeted history search on 24 October produced *inconsistent* matches and may have conflated an unrelated WordPress discussion with later phonology summaries. **No complete original May 22 transcript has been reauthenticated**. Its exact date must not be cited as direct proof of specific design decisions without first-party messages.

The 21-letter revised phonology is explicitly preserved in [`1470576`](https://github.com/andreabenetton/unisermo/commit/1470576cee229ff6c37da59d5fb6dac922669d30) on **9 August 2026 at 15:43:31 UTC** (research-side specification), before the live language migration [`04dad80`](https://github.com/andreabenetton/unisermo/commit/04dad808c53f3f3d0beebcb2461811896dd09491) of 10 August. Earlier **8 August** commits `2c6490d`, `37e6a6a`, `011247a` show sequential confirmation of sound choices, person/number and affricates. See [decision chain](may-august-morphology-decision-chain.md).
