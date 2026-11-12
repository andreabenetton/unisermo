"""Typed, deterministic parser for the ratified core proposition grammar.

Preserves the Phase 1 SVO AST for plain sentences. Extended nodes retain
operator identity and constituent attachment; they are not truth evaluators.
Unsupported mixed scopes, uncontrolled recursion and ambiguous attachments
must never acquire guessed interpretations.

Normative sources: language/word_order.md, language/negation.md,
language/verb_specification.md, language/noun_case_system.md,
language/questions.md, language/copula.md. See formalization/GRAMMAR_COVERAGE.md.
"""
from __future__ import annotations

import re

from .clause import ClauseParser

CONNECTORS = {"e", "o", "ma", "ergo", "nam", "due"}
BOOLEAN_CONNECTORS = {"e", "o"}
SUBORDINATES = {"se", "etsi", "etsise", "eksese"}
POSTPOSED = {"etsi", "etsise", "eksese"}
RELATORS = {"kun", "per", "pro", "due", "fin", "tem", "mod"}
CASES = ("accusative", "dative_allative", "ablative", "locative", "resultative")
MODALS = {"pos", "deb", "vol", "pot", "sap", "aut"}
WH_WORDS = {
    "kis": "subject", "kidem": "object", "kidad": "destination",
    "kid": "unmarked_thing", "kos": "location", "kud": "origin",
    "kan": "time", "kom": "manner", "ker": "reason",
    "kot": "quantity", "kal": "kind",
}
MAX_TOKENS = 128
MAX_DEPTH = 16


