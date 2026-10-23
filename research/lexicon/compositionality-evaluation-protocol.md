# Productive composition: lexical economy versus cold-start inference

**Status:** experimental research; this page does not make new canonical words.

The owner prefers a linear, productive communication system to a large flat list of arbitrary lexical items, while recognizing that an untrained LLM pays an initial segmentation/inference cost. Treat that as two distinct quantities:

1. **Compositional encoding:** number of independent morphemes and exceptional lexical entries needed to express a concept.
2. **Cold-start decoding:** errors, prompting/context overhead, and token costs when a model or unfamiliar reader first sees a compound.

Both must be measured. A transparent word is not automatically an unambiguous concept: `sivvok` has the readily recoverable components citizen + voice but could express speech by a citizen, a civic voice, or a public appeal. Do not assign a canonical referent from segmentation alone.

The initial experimental batch is `research/lexicon/productive-compound-trials-001.json`, with 3 existing accepted compounds (`aerplan`, `altmov`, `basmov`) as positive controls and 9 deliberately ambiguous/non-normative novel compounds. Tests verify known components, permitted graphemes, canonical status, and exact concatenation. These checks **do not establish semantics**.

Special caution: `mov` is attested in the formal grammar but its standalone lexical-index status is `decision_attested_not_indexed`. The three already confirmed compound expressions provide established examples; new uses of `mov` must retain an evidence warning and may not silently change its status.

## Next language-model experiment (not yet executed)

Compare **exactly the same generated compound** under three decoding conditions:

- **cold:** compound alone, no dictionary, open-ended segmentation + gloss;
- **rule-only:** one reusable declaration that compounds concatenate their roots with no linker, no root dictionary;
- **one-time seed:** rule + a fixed short dictionary of constituent morphemes, reused for multiple compounds (record amortized one-time prompt cost separately).

Record root-boundary accuracy, compositional gloss quality, unwarranted specificity, API token cost and response validity separately. Both low- and high-ambiguity candidates should be included. Do not use frozen lexical benchmark items to optimize prompts. The human reading/spoken evaluation remains deferred in issue #3.

### Adoption gate

Do not canonize `sivvok`, `kurarager`, `aermov`, etc. merely because an LLM can explain their parts. A lexicalized meaning, if desirable, requires semantic scope, grammar compatibility, phonological collision screening, and a documented owner decision. A nonlexicalized compound may remain interpretable as a phrase even if not registered as a dictionary entry. The existing core 44 canonical entries and numeral/kinship decisions stay unchanged.
