"""Narrow semantic frame recognizer for *already documented* Unisermo valencies.

Does not alter the existing `parse_sentence`, lexicon, canonical grammar or
the closed seven-case inventory. Reuses the existing morphology and NP parser.
Every unlicensed/reordered/ambiguous frame fails closed. This is a reference
projection, not independent semantic validation or a complete syntactic parser.

Source authority: language/verb_specification.md section 8 (mov), and
language/copula.md sections 6-7 / language/noun_case_system.md sections 3-4.
"""
from __future__ import annotations

from formalization.core import Unisermo

# Exactly three explicitly licensed verbal frames.
FRAME_CASES = {
    "move_transitive_to": ("accusative", "dative_allative"),
    "transition_between_states": ("dative_allative", "ablative"),
    "cause_result": ("accusative", "resultative"),
}

FRAME_VERBS = {
    "move_transitive_to": frozenset(("mov", "admov", "inmov", "demov", "remov")),
    "transition_between_states": frozenset(("traes",)),
    "cause_result": frozenset(("traes",)),
}
# The motion-family inheritance is canonical, but not all compounds are
# experimental fixtures. No pel/trak implication of successful movement.


def _explicit_subject(lang: Unisermo, tokens: list[str], verb: dict) -> dict:
    """A demonstrably explicit subject: no guessed ellipsis or coreference."""
    if not tokens:
        raise ValueError("relational frames require an explicit subject")
    subject = lang._np(tokens, "nominative")
    person = verb["person"]
    number = verb["number"]
    if subject["kind"] == "pronoun":
        if (subject["person"], subject["number"]) != (person, number):
            raise ValueError("person/number disagreement")
        return subject
    if person != 3:
        raise ValueError("noun subject requires third-person finite agreement")
    modifiers = subject["modifiers"]
    # bare nominal is number-neutral; wi entails plural, not conversely.
    if "wi" in modifiers and number != "plural":
        raise ValueError("wi subject conflicts with singular finite verb")
    # Canonical modifiers already checked in _np. No referent resolution.
    return subject


def _roles(lang: Unisermo, tail: list[str], cases: tuple[str, str]) -> list[dict]:
    """Enumerate contiguous NP boundaries; reject ambiguity instead of guessing."""
    candidates = []
    for cut in range(1, len(tail)):
        try:
            left = lang._np(tail[:cut], cases[0])
            right = lang._np(tail[cut:], cases[1])
        except ValueError:
            continue
        if left["kind"] != "noun_phrase" or right["kind"] != "noun_phrase":
            continue
        candidates.append([left, right])
    if len(candidates) != 1:
        raise ValueError("unsupported, ambiguous or missing relational complements")
    return candidates[0]


def parse_relational_frame(sentence: str, language: Unisermo | None = None) -> dict:
    """Parse complete, unnegated, SVO-like clauses with one licensed valency.

    Schemas:
      SUBJECT finite-mov OBJECT-em DEST-ad
      THEME finite-traes DEST-ad SOURCE-de
      CAUSER finite-traes PATIENT-em RESULT-da

    The three templates have mutually exclusive case sequences. Locative -in
    remains morphologically valid but is not licensed by these *particular*
    source-defined frames. No claims about general locative predicates.
    """
    lang = language if language is not None else Unisermo()
    if not isinstance(sentence, str):
        raise ValueError("expected a sentence")
    raw = sentence.strip()
    if not raw or raw[-1:] in ("?", "!") or not raw.endswith("."):
        raise ValueError("only punctuated declaratives in this reference subset")
    tokens = raw[:-1].lower().split()
    if len(tokens) < 4 or "no" in tokens or "ka" in tokens:
        raise ValueError("negation, interrogation or insufficient arguments unsupported")
    analyses = [
        (i, entry)
        for i, token in enumerate(tokens)
        for entry in lang.analyze_word(token)["analyses"]
        if entry["kind"] == "finite_verb"
    ]
    if len(analyses) != 1:
        raise ValueError("one unambiguous finite predicate required")
    position, verb = analyses[0]
    subject = _explicit_subject(lang, tokens[:position], verb)
    tail = tokens[position + 1:]
    interpretations = []
    for frame, cases in FRAME_CASES.items():
        if verb["lemma"] not in FRAME_VERBS[frame]:
            continue
        try:
            expressions = _roles(lang, tail, cases)
        except ValueError:
            continue
        if frame == "move_transitive_to":
            names = ("patient", "destination")
            subj_role = "agent"
        elif frame == "transition_between_states":
            names = ("destination_state", "source_state")
            subj_role = "theme"
        else:
            names = ("patient", "result_state")
            subj_role = "causer"
        interpretations.append({
            "kind": "licensed_relational_frame",
            "frame": frame,
            "predicate": verb,
            "subject_role": subj_role,
            "subject": subject,
            "roles": dict(zip(names, expressions)),
            "limitations": (
                "Finite valency and synthetic case only. No reference binding, "
                "pragmatic reordering, adjuncts, scope or independent semantic review."
            ),
        })
    if len(interpretations) != 1:
        raise ValueError("verb-case frame not uniquely licensed by current reference")
    return interpretations[0]
