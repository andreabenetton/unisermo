# Complements and declensions: reconstructed design history

## Status and provenance

This reconstructs a **specific earlier ChatGPT discussion on 24 May 2026**, found through retrospective conversation retrieval, and compares it with the preserved historical noun-case specification and the current canon. The original **entire dialogue/transcript has not yet been exported verbatim**. Quoted decision contents below are paraphrases of recovered time-stamped utterances, not invented verbatim quotations.

### 24 May 2026: original design

- **21:55:24 UTC**: the founder proposed **a distinct ending for each different complement**; later accepted a **base versus extended case** distinction. Design motive: regular and compact encoding of grammatical relations.
- **22:05:25 UTC**: explicitly fixed **`-s` = genitive, possession, of** and **`-de` = origin/from**. This **rejected** an earlier option assigning `-de` to 'of' and `-da` to 'from'. This rejected configuration matters for tracing phonological and semantic collision avoidance.
- **22:09:05 UTC**: confirmed the **original inventory**:
  - Seven base cases: unmarked `Ø` nominative, `-em` accusative, `-s` genitive, `-de` ablative, `-ad` allative/dative, `-in` locative, `-ko` comitative.
  - Six extended cases: `-per` instrumental/perlative, `-pro` benefactive, `-due` causal, `-fin` purposive, `-tem` temporal, `-mod` manner.
- Historical design principle visible in `legacy/original-language/noun_case_system.md`: suffix on the **last word/head of nominal phrase**, once per phrase; modifiers do not carry repeated case agreement, so longer noun phrases remain regular and easy to parse.
- The historical document also describes an older plural suffix `-en`. **Do not mistake this for the current plural system**, which instead uses optional prenominal `wi`.

### 10 August 2026: semantic analysis of transitions

- A conversation at **14:21:22 UTC** accepted `traes` to signal explicit transition.
- Its two-pole frame `traes DEST-ad SOURCE-de` was recorded at **14:22:43 UTC** (commit `16250c8` recalled in conversation): destination `-ad`, source `-de`.
- Later at **14:29:59 UTC**, the conversation distinguished caused transitions (causer + affected object) from spontaneous transitions and discussed a separate **resulting predicate** `-da`. This was **still a proposal at that instant**, and is now a canonical resultative `-da` in the current `language/noun_case_system.md`.
- Distinguish **allative `-ad`** (destination) from **resultative `-da`** (role/state as transformed outcome). Do not read today's meaning of `-da` back into the May rejected `-da` = source alternative.

### Later revision: fewer synthetic cases and analytic complements

The current `language/noun_case_system.md` records a seven-case **closed synthetic core**:
`Ø, -em, -s/-es, -ad, -de, -in, -da`.
The older synthetic `-ko` and all six extended suffixes were **retired as case morphology**. Their relations now use standalone invariant **preposed relators**:
`kun` (with), `per` (through/by means of), `pro` (for benefit), `due` (because of), `fin` (purpose), `tem` (time), `mod` (manner).
The precise dates and conversational reasoning of **each revision** have not yet been recovered; Git history can narrow these changes. Preserve both stages because this is a substantive change in language architecture, **not** a spelling cleanup.

### Explicit historical contrasts for the paper

| Topic | Original May scheme | Current canon |
| --- | --- | --- |
| Synthetic cases | 7 base + 6 extended = 13 | 7 total |
| Comitative | `-ko` suffix | independent `kun` |
| Instruments / cause / purpose / manner | suffixes `-per -due -fin -mod` | free relators `per due fin mod` |
| Temporal and benefactive | `-tem -pro` suffixes | free relators `tem pro` |
| Resultative `-da` | not in accepted May inventory (and rejected as source) | accepted for resulting predicative role |
| Plural | historical `-en` suffix appears in legacy specification | optional `wi` before noun; bare noun number-neutral |
| Case agreement | case once, no adjective/modifier agreement | case once on head noun, no modifier agreement |

## Paper significance

This is evidence of **iterative design and selective reversal**: the early ideal of a unique morphological case ending per complement was later limited to frequent syntactic roles; rarer semantic relations moved to analytic function words, while a new resultative was added for state change. Preserve the exact decisions and revisions and investigate reasons such as parsability, compositionality, phonotactics and cost **as hypotheses until corroborated by the actual conversations**, not as already proven historical motives.

## Primary and secondary references

- Recovered conversation records on 24 May 2026 at 21:55:24, 22:05:25 and 22:09:05 UTC (original full messages not yet archived in repository).
- Recovered conversation records on 10 Aug 2026 at 14:21:22, 14:22:43 and 14:29:59 UTC.
- `legacy/original-language/noun_case_system.md` — preserved historical specification.
- `language/noun_case_system.md` — current normative rule.
- `formalization/data/morphology.json` — parser/generator data contract.

**Archival work remaining:** obtain the full original May transcript, verify exact wording and dates of change from 13 synthetic cases to 7 and from `-en` to `wi`, plus the final adoption of resultative `-da`.

## New primary Git anchors (24 October follow-up)

The August transition took **two** separate, verifiable steps, not one: [`64c2d33`](https://github.com/andreabenetton/unisermo/commit/64c2d33cb83ded768480f8185582025c380a855e) at **10 August 09:16:52 UTC** removed the old `-ko` and six extended suffixal cases, leaving **six synthetic cases** with analytic `kun/per/pro/due/fin/tem/mod`. [`53df8ba`](https://github.com/andreabenetton/unisermo/commit/53df8ba04e5d04ef9794c62c357a712567f86123) at **14:36:39 UTC** added resulting-predicate `-da`, giving the current **seven**. This explains the previously undated middle state **13→6→7**, with no assumption about a fully recovered user transcript.

An earlier conversation-index record now also places `mov`, `et`, past-tense `d`, and an explicit `root+tense+person` versus `root+person+tense` comparison at **24 May 19:57–20:00 UTC**, preceding the 21:55 noun-case discussion. See [chronological reconstruction](may-august-morphology-decision-chain.md). Exact May wording remains unexported.
