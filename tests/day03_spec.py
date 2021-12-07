import unittest

from src.day03 import calc_oxygen_generator_rating, calc_co2_scrubber_rating, load_diagnostics, calc_gamma_rate, calc_epsilon_rate

class Day03Tests(unittest.TestCase):
    def test_load_diagnostics(self):
        self.assertEqual([
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
        ], load_diagnostics('data/day03_diagnostics_test.txt'))

    def test_calc_gamma_rate(self):
        self.assertEqual(31, calc_gamma_rate(["11111"]))
        self.assertEqual(0, calc_gamma_rate(["00000"]))
        self.assertEqual(10, calc_gamma_rate(["11111", "00000", "01010"]))

        self.assertEqual(
            22,
            calc_gamma_rate(load_diagnostics('data/day03_diagnostics_test.txt'))
        )

        self.assertEqual(
            1816,
            calc_gamma_rate(load_diagnostics('data/day03_diagnostics_tm.txt'))
        )

    def test_calc_epsilon_rate(self):
        self.assertEqual(9, calc_epsilon_rate(load_diagnostics('data/day03_diagnostics_test.txt')))
        self.assertEqual(2279, calc_epsilon_rate(load_diagnostics('data/day03_diagnostics_tm.txt')))

    def test_calc_oxygen_generator_rating(self):
        self.assertEqual(23, calc_oxygen_generator_rating(load_diagnostics('data/day03_diagnostics_test.txt')))
        self.assertEqual(2031, calc_oxygen_generator_rating(load_diagnostics('data/day03_diagnostics_tm.txt')))

    def test_calc_co2_scrubber_rating(self):
        self.assertEqual(10, calc_co2_scrubber_rating(load_diagnostics('data/day03_diagnostics_test.txt')))
        self.assertEqual(2104, calc_co2_scrubber_rating(load_diagnostics('data/day03_diagnostics_tm.txt')))
