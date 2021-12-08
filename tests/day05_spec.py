import unittest
import os

from src.day05 import load_vent_lines, VentLine, count_all_crossings

class Day05Tests(unittest.TestCase):
    def test_vent_line(self):
        self.assertEqual({(0,0), (0,1), (0,2), (0,3)}, VentLine("0,0 -> 0,3").get_points())
        self.assertEqual({(4,6), (3,6), (2,6), (1,6)}, VentLine("4,6 -> 1,6").get_points())
        self.assertEqual({(2,2), (3,3), (4,4), (5,5)}, VentLine("2,2 -> 5,5").get_points())
        self.assertEqual({(7,2), (6,3), (5,4), (4,5)}, VentLine("7,2 -> 4,5").get_points())

    def test_load_vent_lines(self):
        vent_lines = load_vent_lines('data/day05_vent_lines_test.txt')
        self.assertEqual(
            [
                VentLine("0,9 -> 5,9"),
                VentLine("8,0 -> 0,8"),
                VentLine("9,4 -> 3,4"),
                VentLine("2,2 -> 2,1"),
                VentLine("7,0 -> 7,4"),
                VentLine("6,4 -> 2,0"),
                VentLine("0,9 -> 2,9"),
                VentLine("3,4 -> 1,4"),
                VentLine("0,0 -> 8,8"),
                VentLine("5,5 -> 8,2")
            ],
            vent_lines
        )

    def test_get_crossings(self):
        self.assertEqual(
            {(4,4)},
            VentLine("4,1 -> 4,7").get_crossings(VentLine("1,4 -> 7,4"))
        )

        self.assertEqual(
            {(3,4), (3,5)},
            VentLine("3,1 -> 3,5").get_crossings(VentLine("3,4 -> 3,8"))
        )

        self.assertEqual(
            set(),
            VentLine("6,2 -> 6,8").get_crossings(VentLine("7,9 -> 2,9"))
        )

    def test_count_all_crossings(self):
        self.assertEqual(
            5,
            count_all_crossings(
                load_vent_lines('data/day05_vent_lines_test.txt'),
                ignore_diagonals = True
            )
        )

        self.assertEqual(12,count_all_crossings(load_vent_lines('data/day05_vent_lines_test.txt')))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_count_all_crossings_tm(self):
        self.assertEqual(
            5576,
            count_all_crossings(
                load_vent_lines('data/day05_vent_lines_tm.txt'),
                ignore_diagonals = True
            )
        )

        self.assertEqual(
            18144,
            count_all_crossings(
                load_vent_lines('data/day05_vent_lines_tm.txt'),
                ignore_diagonals = False
            )
        )
