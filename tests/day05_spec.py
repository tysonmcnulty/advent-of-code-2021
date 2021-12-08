import unittest

from src.day05 import load_vent_lines, VentLine

class Day05Tests(unittest.TestCase):
    def test_vent_line(self):
        self.assertEqual(set([(0,0), (0,1), (0,2), (0,3)]), VentLine("0,0 -> 0,3").vent_points)
        self.assertEqual(set([(4,6), (3,6), (2,6), (1,6)]), VentLine("4,6 -> 1,6").vent_points)
        self.assertEqual(set(), VentLine("1,1 -> 5,5").vent_points)

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
