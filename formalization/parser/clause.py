"""Unisermo Phase 1 reference parser/clause methods. No guesswork outside the accepted subset."""
from __future__ import annotations

class ClauseParser:
    def _np(self, words: list[str], required_case: str) -> dict:
        if not words:
            raise ValueError("empty noun phrase")
        if len(words) == 1 and required_case == "nominative" and words[0] in self.pronoun_to_person:
            number, person = self.pronoun_to_person[words[0]]
            return {"kind": "pronoun", "person": person, "number": number, "form": words[0]}
        head = words[-1]
        choices = [a for a in self.analyze_word(head)["analyses"]
                   if a["kind"] == "nominal_case" and a["case"] == required_case]
        if not choices:
            raise ValueError(f"unrecognized {required_case} nominal head: {head}")
        modifiers = words[:-1]
        if not (len(modifiers) == len(set(modifiers)) and
                all(x in self.demonstratives | self.quantifiers | {"wi"} or self.parse_numeral(x) is not None or self.parse_ordinal(x) is not None for x in modifiers)):
            raise ValueError(f"unsupported noun modifiers: {modifiers}")
        ordinal_analyses = [self.parse_ordinal(x) for x in modifiers]
        ordinals = [x for x in ordinal_analyses if x is not None]
        # Mixed ordinal + other modifiers needs its own ratified scope/order rule.
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
        result = {"kind": "noun_phrase", "lemma": choices[0]["lemma"], "case": required_case, "modifiers": modifiers,
                  "lexical_status": choices[0]["status"], "numerical_value": values[0] if values else None}
        if ordinals:
            result["ordinal_value"] = ordinals[0]["value"]
        return result

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
