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

    def is_force_verb(self, lemma: str) -> bool:
        if lemma in self.valency["force_manner"]["verbs"]:
            return True
        phase = self.parse_derivation(lemma)
        return (phase is not None and phase["base"] in self.valency["force_manner"]["verbs"]
                and phase["operation"] in {
                    "phase_begin", "phase_continue",
                    "phase_cease", "phase_resume"
                })

    def is_state_copula(self, lemma: str) -> bool:
        spec = self.valency["copula_state"]
        return lemma == spec["base"] or lemma in spec["phase_verbs"]

    def has_documented_valency(self, lemma: str) -> bool:
        return (lemma == "traes" or self.is_motion_verb(lemma)
                or self.is_force_verb(lemma) or self.is_state_copula(lemma))

    def valency_evidence(self, lemma: str) -> dict:
        """Expose the evidence boundary for a canonical or productive verb."""
        if lemma not in self.verbs and not self.is_derived_verb(lemma):
            raise ValueError("not a canonical or permitted productive verb")
        source = None
        family = None
        if lemma == "traes":
            source, family = "language/derivation.md#explicit-transition-between-states", "transition"
        elif self.is_motion_verb(lemma):
            source, family = "language/derivation.md#mov-valency-alternation", "motion"
        elif self.is_force_verb(lemma):
            source, family = self.valency["force_manner"]["source"], "force_manner"
        elif self.is_state_copula(lemma):
            source, family = self.valency["copula_state"]["source"], "state_predication"
        return {"lemma": lemma, "status": "documented" if source else "undetermined",
                "family": family, "source": source,
                "note": ("Unspecified lexical valency is NOT automatically grammatical"
                         if source is None else
                         "Only explicitly attested frames are parser-supported")}

    def _validate_known_case_adjuncts(self, complements: list[dict],
                                      permitted: set[str], label: str) -> None:
        for item in complements:
            if item["kind"] != "case_complement":
                # A free relator can introduce an independent adjunct; it
                # cannot by itself supply an omitted lexical object.
                continue
            if item["case"] not in permitted:
                raise ValueError(f"{label}: unsupported lexical case role " + item["case"])

    def validate_valency(self, lemma: str, obj: dict | None,
                         complements: list[dict]) -> str | None:
        """Check attested frames; unknown roles remain unlicensed by parser."""
        if self.is_state_copula(lemma):
            raise ValueError("state predicates require typed copular complement analysis")
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

        if self.is_force_verb(lemma):
            spec = self.valency["force_manner"]
            if obj is None:
                raise ValueError("force/manner frame requires explicit X-em patient")
            self._validate_known_case_adjuncts(
                complements, set(spec["allowed_case_adjuncts"]), "force/manner")
            return spec["frame"]

        if not self.is_motion_verb(lemma):
            # The seven cases are grammatical, but the roles permitted
            # by a particular verb are not necessarily ratified. Avoid
            # guessing DEST-ad or SOURCE-de on any arbitrary lexical root.
            self._validate_known_case_adjuncts(
                complements, {"locative"}, "undetermined verb valency")
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
