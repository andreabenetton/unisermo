"""The ratified interval relations and conservative finite-clause parser."""

import unittest

from formalization.core import Unisermo
from formalization.semantics.intervals import allen_relation


# A and B are bounded positive-duration intervals.  The 13 cases are
# deliberately exhaustive; the second field is the user-ratified connective
# with its semantic operands in the natural order.
CASES = [
    ("before", (0, 2), (4, 6), "pretem", False),
    ("meets", (0, 3), (3, 6), "sim", False),
    ("overlaps", (0, 4), (2, 6), "solap", False),
    ("starts", (0, 3), (0, 6), "simpre", False),
    ("during", (2, 4), (0, 6), "tem", False),
    ("finishes", (3, 6), (0, 6), "simpost", False),
    ("equals", (0, 6), (0, 6), "simtem", False),
    ("finished_by", (0, 6), (3, 6), "simpost", True),
    ("contains", (0, 6), (2, 4), "tem", True),
    ("started_by", (0, 6), (0, 3), "simpre", True),
    ("overlapped_by", (2, 6), (0, 4), "solap", True),
    ("met_by", (3, 6), (0, 3), "sim", True),
    ("after", (4, 6), (0, 2), "postem", False),
]

INVERSES = {
    "before": "after", "after": "before",
    "meets": "met_by", "met_by": "meets",
    "overlaps": "overlapped_by", "overlapped_by": "overlaps",
    "starts": "started_by", "started_by": "starts",
    "during": "contains", "contains": "during",
    "finishes": "finished_by", "finished_by": "finishes",
    "equals": "equals",
}


class IntervalSemanticsTests(unittest.TestCase):
    def test_all_13_analytically_distinct(self):
        self.assertEqual(len(CASES), 13)
        self.assertEqual(len({case[0] for case in CASES}), 13)
        for name, a, b, _, _ in CASES:
            with self.subTest(relation=name):
                self.assertEqual(allen_relation(*a, *b), name)
                self.assertEqual(allen_relation(*b, *a), INVERSES[name])

    def test_strict_containment_excludes_shared_endpoints(self):
        self.assertEqual(allen_relation(2, 4, 0, 6), "during")
        self.assertEqual(allen_relation(0, 4, 0, 6), "starts")
        self.assertEqual(allen_relation(2, 6, 0, 6), "finishes")

    def test_zero_duration_and_incomparable_endpoints_fail_closed(self):
        for bad in [(0, 0, 1, 2), (3, 2, 1, 4), (0, 1, 2, 2),
                    (0, 1, "a", "b")]:
            with self.subTest(intervals=bad), self.assertRaises(ValueError):
                allen_relation(*bad)


class TemporalPropositionParserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Unisermo()

    def test_eight_temporal_connectives_preserve_both_clauses(self):
        for operator, relation in (
            ("pretem", "before"), ("postem", "after"),
            ("sim", "meets"), ("solap", "overlaps"),
            ("simpre", "starts"), ("simpost", "finishes"),
            ("tem", "during"), ("simtem", "equals"),
        ):
            with self.subTest(operator=operator):
                ast = self.parser.parse_proposition(f"vidi {operator} movi")
                self.assertEqual(ast["kind"], "temporal_relation")
                self.assertEqual(ast["operator"], operator)
                self.assertEqual(ast["relation"], relation)
                self.assertEqual(ast["left"]["predicate"]["lemma"], "vid")
                self.assertEqual(ast["right"]["predicate"]["lemma"], "mov")
                self.assertFalse(ast["asserts_event_occurrence"])
                self.assertEqual(ast["interval_semantics"],
                                 "bounded_positive_duration")

    def test_converse_mappings_parse_as_distinct_argument_order(self):
        for name, _, _, operator, reverse in CASES:
            with self.subTest(relation=name):
                sentence = (f"movi {operator} vidi" if reverse
                            else f"vidi {operator} movi")
                ast = self.parser.parse_proposition(sentence)
                self.assertEqual(ast["operator"], operator)
                self.assertEqual(ast["left"]["predicate"]["lemma"],
                                 "mov" if reverse else "vid")
                self.assertEqual(ast["right"]["predicate"]["lemma"],
                                 "vid" if reverse else "mov")

    def test_immediate_before_and_after_preserve_strict_direction(self):
        for op, rel in (("pretem", "before"), ("postem", "after")):
            with self.subTest(operator=op):
                ast = self.parser.parse_proposition(f"vidi imedi {op} movi")
                self.assertEqual(ast["kind"], "temporal_relation")
                self.assertEqual(ast["operator"], op)
                self.assertEqual(ast["relation"], rel)
                self.assertEqual(ast["proximity"], "contextually_immediate")
                self.assertEqual(ast["proximity_marker"], "imedi")
                self.assertEqual(ast["left"]["predicate"]["lemma"], "vid")
                self.assertEqual(ast["right"]["predicate"]["lemma"], "mov")
                self.assertIsNone(self.parser.parse_proposition(f"vidi {op} movi")["proximity"])

    def test_imedi_does_not_become_sim_or_free_adverb(self):
        for invalid in (
            "vidi imedi sim movi", "vidi imedi tem movi",
            "vidi imedi solap movi", "vidi imedi simtem movi",
            "vidi imedi simpre movi", "vidi imedi simpost movi",
            "vidi postem imedi movi", "imedi vidi postem movi",
            "vidi imedi imedi postem movi", "vidi imedi",
            "vidi imedi postem movi e faki",
            "vidi e faki imedi pretem movi",
        ):
            with self.subTest(sentence=invalid), self.assertRaises(ValueError):
                self.parser.parse_proposition(invalid)

    def test_instan_is_a_noun_not_a_zero_length_allen_interval(self):
        self.assertIn("instan", self.parser.nouns)
        clause = self.parser.parse_proposition("vidi instanem")
        self.assertEqual(clause["object"]["lemma"], "instan")
        with self.assertRaises(ValueError):
            allen_relation(1, 1, 1, 2)

    def test_nominal_tem_stays_nominal(self):
        # Supported event nominalization must remain an ordinary complement,
        # even when followed by an independent e coordination.
        for sentence in ("faki tem fakit", "faki tem fakit e movi"):
            with self.subTest(sentence=sentence):
                ast = self.parser.parse_proposition(sentence)
                self.assertNotEqual(ast["kind"], "temporal_relation")

    def test_mixed_connective_scope_rejected(self):
        for sentence in (
            "vidi sim movi e faki",
            "vidi e movi sim faki",
            "vidi sim movi sim faki",
            "vidi tem movi o faki",
            "vidi se movi sim faki",
            "vidi lim sim movi",
            "no lim vidi sim movi",
            "vidi sim",
            "sim movi",
            "vidi sim dom",
            "ka vidi sim movi?",
            "vidi sim movi?",
        ):
            with self.subTest(sentence=sentence), self.assertRaises(ValueError):
                self.parser.parse_proposition(sentence)


if __name__ == "__main__":
    unittest.main()