class PropositionParser:
    """Public `parse_sentence` maintains Phase 1 shape where applicable."""

    def parse_sentence(self, sentence: str) -> dict:
        return self.parse_proposition(sentence)

    def parse_proposition(self, sentence: str) -> dict:
        if not isinstance(sentence, str):
            raise ValueError("sentence must be text")
        raw = sentence.strip()
        if not raw:
            raise ValueError("empty sentence")
        terminal = raw[-1] if raw[-1] in ".?!" else ""
        body = raw[:-1] if terminal else raw
        # A comma is prosodic; it never closes grammatical scope.
        body = body.replace(",", " ")
        words = body.lower().split()
        if not words or len(words) > MAX_TOKENS:
            raise ValueError("empty or excessively long proposition")
        if any(re.fullmatch(r"[a-z]+", token) is None for token in words):
            raise ValueError("unsupported spelling or punctuation in proposition")
        if "ka" in words[1:]:
            raise ValueError("polar marker ka is licensed only clause-initially")
        polar = words[0] == "ka"
        if polar:
            words = words[1:]
        if not words:
            raise ValueError("question lacks proposition")
        if terminal == "!":
            if polar:
                raise ValueError("imperative cannot also be a polar question")
            return self._imperative(words)
        if polar and any(w in SUBORDINATES | CONNECTORS | {"lim"} for w in words):
            raise ValueError("question-wide connective and subordinate scope is not ratified")
        ast = self._expression(words, 0)
        is_wh = ast.get("question", {}).get("kind") == "wh"
        if (polar or terminal == "?") and ast["kind"] not in {"svo_clause", "servile_clause", "zero_copula"}:
            raise ValueError("compound question scope is not ratified")
        if terminal == "?" and not polar and not is_wh:
            raise ValueError("content question requires a canonical wh word; polar question requires ka")
        if polar and is_wh:
            raise ValueError("do not combine ka with a wh question")
        if polar:
            ast["interrogative"] = True
            ast["question"] = {"kind": "polar", "marker": "ka"}
        if terminal == "?" and is_wh:
            ast["interrogative"] = True
        return ast

    def _finite(self, token: str) -> list[dict]:
        return [x for x in self.analyze_word(token)["analyses"] if x["kind"] == "finite_verb"]

    def _expression(self, words: list[str], depth: int) -> dict:
        if depth >= MAX_DEPTH or not words:
            raise ValueError("empty or excessively nested proposition")
        if words[0] in SUBORDINATES:
            return self._anteposed(words, depth)
        # The rightmost closing lim has outermost scope. 'no lim' is an
        # *opening* marker and is deliberately not counted as closing.
        closed = [i for i, tok in enumerate(words)
                  if tok == "lim" and (i == 0 or words[i - 1] != "no")]
        if closed:
            for i in closed:
                if i == 0 or i + 1 >= len(words) or words[i + 1] not in CONNECTORS:
                    raise ValueError("closing lim must precede a connective")
            i = closed[-1]
            left = self._expression(words[:i], depth + 1)
            right = self._expression(words[i + 2:], depth + 1)
            return self._combine(words[i + 1], left, right)
        if len(words) >= 2 and words[:2] == ["no", "lim"]:
            operand = words[2:]
            if not operand:
                raise ValueError("no lim requires an operand")
            if any(w in {"ma", "ergo", "nam", "due", "alor", "se",
                         "etsi", "etsise", "eksese"} for w in operand):
                raise ValueError("wide negation is ratified only for e/o truth-conditional chains")
            if operand[:2] == ["no", "lim"]:
                raise ValueError("stacked wide negation not ratified")
            return {"kind": "wide_negation", "operator": "no lim",
                    "operand": self._expression(operand, depth + 1),
                    "scope": "complete_truth_conditional_operand"}
        if words[0] == "o":
            # Initial o is exactly-one, not binary parity XOR. All later o
            # tokens in this licensed flat group separate alternatives.
            splits = [i for i in range(1, len(words)) if words[i] == "o"]
            if not splits:
                raise ValueError("exclusive o needs at least two alternatives")
            pieces = [words[1:splits[0]]]
            pieces.extend(words[splits[j] + 1:splits[j + 1]]
                          for j in range(len(splits) - 1))
            pieces.append(words[splits[-1] + 1:])
            if any(not p for p in pieces):
                raise ValueError("exclusive o needs nonempty alternatives")
            return {"kind": "exclusive_choice", "operator": "o",
                    "semantics": "exactly_one",
                    "alternatives": [self._expression(p, depth + 1) for p in pieces]}
        if "lim" in words:
            raise ValueError("bare or misplaced lim")
        # Postposed concessives/exception are distinct from ordinary
        # connectors; mixed coordination + postposition is not settled.
        post = [i for i, w in enumerate(words) if i > 0 and w in POSTPOSED]
        if post:
            if len(post) != 1 or any(w in CONNECTORS for w in words):
                raise ValueError("mixed postposed subordinate scope is not ratified")
            i = post[0]
            return {"kind": "subordinate", "operator": words[i],
                    "placement": "postposed",
                    "matrix": self._expression(words[:i], depth + 1),
                    "subordinate": self._expression(words[i + 1:], depth + 1)}
        # Right-associative connector chains, without an implicit
        # precedence hierarchy. Distinguish nominal 'due NP' from
        # 'P due Q' by the existence of a finite clause in Q.
        for i in range(1, len(words)):
            op = words[i]
            if op not in CONNECTORS:
                continue
            if op == "due" and not any(self._finite(w) for w in words[i + 1:]):
                continue
            left = self._expression(words[:i], depth + 1)
            right = self._expression(words[i + 1:], depth + 1)
            return self._combine(op, left, right)
        return self._atom(words)

    def _combine(self, op: str, left: dict, right: dict) -> dict:
        if op == "due":
            return {"kind": "causal_relation", "operator": "due",
                    "effect": left, "cause": right}
        if op == "nam":
            return {"kind": "evidential_relation", "operator": "nam",
                    "claim": left, "reason": right,
                    "causal_implication": False}
        if op == "ergo":
            return {"kind": "inference_relation", "operator": "ergo",
                    "premise": left, "conclusion": right}
        return {"kind": "coordination", "operator": op,
                "relation": {"e": "and", "o": "inclusive_or", "ma": "adversative"}[op],
                "left": left, "right": right}

    def _anteposed(self, words: list[str], depth: int) -> dict:
        nesting = 0
        match = None
        for i, w in enumerate(words):
            if w in SUBORDINATES:
                nesting += 1
            elif w == "alor":
                nesting -= 1
                if nesting < 0:
                    raise ValueError("unpaired alor")
                if nesting == 0:
                    match = i
                    break
        if match is None or match < 2 or match == len(words) - 1:
            raise ValueError("anteposed subordinate requires paired alor")
        inner = words[1:match]
        main = words[match + 1:]
        # Mixed connective/subordinate scoping is explicitly still open;
        # fully recursive subordinate chains are approved.
        if any(w in CONNECTORS for w in inner + main):
            raise ValueError("mixed subordinate and coordination scope is not ratified")
        return {"kind": "subordinate", "operator": words[0],
                "placement": "anteposed",
                "subordinate": self._expression(inner, depth + 1),
                "matrix": self._expression(main, depth + 1)}

    def _imperative(self, words: list[str]) -> dict:
        if len(words) not in (1, 2):
            raise ValueError("this subset supports a single imperative root")
        negative = words[0] == "no"
        root = words[1] if negative and len(words) == 2 else words[0]
        if (negative and len(words) != 2) or root not in self.verbs:
            raise ValueError("imperative requires a licensed bare verb")
        return {"kind": "imperative", "verb": root, "negative": negative}

    def _wh_prefix(self, words: list[str]) -> tuple[list[str], dict | None]:
        if not words or words[0] not in WH_WORDS:
            return words, None
        form, role = words[0], WH_WORDS[words[0]]
        if role in ("quantity", "kind"):
            if len(words) < 2:
                raise ValueError("kot/kal require a following noun")
            noun = words[1]
            if noun not in self.nouns:
                raise ValueError("unknown quantified/kind noun")
            return words[2:], {"kind": "wh", "form": form,
                               "role": role, "nominal_head": noun}
        return words[1:], {"kind": "wh", "form": form, "role": role}

    def _subject(self, tokens: list[str], person: int, number: str) -> dict:
        if not tokens:
            return {"kind": "pro_drop", "person": person, "number": number}
        if len(tokens) == 1 and tokens[0] in self.demonstratives:
            if person != 3:
                raise ValueError("demonstrative subject requires third person")
            return {"kind": "demonstrative_pronoun", "form": tokens[0]}
        subject = self._np(tokens, "nominative")
        if subject["kind"] == "pronoun" and (subject["person"], subject["number"]) != (person, number):
            raise ValueError("subject/finite agreement mismatch")
        return subject

    def _front(self, prefix: list[str], person: int, number: str) -> tuple[dict, dict | None]:
        """Return subject and an *unresolved* preposed locative attachment."""
        if not prefix:
            return self._subject([], person, number), None
        try:
            return self._subject(prefix, person, number), None
        except ValueError:
            pass
        for i in range(1, len(prefix) + 1):
            try:
                front = self._np(prefix[:i], "locative")
                subj = self._subject(prefix[i:], person, number)
                return subj, {"kind": "preposed_locative",
                              "phrase": front, "attachment": "undetermined",
                              "note": "fronting alone never proves proposition-domain scope"}
            except ValueError:
                continue
        raise ValueError("unsupported prenominal subject or locative fronting")

    def _read_np(self, words: list[str], offset: int, case: str) -> tuple[dict, int] | None:
        # Longest licensed NP: modifiers precede one case-bearing head.
        valid = []
        for end in range(offset + 1, min(len(words), offset + 7) + 1):
            candidate = words[offset:end]
            try:
                np = self._np(candidate, case)
                valid.append((np, end))
            except ValueError:
                if case == "resultative" and len(candidate) == 1:
                    name = candidate[0]
                    if name.endswith("da") and name[:-2] in self.properties:
                        valid.append(({"kind": "property_result",
                                      "lemma": name[:-2], "case": "resultative"}, end))
        return valid[-1] if valid else None

    def _args(self, words: list[str], head: str) -> tuple[dict | None, list[dict]]:
        pos, obj, other = 0, None, []
        while pos < len(words):
            word = words[pos]
            if word in RELATORS:
                if word == "fin" and pos + 1 < len(words) and words[pos + 1] in self.verbs:
                    purpose = words[pos + 1]
                    subobj, extras = self._args(words[pos + 2:], purpose)
                    if extras:
                        raise ValueError("complex purpose adjunct requires separate valency rules")
                    other.append({"kind": "purpose_infinitive", "relator": "fin",
                                  "verb": purpose, "object": subobj})
                    return obj, other
                nominal = self._read_np(words, pos + 1, "nominative")
                if nominal is None:
                    raise ValueError("relator requires an uninflected nominal phrase")
                np, end = nominal
                other.append({"kind": "relator", "relator": word, "nominal": np})
                pos = end
                continue
            candidates = [(case, found) for case in CASES
                          if (found := self._read_np(words, pos, case)) is not None]
            if not candidates:
                raise ValueError("unsupported argument or unknown word: " + word)
            maxend = max(found[1] for _, found in candidates)
            best = [(case, found) for case, found in candidates if found[1] == maxend]
            if len(best) != 1:
                raise ValueError("ambiguous case assignment")
            case, (np, pos) = best[0]
            if case == "accusative":
                if obj is not None:
                    raise ValueError("multiple accusative objects require another valency rule")
                obj = np
            else:
                if case == "resultative" and head != "traes":
                    raise ValueError("transformative result case requires a licensed frame")
                other.append({"kind": "case_complement", "case": case, "nominal": np})
        return obj, other

    def _atom(self, words: list[str]) -> dict:
        if not words:
            raise ValueError("empty proposition")
        if any(w in SUBORDINATES | {"alor", "lim", "ka"} for w in words):
            raise ValueError("unpaired subordinate or scope marker")
        original, question = self._wh_prefix(words)
        if question is not None:
            words = original
        if not words:
            raise ValueError("question lacks a predicate")
        if question is None:
            # Preserve the old AST only where the old SVO parser has a
            # licensed valency model. Strict serviles and traes must be
            # parsed structurally, not mistaken for arbitrary transitive
            # predicates with a lone nominal object.
            provisional = [a for w in words for a in self._finite(w)]
            special = {"pos", "deb", "vol", "pot", "aut", "traes"}
            if not any(a["lemma"] in special for a in provisional):
                try:
                    return ClauseParser.parse_sentence(self, " ".join(words))
                except ValueError:
                    pass
        finite = [(i, analyses) for i, word in enumerate(words)
                  if (analyses := self._finite(word))]
        if len(finite) == 0:
            if question is not None:
                raise ValueError("wh question requires a finite predicate in this subset")
            return self._zero_copula(words)
        if len(finite) != 1 or len(finite[0][1]) != 1:
            raise ValueError("expected exactly one unambiguous finite predicate")
        idx, analyses = finite[0]
        verb = analyses[0]
        prefix = words[:idx]
        negative = bool(prefix and prefix[-1] == "no")
        if negative:
            prefix = prefix[:-1]
        if "no" in prefix:
            raise ValueError("ambiguous or repeated local negation")
        if question is not None and question["role"] == "subject":
            if prefix or verb["person"] != 3 or verb["number"] != "singular":
                raise ValueError("wh subject must agree with third singular")
            subject, front = {"kind": "wh_subject", "form": question["form"]}, None
        else:
            subject, front = self._front(prefix, verb["person"], verb["number"])
        rest = words[idx + 1:]
        head = verb["lemma"]
        source = None
        if head == "aut" and rest:
            source_read = self._read_np(rest, 0, "ablative")
            if source_read is not None:
                candidate, end = source_read
                upcoming = rest[end:]
                if upcoming and (upcoming[0] in self.verbs or
                                 (len(upcoming) >= 2 and upcoming[0] == "no" and upcoming[1] in self.verbs)):
                    source, rest = candidate, upcoming
        neg_embedded = bool(rest and rest[0] == "no")
        if neg_embedded:
            rest = rest[1:]
        if head in MODALS and rest and rest[0] in self.verbs:
            if negative and neg_embedded:
                raise ValueError("stacked modal and dependent negation not ratified")
            dependent = rest[0]
            obj, complements = self._args(rest[1:], dependent)
            if question is not None and question["role"] in {"object", "destination"}:
                if question["role"] == "object" and obj is not None:
                    raise ValueError("wh object duplicates explicit object")
                if question["role"] == "destination" and any(x.get("case") == "dative_allative" for x in complements):
                    raise ValueError("wh destination duplicates explicit destination")
            out = {"kind": "servile_clause", "head": verb,
                   "modal": head, "negative": negative,
                   "source": source, "subject": subject,
                   "dependent": {"kind": "bare_infinitive", "lemma": dependent,
                                 "negative": neg_embedded, "object": obj,
                                 "complements": complements},
                   "interrogative": question is not None}
            if question:
                out["question"] = question
        else:
            if neg_embedded:
                raise ValueError("dependent no requires a finite servile head")
            if source is not None or (head in MODALS and head != "sap"):
                raise ValueError("servile requires a bare verbal complement")
            obj, complements = self._args(rest, head)
            frame = None
            if head == "traes":
                cases = [c["case"] for c in complements
                         if c["kind"] == "case_complement"]
                if obj is None:
                    if sorted(cases) != ["ablative", "dative_allative"] or len(complements) != 2:
                        raise ValueError("traes transition requires DEST-ad and SOURCE-de")
                    frame = "state_transition"
                else:
                    if cases != ["resultative"] or len(complements) != 1:
                        raise ValueError("causative traes requires OBJ-em and RESULT-da")
                    frame = "causative_transformation"
            if question is not None and question["role"] in {"object", "destination"}:
                if question["role"] == "object" and obj is not None:
                    raise ValueError("wh object duplicates explicit object")
                if question["role"] == "destination" and any(x.get("case") == "dative_allative" for x in complements):
                    raise ValueError("wh destination duplicates explicit destination")
            out = {"kind": "svo_clause", "predicate": verb,
                   "negative": negative, "subject": subject,
                   "object": obj, "complements": complements,
                   "interrogative": question is not None,
                   "limitations": "typed deterministic subset, not referent or truth evaluation"}
            if question:
                out["question"] = question
            if frame is not None:
                out["valency"] = frame
        if front is not None:
            out["preposed_locative"] = front
        return out

    def _zero_copula(self, words: list[str]) -> dict:
        predicate = words[-1]
        lexical = predicate in self.properties
        productive_antonym = (predicate.startswith("ne") and
                             predicate[2:] in self.properties)
        if not (lexical or productive_antonym):
            raise ValueError("unsupported zero-copula predicate")
        prefix = words[:-1]
        negative = bool(prefix and prefix[-1] == "no")
        if negative:
            prefix = prefix[:-1]
        if not prefix or "no" in prefix:
            raise ValueError("zero copula requires an explicit subject in this subset")
        subject = self._subject(prefix, 3 if prefix[0] in self.demonstratives else
                                self.pronoun_to_person.get(prefix[0], ("singular", 3))[1],
                                self.pronoun_to_person.get(prefix[0], ("singular", 3))[0])
        return {"kind": "zero_copula", "subject": subject,
                "predicate": {"lemma": predicate,
                              "status": "confirmed_lexicon" if lexical else "productive_from_confirmed"},
                "negative": negative, "interrogative": False}
