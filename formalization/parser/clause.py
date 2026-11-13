"""Unisermo Phase 1 reference parser/clause methods. No guesswork outside the accepted subset."""
from __future__ import annotations

class ClauseParser:
    # Canonical pronouns with productive genitive -s. The third-person
    # specificity forms are already ratified; no gender agreement is inferred.
    PERSONAL_GENITIVES = {
        "is": ("i", "singular", 1),
        "us": ("u", "singular", 2),
        "as": ("a", "singular", 3),
        "ins": ("in", "plural", 1),
        "uns": ("un", "plural", 2),
        "ans": ("an", "plural", 3),
        "aos": ("ao", "singular", 3),
        "aes": ("ae", "singular", 3),
        "anos": ("ano", "plural", 3),
        "anes": ("ane", "plural", 3),
    }

    def _np(self, words: list[str], required_case: str) -> dict:
        """Bounded case-bearing NP, with visible genitive and focus structure.

        Focus suffix attaches to the RIGHT EDGE of the whole constituent,
        never to a guessed subtoken. A pre-head genitive modifier is an
        explicit possessor; postposed genitive is recognized only for the
        ratified 'part WHOLE-s' part-whole frame.
        """
        if not words:
            raise ValueError("empty noun phrase")
        words = list(words)
        marker = None
        if "-" in words[-1]:
            host, separator, suffix = words[-1].rpartition("-")
            if separator != "-" or suffix not in {"si", "no"} or not host or "-" in host:
                raise ValueError("unsupported focus enclitic")
            marker = suffix
            words[-1] = host
        if any("-" in token for token in words):
            raise ValueError("focus enclitic must attach to the right edge of its nominal constituent")

        # Personal pronouns have distinct base and genitive forms, without
        # agreement with a following possessed head noun.
        if len(words) == 1 and required_case == "nominative" and words[0] in self.pronoun_to_person:
            number, person = self.pronoun_to_person[words[0]]
            result = {"kind": "pronoun", "person": person, "number": number, "form": words[0]}
            if marker:
                result["focus"] = self._focus_annotation(marker, "pronoun")
            return result
        if len(words) == 1 and required_case == "genitive" and words[0] in self.PERSONAL_GENITIVES:
            source, number, person = self.PERSONAL_GENITIVES[words[0]]
            result = {"kind": "genitive_pronoun", "person": person, "number": number,
                      "form": words[0], "source_pronoun": source, "case": "genitive"}
            if marker:
                result["focus"] = self._focus_annotation(marker, "genitive_pronoun")
            return result

        # The explicitly ratified part-whole construction is head-first:
        # part doms, kin part doms, partem umans, etc.
        if len(words) >= 2 and required_case != "genitive":
            final = words[-1]
            genitives = [a for a in self.analyze_word(final)["analyses"]
                        if a["kind"] == "nominal_case" and a["case"] == "genitive"]
            if genitives:
                if marker:
                    # doms-no at the end could focus on the possessor or
                    # the whole part phrase; no nesting rule is ratified.
                    raise ValueError("focus on postposed genitive needs explicit attachment rules")
                host = self._np(words[:-1], required_case)
                if host["kind"] != "noun_phrase" or host["lemma"] != "part" or host.get("possessor"):
                    raise ValueError("postposed genitive licensed only with part")
                whole = self._np([final], "genitive")
                host["part_whole"] = {"kind": "part_whole", "whole": whole}
                return host

        head = words[-1]
        choices = [a for a in self.analyze_word(head)["analyses"]
                   if a["kind"] == "nominal_case" and a["case"] == required_case]
        if not choices:
            raise ValueError(f"unrecognized {required_case} nominal head: {head}")
        modifiers = words[:-1]
        possessor = None
        # A complete prenominal genitive constituent is case-marked on its
        # final head. Only ONE possessor per NP in this executable subset.
        genitive_positions = [
            i for i, token in enumerate(modifiers)
            if token in self.PERSONAL_GENITIVES or any(
                a["kind"] == "nominal_case" and a["case"] == "genitive"
                for a in self.analyze_word(token)["analyses"]
            )
        ]
        if genitive_positions:
            if len(genitive_positions) != 1:
                raise ValueError("genitive attachment is ambiguous")
            i = genitive_positions[0]
            possessor = self._np(modifiers[:i + 1], "genitive")
            if possessor.get("possessor"):
                raise ValueError("nested genitives are outside the typed subset")
            modifiers = modifiers[i + 1:]
        # Quantitative restrictions on a nominal count use the very same
        # scalar grammar as all numerical values, not new noun-specific
        # words or semantic limits.  Mixed adjective/demonstrative ordering
        # is still unratified and therefore not guessed.
        if modifiers and modifiers[0] in {"sirka", "inter", "major", "minor", "ekwal", "no"}:
            numeric = self._quantitative_prefix(modifiers)
            if numeric is not None and numeric[1] == len(modifiers):
                if len(choices) != 1:
                    raise ValueError("ambiguous noun under quantitative constraint")
                return {"kind": "noun_phrase", "lemma": choices[0]["lemma"],
                        "case": required_case, "modifiers": modifiers,
                        "lexical_status": choices[0]["status"],
                        "numerical_value": None,
                        "quantitative_constraint": numeric[0]}
        factors = [self.parse_multiplicative(x) for x in modifiers]
        parsed_factors = [x for x in factors if x is not None]
        if len(parsed_factors) > 1:
            raise ValueError("more than one multiplicative factor per noun phrase")
        if parsed_factors:
            # A factor is not an explicit quantity of referents. Its mixed
            # scope with numerals and other modifiers is still unresolved.
            if len(modifiers) != 1:
                raise ValueError("NUMfol with other modifiers is outside the supported subset")
            if len(choices) != 1:
                raise ValueError(f"ambiguous nominal head {head}: {choices}")
            result = {
                "kind": "noun_phrase", "lemma": choices[0]["lemma"],
                "case": required_case, "modifiers": modifiers,
                "lexical_status": choices[0]["status"],
                "numerical_value": None,
                "multiplicative_factor": parsed_factors[0]["factor"],
            }
        else:
            # A single productive -al adjective may modify a noun.
            # Ordering/scope against quantifiers or other adjectives is not
            # defined by the current parser and therefore rejected.
            adjectives = [x for x in modifiers if self.is_derived_adjective(x)]
            if adjectives and len(modifiers) != 1:
                raise ValueError("mixed derived adjectives and other nominal modifiers are not in this subset")
            if not (len(modifiers) == len(set(modifiers)) and
                    all(x in self.demonstratives | self.quantifiers | {"wi"}
                        or self.parse_numeral(x) is not None
                        or self.parse_ordinal(x) is not None
                        or self.is_derived_adjective(x) for x in modifiers)):
                raise ValueError(f"unsupported noun modifiers: {modifiers}")
            ordinal_analyses = [self.parse_ordinal(x) for x in modifiers]
            ordinals = [x for x in ordinal_analyses if x is not None]
            if ordinals and len(modifiers) != 1:
                raise ValueError("combined ordinal modifier scope is not yet ratified")
            demonstratives = [x for x in modifiers if x in self.demonstratives]
            numerals = [x for x in modifiers if x in self.quantifiers or self.parse_numeral(x) is not None]
            if len(demonstratives) > 1 or len(numerals) > 1 or ("wi" in modifiers and numerals):
                raise ValueError("unsupported or redundant quantification")
            if demonstratives and modifiers[0] not in self.demonstratives:
                raise ValueError("demonstrative must precede quantifier/plural")
            if "wi" in modifiers and modifiers[-1] != "wi":
                raise ValueError("wi must directly precede noun in this subset")
            if len(choices) != 1:
                raise ValueError(f"ambiguous nominal head {head}: {choices}")
            parsed_cardinals = [self.parse_numeral(x) for x in numerals]
            values = [x["value"] for x in parsed_cardinals if x is not None]
            result = {
                "kind": "noun_phrase", "lemma": choices[0]["lemma"],
                "case": required_case, "modifiers": modifiers,
                "lexical_status": choices[0]["status"],
                "numerical_value": values[0] if values else None
            }
            if ordinals:
                result["ordinal_value"] = ordinals[0]["value"]
            if adjectives:
                result["relational_adjectives"] = [
                    self.parse_derivation(x) for x in adjectives
                ]
        if possessor is not None:
            result["possessor"] = {"kind": "genitive_relation", "phrase": possessor}
        if marker:
            result["focus"] = self._focus_annotation(marker, "noun_phrase")
        return result

    @staticmethod
    def _focus_annotation(marker: str, target: str) -> dict:
        return {"kind": "negative_additive_focus" if marker == "no" else "additive_focus",
                "marker": "-" + marker, "target": target,
                "scope": "entire_constituent",
                "clause_negative": marker == "no"}

    def parse_sentence(self, sentence: str) -> dict:
        """Subset: [ka] [S-NP] [no] finite-V [OBJ-NP]. Unsupported syntax fails closed."""
        raw = sentence.strip()
        question = raw.endswith("?")
        words = raw.rstrip(".?!").lower().split()
        if not words:
            raise ValueError("empty sentence")
        interrogative = words[0] == "ka"
        if interrogative:
            words = words[1:]
        if question and not interrogative:
            raise ValueError("only polar ka questions are supported")
        verbs = [(i, a) for i, word in enumerate(words) for a in self.analyze_word(word)["analyses"]
                 if a["kind"] == "finite_verb"]
        if len(verbs) != 1:
            raise ValueError("expected exactly one identifiable finite verb in supported SVO clause")
        position, verb = verbs[0]
        prefix = words[:position]
        negative = bool(prefix and prefix[-1] == "no")
        if negative:
            prefix = prefix[:-1]
        subject = self._np(prefix, "nominative") if prefix else None
        if subject and subject["kind"] == "pronoun":
            if (subject["person"], subject["number"]) != (verb["person"], verb["number"]):
                raise ValueError("pronoun disagrees with finite person/number")
        obj = self._np(words[position + 1:], "accusative") if words[position + 1:] else None
        return {"kind": "svo_clause", "interrogative": interrogative, "negative": negative,
                "subject": subject or {"kind": "pro_drop", "person": verb["person"], "number": verb["number"]},
                "predicate": verb, "object": obj,
                "limitations": "SVO reference subset; not a full semantic interpretation"}
