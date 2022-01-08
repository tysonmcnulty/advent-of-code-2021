import os
import unittest

from src.day21 import load_starting_spaces

class Day21Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.starting_spaces_test = load_starting_spaces('data/day21_starting_spaces_test.txt')
        cls.starting_spaces_tm = load_starting_spaces('data/day21_starting_spaces_tm.txt')

    def test_load_starting_spaces(self):
        self.assertEqual({ "Player 1": 4, "Player 2": 8 }, self.starting_spaces_test)
        self.assertEqual({ "Player 1": 7, "Player 2": 2 }, self.starting_spaces_tm)
