import unittest

from src.day03_bm import (
    load_report,
    calc_power_str,
    calc_life_support_str,
    most_common_bits_str,
)


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

    def test_calc_power_str(self):
        self.assertEqual(198, calc_power_str("data/day03_report_test.txt"))
        self.assertEqual(2261546, calc_power_str("data/day03_report_bm.txt"))

    def test_most_common_bits_str(self):
        self.assertEqual(
            "10110",
            most_common_bits_str(
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
            ),
        )  # sample data
        self.assertEqual(
            "11111",
            most_common_bits_str(
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
                    "01010",
                    "01011",
                ],
            ),
        )  # modified sample data; equal counts in positions 1 & 4

    def test_calc_life_support_str(self):
        self.assertEqual(230, calc_life_support_str("data/day03_report_test.txt"))
        self.assertEqual(6775520, calc_life_support_str("data/day03_report_bm.txt"))
        # self.assertEqual(6775520, calc_life_support_str("data/day03_report_tm.txt"))

