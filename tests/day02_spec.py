import unittest

from src.day02 import load_steps

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