# Phoneme and grapheme design: recoverable historical stages

**Status (24 Oct 2026):** the complete pre-May conversation could NOT be located in the available conversation search. This record is a documentary reconstruction from an immutable imported specification plus dated Git commits. Do **not** describe it as a recovered conversation transcript or claim the choices were first made on the import date.

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
