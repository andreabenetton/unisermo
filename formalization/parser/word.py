"""Unisermo Phase 1 reference parser/word methods. No guesswork outside the accepted subset."""
from __future__ import annotations

class WordParser:
    def analyze_word(self, surface: str) -> dict:
        if not surface.isascii() or not surface.isalpha() or surface != surface.lower() or not set(surface) <= set(self.morph["alphabet"]):
            return {"surface": surface, "analyses": []}
        out: list[dict] = []
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
        return {"surface": surface, "analyses": out}

