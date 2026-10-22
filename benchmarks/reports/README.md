# Benchmark outputs

`readiness.json` reports local capability only; it is not a token-count report.

When the official OpenAI tokenizer dependency and its vocabularies are installed,
`python -m benchmarks measure-openai --include-draft` will create
`o200k_base-pilot.json` and `cl100k_base-pilot.json` here. Those generated
files are gitignored to avoid confusing one machine's experimental results
with accepted language specifications. Publish them separately as a CI artifact
or along with an explicitly reviewed report, preserving corpus and vocabulary
hashes. There are no genuine tokenizer measurements in the present snapshot.
