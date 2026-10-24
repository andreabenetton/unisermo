"""Lock in original, explicitly post-hoc endpoint / case-role diagnostics."""
import unittest
from benchmarks.relational_frame_diagnostics import retrospective


class OriginalEndpointAuditTests(unittest.TestCase):
    def test_retrospective_from_unchanged_raw_qwen_answers(self):
        x = retrospective()
        self.assertEqual(x["status"], "EXPLORATORY_POST_HOC_NOT_PRE_REGISTERED")
        for condition in ("cold","guided"):
            for family in ("move","transition","cause_result"):
                self.assertEqual(x["outcomes"][condition][family]["events"],8)
        cold = x["outcomes"]["cold"]
        guided = x["outcomes"]["guided"]
        self.assertEqual(cold["transition"]["end_value_recognized_any_of_destination_result"],8)
        self.assertEqual(guided["transition"]["end_value_recognized_any_of_destination_result"],7)
        self.assertEqual(cold["transition"]["end_value_put_in_wrong_slot"],8)
        self.assertEqual(guided["transition"]["end_value_put_in_wrong_slot"],7)
        self.assertEqual(cold["cause_result"]["spurious_source_state"],6)
        self.assertEqual(guided["cause_result"]["spurious_source_state"],4)
        self.assertEqual(cold["cause_result"]["end_value_recognized_any_of_destination_result"],8)
        self.assertEqual(guided["cause_result"]["end_value_recognized_any_of_destination_result"],8)

if __name__=="__main__":
    unittest.main()
