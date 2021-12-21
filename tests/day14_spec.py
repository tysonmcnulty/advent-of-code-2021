import unittest

from collections import Counter

from src.day14 import load_instructions

class Day14Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.instructions_test = load_instructions('data/day14_instructions_test.txt')
        cls.instructions_tm = load_instructions('data/day14_instructions_tm.txt')

    def test_load_instructions(self):
        self.assertEqual((
            "NNCB",
            {
                "CH": "B",
                "HH": "N",
                "CB": "H",
                "NH": "C",
                "HB": "C",
                "HC": "B",
                "HN": "C",
                "NN": "C",
                "BH": "H",
                "NC": "B",
                "NB": "B",
                "BN": "B",
                "BB": "N",
                "BC": "B",
                "CC": "N",
                "CN": "C",
            }
        ), self.instructions_test)
