# Document dictionary transport benchmark — 2026-10-23

Completed GitHub Actions run: https://github.com/andreabenetton/unisermo/actions/runs/39907281599

This is an offline tokenizer test, not LLM comprehension, and does not add any canonical vocabulary. Each comparison uses the same eight synthetic compound examples. Expanded dictionaries contain 15 existing research glosses and 85 or 985 additional **artificial placeholders**, not researched word roots.

| Entries | Tokenizer | Minimal | Expanded | Ratio |
| --- | --- | ---: | ---: | ---: |
| 100 | o200k_base | 110 | 983 | 8.94 |
| 100 | cl100k_base | 114 | 992 | 8.70 |
| 1000 | o200k_base | 110 | 10477 | 95.25 |
| 1000 | cl100k_base | 114 | 10708 | 93.93 |

Measures only input header transmission under official tokenizers. Actual vocabulary may tokenize differently. No paid LLM requests or semantic scoring were performed for these 100/1000-entry cases. Do not equate the ratio with real-world costs or communication accuracy.

Implementation: benchmarks/document_scaling.py. Tests: tests/test_document_scaling.py. Reproducible report: benchmarks/reports/document-scaling.json in GitHub Actions artifacts.
