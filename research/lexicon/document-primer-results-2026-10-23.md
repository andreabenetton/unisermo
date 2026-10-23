# Document-level minimal glossary pilot — 2026-10-23

## Experiment

GitHub Actions: https://github.com/andreabenetton/unisermo/actions/runs/39906773885 (completed successfully).

Tested eight **novel combinations of existing root components** using Qwen3 32B via OpenRouter. The eight combined surface forms were not part of the prior 12-compound trial; their individual roots were known. The same eight words were sent in **one document request** for each condition (two API calls total).

- **Minimal header:** compound formation rule and only the distinct component roots used by the eight words.
- **Full header:** same rule and entire 15-root research dictionary.
- Both received the same response-format instruction: JSON segmentation and open English gloss.
- No conventional meaning was approved; all free English glosses require semantic review.

## Observed results

| Measure | Minimal per-document header | Full root glossary |
| --- | ---: | ---: |
| Words segmented correctly | **8/8** | **8/8** |
| Input tokens | **169** | **178** |
| Output tokens | 215 | 217 |
| Total tokens | **384** | **395** |
| OpenRouter cost USD | **0.00007372** | **0.00007500** |

In this narrow paired trial, selecting only the roots used in the document saved **9 input tokens**, **11 total tokens** and **$0.00000128** without losing segmentation accuracy. The savings are small because the full glossary contains only 15 roots. This is a demonstration of selective glossary packaging, **not** evidence of large economic benefit.

## Limitations

1. One model, two calls, eight related synthetic compounds, no replicates, fixed order and possible decoding randomness. No statistical inference.
2. The parser produced root-component keys offline; the model was asked to reproduce segmentation. English gloss quality, overconfident conventional interpretations and real communication are not independently assessed.
3. There is no persistent model memory. The one-time header is provided once for each **document request**, not retained across independent requests. The provider bills its actual input tokens; caching not demonstrated.
4. This test compares minimal versus full dictionary **for a single document**, not a full session with one-time knowledge acquisition or against uncomposed lexical alternatives.
5. Roots are attested/confirmed to different degrees (notably standalone `mov`); this experiment does not change their normative status.
6. The prior human listening/reading study is still deferred in issue #3.

## Reproducibility

- Generator: `benchmarks/document_primer.py`
- Evaluator: `benchmarks/document_primer_trial.py`
- Unit tests: `tests/test_document_primer.py`
- Raw replies and scored JSON: GitHub Actions artifact `document-primer-39906773885`, ID `12481610140` (30-day retention).

**Decision:** retain compositionality and selective document headers as useful engineering patterns; do not claim the economic advantage is substantial until tested at larger vocabulary sizes and realistic documents. No canonical lexicon changes.
