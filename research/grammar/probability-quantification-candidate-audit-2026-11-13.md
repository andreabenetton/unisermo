# Probability, quantity and existing degree vocabulary — research audit (2026-11-13)

**Status: research only. No new probability root or quantification syntax ratified.**

## Established and usable pieces

- `pos P` = epistemic possibility, `deb P` = necessity in a fixed modal domain (LDR-0024).
- `kred` = believe; `sert` = certain/certainty. Belief and confidence in a proposition are **not automatically objective probability**.
- `prob` = morally good; cannot be reused for likely/probable.
- Absolute qualitative degree modifiers already ratified in `language/comparison.md`: `minu` (barely), `pok` (slightly), `ase` (moderately), `mult` (very), `ekstrem` (extremely). `suf` marks a **context-dependent threshold**, not a fixed degree.
- Relative comparisons already ratified: `major` more, `minor` less, `masim` most, `minim` least, `ekwal` equal, `dan` than.
- Nominal quantity quantifiers `nul` none, `multi` many, `omni` every/all; `kot` how many.
- Numeric percentage `CARDINAL senim` e.g. `kin senim` = 5%, corresponding to a cardinal/ordinal fraction out of one hundred; rational `uno bisim` = 1/2. Numbers and fraction constructions are canonical, but the syntax of *probability of proposition P = numerical value* remains **open**.
- Count iterations `-jer` and multiplicative factor `-fol` are distinct from probability. Neither entails likelihood.

## Separate concepts that must not collapse

1. **Modal possibility**: There exists at least one admissible situation where P is true. Not equivalent to a probability > 0 when probability-zero events are possible.
2. **Epistemic likelihood / qualitative probability**: Relative plausibility of P according to a speaker or body of evidence; may be low, moderate, high, and updated with evidence.
3. **Numerical probability**: a measure in [0,1] with an identified basis/model/reference class. Often expressed as a percentage; probability must not be conflated with raw frequency.
4. **Confidence/certainty**: how strongly an agent endorses or trusts the proposition or its probability estimate; distinct from its modeled chance.
5. **Relative comparative probability**: P is more/less likely than Q. Relative modifiers should reuse existing `major/minor/ekwal/masim/minim` where semantic and syntactic type permits, instead of new comparative roots.
6. **Threshold sufficiency**: P is likely **enough for some decision**; `suf` may mark the relevant decision threshold once probability degree attachment is canonical. This is not `ase` moderate strength.

## New root candidates for a basic 'likely/probable' scale

**All only candidates.** Each requires lexical recognizability, phonotactics, collision and listening review before the owner ratifies:

| Candidate | Motivation | Tradeoff |
| --- | --- | --- |
| `lik` | short, recognizable via English *likely* | strongly anglocentric; possible unrelated English 'like' association |
| `veri` | Latin/Romance *veri-* = truth family, recognizable via *verisimile* | danger of confusing **truth** with probability; existing lexical search found no confirmed `veri` |
| `plau` | attempt to adapt *plausible* without disallowed initial PL onset | 4 letters but unfamiliar and semantically 'plausible' weaker than 'likely' |
| `probab` | explicit Latin/Romance and international *probable* | long but retains morphological separation from confirmed `prob`; risk of near-collision with unrelated moral-good `prob` in speech, and derivational apparent relation where none exists |

No numerical percentage root is needed. A root `lik` could potentially be a **gradable** probability predicate rather than a binary "likely yes/no" operator, permitting existing degree modifiers and comparative operators. But its lexical category/syntactic valency must first be decided: `lik P` as proposition-scoped likelihood vs `P lik` adjectival predication vs `lik VALUE P` for numeric chance. Do not mix types until scoped examples parse unambiguously.

## Candidate design routes for discussion

**Route A — reusable probability quality.** Approve one new gradable proposition-scope root `lik`, meaning 'P is likely under the relevant model'. Reuse `pok/ase/mult/ekstrem/suf` for scalar qualification, but qualify that unmarked `lik P` has a threshold (e.g. greater-than-even chance or contextually considerable plausibility) while `pok lik P` may not mean 'unlikely' without a defined baseline. Naively `mult lik P` can wrongly suggest intensifying a binary predicate.

**Route B — degree of probability independent of root meaning.** Approve one general *probability* scalar root (not necessarily `lik`), with analytical degrees expressing how high/low a value on that scale is; e.g. `[SCALAR] P`. Then 'probably' requires a context-specific threshold modifier such as `suf`; `mult` expresses high degree but no exact 51% claim. More systematic and permits precise percentages.

**Route C — probability = quantified uncertain frequency.** No new root, use percentages only. Rejected as **sole** strategy: 'probably P' does not require a numerical estimate, and frequency on a reference class is not equivalent to epistemic plausibility for a single event.

## Working proposed framework (not canonical)

Keep probability at **three complementary levels**:

- **Logical/modal:** `pos P` / `deb P` (now canonical).
- **Qualitative:** a new *graded probability notion* using **one** candidate root, plus already confirmed degree modifiers `pok/ase/mult/ekstrem/suf` and relative comparisons `major/minor/ekwal`. Exact syntax needs formal scope design.
- **Numerical:** `PROBABILITY_OF(P) = CARDINAL senim` as an abstract semantic representation, not a current Unisermo sentence. `kin senim` already means 5%; only the attachment of that number to P is missing. Avoid proposing a new percent symbol or affix.

### Truth-conditional tests before ratification

- It is possible but very unlikely P; P may be rare despite being possible.
- It is likely but not necessary P; an event can have high chance without certainty.
- It is certain according to agent A, but objective chance is lower.
- `suf` decision threshold is context-dependent (same chance sufficient for some decisions, insufficient for others).
- P is more likely than Q, but both are unlikely.
- Probability(P and Q) is not generally Probability(P) × Probability(Q) without independence.
- Probability(P or Q) is not generally sum of individual probabilities without accounting for overlap.
- Probability 0% vs impossibility; 100% vs necessity (measure-theoretic exceptions).
- Estimated probability and observed frequencies may diverge.
- 'Unlikely P' is not automatically 'probable not P' unless thresholds and complements are fixed.

## Next design decision

First choose a root for a **gradable** probability relation and define its scale baseline. Then evaluate whether previously ratified degree modifiers apply directly or require a common analytical *degree-of* construction. Lastly ratify quantitative probability attachment using existing fraction/percentage syntax. Do not add a standalone binary 'probably' root plus redundant degree roots.
