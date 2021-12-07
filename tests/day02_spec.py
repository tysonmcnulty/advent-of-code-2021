import unittest

from src.day02 import load_steps, calc_position

class Day02Tests(unittest.TestCase):
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
        self.assertEqual(150, self.get_solution(calc_position('data/day02_steps_test.txt')))
        self.assertEqual(1635930, self.get_solution(calc_position('data/day02_steps_tm.txt')))

    def test_calc_position_with_aim(self):
        self.assertEqual(900, self.get_solution(calc_position('data/day02_steps_test.txt', use_aim = True)))
        self.assertEqual(1781819478, self.get_solution(calc_position('data/day02_steps_tm.txt', use_aim = True)))

    def get_solution(self, position):
        return position["x"] * position["y"]
