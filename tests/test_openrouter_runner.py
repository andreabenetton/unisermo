import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from benchmarks.openrouter_runner import invoke, run, MODELS


class FakeResponse:
    def __enter__(self):
        return io.BytesIO(json.dumps({
            "id": "test-response", "model": "qwen/qwen3-32b",
            "choices": [{"message": {"content": "A"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 20, "completion_tokens": 1, "total_tokens": 21},
        }).encode())
    def __exit__(self, *args):
        return False


class OpenRouterRunnerTests(unittest.TestCase):
    def test_isolated_single_message_and_routing(self):
        question = {"id": "R001", "messages": [{"role": "user", "content": "Test?"}]}
        payloads = []
        def intercept(request, timeout):
            obj = json.loads(request.data)
            payloads.append(obj)
            self.assertEqual(timeout, 75)
            self.assertEqual(len(obj["messages"]), 1)
            self.assertEqual(obj["provider"]["order"], ["deepinfra"])
            self.assertEqual(obj["provider"]["only"], ["deepinfra"])
            self.assertFalse(obj["provider"]["allow_fallbacks"])
            self.assertEqual(obj["provider"]["data_collection"], "deny")
            self.assertFalse(obj["stream"])
            self.assertEqual(obj["max_tokens"], 48)
            return FakeResponse()
        with patch("benchmarks.openrouter_runner.urllib.request.urlopen", side_effect=intercept):
            result = invoke("fake-test-only", MODELS["qwen"], question, "deepinfra")
        self.assertEqual(result["answer"], "A")
        self.assertEqual(result["usage"]["total_tokens"], 21)
        self.assertEqual(len(payloads), 1)

    def test_missing_token_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "missing"):
                run("", MODELS["qwen"], None, "smoke", 6, Path(tmp)/"data.jsonl")

    def test_unknown_model_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "Only approved"):
                run("fake", "unknown/model", None, "smoke", 6, Path(tmp)/"data.jsonl")

    def test_insufficient_cap_refused_before_api_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "requires 54"):
                run("fake", MODELS["qwen"], None, "development", 6, Path(tmp)/"data.jsonl")

    def test_smoke_writes_six_actual_response_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/"responses.jsonl"
            with patch("benchmarks.openrouter_runner.invoke",
                       side_effect=lambda key, model, q, provider: {
                           "id": q["id"], "answer": "A", "usage": {"total_tokens": 2}}), \
                 patch("benchmarks.openrouter_runner.time.sleep"):
                run("fake", MODELS["gemma"], None, "smoke", 6, path)
            rows = [json.loads(x) for x in path.read_text().splitlines()]
            self.assertEqual(len(rows), 6)
            self.assertFalse(path.with_suffix(".score.json").exists())

    def test_existing_result_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"responses.jsonl"
            path.write_text("old")
            with self.assertRaisesRegex(ValueError, "overwrite"):
                run("fake", MODELS["qwen"], None, "smoke", 6, path)


if __name__ == "__main__":
    unittest.main()
