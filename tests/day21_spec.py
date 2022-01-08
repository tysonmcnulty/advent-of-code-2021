import os
import unittest

from src.day21 import load_starting_squares

class Day21Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.starting_squares_test = load_starting_squares('data/day21_starting_squares_test.txt')
        cls.starting_squares_tm = load_starting_squares('data/day21_starting_squares_tm.txt')
