import json
import unittest
from pathlib import Path

from benchmarks.root_family_collisions import analyze, possible_family

ROOT = Path(__file__).resolve().parents[1]
MORPH = json.loads((ROOT / "formalization/data/morphology.json").read_text())
LEXICON = json.loads((ROOT / "formalization/data/lexicon_index.json").read_text())["entries"]


class FamilyCollisionTests(unittest.TestCase):
    def test_generator_uses_all_54_inflections(self):
        words = possible_family("dir", MORPH)
        self.assertIn("diri", words)
        self.assertIn("dirodi", words)
        self.assertIn("dirit", words)
        self.assertGreater(len(words), 54)

    def test_existing_dik_merges_with_tik(self):
        observed = analyze("dik", "dik", MORPH, LEXICON)
        self.assertTrue(any(x["candidate_form"] == "dik" and
                            x["other_form"] == "tik"
                            for x in observed["accent_merge_risks"]))

    def test_dir_does_not_merge_with_tik(self):
        observed = analyze("dir", "dik", MORPH, LEXICON)
        self.assertFalse(any(x["other_form"] == "tik"
                             for x in observed["accent_merge_risks"]))
        self.assertEqual(observed["status"], "mechanical_overgeneration_not_human_validated")

    def test_invalid_spelling_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "noncanonical"):
            analyze("constru", "stru", MORPH, LEXICON)

    def test_derived_homographs_are_detected(self):
        fake = [{"form": "testor", "status": "confirmed_lexicon",
                 "categories": ["noun"]}]
        result = analyze("test", "other", MORPH, fake)
        self.assertTrue(any(x["candidate_form"] == "testor"
                            for x in result["exact_collisions"]))


if __name__ == "__main__":
    unittest.main()
