import unittest

from src.day15 import load_risk_levels

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
