# Functional-word audit — 24 October 2026

This audit separates rules **already documented** in the active normative specification, explicit ratifications, lexical-index coverage, and unresolved grammar. It does not invent retrospective approvals.

| Family | Established documentary source | Audit status |
| --- | --- | --- |
| Additive AND / disjunctive OR | `language/word_order.md`; new 24 Oct author confirmation | `e`, `o` ratified as standalone function words; coordination scope not yet modeled |
| Polarity, negation and focus | `language/negation.md`; `research/grammar/confirmed_decisions.json` | `si`, `no`, `-si`, `-no` documented and ratified |
| Polar and content questions | `language/questions.md`; question-word decisions | `ka`, `kid`, `kis`, `kos`, `kud`, `kan`, `kom`, `ker`, `kot`, `kal` documented; inventory should not be re-invented |
| Quantification | `language/noun_number_system.md`; confirmed grammar decisions | `nul`, `omni`, `tot`, `uno`, `wi` documented; some are deliberately decision-attested rather than confirmed-core lexicon |
| Demonstratives | `language/demonstratives.md` | `tik`, `tes`, `tan` documented as grammar; lexical-index example status does not by itself mean unapproved |
| Free analytic relators | `language/noun_case_system.md`; confirmed grammar decisions | `kun`, `per`, `pro`, `due`, `fin`, `tem`, `mod` documented / confirmed |
| Comparative operators | `language/comparison.md` | `major`, `minor`, `masim`, `minus`, `dan`, `ekwal` documented; lexical index is not an exhaustive grammar registry |

## Open, not retrospectively ratified

The author does not recall having designed (1) conditional connectors/conditional subordination, (2) adversative and concessive coordination/subordination, or (3) propositional causal connectors (distinct from the already confirmed `due + NP` meaning 'because of'). A repository audit so far found no confirmed normative decision for those three **families as such**. Record as new pending analysis, not as missing implementations of supposedly ratified rules.

## Historical attestation versus current lexical authority

`bon` remains in `formalization/data/attested_forms.json` as an example attested in `language/copula.md`, while the confirmed lexicon now also contains `bon`. The generated current lexical index selects the confirmed status; the historical attestation is preserved in its source registry. This is a provenance-preserving promotion, not deletion or silent re-ratification.

## Parser boundary

The Phase 1 clause parser is explicitly restricted; documenting free conjunctions does not imply full nested coordination, operator precedence, or inclusive/exclusive OR semantics. Implement those only following separate explicit rules.
