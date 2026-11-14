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
TEMPORAL_RELATIONS = {
    "pretem": "before", "postem": "after", "tem": "during",
    "sim": "meets", "solap": "overlaps", "simpre": "starts",
    "simpost": "finishes", "simtem": "equals",
}
TEMPORAL_OPERANDS = {"svo_clause", "servile_clause", "copular_clause"}
SUBORDINATES = {"se", "etsi", "etsise", "eksese"}
POSTPOSED = {"etsi", "etsise", "eksese"}
RELATORS = {"kun", "per", "pro", "due", "fin", "tem", "mod"}
CASES = ("accusative", "dative_allative", "ablative", "locative", "resultative")
MODALS = {"pos", "deb", "vol", "int", "pot", "tent", "sap", "adsap", "insap", "desap", "resap", "aut"}
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
        # Historical clause-initial 'due Q, P' is explicitly licensed.
        # The comma separates two finite *simple* clauses in this one
        # construction; it cannot replace lim/alor elsewhere.
        if body.lower().lstrip().startswith("due "):
            if terminal in ("?", "!") or body.count(",") != 1:
                raise ValueError("fronted finite due requires the attested simple-clause comma boundary")
            cause, effect = body.split(",", 1)
            cause_tokens = cause.strip().lower().split()[1:]
            effect_tokens = effect.strip().lower().split()
            if not cause_tokens or not effect_tokens:
                raise ValueError("fronted due requires cause and effect")
            if not any(self._finite(w) for w in cause_tokens):
                raise ValueError("fronted due NP is not a full causal proposition")
            if any(self._is_clause_connector(part, i)
                   for part in (cause_tokens, effect_tokens)
                   for i in range(len(part))):
                raise ValueError("fronted due with mixed clause coordination is not defined")
            if any(w in SUBORDINATES | {"lim", "alor", "ka"} for w in cause_tokens + effect_tokens):
                raise ValueError("fronted due does not accept nested subordinate scope")
            return {"kind": "causal_relation", "operator": "due",
                    "placement": "fronted",
                    "cause": self._atom(cause_tokens),
                    "effect": self._atom(effect_tokens)}
        # Ordinary commas are prosodic and never create lim/alor scope.
        body = body.replace(",", " ")
        words = body.lower().split()
        if not words or len(words) > MAX_TOKENS:
            raise ValueError("empty or excessively long proposition")
        if any(re.fullmatch(r"[a-z]+(?:-(?:si|no))?", token) is None for token in words):
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
        if (polar or terminal == "?") and any("-" in w for w in words):
            raise ValueError("question scope with bound focus remains outside this subset")
        if polar and (any(w in SUBORDINATES | {"lim"} for w in words)
                      or any(self._is_clause_connector(words, i)
                             for i in range(len(words)))):
            raise ValueError("question-wide connective and subordinate scope is not ratified")
        ast = self._expression(words, 0)
        is_wh = ast.get("question", {}).get("kind") == "wh"
        if (polar or terminal == "?") and ast["kind"] not in {"svo_clause", "servile_clause", "zero_copula", "copular_clause"}:
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

    def _bare_verb(self, token: str) -> bool:
        return token in self.verbs or self.is_derived_verb(token)

    def _is_clause_connector(self, words: list[str], index: int) -> bool:
        """Distinguish due + NP from due + finite causal proposition.

        A nominal due belongs to its immediately following NP; finite
        verbs after a *later* connector do not retroactively turn it
        into a clausal linker.
        """
        word = words[index]
        if word not in CONNECTORS:
            return False
        # The 'e' between two numeric endpoints belongs to 'inter A e B',
        # not to proposition coordination.  Keep later e connectors intact.
        if word == "e":
            for j in range(index):
                if words[j] != "inter":
                    continue
                parsed = self._quantitative_prefix(words, j)
                if parsed is not None and j < index < parsed[1]:
                    return False
        if word != "due":
            return True
        stop = next((i for i in range(index + 1, len(words))
                     if words[i] in CONNECTORS | SUBORDINATES | {"lim", "alor"}),
                    len(words))
        return any(self._finite(w) for w in words[index + 1:stop])

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
            return self._combine(words[i + 1], left, right, closing_lim=True)
        if len(words) >= 2 and words[:2] == ["no", "lim"]:
            operand = words[2:]
            if any("-" in w for w in operand):
                raise ValueError("focus interactions with no lim are not yet ratified")
            if not operand:
                raise ValueError("no lim requires an operand")
            if (any(w in {"alor", "se", "etsi", "etsise", "eksese"}
                    for w in operand)
                    or any(self._is_clause_connector(operand, i) and
                           operand[i] not in BOOLEAN_CONNECTORS
                           for i in range(len(operand)))):
                raise ValueError("wide negation is ratified only for e/o truth-conditional chains")
            if operand[:2] == ["no", "lim"]:
                raise ValueError("stacked wide negation not ratified")
            inner = self._expression(operand, depth + 1)
            if inner["kind"] == "temporal_relation":
                raise ValueError("wide negation of a temporal relation is not yet defined")
            return {"kind": "wide_negation", "operator": "no lim",
                    "operand": inner,
                    "scope": "complete_truth_conditional_operand"}
        # The same gradable likelihood property accepts a qualitative
        # degree or a ratified two-token CARDINAL ORDINAL numeric fraction.
        # Do not reject > 1 fractions: rhetorical hyperbole remains valid
        # syntax and arithmetic/model assessment is a separate layer.
        probability_degrees = {"minu", "pok", "ase", "mult", "ekstrem", "suf"}
        negative_lik = len(words) >= 2 and words[0] == "no" and words[1] == "lik"
        prob_index = (1 if len(words) >= 2 and words[0] in probability_degrees
                      else (1 if negative_lik else 0))
        if len(words) > prob_index and words[prob_index] == "lik":
            grade = words[0] if prob_index and not negative_lik else None
            numeric_measure = None
            operand_start = prob_index + 1
            quantitative = self._quantitative_prefix(words, operand_start)
            if quantitative is not None:
                possible_measure, end = quantitative
                # Unmarked cardinal alone may instead be the subject
                # quantifier, e.g. 'lik setdek uman movan'.
                if possible_measure["kind"] != "cardinal_numeral":
                    numeric_measure = possible_measure
                    operand_start = end
            if numeric_measure is not None and grade is not None:
                raise ValueError("combined numeric and qualitative likelihood degrees are not ratified")
            operand_words = words[operand_start:]
            if not operand_words or not any(self._finite(w) for w in operand_words):
                raise ValueError("lik requires a finite proposition")
            if any(w in SUBORDINATES | {"alor", "lim", "ka", "ma", "ergo", "nam", "due"}
                   for w in operand_words):
                raise ValueError("mixed likelihood and discourse scope not ratified")
            if operand_words[0] in {"pos", "deb", "lik"}:
                raise ValueError("nested probability or modal scope not ratified")
            operand = self._expression(operand_words, depth + 1)
            if operand["kind"] not in {"svo_clause", "servile_clause",
                                       "zero_copula", "copular_clause",
                                       "coordination", "exclusive_choice"}:
                raise ValueError("lik requires a licensed finite proposition")
            return {"kind": "propositional_degree_property",
                    "property": "lik",
                    "scale": "probability",
                    "degree": grade,
                    "negative": negative_lik,
                    "threshold_relative": grade == "suf",
                    "numeric_threshold_defined": numeric_measure is not None,
                    "operand": operand,
                    "entails_operand_truth": False,
                    "numeric_measure": numeric_measure}
        # Subject-explicit propositional serviles are bare heads with an
        # independent finite complement. No person is encoded on the head.
        # This is a bounded semantic license, not a blanket coercion of
        # all intransitive/ordinary predicates into clausal operators.
        propositional_subject_heads = {
            "vol": "desire_that",
            "int": "intention_that",
            "tent": "attempt_that",
            "sap": "knowledge_that",
            "kred": "belief_that",
        }
        # Only propositional heads carry personless tense Ø / d / f.
        # An ordinary finite lexical verb still requires person agreement.
        propositional_tenses = {"": "present", "d": "past", "f": "future"}

        def parse_head(token, licensed):
            for lemma, interpretation in licensed.items():
                for suffix, tense in propositional_tenses.items():
                    if token == lemma + suffix:
                        return lemma, interpretation, tense
            return None

        for i in range(1, min(len(words), 8)):
            parsed_head = parse_head(words[i], propositional_subject_heads)
            if parsed_head is None:
                continue
            head, interpretation, assessment_tense = parsed_head
            prefix = words[:i]
            negated = bool(prefix and prefix[-1] == "no")
            if negated:
                prefix = prefix[:-1]
            if not prefix or "no" in prefix:
                continue
            try:
                # Explicit subject, including pronouns and canonical NPs.
                # Its person is not tied to the embedded finite predicate.
                subject = self._np(prefix, "nominative")
            except ValueError:
                continue
            operand_words = words[i + 1:]
            if not operand_words or not any(self._finite(w) for w in operand_words):
                raise ValueError("subject-explicit bare servile needs a finite proposition")
            if any(w in SUBORDINATES | {"alor", "lim", "ka", "ma", "ergo", "nam", "due"}
                   for w in operand_words):
                raise ValueError("mixed subject-explicit modal scope not yet ratified")
            operand = self._expression(operand_words, depth + 1)
            if operand["kind"] not in {"svo_clause", "servile_clause",
                                       "zero_copula", "copular_clause",
                                       "coordination", "exclusive_choice"}:
                raise ValueError("unsupported embedded proposition kind")
            return {"kind": "propositional_servile",
                    "operator": head, "operator_form": ("bare_root" if assessment_tense == "present"
                                      else "personless_tensed_head"),
                    "assessment_tense": assessment_tense,
                    "embedded_tense_anchor": "relative_to_assessment",
                    "interpretation": interpretation,
                    "subject": subject, "negative": negated,
                    "operand": operand, "operand_finite": True,
                    "entails_operand_truth": head == "sap" and not negated,
                    "entails_attempt": head == "tent" and not negated,
                    "entails_intention": head == "int" and not negated}
        # Ratified shared-subject serviles are finite heads plus bare V.

        # The separate proposition-level frame is an invariant bare head
        # plus a complete *finite* proposition. Only epistemic pos is
        # semantically licensed in this parser subset; other heads need an
        # explicit, independently ratified propositional reading.
        impersonal_heads = {
            "pos": "epistemic_possibility",
            "deb": "propositional_necessity",
        }
        negated_impersonal = len(words) >= 2 and words[0] == "no"
        impersonal_index = 1 if negated_impersonal else 0
        impersonal = (parse_head(words[impersonal_index], impersonal_heads)
                      if len(words) > impersonal_index else None)
        if impersonal is not None:
            head, interpretation, assessment_tense = impersonal
            scope_words = words[impersonal_index + 1:]
            if not scope_words or not any(self._finite(w) for w in scope_words):
                raise ValueError("bare propositional servile needs a finite proposition")
            if (parse_head(scope_words[0], impersonal_heads) is not None
                    or (len(scope_words) >= 2 and scope_words[0] == "no"
                        and parse_head(scope_words[1], impersonal_heads) is not None)):
                raise ValueError("stacked bare epistemic modals are not ratified")
            if any(w in SUBORDINATES | {"alor", "lim", "ka", "ma", "ergo", "nam", "due"}
                   for w in scope_words):
                raise ValueError("bare modal with non-Boolean/mixed subordinate scope is not ratified")
            operand = self._expression(scope_words, depth + 1)
            if operand["kind"] not in {"svo_clause", "servile_clause",
                                       "zero_copula", "copular_clause",
                                       "coordination", "exclusive_choice"}:
                raise ValueError("unsupported proposition kind under bare pos")
            return {"kind": "propositional_servile",
                    "operator": head, "operator_form": ("bare_root" if assessment_tense == "present"
                                      else "personless_tensed_head"),
                    "assessment_tense": assessment_tense,
                    "embedded_tense_anchor": "relative_to_assessment",
                    "interpretation": interpretation,
                    "negative": negated_impersonal,
                    "operand": operand, "operand_finite": True,
                    "entails_operand_truth": False}
        if words[0] == "o":
            # Initial o is exactly-one, not binary XOR. All later o
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
            alternatives = [self._expression(p, depth + 1) for p in pieces]
            if any(x["kind"] in {"subordinate", "causal_relation",
                                 "evidential_relation", "inference_relation",
                                 "wide_negation"} for x in alternatives):
                raise ValueError("exclusive alternatives with subordinate or discourse scope are not settled")
            return {"kind": "exclusive_choice", "operator": "o",
                    "semantics": "exactly_one", "alternatives": alternatives}
        if "lim" in words:
            raise ValueError("bare or misplaced lim")
        # Postposed concessives/exception are distinct from ordinary
        # connectors; mixed coordination + postposition is not settled.
        post = [i for i, w in enumerate(words) if i > 0 and w in POSTPOSED]
        if post:
            if len(post) != 1 or any(self._is_clause_connector(words, j)
                                     for j in range(len(words))):
                raise ValueError("mixed postposed subordinate scope is not ratified")
            i = post[0]
            return {"kind": "subordinate", "operator": words[i],
                    "placement": "postposed",
                    "matrix": self._expression(words[:i], depth + 1),
                    "subordinate": self._expression(words[i + 1:], depth + 1)}
        # A temporal relation links exactly two independent finite event
        # clauses in this initial subset.  Nominal `tem NP` remains an
        # adjunct, not a second finite clause.  Never guess mixed scope.
        temporal = []
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word not in TEMPORAL_RELATIONS:
                continue
            # Prevent nominal `tem dia` from capturing a later finite
            # verb across an independent clause connector.
            right_end = next((j for j in range(i + 1, len(words))
                              if words[j] in CONNECTORS | SUBORDINATES | {"alor", "lim"}),
                             len(words))
            if word != "tem" or any(self._finite(w) for w in words[i + 1:right_end]):
                temporal.append(i)
        if temporal:
            if (len(temporal) != 1 or any(
                    self._is_clause_connector(words, j)
                    for j in range(len(words)))
                    or any(w in SUBORDINATES | {"alor", "lim", "ka"} for w in words)):
                raise ValueError("mixed or nested temporal scope is not defined")
            i = temporal[0]
            left = self._atom(words[:i])
            right = self._atom(words[i + 1:])
            if left["kind"] not in TEMPORAL_OPERANDS or right["kind"] not in TEMPORAL_OPERANDS:
                raise ValueError("temporal relation requires two simple finite event clauses")
            if left.get("question") or right.get("question"):
                raise ValueError("temporal questions need explicit future scoping rules")
            return {"kind": "temporal_relation", "operator": words[i],
                    "relation": TEMPORAL_RELATIONS[words[i]],
                    "left": left, "right": right,
                    "interval_semantics": "bounded_positive_duration",
                    "asserts_event_occurrence": False,
                    "limitations": "structure only; no inferred event reference, bounds or truth"}
        # Right-associative connector chains, without an implicit
        # precedence hierarchy. Distinguish nominal 'due NP' from
        # 'P due Q' by the existence of a finite clause in Q.
        for i in range(1, len(words)):
            op = words[i]
            if not self._is_clause_connector(words, i):
                continue
            left = self._expression(words[:i], depth + 1)
            right = self._expression(words[i + 1:], depth + 1)
            return self._combine(op, left, right)
        return self._atom(words)

    def _combine(self, op: str, left: dict, right: dict,
                 closing_lim: bool = False) -> dict:
        # Coordinating an explicit subordinate/cause with another connector
        # is not yet ratified. In particular a source-clause 'due'
        # is NOT an unrestricted Boolean function.
        mixed = {"subordinate", "causal_relation"}
        if left["kind"] in mixed or right["kind"] in mixed:
            raise ValueError("mixed causal/subordinate and coordination scope is not ratified")
        if right["kind"] == "wide_negation" or (
                left["kind"] == "wide_negation" and not closing_lim):
            raise ValueError("nested no lim without a closing boundary is not ratified")
        if op == "due" and (
                left["kind"] in {"coordination", "exclusive_choice",
                                  "wide_negation", "evidential_relation",
                                  "inference_relation"}
                or right["kind"] in {"coordination", "exclusive_choice",
                                     "wide_negation", "evidential_relation",
                                     "inference_relation"}):
            raise ValueError("mixed causal and connective scope is not ratified")
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
        if any(self._is_clause_connector(part, i)
               for part in (inner, main) for i in range(len(part))):
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
        if (negative and len(words) != 2) or not self._bare_verb(root):
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

    def _state_complement(self, lemma: str, words: list[str]) -> dict | None:
        """One attested predicative state, not an arbitrary verbal object.

        The overt copula es can stand alone existentially or carry a
        qualitative/nominal/local predicate. Its phase forms require an
        explicit predicate in this bounded implementation.
        """
        if not words:
            if lemma == self.valency["copula_state"]["base"]:
                return None
            raise ValueError("state-phase verb requires an explicit state predicate")
        if len(words) != 1:
            raise ValueError("copula/state phase requires exactly one simple state predicate")
        state = words[0]
        if state in self.properties or (
                (self.parse_derivation(state) or {}).get("category") == "property"):
            return {"kind": "quality_state", "lemma": state}
        if state in self.nouns or self.is_derived_noun(state):
            return {"kind": "nominal_state", "lemma": state}
        if lemma == "es":
            candidate = self._read_np(words, 0, "locative")
            if candidate is not None and candidate[1] == len(words):
                return {"kind": "locative_state", "phrase": candidate[0]}
        raise ValueError("unsupported state predicate or illegitimate nominal case")

    def _args(self, words: list[str], head: str) -> tuple[dict | None, list[dict]]:
        pos, obj, other = 0, None, []
        while pos < len(words):
            word = words[pos]
            if word in RELATORS:
                if word == "fin" and pos + 1 < len(words) and self._bare_verb(words[pos + 1]):
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
        if question is None and not any("-" in w for w in words):
            # Preserve the old AST only where the old SVO parser has a
            # licensed valency model. Strict serviles and traes must be
            # parsed structurally, not mistaken for arbitrary transitive
            # predicates with a lone nominal object.
            provisional = [a for w in words for a in self._finite(w)]
            special = {"pos", "deb", "vol", "int", "pot", "tent", "aut", "traes"}
            if not any(a["lemma"] in special or
                       self.has_documented_valency(a["lemma"])
                       for a in provisional):
                try:
                    legacy = ClauseParser.parse_sentence(self, " ".join(words))
                    frame = self.validate_valency(
                        legacy["predicate"]["lemma"], legacy.get("object"), [])
                    if frame is not None:
                        legacy["valency"] = frame
                    return legacy
                except ValueError:
                    pass
        finite = [(i, analyses) for i, word in enumerate(words)
                  if (analyses := self._finite(word))]
        if len(finite) == 0:
            if question is not None:
                raise ValueError("wh question requires a finite predicate in this subset")
            return self._annotate_focus(self._zero_copula(words))
        if len(finite) != 1 or len(finite[0][1]) != 1:
            raise ValueError("expected exactly one unambiguous finite predicate")
        idx, analyses = finite[0]
        verb = analyses[0]
        prefix = words[:idx]
        negative = bool(prefix and prefix[-1] == "no")
        if negative:
            prefix = prefix[:-1]
        if "no" in prefix:
            # A leftmost 'no minor N noun' is a quantified subject, not
            # negation of the finite verb.  Do not let any other 'no'
            # elsewhere in a subject silently change the scope.
            quantity = (self._quantitative_prefix(prefix[:-1])
                        if len(prefix) >= 4 and prefix[0] == "no"
                        and prefix[1] in {"major", "minor", "ekwal"}
                        else None)
            if quantity is None or quantity[1] != len(prefix) - 1:
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
                if upcoming and (self._bare_verb(upcoming[0]) or
                                 (len(upcoming) >= 2 and upcoming[0] == "no" and self._bare_verb(upcoming[1]))):
                    source, rest = candidate, upcoming
        neg_embedded = bool(rest and rest[0] == "no")
        if neg_embedded:
            rest = rest[1:]
        if head in MODALS and rest and self._bare_verb(rest[0]):
            if negative and neg_embedded:
                raise ValueError("stacked modal and dependent negation not ratified")
            dependent = rest[0]
            state = None
            if self.is_state_copula(dependent):
                state = self._state_complement(dependent, rest[1:])
                obj, complements = None, []
                if question is not None and question["role"] in {"object", "destination"}:
                    raise ValueError("wh argument with state predication needs separate scope rules")
            else:
                obj, complements = self._args(rest[1:], dependent)
                dependent_frame = self.validate_valency(dependent, obj, complements)
            if self.is_knowledge_verb(head):
                self.validate_knowledge_procedure(head, obj, complements)
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
            if head == "int":
                out["intention_frame"] = "committed_intention"
                out["entails_intention"] = not negative
                out["denies_intention"] = negative
                out["entails_attempt"] = False
                out["entails_performance"] = False
            if head == "tent":
                out["attempt_frame"] = "attempt_goal_directed"
                out["entails_attempt"] = not negative
                out["denies_attempt"] = negative
                out["entails_success"] = False
            if self.is_knowledge_verb(head):
                out["knowledge_frame"] = "procedural_knowledge"
                out["knowledge_phase"] = head
                out["entails_performance"] = False
            if self.is_state_copula(dependent):
                out["dependent"]["state"] = state
                out["dependent"]["valency"] = (
                    self.valency["copula_state"]["frame_ids"][dependent]
                    if state is not None else "existential_copula")
            elif dependent_frame is not None:
                out["dependent"]["valency"] = dependent_frame
                if dependent_frame == self.valency["force_manner"]["frame"]:
                    out["dependent"]["entails_successful_displacement"] = False
                physical_roles = self.physical_argument_roles(dependent, complements)
                if physical_roles is not None:
                    out["dependent"]["argument_roles"] = physical_roles
            if question:
                out["question"] = question
        else:
            if neg_embedded:
                raise ValueError("dependent no requires a finite servile head")
            if source is not None or (head in MODALS and not self.is_knowledge_verb(head)):
                raise ValueError("servile requires a bare verbal complement")
            if self.is_state_copula(head):
                state = self._state_complement(head, rest)
                if question is not None and question["role"] in {"object", "destination"}:
                    raise ValueError("wh object/destination with state predication is not resolved")
                copula = {"kind": "copular_clause", "predicate": verb,
                          "subject": subject, "negative": negative,
                          "interrogative": question is not None,
                          "state": state,
                          "valency": (self.valency["copula_state"]["frame_ids"][head]
                                      if state is not None else "existential_copula")}
                if front is not None:
                    copula["preposed_locative"] = front
                if question is not None:
                    copula["question"] = question
                return self._annotate_focus(copula)
            obj, complements = self._args(rest, head)
            frame = self.validate_valency(head, obj, complements)
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
                if frame == self.valency["force_manner"]["frame"]:
                    out["entails_successful_displacement"] = False
                physical_roles = self.physical_argument_roles(head, complements)
                if physical_roles is not None:
                    out["argument_roles"] = physical_roles
        if front is not None:
            out["preposed_locative"] = front
        return self._annotate_focus(out)

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
        first = prefix[0].split("-", 1)[0]
        subject = self._subject(prefix, 3 if first in self.demonstratives else
                                self.pronoun_to_person.get(first, ("singular", 3))[1],
                                self.pronoun_to_person.get(first, ("singular", 3))[0])
        return {"kind": "zero_copula", "subject": subject,
                "predicate": {"lemma": predicate,
                              "status": "confirmed_lexicon" if lexical else "productive_from_confirmed"},
                "negative": negative, "interrogative": False}

    def _annotate_focus(self, ast: dict) -> dict:
        """Attach one overt NP focus; do not conflate -no and local no."""
        sites = []

        def check(np: dict | None, role: str) -> None:
            if isinstance(np, dict) and np.get("focus"):
                sites.append((role, np["focus"]))

        check(ast.get("subject"), "subject")
        check(ast.get("object"), "object")
        check(ast.get("source"), "permission_source")
        if ast.get("preposed_locative"):
            front = ast["preposed_locative"].get("phrase")
            if isinstance(front, dict) and front.get("focus"):
                raise ValueError("focus on unresolved fronted domain has no licensed attachment")
        for node in ast.get("complements", []):
            check(node.get("nominal"), "complement")
        if ast.get("kind") == "servile_clause":
            dependent = ast["dependent"]
            check(dependent.get("object"), "dependent_object")
            for node in dependent.get("complements", []):
                check(node.get("nominal"), "dependent_complement")
        if len(sites) > 1:
            raise ValueError("multiple focal constituents need explicit scope rules")
        if not sites:
            return ast
        role, focus = sites[0]
        if ast.get("kind") == "servile_clause":
            raise ValueError("focus with servile scope needs a separate ratification")
        if focus["clause_negative"]:
            if ast.get("negative"):
                raise ValueError("focus -no already carries negative polarity; no stacking")
            ast["negative"] = True
            ast["negation_type"] = "negative_additive_focus"
        ast["focus"] = {"kind": focus["kind"], "marker": focus["marker"],
                        "scope": "entire_constituent", "target_role": role}
        return ast
