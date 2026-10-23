# Discourse tense prompt clarification — completed 2026-10-23

[One-shot experiment](https://github.com/andreabenetton/unisermo/actions/runs/40000287573) completed successfully using the unchanged six development documents and Qwen3 32B through OpenRouter.

| Outcome | Original primer | Explicit zero-present clarification |
| --- | ---: | ---: |
| Correct structured events | 13/18 | **18/18** |
| Valid response documents | 6/6 | **6/6** |
| Input tokens | 1,074 | 1,830 |
| Output tokens | 720 | 720 |
| OpenRouter reported cost | $0.00028752 | $0.00034800 |

The explicit variant prepends instructions: present tense has no tense marker, the person ending comes directly after the verb root, while past inserts d immediately before the person ending. It illustrates peli=pel+i (present), peldu=pel+d+u (past), and warns that final i does not mark past. The six source clauses, dictionary, model, scorer and event labels were otherwise unchanged. All 18 exact event tuples (root, object, tense, person) matched the answer key.

This supports the hypothesis that the previous five present-to-past errors were due to insufficiently explicit task instructions, not evidence requiring a grammatical change. However, the test is a single paired prompt contrast with one model and no independent replicates or truly natural discourse. It is not a test of human comprehension or free translation. The provider billed 756 additional input tokens and $0.00006048 additional cost. Do not overinterpret 18/18 on this development-only dataset.

Code: benchmarks/discourse_tense_clarification.py, benchmarks/discourse_tense_runner.py. Artifacts: discourse-tense-40000287573 (ID 12521143841), containing both raw replies and the complete scored report. Human recognition study remains deferred in issue #3; canonical grammar and lexicon remain unchanged.
