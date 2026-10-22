# Modern word-form frequency pilot — measured baseline (2026-10-22)

**Status:** reproducible corpus-form measurements; translations, recognizability and global concept frequency are **not validated**.

- GitHub Actions: https://github.com/andreabenetton/unisermo/actions/runs/39842978276
- GitHub artifact: `unisermo-openai-tokenizer-pilot` (includes `modern-form-frequencies.json`).
- Artifact digest (GitHub): `sha256:bebf6636f74873375b0a75f3a475a59b77822dd8b240020707d646b9e8a97938`.
- Seed SHA-256: `88f2c9ecbabd967e3b10eb627a77db90de1db8a01cbc546bafdef9023a344670`.
- Frequency provider: official `wordfreq==3.1.1`, wordlist `best`.
- Four Latin anchors checked against Kaikki; 32 modern form measurements across seven languages.
- No Unisermo lexeme or phoneme changed.

## Observed surface-form frequencies (Zipf)

| Unisermo | Language | Form | Role | Zipf |
| --- | --- | --- | --- | ---: |
| dik | en | say | possible translation | 5.89 |
| dik | en | dictate | related, not equivalent | 3.58 |
| dik | it | dire | possible translation | 5.86 |
| dik | es | decir | possible translation | 5.78 |
| dik | pt | dizer | possible translation | 5.68 |
| dik | fr | dire | possible translation | 5.96 |
| dik | de | sagen | non-cognate translation | 5.68 |
| stru | en | build | non-cognate translation | 5.04 |
| stru | en | construct | related; sense review | 3.98 |
| stru | it | costruire | possible translation | 4.74 |
| stru | es | construir | possible translation | 4.73 |
| stru | pt | construir | possible translation | 4.78 |
| stru | fr | construire | possible translation | 4.69 |
| stru | de | bauen | non-cognate translation | 4.81 |
| stru | de | konstruieren | related; sense review | 3.45 |
| kurar | en | care | non-cognate translation | 5.56 |
| kurar | en | cure | related; sense review | 4.32 |
| kurar | it | curare | possible translation | 4.28 |
| kurar | es | cuidar | non-cognate translation | 4.40 |
| kurar | es | curar | related; sense review | 3.98 |
| kurar | pt | cuidar | non-cognate translation | 4.75 |
| kurar | pt | curar | related; sense review | 4.07 |
| kurar | fr | soigner | non-cognate translation | 4.20 |
| kurar | de | pflegen | non-cognate translation | 4.10 |
| sentr | en | center | possible translation | 5.19 |
| sentr | en | centre | orthographic variant | 4.95 |
| sentr | it | centro | possible translation | 5.46 |
| sentr | es | centro | possible translation | 5.44 |
| sentr | pt | centro | possible translation | 5.47 |
| sentr | fr | centre | possible translation | 5.39 |
| sentr | de | Zentrum | possible translation | 4.69 |
| sentr | ru | центр | possible translation | 5.17 |

The frequency of a lexical form is not the frequency of an unambiguous meaning. The spellings `center` and `centre` are not to be added as if they were distinct concepts. Neither cross-language sums nor speaker-weighted recognition percentages can be derived from this table. These corpora are not an exhaustive 2026 spoken-language or multilingual sample; modern-form sense review remains pending.

## Interpretation and next gates

The everyday English forms `say` and `build` are more frequent than the related Latinate forms `dictate` and `construct`, but these are **not guaranteed exact synonyms**, so this cannot justify altering `dik` or `stru`. The result demonstrates why comparing the same intended sense and the contemporary speech register is essential.

`sentr` and `kentr` remain native inventory-valid spellings; no quantified auditory-recognition result is available. The comparative Latin source spelling is not a permitted Unisermo grapheme sequence.

**Additional mechanical finding:** `dik` can merge acoustically with `tik` (proximal demonstrative) under the documented `d → t` accent tolerance. The canonical root `dik` stays unchanged. `language/demonstratives.md` treats `tik` as normative, but the generated lexicon index calls it `example_only`; this metadata discrepancy and phonetic ambiguity are tracked in https://github.com/andreabenetton/unisermo/issues/1.

Follow-up: independent modern-language sense reviews, verified pronunciations, lexical-frequency-vs-concept-frequency separation, and non-Indo-European language coverage before evaluating global recognizability or root-length priorities.
