"""UCUB-001 safety, corpus and offline protocol checks."""
import json
import unittest
from pathlib import Path

from benchmarks.ucub001.build import GROUPS, build, render
from benchmarks.ucub001.runner import load_corpus, prompt, select, parse_label, parse_label_with_format, score


class UCUB001Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.manifest = load_corpus()

    def test_frozen_corpus_regeneration(self):
        corpus, manifest = render()
        root = Path(__file__).resolve().parents[1] / "benchmarks" / "ucub001"
        self.assertEqual((root / "corpus.jsonl").read_text(encoding="utf-8"), corpus)
        self.assertEqual((root / "manifest.json").read_text(encoding="utf-8"), manifest)
        self.assertEqual(build(), self.rows)

    def test_balanced_levels_and_group_safe_holdout(self):
        self.assertEqual(len(self.rows), 80)
        self.assertEqual(len(GROUPS), 20)
        for level in ("L1", "L2", "L3", "L4"):
            self.assertEqual(sum(r["level"] == level for r in self.rows), 20)
        self.assertEqual(len(select(self.rows, "development", None)), 64)
        self.assertEqual(len(select(self.rows, "holdout", None)), 16)
        self.assertEqual(self.manifest["holdout_group_ids"], ["G05","G10","G15","G20"])
        dev_groups = {r["group"] for r in select(self.rows, "development", None)}
        hold_groups = {r["group"] for r in select(self.rows, "holdout", None)}
        self.assertFalse(dev_groups & hold_groups)

    def test_independent_gold_not_parser_output(self):
        for row in self.rows:
            self.assertEqual(row["semantic_review"], "author_draft_pending_independent_review")
            self.assertIn(row["gold"], ("entailed","contradicted","undetermined"))
            self.assertNotIn("gold", prompt(row, "cold"))
            for arm in ("cold","lexicon","grammar","english"):
                text = prompt(row, arm)["messages"][0]["content"]
                self.assertNotIn("author_draft_pending_independent_review", text)
                self.assertNotIn('"gold"', text)
            cold = prompt(row, "cold")["messages"][0]["content"]
            self.assertNotIn("Unisermo dictionary:", cold)
            self.assertNotIn("Unisermo grammar:", cold)
            self.assertIn(row["english"], prompt(row, "english")["messages"][0]["content"])
            self.assertIn("Unisermo dictionary:", prompt(row, "lexicon")["messages"][0]["content"])
            self.assertIn("Unisermo grammar:", prompt(row, "grammar")["messages"][0]["content"])

    def test_markdown_fence_is_separately_scored_not_silently_accepted_as_raw_json(self):
        fenced = '```json\\n{"label": "entailed"}\\n```'
        self.assertIsNone(parse_label(fenced))
        self.assertEqual(parse_label_with_format(fenced), ("entailed", "fenced_json"))
        self.assertEqual(parse_label_with_format('{"label": "entailed"}'), ("entailed", "raw_json"))
        self.assertEqual(parse_label_with_format("entailed"), (None, "invalid"))
        self.assertEqual(parse_label_with_format('Answer: {"label":"entailed"}'), (None, "invalid"))
        self.assertEqual(parse_label_with_format('```json\\n{"label": "entailed", "other": 1}\\n```'), (None, "invalid"))
        self.assertEqual(parse_label_with_format('```json\\n{"label": "entailed"}\\n``` trailing'), (None, "invalid"))
        self.assertEqual(parse_label_with_format('```json\\n{"label": "entailed"}\\n```\\n```json\\n{"label": "contradicted"}\\n```'), (None, "invalid"))
        chosen = select(self.rows, "development", 4)
        predictions = [
            {"id": r["id"], "condition": "cold",
             "answer": "```json\\n" + json.dumps({"label": r["gold"]}) + "\\n```",
             "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
            for r in chosen
        ]
        report = score(predictions, chosen)
        self.assertEqual(report["schema"], "unisermo/ucub001-score@2")
        self.assertEqual(report["correct"], 4)
        self.assertEqual(report["accuracy"], 1.0)
        self.assertEqual(report["raw_json_compliant"], 0)
        self.assertEqual(report["raw_json_compliance_rate"], 0.0)
        self.assertEqual(report["strict_invalid_outputs"], 4)
        self.assertEqual(report["fenced_json_outputs"], 4)
        self.assertEqual(report["invalid_outputs"], 0)
        self.assertEqual(report["strict_contract_correct"], 0)
        self.assertEqual([x["output_format"] for x in report["items"]],
                         ["fenced_json"] * 4)
        predictions[0]["answer"] = "garbage"
        changed = score(predictions, chosen)
        self.assertEqual(changed["correct"], 3)
        self.assertEqual(changed["fenced_json_outputs"], 3)
        self.assertEqual(changed["invalid_outputs"], 1)

    def test_strict_invalid_output_scoring(self):
        self.assertEqual(parse_label('{"label":"entailed"}'), "entailed")
        self.assertIsNone(parse_label("entailed"))
        self.assertIsNone(parse_label('{"label":"entailed","extra":1}'))
        self.assertIsNone(parse_label('{"label":"not determined"}'))
        chosen = select(self.rows, "development", 4)
        predictions = [
            {"id":r["id"], "condition":"cold", "answer":json.dumps({"label":r["gold"]}),
             "usage":{"prompt_tokens":10, "completion_tokens":2}}
            for r in chosen
        ]
        report = score(predictions, chosen)
        self.assertEqual(report["count"],4)
        self.assertEqual(report["accuracy"],1.0)
        self.assertEqual(report["usage_totals"]["prompt_tokens"],40)
        predictions[0]["answer"] = "garbage"
        report = score(predictions,chosen)
        self.assertEqual(report["invalid_outputs"],1)
        self.assertEqual(report["correct"],3)
        with self.assertRaises(ValueError):
            score(predictions[:2],chosen)
        with self.assertRaises(ValueError):
            score(predictions+[predictions[0]],chosen)
        with self.assertRaises(ValueError):
            score([{**predictions[0],"condition":"grammar"}]+predictions[1:], chosen)


if __name__ == "__main__":
    unittest.main()
