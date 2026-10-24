"""No-API tests for constrained Unisermo proposition-meaning pilot."""
import json
import unittest

from formalization.core import Unisermo
from benchmarks.proposition_meaning import (
    CORPUS, FIELDS, GUIDE, MAX_OBSERVED_COST_USD, MAX_REQUESTS, build_questions,
    decode, load_corpus, meaning, score,
)


class MeaningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_all_24_complete_propositions_parse(self):
        corpus=load_corpus()
        self.assertEqual(len(corpus),12)
        self.assertEqual(sum(len(r["clauses"]) for r in corpus),24)
        self.assertEqual(len(set(clause for r in corpus for clause in r["clauses"])),24)
        for row in corpus:
            for clause in row["clauses"]:
                gold=meaning(clause,self.lang)
                self.assertEqual(set(gold),set(FIELDS))
                self.assertEqual(gold["agent_number"] in ("singular","plural"),True)

    def test_structural_semantic_contrasts(self):
        self.assertEqual(meaning("i vidi domem.",self.lang)["agent"],"speaker")
        self.assertEqual(meaning("u vidu domem.",self.lang)["agent"],"listener")
        self.assertEqual(meaning("i vidi tik wi domem.",self.lang)["patient_quantity"],"explicit_plural")
        self.assertEqual(meaning("i vidi tik wi domem.",self.lang)["patient_deixis"],"speaker_near")
        self.assertEqual(meaning("i vidi ter domem.",self.lang)["patient_quantity"],"three")
        self.assertEqual(meaning("i vidi omni umanem.",self.lang)["patient_quantity"],"all_members")
        self.assertEqual(meaning("i vidi nul umanem.",self.lang)["patient_quantity"],"zero")
        self.assertEqual(meaning("i peldi akwaem.",self.lang)["tense"],"past")
        self.assertEqual(meaning("in movefin domem.",self.lang)["aspect"],"progressive")
        self.assertEqual(meaning("in movefin domem.",self.lang)["tense"],"future")
        self.assertEqual(meaning("un trakodun aerplanem.",self.lang)["aspect"],"perfect")
        self.assertEqual(meaning("ka i no viddi ter domem?",self.lang)["speech_act"],"polar_question")
        self.assertEqual(meaning("ka i no viddi ter domem?",self.lang)["polarity"],"negative")

    def test_rejects_unsupported_frames_and_referents(self):
        for text in ("a vida domem.", "i vidi domde.", "i vidi dom.", "uman vidan domem.",
                     "i vidi ter wi domem.", "i vidi domem. u vidu domem."):
            with self.subTest(text=text), self.assertRaises(ValueError):
                meaning(text,self.lang)

    def test_prompt_and_cost_constraints(self):
        corpus=load_corpus()
        requests=build_questions(corpus)
        self.assertEqual(len(requests),MAX_REQUESTS)
        self.assertLess(MAX_OBSERVED_COST_USD,0.03)
        for row in corpus:
            pair=[x for x in requests if x["doc"]==row["id"]]
            self.assertEqual({x["condition"] for x in pair},{"cold","guided"})
            for q in pair:
                self.assertTrue(all(c in q["messages"][0]["content"] for c in row["clauses"]))
                self.assertNotIn("expected_events",q["messages"][0]["content"])
            self.assertNotIn(GUIDE,next(q for q in pair if q["condition"]=="cold")["messages"][0]["content"])

    def test_scoring_and_format_failure(self):
        corpus=load_corpus()
        result=[]
        for q in build_questions(corpus):
            doc=next(r for r in corpus if r["id"]==q["doc"])
            events=[meaning(s,self.lang) for s in doc["clauses"]]
            result.append({
                "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                "prompt_sha256":q["prompt_sha256"],
                "answer":json.dumps({"events":events}),
                "usage":{"prompt_tokens":100,"completion_tokens":150,"total_tokens":250,"cost":0.0001}
            })
        scored=score(result,corpus)
        self.assertEqual(scored["conditions"]["cold"]["exact_propositions"],24)
        self.assertEqual(scored["conditions"]["guided"]["exact_propositions"],24)
        self.assertEqual(len(scored["paired_documents"]),12)
        result[0]["answer"]='{"events":[{}]}'
        scored=score(result,corpus)
        self.assertEqual(sum(v["exact_propositions"] for v in scored["conditions"].values()),46)
        with self.assertRaises(ValueError): score(result[:-1],corpus)
        result[0]["prompt_sha256"]="altered"
        with self.assertRaises(ValueError): score(result,corpus)

    def test_bool_and_extra_fields_not_valid(self):
        x=meaning("i vidi domem.",self.lang)
        self.assertNotIn("referent_id",x)
        self.assertIsNotNone(decode('{"events":[]}')[1])
        self.assertIsNotNone(decode('not-json')[1])


if __name__=="__main__":
    unittest.main()
