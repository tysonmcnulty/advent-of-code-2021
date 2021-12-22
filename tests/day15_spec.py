import unittest

from src.day15 import load_risk_levels, navigate, Cave

class Day15Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.risk_levels_test = load_risk_levels('data/day15_risk_levels_test.txt')
        cls.risk_levels_tm = load_risk_levels('data/day15_risk_levels_tm.txt')

    def test_load_risk_levels(self):
        self.assertEqual([
            [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
            [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
            [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
            [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
            [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
            [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
            [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
            [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
            [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
            [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
        ], self.risk_levels_test)

    def test_navigate(self):
        start = (0, 0)
        end = (9, 9)
        get_total_risk_level, get_safest_path = navigate(Cave(self.risk_levels_test), start)

        self.assertEqual(41, get_total_risk_level(end))
        self.assertEqual(40, get_total_risk_level(end, exclude_start = True))
        self.assertIn(get_safest_path(end), [
            [
                (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3),
                (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (9, 8), (9, 9),
            ],[
                (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3),
                (7, 3), (7, 4), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 8), (9, 9),
            ]])

    def test_navigate_tm(self):
        start = (0, 0)
        end = (99, 99)
        get_total_risk_level, _ = navigate(Cave(self.risk_levels_tm), start)

        self.assertEqual(373, get_total_risk_level(end, exclude_start = True))
