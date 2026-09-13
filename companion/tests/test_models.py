import unittest
from src.games import MAX_ROUNDS, PRESET_PATHS, GameState, one_shot_benchmark, preset_results, run_path, step


class AdaptiveTaxGameTests(unittest.TestCase):
    def test_expected_preset_outputs(self):
        results = preset_results()
        self.assertEqual((results["transparent_cooperation"]["taxpayer_payoff"], results["transparent_cooperation"]["authority_payoff"], results["transparent_cooperation"]["final_trust"]), (24, 24, 100))
        self.assertEqual((results["opaque_breakdown"]["taxpayer_payoff"], results["opaque_breakdown"]["authority_payoff"], results["opaque_breakdown"]["final_trust"]), (7, 11, 0))
        self.assertEqual((results["mixed_recovery"]["taxpayer_payoff"], results["mixed_recovery"]["authority_payoff"], results["mixed_recovery"]["final_trust"]), (23, 19, 90))

    def test_complete_event_logs(self):
        for result in preset_results().values():
            self.assertEqual(result["rounds_completed"], MAX_ROUNDS)
            self.assertTrue(result["complete_log"])

    def test_trust_bounds(self):
        self.assertEqual(run_path(PRESET_PATHS["transparent_cooperation"], initial_trust=95).trust, 100)
        self.assertEqual(run_path(PRESET_PATHS["opaque_breakdown"], initial_trust=5).trust, 0)

    def test_invalid_actions_and_ninth_round(self):
        with self.assertRaises(ValueError):
            step(GameState(), "hide", "transparent")
        state = run_path(PRESET_PATHS["transparent_cooperation"])
        with self.assertRaises(ValueError):
            step(state, "C", "T")

    def test_one_shot_benchmark(self):
        benchmark = one_shot_benchmark()
        self.assertTrue(benchmark["taxpayer_avoid_strictly_dominant"])
        self.assertTrue(benchmark["authority_opaque_strictly_dominant"])
        self.assertEqual(benchmark["unique_one_shot_nash"], "A/O")
        self.assertEqual(benchmark["pareto_superior_profile"], "C/T")


if __name__ == "__main__":
    unittest.main()
