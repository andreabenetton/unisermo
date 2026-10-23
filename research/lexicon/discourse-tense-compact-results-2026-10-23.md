# Compact tense primer A/B — 2026-10-23

Completed Qwen3 32B OpenRouter run: https://github.com/andreabenetton/unisermo/actions/runs/40000898321

Exactly the previous six development documents, original root glossary, original answer key, model and strict event scorer were reused. The compact prompt prepended a short morphology reminder (root + optional past d + person suffix i/u, with one present and one past example).

| Condition | Correct structured events | Prompt tokens | Completion tokens | OpenRouter cost USD |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 13/18 | 1074 | 720 | 0.00028752 |
| Full explicit tense instruction | 18/18 | 1830 | 720 | 0.00034800 |
| Compact tense instruction | 13/18 | 1320 | 720 | 0.00030720 |

The compact instruction saves 510 prompt tokens versus the full explanation over six documents, but its event-slot score falls from 18/18 to 13/18. All six compact responses were structurally parseable. Correct scores by document: D001 2/3, D002 3/3, D003 1/3, D004 3/3, D005 1/3, D006 3/3. This reproduces errors concentrated in present-tense items while past-tense items remain correct.

Neither one sample per prompt variant nor six development documents demonstrates a generalizable optimal instruction length. The full prompt also changes redundancy and examples together, so the causal contribution of each is not isolated. Do not replace the proven long instruction with the compact one for accuracy-sensitive tasks before stronger replication. No grammar/lexicon changes.

Code: benchmarks/discourse_tense_compact.py, benchmarks/discourse_tense_compact_runner.py. Raw artifacts: discourse-compact-40000898321, ID 12521836938.
