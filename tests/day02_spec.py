import unittest

from src.day02 import load_steps, calc_position

class DayO1Tests(unittest.TestCase):
    def test_load_steps(self):
        self.assertEqual([
            ["forward", 5],
            ["down", 5],
            ["forward", 8],
            ["up", 3],
            ["down", 8],
            ["forward", 2]
        ], load_steps('data/day02_steps_test.txt'))

        self.assertEqual(1000, len(load_steps('data/day02_steps_tm.txt')))

    def test_calc_position(self):
        self.assertEqual({ "x": 15, "y": 10 }, calc_position('data/day02_steps_test.txt'))
        self.assertEqual({ "x": 1971, "y": 830 }, calc_position('data/day02_steps_tm.txt'))
