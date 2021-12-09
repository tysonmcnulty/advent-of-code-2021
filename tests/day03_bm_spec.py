import unittest

from src.day03_bm import load_report, calc_power, calc_life_support


class Day03Tests(unittest.TestCase):
    def test_load_report(self):
        self.assertEqual(
            [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ],
            load_report("data/day03_report_test.txt"),
        )
        self.assertEqual(1000, len(load_report("data/day03_report_bm.txt")))

    def test_calc_power(self):
        self.assertEqual(198, calc_power("data/day03_report_test.txt"))
        self.assertEqual(2261546, calc_power("data/day03_report_bm.txt"))

    def test_calc_life_support(self):
        self.assertEqual(198, calc_life_support("data/day03_report_test.txt"))

