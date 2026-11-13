"""Unisermo Phase 1 reference parser/word methods. No guesswork outside the accepted subset."""
from __future__ import annotations

class WordParser:
    def analyze_word(self, surface: str) -> dict:
        if not isinstance(surface, str) or not surface.isascii() or surface != surface.lower():
            return {"surface": surface, "analyses": []}
        if "-" in surface:
            # A bound focus enclitic is a single hyphenated surface token.
            # The whole nominal constituent's scope is identified in _np,
            # NOT by analysing its final word in isolation.
            host, separator, suffix = surface.rpartition("-")
            if (separator != "-" or suffix not in {"si", "no"} or not host
                    or "-" in host or not host.isalpha()):
                return {"surface": surface, "analyses": []}
            host_analyses = self.analyze_word(host)["analyses"]
            if (host not in self.pronoun_to_person and
                    not any(a["kind"] in {"nominal_case", "genitive_pronoun"}
                            for a in host_analyses)):
                return {"surface": surface, "analyses": []}
            status = (self.lexicon[host]["status"] if host in self.lexicon else
                      next((a["status"] for a in host_analyses if a["kind"] in
                            {"nominal_case", "genitive_pronoun"}), "canonical_by_rule"))
            return {"surface": surface, "analyses": [{
                "kind": "focus_enclitic", "lemma": host, "status": status,
                "suffix": suffix, "focus": "negative_additive" if suffix == "no" else "additive"
            }]}
        if not surface.isalpha() or not set(surface) <= set(self.morph["alphabet"]):
            return {"surface": surface, "analyses": []}
        out: list[dict] = []
        if surface in self.PERSONAL_GENITIVES:
            source, number, person = self.PERSONAL_GENITIVES[surface]
            out.append({"kind": "genitive_pronoun", "lemma": source,
                        "status": "canonical_by_rule", "case": "genitive",
                        "person": person, "number": number})

        for lemma, entry in self.lexicon.items():
            if surface == lemma:
                out.append({"kind": "lexical_form", "lemma": lemma, "status": entry["status"],
                            "category": "/".join(entry["categories"])})
        finite = self.morph["finite"]
        for lemma in sorted(self.verbs):
            for aspect, a in finite["aspect"].items():
                for tense, t in finite["tense"].items():
                    for person, p in finite["person"].items():
                        for number, n in finite["number"].items():
                            if surface == lemma + a + t + p + n:
                                out.append({"kind": "finite_verb", "lemma": lemma, "status": self.lexicon[lemma]["status"],
                                            "tense": tense, "aspect": aspect, "person": int(person), "number": number})
        for lemma in sorted(self.verbs):
            if surface == self.generate_participle(lemma):
                out.append({"kind": "participle", "lemma": lemma, "status": self.lexicon[lemma]["status"]})
        nominal_stems = self.nouns | {self.generate_participle(lemma) for lemma in self.verbs}
        for lemma in sorted(nominal_stems):
            for case in self.morph["nominal"]["case"]:
                if surface == self.generate_noun(lemma, case):
                    source_lemma = lemma[:-2] if lemma.endswith("it") and lemma[:-2] in self.verbs else lemma
                    out.append({"kind": "nominal_case", "lemma": lemma, "status": self.lexicon[source_lemma]["status"],
                                "case": case, "suffix": self.genitive_suffix(lemma) if case == "genitive" else self.morph["nominal"]["case"][case]})
        # One productive derivation per lemma; original lexical analyses
        # retain priority and do not get silently reinterpreted by endings.
        derived = self.parse_derivation(surface)
        if derived is not None:
            if derived["category"] == "adjective":
                out.append({"kind": "derived_adjective", "lemma": surface,
                            "status": derived["status"], "derivation": derived})
            elif derived["category"] == "property":
                out.append({"kind": "derived_property", "lemma": surface,
                            "status": derived["status"], "derivation": derived})
            else:
                out.append({"kind": "productive_derivation", "lemma": surface,
                            "status": derived["status"], "derivation": derived})
        out.extend(self.finite_derived_analyses(surface))
        out.extend(self.nominal_derived_analyses(surface))

        # Participial -it is inflection of an event root; it follows a
        # productive phase prefix but is not a second lexical derivation.
        if surface.endswith("it"):
            event_lemma = surface[:-2]
            event = self.parse_derivation(event_lemma)
            if event is not None and event["category"] == "verb":
                out.append({"kind": "participle", "lemma": event_lemma,
                            "status": event["status"], "derivation": event})
                out.append({"kind": "nominal_case", "lemma": surface,
                            "status": event["status"], "case": "nominative",
                            "suffix": "", "derivation": event})
        for case, suffix in self.morph["nominal"]["case"].items():
            if case == "nominative":
                continue
            for ending in ((suffix, self.morph["nominal"]["genitive_alternate"])
                           if case == "genitive" else (suffix,)):
                if not surface.endswith(ending) or len(surface) <= len(ending):
                    continue
                stem = surface[:-len(ending)]
                if not stem.endswith("it"):
                    continue
                event = self.parse_derivation(stem[:-2])
                if event is None or event["category"] != "verb":
                    continue
                expected = self.genitive_suffix(stem) if case == "genitive" else suffix
                if ending == expected:
                    out.append({"kind": "nominal_case", "lemma": stem,
                                "status": event["status"], "case": case,
                                "suffix": ending, "derivation": event})
        # Surface-transparent genealogical compounds are licensed by the
        # confirmed relation inventory, even if their *whole* lemma is not
        # explicitly indexed. Keep the structural path separate from lexical
        # status; an unlisted but valid compound is productive, not a new root.
        kinship = self.parse_kinship(surface)
        if kinship is not None:
            out.append(kinship)
            if surface not in self.nouns:
                out.append({
                    "kind": "nominal_case", "lemma": surface,
                    "status": "productive_from_confirmed",
                    "case": "nominative", "suffix": "",
                    "kinship": kinship,
                })
        for case, suffix in self.morph["nominal"]["case"].items():
            if case == "nominative":
                continue
            # The alternate genitive form -es is root-dependent: do not
            # accept it indiscriminately when the nominal ends in a vowel.
            if case == "genitive":
                suffixes = {suffix, self.morph["nominal"]["genitive_alternate"]}
            else:
                suffixes = {suffix}
            for ending in suffixes:
                if not surface.endswith(ending) or len(surface) <= len(ending):
                    continue
                stem = surface[:-len(ending)]
                if stem in self.nouns:
                    continue  # Existing nominal loop already owns this case.
                parsed = self.parse_kinship(stem)
                if parsed is None:
                    continue
                proper = (self.genitive_suffix(stem) if case == "genitive"
                          else self.morph["nominal"]["case"][case])
                if proper != ending:
                    continue
                out.append({
                    "kind": "nominal_case", "lemma": stem,
                    "status": "productive_from_confirmed",
                    "case": case, "suffix": ending, "kinship": parsed,
                })
        cardinal = self.parse_numeral(surface)
        if cardinal is not None:
            out.append({"kind": "cardinal_numeral", "lemma": surface,
                        "status": cardinal["status"], "value": cardinal["value"]})
        ordinal = self.parse_ordinal(surface)
        if ordinal is not None:
            out.append({"kind": "ordinal_numeral", "lemma": surface,
                        "status": ordinal["status"], "value": ordinal["value"], "canonical_form": ordinal["canonical_form"]})
        iteration = self.parse_iteration(surface)
        if iteration is not None:
            out.append({"kind": "iteration_counter", "lemma": surface,
                        "status": iteration["status"], "count": iteration["count"]})
        multiple = self.parse_multiplicative(surface)
        if multiple is not None:
            out.append({"kind": "multiplicative_factor", "lemma": surface,
                        "status": multiple["status"], "factor": multiple["factor"]})
        return {"surface": surface, "analyses": out}

