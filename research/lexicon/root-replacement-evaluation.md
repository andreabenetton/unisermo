# Evaluation dossier — `dik` / `dir`; `stru` / `konstru` / `kostru`

Status: experimental, **no canonical root change**. Governing record: [LDR-0009](../../docs/ldr/LDR-0009-alternative-roots-dir-konstru.md).

## The exact alternatives

| Concept | Current root | Alternative | Letters | Canonical inventory | Initial interpretation |
| --- | --- | --- | ---: | --- | --- |
| say / tell | `dik` | `dir` | 3 vs 3 | Both valid | Reconsider: modern Romance recognition and `dik/tik` collision |
| build / structure | `stru` | `konstru` | 4 vs 7 | Both valid | More recognizably *construct* family; longer |
| build / structure | `stru` | `kostru` | 4 vs 6 | Both valid | Near Italian *costruire*; lacks /n/ |
| build / structure | `stru` | `constru` | — | **Invalid** | Historical/source spelling; `c` excluded |

`sentr` and `kurar` are held constant at the owner's request.

## `dir`: comparative evidence and cautions

- Catalan `dir` is an exact written match; **Eastern Catalan often pronounces it /di/** with no final audible `r`, while Valencian /diɾ/ is also documented. Thus a graphic match is not always a spoken match. Source: https://ca.wiktionary.org/wiki/dir .
- Italian `dire` and French `dire` have a very close visible stem and mean "say"; Spanish `decir` and Portuguese `dizer` belong to the family with consonant changes. Source: https://www.treccani.it/vocabolario/dire/ ; https://www.dictionnaire-academie.fr/article/A9D2606 ; https://www.littre.org/definition/dire .
- German `dir` is an unrelated, common pronoun ("to you"); the exact spelling therefore can produce **false recognition** in some populations despite not colliding inside Unisermo. Source: https://kaikki.org/dictionary/German/meaning/d/di/dir.html .
- Existing Unisermo `dik` can be heard as `tik` ("this") under allowed `d → t` accent merger; `dir` does **not** cause that specific problem. Whether syntax rescues `dik` in ordinary dialogue is not established. Internal reference: https://github.com/andreabenetton/unisermo/issues/1 .
- `dir` is also a prefix of already canonical `dirig` ("direct / guide"), but there is no automatic segmentation into `dir + ig` because `-ig` is not an approved derivational suffix. This is a **parsing audit point**, not an established collision.

*Provisional assessment:* `dir` merits serious adoption consideration, provided corpus frequency, semantic scope, model comprehension, and paradigm safety all hold. This is not an approval.

## `konstru` / `kostru`: comparative evidence and cautions

Latin `construere` = prefix `con-` + `struere`. French `construire`, Spanish/Portuguese `construir`, German `konstruieren` and English `construct` have the nasal-initial prefix; Italian `costruire` frequently lacks the nasal. Source: https://www.littre.org/definition/construire ; https://www.etymonline.com/word/construct .

- `konstru` contains the consonant sequence `nstr`, which can be syllabified as `kon-stru`; do **not** falsely describe this as a four-consonant syllable onset. The `str` cluster already exists in `stru` and `kostru`. Pronounceability needs population testing.
- `konstru` is three graphemes longer than `stru`; `kostru` is two longer. A character difference is **not** a token count: the exact BPE results on all 54 generated finite inflections are needed.
- Both existing `stru` and alternatives are Latin-family forms. *Structure*, *construct* and *build* are not always the same sense; adopting one form as the universal root for "build/structure" must not erase useful distinctions.
- The existing 78-pair pilot contains **no** `stru` sentence. Generated paradigms are useful for tokenizer diagnostics but **not** independent validation of syntax, semantics, or corpus representativeness.

*Provisional assessment:* compare both alternatives objectively. Recognition gains must overcome length, cluster accessibility and semantic tradeoffs; `stru` remains a plausible efficient baseline.

## Reproducible scoring

Run:

```sh
python -m pip install -r benchmarks/requirements-openai.txt
python -m benchmarks.root_substitution --output-dir benchmarks/reports
python -m unittest discover -s tests -p 'test_root_substitution.py'
```

GitHub Actions produces `root-substitution-o200k_base.json` and `root-substitution-cl100k_base.json` as downloadable artifacts. Each contains tokenizer and vocabulary versions/hashes, 54 hypothetical finite clauses, seven case and six derivation samples, and measured development-only sentences from the existing pilot where available. Output retains full risk screens and *null* for unmeasured human recognition.

**Do not optimize on or inspect ranked frozen holdout examples.** Changes to the authoritative lexicon require explicit owner approval, a migration plan and refreshed grammar tests.

## Measured tokenizer results — GitHub Actions run 39848642034

All measurements below are from **official tiktoken 0.14.0**, not grapheme or word-count estimates. Source: https://github.com/andreabenetton/unisermo/actions/runs/39848642034 , artifact `unisermo-openai-tokenizer-pilot` (GitHub artifact ID 12455044936; archive SHA-256 `a15f2a6fa1a6fa3470970ef87af2ce5553bea2ebf0644e283b440daeac7379d1`).

Tokenizer vocabulary SHA-256:
- `o200k_base`: `f2f614601c635339047c0ec251d13afcfd8e3bc01440bca9ab0bdf17ed61e2d0`
- `cl100k_base`: `5688dbbcc53725d351e7779722db09fa3538651706099d1b89ca49f38dd4cf4e`

### Controlled finite verb forms: 54 per root

| Baseline → candidate | Encoding | Baseline tokens | Candidate tokens | Difference |
| --- | --- | ---: | ---: | ---: |
| `dik → dir` | o200k_base | 181 | 183 | **+1.105%** |
| `dik → dir` | cl100k_base | 221 | 186 | **−15.837%** |
| `stru → konstru` | o200k_base | 181 | 235 | **+29.834%** |
| `stru → konstru` | cl100k_base | 216 | 270 | **+25.000%** |
| `stru → kostru` | o200k_base | 181 | 235 | **+29.834%** |
| `stru → kostru` | cl100k_base | 216 | 270 | **+25.000%** |

The 54 forms are synthetic regular finite inflections, not evidence that `stru` or alternatives have been independently certified as full verbal lexical categories by the parser.

### Existing pilot development examples for `dik`: 26

| Encoding | `dik` tokens | `dir` tokens | Difference |
| --- | ---: | ---: | ---: |
| o200k_base | 84 | 90 | **+7.143%** |
| cl100k_base | 107 | 91 | **−14.953%** |

There are **no corresponding `stru` contexts** in the existing pilot. The holdout was not used for selection, ranking or tuning.

### Full-family mechanical screen

The conservative family scanner generated **65 distinct candidate surfaces per root** (bare form, hypothetical verb finite inflections, cases and derivatives), and compared them to all confirmed lexicon families plus protected grammar words. Results:

| Candidate | Exact collision flags | Accent-merger risk flags |
| --- | ---: | ---: |
| `dik` baseline | 0 | 1: `tik` |
| `dir` | 0 | 0 |
| `stru` baseline | 0 | 0 |
| `konstru` | 0 | 0 |
| `kostru` | 0 | 0 |

This screening is limited to modeled morphological rules and documented single-grapheme soft mergers. It overgenerates hypothetical forms; **no flags** is not proof of phonotactic accessibility or guaranteed interpretability.

### Recommendation from current evidence

**Favor testing `dir` as the next possible canonical replacement for `dik`.** It is the same length, has modern Romance direct recognition evidence, removes the modeled `dik/tik` phonetic collision, and shows a substantial reduction on `cl100k_base`; its measurable `o200k_base` disadvantage is modest on generated forms but larger on 26 development examples. This is a **conditional design recommendation**, not a final linguistic or human comprehension verdict.

**Do not replace `stru` with `konstru` or `kostru` at present.** Both candidates require 25–30% more tokens on the 54-form paradigms. Their international resemblance may still matter, but no human recognition study has established gains strong enough to justify this repeated cost. Retain `stru` until direct comparisons demonstrate an overall communication advantage. A separately defined meaning for `konstru` (e.g. specialized construct) would be a *new* lexical proposal requiring its own semantic analysis; do not invent it automatically.

Keep `sentr` and `kurar` unchanged. No canonical roots have been modified, and no historical benchmark or holdout data have been overwritten.
