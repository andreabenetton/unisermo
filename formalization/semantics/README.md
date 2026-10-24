# Semantics boundary

The baseline `formalization.parser` returns morphology and a restricted SVO clause AST.
It is **not** a complete semantic interpreter. Ambiguity is preserved at word level.

## Additional source-licensed relational-valency gate (research only)

`formalization/semantics/relational_frames.py` is a small independent parser
for **three expressly documented clause templates** only:

- `SUBJECT finite-mov PATIENT-em DESTINATION-ad` — source:
  `language/verb_specification.md` motion-family valency;
- `SUBJECT finite-traes DESTINATION-ad SOURCE-de` — two-pole transition:
  `language/copula.md` section 6 and `language/noun_case_system.md`;
- `SUBJECT finite-traes PATIENT-em RESULT-da` — causative result:
  `language/copula.md` section 7 and `language/noun_case_system.md`.

It reuses existing nominal and finite morphology, rejects unsupported
valencies and orders, and leaves `parse_sentence` **unchanged**. These narrow
schemas are a *source-linked research implementation*, **not** a newly approved
definition of the full language. The semantic label `theme` for the
two-state transition subject is a research interpretation **pending human
validation**, even though the source/destination cases are already canonical.

Locative `-in` is valid synthetic case morphology and is tested as such.
A finite verb frame containing `-in` is deliberately **not inferred** from
the above three templates: absence in this research recognizer does not
prohibit that construction in the real language.

Original parser support, broader locative/copular argument semantics, free
relators, reordering, case ambiguity, pro-drop, negative scope, finite clauses
with inter-sentential reference, quantifier scope and all remaining valencies
are outside this addition.

A future owner-approved LDR must define referent tracking, negation scope,
quantification, presuppositions, valency and logical-form serialization.
No LLM-efficiency claim may imply semantic equivalence from morphology alone.
