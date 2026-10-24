"""Post-hoc retrospective diagnosis of the ORIGINAL relational-role model replies.

These exploratory metrics do not replace the preregistered strict results in
PR #12 and are not a new trial. Run offline, preserving raw responses.
"""
from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path

from benchmarks.relational_frame_meaning import decode, normalize
from formalization.core import Unisermo

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "benchmarks/evidence/relational-frame-2026-10-24-run40089793501.jsonl"
CORPUS = ROOT / "benchmarks/corpus/relational-frames-dev-001.jsonl"


def retrospective(raw_path=RAW, corpus_path=CORPUS):
    corpus = [json.loads(line) for line in corpus_path.read_text(encoding="utf8").splitlines() if line.strip()]
    records = [json.loads(line) for line in raw_path.read_text(encoding="utf8").splitlines() if line.strip()]
    if len(corpus) != 12 or len(records) != 24:
        raise ValueError("unexpected source corpus / original response count")
    index = {(x["doc"], x["condition"]): x for x in records}
    if len(index) != 24:
        raise ValueError("duplicate original response")
    language = Unisermo()
    table = {}
    for condition in ("cold", "guided"):
        families = defaultdict(lambda: {"events": 0, "end_value_recognized_any_of_destination_result": 0,
                                        "canonical_end_slot_correct": 0,
                                        "end_value_put_in_wrong_slot": 0,
                                        "spurious_source_state": 0,
                                        "inferred_extra_patient": 0})
        for doc in corpus:
            reply = index[(doc["id"], condition)]
            events, error = decode(reply.get("answer"))
            if error:
                raise ValueError("original response has changed shape")
            for sentence, event in zip(doc["clauses"], events, strict=True):
                gold = normalize(sentence, language)
                if not isinstance(event, dict):
                    raise ValueError("invalid original event type")
                family = doc["family"]
                count = families[family]
                count["events"] += 1
                endpoint = gold["destination"] if gold["destination"] is not None else gold["result_state"]
                assert endpoint is not None
                in_destination = event.get("destination") == endpoint
                in_result = event.get("result_state") == endpoint
                count["end_value_recognized_any_of_destination_result"] += int(in_destination or in_result)
                expected_end_field = "destination" if gold["destination"] is not None else "result_state"
                other_end_field = "result_state" if expected_end_field == "destination" else "destination"
                expected_found = event.get(expected_end_field) == endpoint
                other_absent = event.get(other_end_field) is None
                count["canonical_end_slot_correct"] += int(expected_found and other_absent)
                count["end_value_put_in_wrong_slot"] += int(
                    event.get(expected_end_field) is None and event.get(other_end_field) == endpoint)
                count["spurious_source_state"] += int(
                    gold["source_state"] is None and event.get("source_state") is not None)
                count["inferred_extra_patient"] += int(
                    gold["patient"] is None and event.get("patient") is not None)
        table[condition] = dict(families)
    return {
        "schema": "unisermo/relational-frame-retrospective-diagnosis@1",
        "status": "EXPLORATORY_POST_HOC_NOT_PRE_REGISTERED",
        "old_raw_path": str(raw_path.relative_to(ROOT)) if raw_path.is_relative_to(ROOT) else str(raw_path),
        "old_corpus_path": str(corpus_path.relative_to(ROOT)) if corpus_path.is_relative_to(ROOT) else str(corpus_path),
        "outcomes": table,
        "caveats": "Finding an endpoint in either slot is weaker than correct case, frame, argument structure or semantic interpretation. Never promote to original primary metric or independent human validation."
    }


if __name__ == "__main__":
    print(json.dumps(retrospective(),indent=2,ensure_ascii=False))
