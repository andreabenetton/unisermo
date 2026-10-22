# Modern lexical evidence — experimental

This research implements [LDR-0008](../../docs/ldr/LDR-0008-lexical-recognizability.md) without altering any accepted Unisermo root.

## Data provenance

- **Latin etymons:** `research/lexicon/modern-form-seeds.json` gives independently located Kaikki Latin entry URLs for `dico`, `struo`, `cura` and `centrum`. These source pages are evidence of Latin words, **not** of current recognition.
- **Modern forms:** 32 initial spelling/lemma comparison inputs in English, Italian, Spanish, Portuguese, French, German and Russian. All have `modern_sense_review: pending`. A translation candidate is not a verified translation; a cognate can have a related but different meaning.
- **Measured corpus form frequency:** pinned `wordfreq==3.1.1` returns per-language, per-form Zipf frequencies. It combines written and subtitle/social sources of heterogeneous vintages; it does not represent a pure spoken-language corpus or 2026 live usage. It is a **form-frequency proxy only**, not a measured frequency of the meaning or an estimate of a population's recognition.
- **Phonetics:** no pronunciation or phonological similarity scores have been fabricated. Modern pronunciation needs verified source-specific IPA; only then may sounds be mapped into Unisermo's approved inventory.
- **Population coverage:** no weights or rankings assigned. Languages in this small pilot are not globally representative; demographic weights must not double-count multilingual speakers.

## Reproduce the modern-frequency report

From repository root on a networked Python installation:

```sh
python -m pip install -r benchmarks/requirements-frequency.txt
python -m unittest discover -s tests -p 'test_modern_evidence.py' -v
python -m benchmarks.modern_evidence --output benchmarks/reports/modern-form-frequencies.json
```

The report includes source-seed SHA-256, `wordfreq` version, wordlist variant, raw Zipf values by language/form, and explicit `null` for unmeasured concept frequency and auditory/written recognition. A Zipf value of 0 is censored by the corpus thresholds; **it does not mean that the word is never used**. Do not sum across languages, combine UK and US spelling variants, or infer linguistic economy from the word-frequency list alone.

## Extract Latin entries from a Kaikki JSONL dump

Kaikki distributes machine-readable Wiktionary/Wiktextract JSONL. The full language dump can be large; the importer streams one JSON line at a time and supports `.gz`.

```sh
python -m benchmarks.kaikki_extract \
  --dump /path/to/downloaded-raw-wiktextract-data.jsonl.gz \
  --source-url 'https://kaikki.org/dictionary/rawdata.html' \
  --require-all \
  --output benchmarks/reports/kaikki-latin-subset.json
```

Supply the **exact downloaded dataset URL** rather than the landing-page example when known. The importer records the SHA-256 of the uncompressed JSONL stream and Latin word, part of speech, source IPA and number of senses. It deliberately does **not** copy full glosses. Normalized macrons support matching dictionary lemmas `dīcō` with anchor `dico`; absent entries are shown as missing, never filled by inference.

Downloading and republishing Wiktionary-derived data may involve CC BY-SA and attribution obligations. Consult Kaikki's provenance/licensing information before redistributing extracts. The repository's source links do not imply a live API or a pinned reproducible dump.

## Next gates

1. Independent sense review of each modern-language comparison, including regional variants and register.
2. Attested phonemic transcriptions for auditory comparison, distinct from orthographic similarity.
3. Reliable multilingual **concept-level** frequency estimates, ideally stratified by spoken/dialogue, written, and agent-technical communication.
4. Phoneme-inventory filter and full paradigm collision analysis for shortened candidates.
5. Speaker recognition tests, with explicit population samples; publish metrics with uncertainty before ranking.
6. No lexical change without a separate owner-accepted LDR.

Sources: https://kaikki.org/dictionary/Latin/index.html , https://kaikki.org/dictionary/rawdata.html , https://pypi.org/project/wordfreq/ .
