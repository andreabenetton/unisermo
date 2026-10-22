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
