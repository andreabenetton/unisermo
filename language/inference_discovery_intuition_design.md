# Decision study: infer, discover, intuit — minimal semantic operators

**Status: unratified research, 2026-11-15.** This note does not change the
ratified lexicon, valency, productive morphology, or parser. Extends the
earlier cognitive factorization analysis after the author ratified bound
`memor` with `admemor/inmemor/dememor/rememor` and `memoria`
(PR #102, merged to main).

## 1. Relevant existing machinery

- `pens` think/mentally process; `kred` believe (nonfactive);
  `kap` understand meaning; `sap` know (factive in approved positive
  propositional frame); `adsap` acquire knowledge, `adkap`
  enter understanding; `rememor` regain access to retained mnemonic content.
- `P ergo Q` presents Q as inferentially following from P in discourse,
  but does **not** assert person X mentally inferred it or certify validity.
  `Q nam P` presents P as justification supplied for asserting Q;
  neither is identical to `Q due P`, a causal statement.
- `-de` source, `-ad` destination, `-in` domain,
  `mod NP` manner, `per NP` instrument. Case availability is not
  automatic valency approval. Existing `sap` knowledge content frame
  rejects arbitrary extra SOURCE-de.
- `memor` is a bound semantic root with explicitly typed operators,
  **not** authorization to introduce such bound-root types or operator
  interpretations unrestrictedly.

## 2. Inferire / dedurre: separate process from epistemic outcome

| Case | Truth requirements | Already expressible | Residual |
| --- | --- | --- | --- |
| Speaker presents P, therefore Q | Q need not be logically proven by wording alone | `P ergo Q` | none for rhetorical/discourse inference |
| X understands why P supports Q | X understands relation | `kap` plus a yet-to-specify structured object | complex explicit relation nominal/propositional frame |
| X personally derives conclusion Q from premises P | inference attempt can be *invalid* and Q can be false | `pens` and `ergo` can describe discourse separately | **actor-bound inference event** |
| X proves Q by valid steps | validity requires separate criterion/proof semantics | `ergo` insufficient | proof/validity predicate |
| X comes to know Q from P | successful factive acquisition | `adsap` plus provenance not yet approved | source attachment & validity |

**Candidate narrow root `infer`** (spelling unratified):
a cognitive process in which an actor constructs a conclusion from given
premises by applying purported inferential relations. It neither
guarantees logical validity nor entails knowledge of Q.
Provisional argument graph: ACTOR, PREMISE(S), CONCLUSION. A SOURCE-de
for premises and DEST-ad for conclusions is **not yet licensed**
and should be assessed against the alternative of source + object
for conclusion. The conclusion might be a proposition rather than a noun,
so a grammar for full proposition arguments is also needed. If a
general `pens` manner frame could express actor-bound inference with
complete entailments, the new root can be dropped.

**Counterexamples:** A person can infer Q incorrectly; know Q without
ever deducing Q; recognize a valid proof without generating it.

## 3. Scoprire: novel to whom, and discover what?

| Usage | Minimal semantics | Coverage | Gap |
| --- | --- | --- | --- |
| Discover that P by hearing from another | agent gains knowledge of P | `adsap` | source/timing if expressed; finite P under phase `adsap` not licensed |
| Independently arrive at previously unknown P | agent gains knowledge and may have produced the insight | `adsap` | source/method and originality relative to *agent* |
| Discover a hidden artifact or object | agent locates/identifies a referent | `advid` begins seeing only, `adsap` acquires knowledge only | **finding/locating event** with target role |
| Discover a principle new to a whole community | agent obtains understanding/knowledge, novelty relative to community | `adkap/adsap` | novelty's comparison population and time |

A new generic **discover** root is unnecessary: it would reintroduce
heterogeneous polysemy. A narrow *find/locate* predicate may be a
separate genuine need, but check existing `vid`, `spets` and
motion/perception roles first. `nov` is NOT currently approved;
avoid using unattested lexical labels in canonical examples.

Do not infer "new to humanity" from `adsap`; it marks acquisition
for the subject only.

## 4. Intuire: manner != factivity != timing

Use independent axes:
- **epistemic result:** `kred` belief vs `kap` understanding vs
  `sap` knowledge; acquisition via `ad-` if applicable;
- **process:** explicit stepwise/deliberate reasoning vs non-deliberate,
  non-stepwise emergence;
- **duration:** immediate vs lengthy incubation; `imedi`
  is **only** licensed as a modifier for certain temporal
  before/after relations, not a universal adverb;
- **validity:** correctly grasped relationship vs unsupported hunch.

A single root `intui` meaning hunch, true insight, creative idea and
rapid inference is **rejected as over-broad**. The *manner* can be
expressed in principle with `mod PROCESS-NP`, but a narrow
notion of non-deliberate cognitive processing (and an eligible
nominal complement) has not been ratified.

**Counterexamples:** Intuition may lead to a false belief; a fast proof
can be deliberative; a non-discursive insight can arrive after long
incubation; memory retrieval `rememor` may be immediate but is not
an inference or an intuition by that fact alone.

## 5. Minimal candidate roadmap and tests

1. **Decide first** whether a general provenance/method construction
   applies to cognitive *events*; specify which heads accept a SOURCE-de,
   which kinds of SOURCE are evidence, and when `mod` attaches.
2. Decide how a **person's inference event** is encoded: one narrowly
   typed `infer` root or a formally specified `pens` process
   construction. The discourse connective `ergo` remains independent.
3. Resolve a *find/locate object* event separately from acquiring
   propositional knowledge. Do not ratify generic `discover`.
4. Specify non-deliberate cognition as a **manner**, not an epistemic
   truth condition. Do not ratify generic `intui`.
5. Only then define typed full-proposition complements on phase heads
   such as `adsap`; their nominal-content valency does not license
   them automatically.

**Acceptance probes before any new root is approved:**
- "I deduced Q from P, but Q is false": inference possible, knowledge not.
- "I knew Q already, but did not derive it": knowledge possible, inference absent.
- "I found the hidden key, but don't know what it opens": localization
  does not imply broader understanding.
- "I learned this theorem from a teacher" vs "I independently discovered
  it": both include acquisition; method/origin differ.
- "I intuited Q, but Q was wrong": hunch or inference-like processing;
  cannot be `sap Q`.
- "I had sudden awareness of a stored name": `rememor`, not
  automatically `infer` or `intui`.

**No changes to canonical grammar/lexicon/parser are authorized by this
research file.**
