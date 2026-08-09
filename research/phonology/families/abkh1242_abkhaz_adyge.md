# Family phoneme study — Abkhaz-Adyge

> **Status:** experimental family-level evidence. No canonical GlottoDelta/auxiliary-language decision is changed by this report.

## Scope and method

- Top-level Glottolog unit: **Abkhaz-Adyge (`abkh1242`)**.
- Unit type: **family**.
- Macroarea metadata: **Eurasia** (descriptive only; it does not determine weighting).
- Frozen GlottoDelta sample: **3** distinct relevant languages from **3** source records.
- Glottolog 5.3 language-member coverage: **3/5 = 60.0%**.
- Population-based analysis order: **rank 23**; frozen CLDR speaker-exposure proxy **1,573,826** with **100.0%** of sampled languages carrying an estimate.
- Population rank controls **analysis order only**; it does not determine genealogical `F` weight.
- Target support below is the unweighted share of sampled distinct languages attesting the target realization family.
- `strict+soft` additionally allows only the soft-merger fallbacks already defined in `phoneme_targets.json`.
- This report deliberately **does not define or calculate the eventual cross-family F score**.
- The frozen baseline contains **111 tracked phoneme cells**, not complete upstream PHOIBLE inventories; an absent match may therefore reflect a nearby segment outside the tracked chart.

## Family membership coverage

Represented Glottolog language members: Abkhaz (`abkh1244`), Kabardian (`kaba1278`), West Circassian (`adyg1241`).

Absent from the frozen GlottoDelta sample: Abaza (`abaz1241`), Ubykh (`ubyk1235`).

## Target support

| Target | Canonical | Strict | Strict+soft | Strict languages | Soft-only |
|---|---:|---:|---:|---|---|
| a | /a/ | 2/3 (66.7%) | 2/3 (66.7%) | Adyghe, Kabardian | — |
| e | /e/ | 1/3 (33.3%) | 1/3 (33.3%) | Adyghe | — |
| i | /i/ | 0/3 (0.0%) | 0/3 (0.0%) | — | — |
| o | /o/ | 0/3 (0.0%) | 0/3 (0.0%) | — | — |
| u | /u/ | 0/3 (0.0%) | 0/3 (0.0%) | — | — |
| schwa | /ə/ | 2/3 (66.7%) | 2/3 (66.7%) | Adyghe, Kabardian | — |
| p | /p/ | 2/3 (66.7%) | 2/3 (66.7%) | Adyghe, Kabardian | — |
| b | /b/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| t | /t/ | 2/3 (66.7%) | 2/3 (66.7%) | Adyghe, Kabardian | — |
| d | /d/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| k | /k/ | 1/3 (33.3%) | 1/3 (33.3%) | Adyghe | — |
| g | /ɡ/ | 1/3 (33.3%) | 2/3 (66.7%) | Abkhaz | Adyghe |
| m | /m/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| n | /n/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| f | /f/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| v | /v/ | 2/3 (66.7%) | 3/3 (100.0%) | Abkhaz, Kabardian | Adyghe |
| s | /s/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| z | /z/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| sh | /ʃ/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| l | /l/ | 2/3 (66.7%) | 3/3 (100.0%) | Abkhaz, Kabardian | Adyghe |
| r | /r/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| y | /j/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| w | /w/ | 3/3 (100.0%) | 3/3 (100.0%) | Abkhaz, Adyghe, Kabardian | — |
| h | /h/ | 2/3 (66.7%) | 2/3 (66.7%) | Adyghe, Kabardian | — |
| ng | /ŋ/ | 0/3 (0.0%) | 0/3 (0.0%) | — | — |

## Per-language target matrix

`S` = strict target-family match, `~` = only an existing soft-merger fallback, `—` = absent in the frozen phonemic inventory.

| Language | a | e | i | o | u | schwa | p | b | t | d | k | g | m | n | f | v | s | z | sh | l | r | y | w | h | ng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Abkhaz | — | — | — | — | — | — | — | S | — | S | — | S | S | S | S | S | S | S | S | S | S | S | S | — | — |
| Adyghe | S | S | — | — | — | S | S | S | S | S | S | ~ | S | S | S | ~ | S | S | S | ~ | S | S | S | S | — |
| Kabardian | S | — | — | — | — | S | S | S | S | S | — | — | S | S | S | S | S | S | S | S | S | S | S | S | — |

## Candidate inventory pressure

Mean missing target categories per sampled language. The tolerant column applies only the pre-existing soft-merger experiment; it does not invent new family-specific substitutions.

| Candidate | Targets | Mean strict missing | Mean tolerant missing |
|---|---:|---:|---:|
| current_simple_21 | 21 | 7.00 | 6.00 |
| no_schwa_20 | 20 | 6.67 | 5.67 |
| latin17 | 17 | 6.33 | 5.67 |
| latin17_yw | 19 | 6.33 | 5.67 |
| lexical22_yw | 22 | 6.67 | 5.67 |
| grammar6 | 6 | 2.33 | 2.33 |
| grammar8 | 8 | 3.33 | 3.33 |
| grammar10 | 10 | 3.33 | 3.33 |

## Reading for GlottoDelta auxiliary-language design

- Strictly universal in this sampled family set: **b, d, m, n, f, s, z, sh, r, y, w**.
- Partial strict support: **a, e, schwa, p, t, k, g, v, l, h**.
- Zero strict support: **i, o, u, ng**.
- Lowest strict-support targets in this family sample: `i` 0/3 (0.0%), `ng` 0/3 (0.0%), `o` 0/3 (0.0%), `u` 0/3 (0.0%), `e` 1/3 (33.3%).
- Vowel subsystem: `a` 2/3, `e` 1/3, `i` 0/3, `o` 0/3, `u` 0/3, `schwa` 2/3.
- This is a **dispersion warning, not an automatic veto**. The project-wide P/L evidence and already-confirmed design constraints remain separate evidence, and the 111-cell baseline does not enumerate every upstream PHOIBLE segment or producible allophone.
- Before turning this family result into the final cross-family `F` metric, the aggregation rule should be fixed consistently for all families; this report intentionally preserves the raw within-family evidence needed for that choice.
