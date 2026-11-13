"""Narrow, source-backed lexical valency validation.

The registry models only the ratified mov family alternation and the two
traes frames. Other verbs stay outside the closed-valency subset; they do
not inherit movement or transformation argument semantics.
"""
from __future__ import annotations


class ValencyParser:
    def is_motion_verb(self, lemma: str) -> bool:
        spec = self.valency["motion"]
        if lemma == spec["base"] or lemma in spec["directional_lexical"]:
            return True
        # Approved phase forms may already appear in the source-derived
        # lexicon as decision-attested entries; preserve the family even
        # when lexical-index precedence prevents re-segmentation.
        if (lemma in self.verbs and any(
                lemma == prefix + spec["base"]
                for prefix in spec["phase_prefixes"])):
            return True
        # Phase prefixes modify the base motion event. A single productive
        # associative kun- prefix is permitted on the event too.
        parsed = self.parse_derivation(lemma)
        return (parsed is not None and parsed["category"] == "verb"
                and parsed["base"] == spec["base"]
                and parsed["operation"] in {
                    "phase_begin", "phase_continue", "phase_cease",
                    "phase_resume", "joint_event"
                })

    def validate_valency(self, lemma: str, obj: dict | None,
                         complements: list[dict]) -> str | None:
        """Return a ratified frame ID or reject malformed known frames."""
        if lemma == "traes":
            cases = [x["case"] for x in complements
                     if x["kind"] == "case_complement"]
            for frame in self.valency["traes"]["frames"]:
                required_obj = frame["object"] == "required"
                if (bool(obj) == required_obj and
                        sorted(cases) == sorted(frame["required_cases"]) and
                        (frame["other_complements"]
                         or len(complements) == len(frame["required_cases"]))):
                    return frame["id"]
            raise ValueError("traes requires DEST-ad SOURCE-de, or OBJ-em RESULT-da")

        if not self.is_motion_verb(lemma):
            return None
        spec = self.valency["motion"]
        seen = {}
        for argument in complements:
            if argument["kind"] != "case_complement":
                # The comitative/purpose/other free relators are adjuncts;
                # no movement-specific valency claim is made about them.
                continue
            case = argument["case"]
            if case not in spec["allowed_cases"]:
                raise ValueError("unsupported case role for canonical mov frame")
            seen[case] = seen.get(case, 0) + 1
            if seen[case] > spec["maximum_each_case"]:
                raise ValueError("duplicate movement case relation is ambiguous")
        role = "present" if obj is not None else "absent"
        return spec["roles"][role]
