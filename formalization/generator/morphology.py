"""Unisermo Phase 1 reference generator methods. No guesswork outside the accepted subset."""
from __future__ import annotations

class MorphologyGenerator:
    def check_lemma(self, lemma: str, domain: str) -> None:
        if lemma not in (self.verbs if domain == "verb" else self.nouns):
            raise ValueError(f"unsupported {domain} lemma: {lemma!r}; documentary attestations are not automatically canonical")

    def generate_verb(self, lemma: str, tense: str = "present", aspect: str = "simple",
                      person: int = 1, number: str = "singular") -> str:
        self.check_lemma(lemma, "verb")
        finite = self.morph["finite"]
        try:
            return (lemma + finite["aspect"][aspect] + finite["tense"][tense]
                    + finite["person"][str(person)] + finite["number"][number])
        except KeyError as exc:
            raise ValueError(f"unsupported verbal feature: {exc}") from exc

    def genitive_suffix(self, lemma: str) -> str:
        nominal = self.morph["nominal"]
        return (nominal["genitive_alternate"] if any(lemma.endswith(edge) for edge in
                 nominal["genitive_alternate_after"]) else nominal["case"]["genitive"])

    def generate_noun(self, lemma: str, case: str = "nominative") -> str:
        if lemma.endswith("it") and lemma[:-2] in self.verbs:
            # Nominalized resultatives are licensed in the live verb specification.
            pass
        else:
            self.check_lemma(lemma, "noun")
        cases = self.morph["nominal"]["case"]
        if case not in cases:
            raise ValueError(f"unsupported nominal case: {case}")
        ending = self.genitive_suffix(lemma) if case == "genitive" else cases[case]
        return lemma + ending

    def generate_participle(self, lemma: str) -> str:
        self.check_lemma(lemma, "verb")
        return lemma + self.morph["non_finite"]["participle_resultative"]

