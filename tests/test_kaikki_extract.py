import gzip
import json
import tempfile
import unittest
from pathlib import Path

from benchmarks.kaikki_extract import latin_key, extract


class KaikkiExtractorTests(unittest.TestCase):
    def test_macron_normalization(self):
        self.assertEqual(latin_key("dīcō"), "dico")
        self.assertEqual(latin_key("strūō"), "struo")

    def test_extracts_only_matching_latin(self):
        entries = [
            {"lang_code": "la", "word": "dīcō", "pos": "verb",
             "sounds": [{"ipa": "/diːkoː/"}], "senses": [{"glosses": ["say"]}]},
            {"lang_code": "it", "word": "dico", "pos": "verb"},
            {"lang_code": "la", "word": "centrum", "pos": "noun", "senses": []},
            {"lang_code": "la", "word": "irrelevant", "pos": "noun"},
        ]
        data = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in entries).encode()
        with tempfile.TemporaryDirectory() as tmp:
            plain = Path(tmp) / "source.jsonl"
            zipped = Path(tmp) / "source.jsonl.gz"
            plain.write_bytes(data)
            with gzip.open(zipped, "wb") as f:
                f.write(data)
            url = "https://kaikki.org/dictionary/rawdata.html"
            a = extract(plain, {"dico", "centrum"}, url)
            b = extract(zipped, {"dico", "centrum"}, url)
            self.assertEqual(a, b)
            self.assertEqual(len(a["entries"]), 2)
            self.assertEqual(a["missing_latin_keys"], [])
            self.assertEqual(a["entries"][0]["source_ipa"], ["/diːkoː/"])
            self.assertNotIn("glosses", a["entries"][0])

    def test_incomplete_subset_is_explicit(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "data.jsonl"
            source.write_text('{"lang_code":"la","word":"cura"}\n')
            report = extract(source, {"cura", "struo"}, "https://kaikki.org/dictionary/rawdata.html")
            self.assertEqual(report["missing_latin_keys"], ["struo"])
            self.assertEqual(report["status"], "incomplete")

    def test_untraceable_source_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "data.jsonl"
            source.write_text("")
            with self.assertRaisesRegex(ValueError, "Kaikki"):
                extract(source, {"centrum"}, "https://example.com/data")


if __name__ == "__main__":
    unittest.main()
