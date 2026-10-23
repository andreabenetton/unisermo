# Seven-variant tense instruction ablation — 2026-10-23

Complete paid run: https://github.com/andreabenetton/unisermo/actions/runs/40001562195 ; artifact tense-ablation-40001562195, ID 12522981343. Exactly six previously used development documents, 42 Qwen3 32B requests, no canonical changes.

| Added instruction | Exact events | Input tokens | Output tokens | Cost USD |
| --- | ---: | ---: | ---: | ---: |
| Zero-present rule only | 12/18 | 1182 | 720 | 0.00029616 |
| Examples only | 14/18 | 1212 | 720 | 0.00029856 |
| Parsing procedure only | 10/18 | 1290 | 720 | 0.00030480 |
| Rule + examples | 16/18 | 1320 | 720 | 0.00030720 |
| Rule + procedure | 10/18 | 1398 | 720 | 0.00031344 |
| Examples + procedure | 16/18 | 1428 | 720 | 0.00031584 |
| All three | 16/18 | 1536 | 720 | 0.00032448 |

Previous tests on same documents: baseline 13/18 at 1074 prompt tokens, compact instruction 13/18 at 1320, full explicit instruction 18/18 at 1830. The ablation's all-three variant is NOT textually identical to the earlier full explicit instruction and reached 16/18 rather than 18/18.

Interpretation: Concrete examples appear helpful in this prompt design; rules plus examples achieve 16/18 using 510 fewer input tokens than the earlier full instruction. An analysis procedure alone scored worse, but no causal claim about procedural instructions in general is warranted. Each variant had one sequential, non-randomized run with the same six development examples. Qwen uses a fixed provider-seed request but outputs can still vary. Grading only measures exact verb, object, person and tense slots, not unconstrained semantics.

Next: replicate the top candidates and full explicit prompt in randomized or counterbalanced order, and test on independent development examples rather than tuning repeatedly on the same six. No human experiment or canonical lexical/grammatical change is implied.

Implementations: benchmarks/discourse_tense_ablation.py and benchmarks/discourse_tense_ablation_runner.py.
