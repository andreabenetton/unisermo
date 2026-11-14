"""Bounded productive morphology from the accepted Unisermo derivation spec.

A derived form is built from a **known base and one licensed operation**.
The right edge alone is never proof of derivation: lexical entries win,
major/minor remain indivisible, and phase/modal extensions not supported
by the normative grammar fail closed. No generated word is silently
inserted into the confirmed lexicon.

Sources: language/derivation.md and language/verb_specification.md.
"""
from __future__ import annotations


class DerivationParser:
    # Form -> syntactic role, semantic derivation. A generated *adjective*
    # cannot automatically become a nominal head or finite verb.
    DERIVATIONAL_SUFFIXES = {
        "itat": ("noun", "abstract_quality"),
        "or": ("noun", "agent"),
        "il": ("noun", "instrument"),
        "ia": ("noun", "domain_place"),
        "al": ("adjective", "relational_adjective"),
        "abil": ("adjective", "passive_potential"),
    }
    PHASE_PREFIXES = {
        "in": "continue", "ad": "begin", "de": "cease", "re": "resume"
    }
    MODAL_HEADS = {"pos", "deb", "vol", "pot", "aut"}
    # No property lacking a determined opposite is automatically prefixed.
    OPPOSABLE_PROPERTIES = {"bon", "bel", "prob", "just", "legal", "fas", "apt"}

    def parse_derivation(self, lemma: str) -> dict | None:
        """Return one unambiguous productive analysis, or None.

        Lexicalized forms always retain their own lexical sense.
        A single suffix or a single approved prefix is supported;
        productive chaining awaits explicit collision and scope rules.
        """
        if not isinstance(lemma, str) or not lemma.isascii() or not lemma.isalpha():
            return None
        if lemma in self.lexicon or not set(lemma) <= set(self.morph["alphabet"]):
            return None
        candidates = []
        for ending, (category, operation) in self.DERIVATIONAL_SUFFIXES.items():
            if not lemma.endswith(ending) or len(lemma) <= len(ending):
                continue
            base = lemma[:-len(ending)]
            if ending == "itat":
                allowed = base in self.properties or base == "uman"
            elif ending == "abil":
                # A passive potential presupposes an affected patient.
                # Only explicitly identified eligible roots are enabled here;
                # untyped verbs and modals must not silently acquire one.
                allowed = base in {"mov", "vid", "dik", "fak", "portar"} and base in self.verbs
            else:
                allowed = base in self.verbs and base not in self.MODAL_HEADS
            if allowed:
                candidates.append((base, category, ending, operation, "suffix"))
        for prefix, operation in self.PHASE_PREFIXES.items():
            if lemma.startswith(prefix):
                base = lemma[len(prefix):]
                if base in self.verbs and base not in self.MODAL_HEADS:
                    candidates.append((base, "verb", prefix, "phase_" + operation, "prefix"))
        if lemma.startswith("kun"):
            base = lemma[3:]
            # kunten is already a lexicalized containment root, not
            # transparent kun + ten. A further kunkunten is an
            # unratified double associative construction, not a
            # productive joint-containment verb in this parser subset.
            if (base in self.verbs and base not in self.MODAL_HEADS
                    and base != "kunten"):
                candidates.append((base, "verb", "kun", "joint_event", "prefix"))
        if lemma.startswith("ne"):
            base = lemma[2:]
            if base in self.OPPOSABLE_PROPERTIES and base in self.properties:
                candidates.append((base, "property", "ne", "semantic_antonym", "prefix"))
        # Multiple analyses are not arbitrarily disambiguated by affix
        # length or order; a lexical decision must resolve collisions.
        if len(candidates) != 1:
            return None
        base, category, affix, operation, position = candidates[0]
        parent = self.lexicon[base]
        approved = parent["status"] == "confirmed_lexicon"
        return {
            "kind": "productive_derivation",
            "lemma": lemma,
            "base": base,
            "category": category,
            "affix": affix,
            "affix_position": position,
            "operation": operation,
            "status": "productive_from_confirmed" if approved else "productive_from_attested",
            "base_status": parent["status"],
        }

    def derived_category(self, lemma: str) -> str | None:
        parsed = self.parse_derivation(lemma)
        return parsed["category"] if parsed is not None else None

    def is_derived_verb(self, lemma: str) -> bool:
        return self.derived_category(lemma) == "verb"

    def is_derived_noun(self, lemma: str) -> bool:
        return self.derived_category(lemma) == "noun"

    def is_derived_adjective(self, lemma: str) -> bool:
        return self.derived_category(lemma) == "adjective"

    def finite_derived_analyses(self, surface: str) -> list[dict]:
        """Decode the inflection of a single productive verbal lemma."""
        out = []
        features = self.morph["finite"]
        for aspect, asp in features["aspect"].items():
            for tense, tmp in features["tense"].items():
                for person, pv in features["person"].items():
                    for number, nv in features["number"].items():
                        ending = asp + tmp + pv + nv
                        if not surface.endswith(ending):
                            continue
                        lemma = surface[:-len(ending)]
                        derived = self.parse_derivation(lemma)
                        if derived is None or derived["category"] != "verb":
                            continue
                        out.append({
                            "kind": "finite_verb", "lemma": lemma,
                            "status": derived["status"], "derivation": derived,
                            "aspect": aspect, "tense": tense,
                            "person": int(person), "number": number,
                        })
        return out

    def nominal_derived_analyses(self, surface: str) -> list[dict]:
        """Decode case after a derived nominal stem (not before it)."""
        out = []
        cases = self.morph["nominal"]["case"]
        for case, suffix in cases.items():
            endings = (suffix, self.morph["nominal"]["genitive_alternate"]) if case == "genitive" else (suffix,)
            for ending in endings:
                if ending and not surface.endswith(ending):
                    continue
                stem = surface[:-len(ending)] if ending else surface
                derived = self.parse_derivation(stem)
                if derived is None or derived["category"] != "noun":
                    continue
                expected = self.genitive_suffix(stem) if case == "genitive" else suffix
                if ending != expected:
                    continue
                out.append({
                    "kind": "nominal_case", "lemma": stem, "status": derived["status"],
                    "case": case, "suffix": ending, "derivation": derived,
                })
        return out
