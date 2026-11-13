# Agent nouns: caregiver, teacher, student — lexical clarification

Status: **partial author decision / open study root**, 2026-11-13.

The author confirmed that occupations or participant labels should be compositionally derived from the relevant activity root using the already canonical person/agent suffix `-or`.

| Intended meaning | Canonical activity root | Compositional person | Status |
|---|---|---|---|
| caregiver / person who cures (including a physician in context) | `kurar` = care/cure | `kuraror` | Productive derivation from confirmed root and suffix; professional licensing is not implied |
| teacher | `dok` = teach | `dokor` | Already illustrated in `language/derivation.md` |
| student / person who studies | NOT YET RATIFIED | `STUDY_ROOT+or` | Root selection pending; `student` is currently example-only |

The Latin etymology of 'doctor' must not license treating `dokor` as a physician: in current Unisermo `dok` means **teach**. Conversely, `kuraror` is compositionally someone who cares/cures, and additional institution/profession credentials would require lexical or contextual specification rather than being entailed by the agent suffix.

Do **not** promote `doktor` or `student` from `example_only` into `research/lexicon/confirmed_lexicon.json` as opaque nouns. The forms appear in legacy/current illustrative text and must not be taken as fresh ratifications. Before replacing examples with `STUDY_ROOT+or`, select and ratify a canonical root for 'study' (distinct from `sap` know, `kap` understand and `pens` think) following `language/vocabulary_design_rules.md`.

This document records the semantic distinction without silently changing historical examples, frozen corpus materials, grammar, or executable parser behavior. Once a study root is accepted, replace the relevant **live** example forms, regenerate formalization indexes and add tests; keep frozen histories immutable.
