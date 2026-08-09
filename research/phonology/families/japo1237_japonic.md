# Family phoneme study — Japonic

> **Status:** experimental family-level evidence. No canonical GlottoDelta/auxiliary-language decision is changed by this report.

## Scope and method

- Top-level Glottolog unit: **Japonic (`japo1237`)**.
- Unit type: **family**.
- Macroarea metadata: **Eurasia, Papunesia** (descriptive only; it does not determine weighting).
- Frozen GlottoDelta sample: **3** distinct relevant languages from **3** source records.
- Glottolog 5.3 language-member coverage: **3/17 = 17.6%**.
- Population-based analysis order: **rank 8**; frozen CLDR speaker-exposure proxy **121,249,490** with **33.3%** of sampled languages carrying an estimate.
- Population exposure controls **analysis order and cross-family `F` weight**. The support percentages in this family report remain unweighted across distinct sampled languages.
- Target support below is the unweighted share of sampled distinct languages attesting the target realization family.
- `strict+soft` additionally allows only the soft-merger fallbacks already defined in `phoneme_targets.json`.
- This report deliberately **does not calculate cross-family `F` itself**; it preserves the within-family support that the population-weighted aggregate consumes.
- The frozen baseline contains **111 tracked phoneme cells**, not complete upstream PHOIBLE inventories; an absent match may therefore reflect a nearby segment outside the tracked chart.

## Family membership coverage

Represented Glottolog language members: Japanese (`nucl1643`), Kunigami (`kuni1268`), Miyako (`miya1259`).

Absent from the frozen GlottoDelta sample: Hachijo (`hach1239`), Vernacular Atayalic Japanese (`yila1234`), Kagoshima (`sats1241`), Old Japanese (`oldj1239`), Tsugaru (`tsug1237`), Kikai (`kika1239`), Oki-No-Erabu (`okin1246`), Toku-No-Shima (`toku1246`), Northern Amami-Oshima (`nort2935`), Southern Amami-Oshima (`sout2954`), Yoron (`yoro1243`), Central Okinawan (`cent2126`), Yaeyama (`yaey1239`), Yonaguni (`yona1241`).

## Target support

| Target | Canonical | Strict | Strict+soft | Strict languages | Soft-only |
|---|---:|---:|---:|---|---|
| a | /a/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| e | /e/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| i | /i/ | 2/3 (66.7%) | 2/3 (66.7%) | Kunigami, Japanese | — |
| o | /o/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| u | /u/ | 3/3 (100.0%) | 3/3 (100.0%) | Kunigami, Miyako, Japanese | — |
| schwa | /ə/ | 0/3 (0.0%) | 0/3 (0.0%) | — | — |
| p | /p/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| b | /b/ | 2/3 (66.7%) | 2/3 (66.7%) | Kunigami, Japanese | — |
| t | /t/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| d | /d/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| k | /k/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |
| g | /ɡ/ | 2/3 (66.7%) | 2/3 (66.7%) | Kunigami, Japanese | — |
| m | /m/ | 3/3 (100.0%) | 3/3 (100.0%) | Kunigami, Miyako, Japanese | — |
| n | /n/ | 2/3 (66.7%) | 2/3 (66.7%) | Miyako, Japanese | — |
| f | /f/ | 1/3 (33.3%) | 1/3 (33.3%) | Miyako | — |
| v | /v/ | 1/3 (33.3%) | 3/3 (100.0%) | Miyako | Kunigami, Japanese |
| s | /s/ | 3/3 (100.0%) | 3/3 (100.0%) | Kunigami, Miyako, Japanese | — |
| z | /z/ | 2/3 (66.7%) | 3/3 (100.0%) | Kunigami, Japanese | Miyako |
| sh | /ʃ/ | 1/3 (33.3%) | 3/3 (100.0%) | Japanese | Kunigami, Miyako |
| l | /l/ | 0/3 (0.0%) | 2/3 (66.7%) | — | Miyako, Japanese |
| r | /r/ | 2/3 (66.7%) | 2/3 (66.7%) | Miyako, Japanese | — |
| y | /j/ | 2/3 (66.7%) | 2/3 (66.7%) | Kunigami, Japanese | — |
| w | /w/ | 2/3 (66.7%) | 2/3 (66.7%) | Kunigami, Japanese | — |
| h | /h/ | 2/3 (66.7%) | 2/3 (66.7%) | Kunigami, Japanese | — |
| ng | /ŋ/ | 1/3 (33.3%) | 1/3 (33.3%) | Japanese | — |

## Per-language target matrix

`S` = strict target-family match, `~` = only an existing soft-merger fallback, `—` = absent in the frozen phonemic inventory.

| Language | a | e | i | o | u | schwa | p | b | t | d | k | g | m | n | f | v | s | z | sh | l | r | y | w | h | ng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Kunigami | — | — | S | — | S | — | — | S | — | — | — | S | S | — | — | ~ | S | S | ~ | — | — | S | S | S | — |
| Miyako | — | — | — | — | S | — | — | — | — | — | — | — | S | S | S | S | S | ~ | ~ | ~ | S | — | — | — | — |
| Japanese | S | S | S | S | S | — | S | S | S | S | S | S | S | S | — | ~ | S | S | S | ~ | S | S | S | S | S |

## Candidate inventory pressure

Mean missing target categories per sampled language. The tolerant column applies only the pre-existing soft-merger experiment; it does not invent new family-specific substitutions.

| Candidate | Targets | Mean strict missing | Mean tolerant missing |
|---|---:|---:|---:|
| current_simple_21 | 21 | 10.67 | 8.33 |
| no_schwa_20 | 20 | 9.67 | 7.33 |
| latin17 | 17 | 8.00 | 7.33 |
| latin17_yw | 19 | 8.67 | 8.00 |
| lexical22_yw | 22 | 10.33 | 8.00 |
| grammar6 | 6 | 1.33 | 1.33 |
| grammar8 | 8 | 2.67 | 2.67 |
| grammar10 | 10 | 3.33 | 3.33 |

## Reading for GlottoDelta auxiliary-language design

- Strictly universal in this sampled family set: **u, m, s**.
- Partial strict support: **a, e, i, o, p, b, t, d, k, g, n, f, v, z, sh, r, y, w, h, ng**.
- Zero strict support: **schwa, l**.
- Lowest strict-support targets in this family sample: `l` 0/3 (0.0%), `schwa` 0/3 (0.0%), `a` 1/3 (33.3%), `d` 1/3 (33.3%), `e` 1/3 (33.3%).
- Vowel subsystem: `a` 1/3, `e` 1/3, `i` 2/3, `o` 1/3, `u` 3/3, `schwa` 0/3.
- This is a **dispersion warning, not an automatic veto**. The project-wide P/L evidence and already-confirmed design constraints remain separate evidence, and the 111-cell baseline does not enumerate every upstream PHOIBLE segment or producible allophone.
- The cross-family aggregate weights this raw within-family evidence by family speaker exposure; keeping this report unweighted internally prevents a single very large language from standing in for its whole family.
