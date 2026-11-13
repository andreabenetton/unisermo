"""Narrow, source-backed lexical valency validation.

The registry encodes only author-ratified valency frames (movement,
force, transitions, state and physical actions). Verbs without
documented frames remain outside these closed valency families.
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

    def physical_action_base(self, lemma: str) -> str | None:
        """Resolve a single licensed phase/associative derivative.

        The literal lexicalized kunten takes precedence over productive
        kun + ten; its patient is a physically contained entity.
        """
        spec = self.valency["physical_action"]
        if lemma == "kunkunten":
            # A second kun- on the lexicalized kunten root is not
            # licensed by the single-layer source ratification.
            return None
        if lemma in spec["frames"]:
            return lemma
        parsed = self.parse_derivation(lemma)
        if parsed is not None and parsed["category"] == "verb":
            if (parsed["base"] in spec["frames"] and
                    (parsed["operation"] in {
                        "phase_begin", "phase_continue",
                        "phase_cease", "phase_resume", "joint_event"
                    })):
                return parsed["base"]
        # Some regular phase roots are already source-indexed as attested
        # verbs. A direct declared phase of a documented base is supported
        # even when lexical precedence defeats mechanical resegmentation.
        for prefix in spec["phase_prefixes"]:
            if lemma.startswith(prefix):
                base = lemma[len(prefix):]
                if base in spec["frames"] and lemma in self.verbs:
                    return base
        if lemma.startswith(spec["associative_prefix"]):
            base = lemma[len(spec["associative_prefix"]):]
            if base in spec["frames"] and lemma in self.verbs:
                return base
        return None

    def physical_argument_roles(self, lemma: str,
                                complements: list[dict]) -> dict | None:
        """Thematic roles, not inferred ownership, permission or arrival."""
        base = self.physical_action_base(lemma)
        if base is None:
            return None
        spec = self.valency["physical_action"]["frames"][base]
        args = []
        for complement in complements:
            if complement["kind"] != "case_complement":
                continue
            case = complement["case"]
            role = spec["case_roles"].get(case, "event_location")
            args.append({"case": case, "role": role})
        return {"base": base, "subject": spec["subject_role"],
                "object": {"case": "accusative", "role": spec["object_role"]},
                "case_complements": args,
                "semantic_entailments": {
                    key: value for key, value in spec.items()
                    if key.startswith("entails_") or key.startswith("requires_")
                }}

    def _validate_physical_action(self, lemma: str, obj: dict | None,
                                  complements: list[dict]) -> str:
        physical = self.valency["physical_action"]
        base = self.physical_action_base(lemma)
        if base is None:
            raise ValueError("no physical-action valency for this verb")
        frame = physical["frames"][base]
        if obj is None and physical["object_required_in_parser"]:
            raise ValueError(f"{lemma} requires explicit X-em in supported parser subset")
        counts = {}
        seen_roles = []
        for component in complements:
            if component["kind"] != "case_complement":
                # Normal free relators remain independent adjuncts; their
                # presence does not replace an absent accusative patient.
                continue
            case = component["case"]
            allowed = set(frame["case_roles"]) | set(
                physical["allowed_independent_adjunct_cases"])
            if case not in allowed:
                raise ValueError(f"{lemma} does not license {case}")
            counts[case] = counts.get(case, 0) + 1
            if counts[case] > physical["maximum_each_case"]:
                raise ValueError("duplicated physical-action complement")
            if case in frame["case_roles"]:
                seen_roles.append(case)
        # The ratified citation frame orders optional source before
        # destination. Other mixed case orders remain to be formalized.
        if (base == "portar" and
                seen_roles != sorted(seen_roles, key=lambda v:
                                     {"ablative": 0, "dative_allative": 1}[v])):
            raise ValueError("noncanonical source/destination order outside parser subset")
        return frame["id"]

    def has_documented_valency(self, lemma: str) -> bool:
        return (lemma == "traes" or self.is_motion_verb(lemma)
                or self.is_force_verb(lemma) or self.is_state_copula(lemma)
                or self.physical_action_base(lemma) is not None)

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
        elif self.physical_action_base(lemma) is not None:
            source, family = self.valency["physical_action"]["source"], "physical_action"
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

        if self.physical_action_base(lemma) is not None:
            return self._validate_physical_action(lemma, obj, complements)

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
