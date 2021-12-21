from itertools import count
import unittest

from collections import Counter

from src.day14 import load_instructions, grow, ElementCounter

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

    def test_grow(self):
        polymer_template, insertion_rules = self.instructions_test
        polymer_step_1 = grow(polymer_template, insertion_rules)
        polymer_step_2 = grow(polymer_step_1, insertion_rules)
        polymer_step_3 = grow(polymer_step_2, insertion_rules)
        polymer_step_4 = grow(polymer_step_3, insertion_rules)

        self.assertEqual("NCNBCHB", polymer_step_1)
        self.assertEqual("NBCCNBBBCBHCB", polymer_step_2)
        self.assertEqual("NBBBCNCCNBBNBNBBCHBHHBCHB", polymer_step_3)
        self.assertEqual("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB", polymer_step_4)

    def test_grow_tm(self):
        polymer_template, insertion_rules = self.instructions_tm
        polymer_tm_step_10 = grow(polymer_template, insertion_rules, steps = 10)
        element_counts_step_10 = Counter(polymer_tm_step_10)
        self.assertEqual(3587, max(element_counts_step_10.values()) - min(element_counts_step_10.values()))
        self.assertEqual(19457, sum(element_counts_step_10.values()))

    def test_pair_counter(self):
        counter_tm = ElementCounter(*self.instructions_tm)

        for _ in range(10): counter_tm.grow()
        element_counts_step_10 = counter_tm.counts
        self.assertEqual(3587, max(element_counts_step_10.values()) - min(element_counts_step_10.values()))
        self.assertEqual(19457, sum(element_counts_step_10.values()))

        for _ in range(30): counter_tm.grow()
        element_counts_step_40 = counter_tm.counts
        self.assertEqual(3906445077999, max(element_counts_step_40.values()) - min(element_counts_step_40.values()))
        self.assertEqual(20890720927745, sum(element_counts_step_40.values()))
