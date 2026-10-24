"""No-network checks for the Tally draft form payload."""
import json
import unittest

from benchmarks.tally_pretest import SPEC, build


class TallyPretestTests(unittest.TestCase):
    def test_no_answer_keys_and_no_contact_fields(self):
        spec=json.loads(SPEC.read_text(encoding="utf-8"))
        self.assertEqual(len(spec["items"]),6)
        self.assertEqual(len({item["id"] for item in spec["items"]}),6)
        payload=build(spec)
        self.assertEqual(payload["status"],"DRAFT")
        self.assertEqual(payload["blocks"][0]["type"],"FORM_TITLE")
        self.assertEqual(sum(b["type"]=="TEXTAREA" for b in payload["blocks"]),6)
        self.assertEqual(sum(b["type"]=="LINEAR_SCALE" for b in payload["blocks"]),6)
        self.assertFalse(any(b["type"] in ("INPUT_EMAIL","INPUT_PHONE_NUMBER") for b in payload["blocks"]))
        for field in payload["blocks"]:
            text=json.dumps(field).lower()
            self.assertNotIn("translation_key",text)
            self.assertNotIn("correct_answer",text)

    def test_fixed_fields_and_range(self):
        spec=json.loads(SPEC.read_text(encoding="utf-8"))
        payload=build(spec)
        ids={x["id"] for x in spec["items"]}
        self.assertEqual({b["payload"]["name"].removeprefix("meaning_")
                          for b in payload["blocks"] if b["type"]=="TEXTAREA"},ids)
        self.assertEqual({b["payload"]["name"].removeprefix("confidence_")
                          for b in payload["blocks"] if b["type"]=="LINEAR_SCALE"},ids)
        for b in payload["blocks"]:
            self.assertIn("uuid",b)
            self.assertIn("groupUuid",b)
            if b["type"]=="LINEAR_SCALE":
                self.assertEqual((b["payload"]["start"],b["payload"]["end"]),(1,5))


if __name__=="__main__":
    unittest.main()
