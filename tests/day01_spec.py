import unittest

from src.day01 import calc_increases, load_depths


class DayO1Tests(unittest.TestCase):
    def test_load_depths(self):
        self.assertEqual(
            [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
            load_depths("data/day01_depths_test.txt"),
        )
        self.assertEqual(2000, len(load_depths("data/day01_depths_bm.txt")))
        self.assertEqual(2000, len(load_depths("data/day01_depths_tm.txt")))

    def test_calc_increases_no_binning(self):
        self.assertEqual(7, calc_increases("data/day01_depths_test.txt"))
        self.assertEqual(1462, calc_increases("data/day01_depths_bm.txt"))
        self.assertEqual(1616, calc_increases("data/day01_depths_tm.txt"))

    def test_calc_increases_with_binning(self):
        self.assertEqual(5, calc_increases("data/day01_depths_test.txt", bin_size=3))
        self.assertEqual(1497, calc_increases("data/day01_depths_bm.txt", bin_size=3))
        self.assertEqual(1645, calc_increases("data/day01_depths_tm.txt", bin_size=3))
