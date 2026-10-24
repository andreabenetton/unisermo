# Recovered 8–10 August 2026 phonological decision chain

Investigation date: 24 October 2026. Four abbreviated Git commit identifiers previously described as unreachable in public GlottoDelta are **independently resolved in `andreabenetton/unisermo`**. The commits and their historical documents were retrieved directly by immutable SHA. These are Git artifact facts, not proof of a verbatim conversation transcript.

| UTC date | Commit | Observed documented step |
| --- | --- | --- |
| 8 Aug 19:41:09 | [`73110321a6f1c4eeb5e8bd71b03efdea52020c36`](https://github.com/andreabenetton/unisermo/commit/73110321a6f1c4eeb5e8bd71b03efdea52020c36) | Phoneme inventory research framework; fixed GlottoDelta original HTML input; eight inventory candidates, population and language compatibility metrics, a 74-root Latin/international lexical seed; open questions include affricates and family dispersion. |
| 8 Aug 20:10:52 | [`011247a1203b1d0f1c1af399feaf1cac85ab2801`](https://github.com/andreabenetton/unisermo/commit/011247a1203b1d0f1c1af399feaf1cac85ab2801) | Decision-ready affricate study, alternatives and explicit machine-readable confirmed design constraints. Removes independent phonemic status for /ts tʃ dʒ/ and licenses coalescent /t+s/, /t+j/, /d+j/; retains /j/ and carries /w/ forward as candidate. |
| 9 Aug 14:18:36 | [`9aa7b4937d2ab83946bebbb0122aafb93ecdbdf3`](https://github.com/andreabenetton/unisermo/commit/9aa7b4937d2ab83946bebbb0122aafb93ecdbdf3) | Family population order and Indo-European study: 245 represented genealogical units; 46 ranked with some demographic information; 199 unranked; 381 contributing sample languages. Population ranks analysis *order*, not a genealogical F score. |
| 10 Aug 15:41:11 | [`8bb979bf5e55f4a1ba713ecfe30e5b5d6c0ec1a6`](https://github.com/andreabenetton/unisermo/commit/8bb979bf5e55f4a1ba713ecfe30e5b5d6c0ec1a6) | Canonization of semantic vertical-motion axis. Separate semantic grammar research, not an IPA/phonological commit. |

## Quantitative alternatives reconstructed from 8 August source

The original [`phoneme_selection.md`](https://github.com/andreabenetton/unisermo/blob/73110321a6f1c4eeb5e8bd71b03efdea52020c36/research/phonology/phoneme_selection.md) defines research `P_attested` as compatibility with an attested member of an acceptable realization family. This is **not** GlottoDelta's UI P, which requires a curated mapped or alternative phoneme–grapheme relation. P0/P1/P2 estimate fractions of the 384-code **demographic speaker-exposure proxy** missing at most 0/1/2 target categories, not successful speech production or comprehension.

| Candidate | Target count | P0 | P2 | Research implication |
| --- | ---: | ---: | ---: | --- |
| `current_simple_21` | 21 | 31.3% | 54.2% | Original simplified inventory without separately scored affricates |
| `no_schwa_20` | 20 | 37.4% | 64.0% | Removing contrastive schwa improves model compatibility |
| `latin17` | 17 | 50.0% | 70.2% | More familiar inventory, weaker preservation of some source roots |
| `latin17_yw` | 19 | 45.4% | 69.4% | Restores glides /j,w/ |
| `lexical22_yw` | 22 | 32.9% | 63.5% | More lexical contrasts, possibly protected by accent-tolerant mergers |
| `grammar6` | 6 | 96.1% | 99.8% | Separate robust grammar-critical subinventory hypothesis |

The old language grammar depended on six distinct person-vowels, including /ə/. The 8 August research argues that removing schwa improves compatibility P0 by 6.1 percentage points at the examined inventory size and that grammar-critical distinctions can instead use three widespread vowels /i u a/. This is a directly documented **reasoning pathway**; exact verbal acceptance still depends on full chat evidence.

The [`person_marker_study.md`](https://github.com/andreabenetton/unisermo/blob/011247a1203b1d0f1c1af399feaf1cac85ab2801/research/phonology/person_marker_study.md) records an actual comparison of `i/u/a` versus `a/u/i`: equal phoneme coverage, with the former chosen by a mnemonic/structural argument rather than frequency. It also compares plural markers: final place-tolerant nasal /N/ written `n` gives P0 98.67% with /a i u/, versus 92.56% for strict `n`; person-vowel then nasal produces zero newly induced CC boundaries versus 440/444 in the tested reverse-order root/TAM contexts. These are **model results and an enumerated sample**, not human pronunciation trials. The author cites WALS and a 2020 phonotactic study; those external citations have not been independently audited here.

## Affricates: question → competing models → evidence → decision

The original 111-symbol HTML cannot score independent `/ts tʃ dʒ/` as direct standalone DATA cells. The historical [`affricate_study.md`](https://github.com/andreabenetton/unisermo/blob/011247a1203b1d0f1c1af399feaf1cac85ab2801/research/phonology/affricate_study.md) therefore separates **component availability** from **direct attestation in 40 curated orthography profiles**. Component availability: `/t+s/` P 86.3%, `/t+j/` P 86.2%, `/d+j/` P 64.0%. Curated direct-affricate profile proportions are reported separately and must not be described as full-population percentages. Argument: a single orthographic affricate symbol does not prove lower temporal speaking cost. Decision: surface coalescence without a phonemic contrast, retaining full transparent sequence pronunciations. The [`confirmed_decisions.json`](https://github.com/andreabenetton/unisermo/blob/011247a1203b1d0f1c1af399feaf1cac85ab2801/research/phonology/confirmed_decisions.json) explicitly says the design constraints are confirmed **but the complete phoneme inventory is not yet frozen**.

## Genealogy versus speaker exposure

The 9 August [`family_population_order.md`](https://github.com/andreabenetton/unisermo/blob/9aa7b4937d2ab83946bebbb0122aafb93ecdbdf3/research/phonology/family_population_order.md) ranks the sampled Indo-European family first and Sino-Tibetan second by CLDR-derived speaker-exposure **proxy**, with explicit warnings that L1/L2 totals overlap and missing estimates are not imputed. Genealogical cross-family dispersion `F` is explicitly **not yet calculated**. The family profile for Indo-European contains 140 sampled languages from 144 source records; its claimed 23.9% member coverage cannot be treated as full family data. Abkhaz–Adyge has an independent study. It is incorrect to say the analysis calculated a validated global family-weighted phoneme score.

## What remains unverified

1. Full user/assistant transcripts on 22–24 May, 27 July, and 8–10 August. Recovered dated conversation excerpts match these commits closely but do not prove that the complete verbal deliberation is archived.
2. Exact chat-to-commit causal relation: adjacent timestamps and topical match now corroborate the research sequence, not every intervening question.
3. Independent reproduction and external validation of all phonological P0/P1/P2 numbers, human pronounceability, phoneme identification and recognition, phonetic timing, speaker overlap.
4. Source repository naming ambiguity: commit text still refers to a `phoneme-study` local branch and GlottoDelta research paths, but the objects are reachable under **Unisermo**. Record the location of *verified Git objects*, not assumed original local worktree topology.

See `glottodelta-chatgpt-snapshot-comparison.md` for confirmation that the 8 August script's 2,122 source languages result from its ISO-first deduplication of the **same unchanged July atlas dataset**, rather than the raw 2,176 Glottocode count.
