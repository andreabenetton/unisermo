# Review sheet — complete proposition semantics

**Status: NOT independently reviewed (0/24).** This worksheet is an invitation for subsequent independent human/linguistic review, not evidence that such a review occurred.

Before seeing Qwen responses, a reviewer should consult the **entire** normative source passages and the restrictions of `benchmarks/proposition_meaning.py`, independently interpret each sentence, and evaluate whether the machine-derived event is natural, correctly typed and semantically licensed. For each row record: `approved`, `ambiguous`, `invalid`, or `requires_context`; confidence; alternative reading; rationale; and which of action, agent, agent number, patient, patient quantity, deictic position, time, aspect, polarity and speech act are supported.

Do **not** assert a unique referent for a bare noun, infer definiteness or distributive scope from `omni`, or invent coreference between the two sentences. Check whether `vid` and `dom` being example-only rather than confirmed lexemes affects publication claims. Record any disagreement with the reference parser without silently rewriting it.

Reviewer identity and role: _not assigned_

Review date: _pending_

Source commit: _pending_

| Sentence | Unisermo text | Stratum | Canonical sources | Human judgment | Confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| P001.1 | `i vidi domem.` | agent_object | `language/word_order.md`, `language/verb_specification.md` | pending | — | — |
| P001.2 | `u vidu akwaem.` | agent_object | `language/word_order.md`, `language/verb_specification.md` | pending | — | — |
| P002.1 | `i no vidi domem.` | polarity_question | `language/questions.md`, `language/negation.md` | pending | — | — |
| P002.2 | `ka u vidu domem?` | polarity_question | `language/questions.md`, `language/negation.md` | pending | — | — |
| P003.1 | `in vidin fratem.` | person_number | `language/verb_specification.md`, `language/word_order.md` | pending | — | — |
| P003.2 | `un trakun aerplanem.` | person_number | `language/verb_specification.md`, `language/word_order.md` | pending | — | — |
| P004.1 | `uman vida domem.` | nominal_agent | `language/noun_number_system.md`, `language/word_order.md` | pending | — | — |
| P004.2 | `wi uman vidan domem.` | nominal_agent | `language/noun_number_system.md`, `language/word_order.md` | pending | — | — |
| P005.1 | `i vidi tik domem.` | deixis | `language/demonstratives.md`, `language/verb_specification.md` | pending | — | — |
| P005.2 | `i vidi tan domem.` | deixis | `language/demonstratives.md`, `language/verb_specification.md` | pending | — | — |
| P006.1 | `i vidi tes domem.` | deixis_plural | `language/demonstratives.md`, `language/noun_case_system.md` | pending | — | — |
| P006.2 | `i vidi tik wi domem.` | deixis_plural | `language/demonstratives.md`, `language/noun_case_system.md` | pending | — | — |
| P007.1 | `i vidi ter domem.` | quantity | `language/numerals.md`, `language/noun_case_system.md` | pending | — | — |
| P007.2 | `u vidu bis domem.` | quantity | `language/numerals.md`, `language/noun_case_system.md` | pending | — | — |
| P008.1 | `i vidi omni umanem.` | quantity_scope_open | `research/grammar/nominal_number_and_quantification.md`, `language/noun_case_system.md` | pending | — | — |
| P008.2 | `u vidu nul umanem.` | quantity_scope_open | `research/grammar/nominal_number_and_quantification.md`, `language/noun_case_system.md` | pending | — | — |
| P009.1 | `i peldi akwaem.` | tense_action | `language/verb_specification.md` | pending | — | — |
| P009.2 | `u trakfu domem.` | tense_action | `language/verb_specification.md` | pending | — | — |
| P010.1 | `in movefin domem.` | aspect_time | `language/verb_specification.md` | pending | — | — |
| P010.2 | `un trakodun aerplanem.` | aspect_time | `language/verb_specification.md` | pending | — | — |
| P011.1 | `i movi akwaem.` | force_vs_motion | `language/verb_specification.md` | pending | — | — |
| P011.2 | `u pelu akwaem.` | force_vs_motion | `language/verb_specification.md` | pending | — | — |
| P012.1 | `i vidi multi umanem.` | quantity_polarity | `language/noun_number_system.md`, `language/questions.md` | pending | — | — |
| P012.2 | `ka i no viddi ter domem?` | quantity_polarity | `language/noun_number_system.md`, `language/questions.md` | pending | — | — |

**Review tally:** approved 0, ambiguous 0, invalid 0, requires context 0, unreviewed 24.

Any later adjudication should be versioned and dated; the original machine-keyed outcomes must be preserved. Post-result reviewer exposure must be disclosed, not represented as blind independent annotation.
