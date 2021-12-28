import unittest

from src.day05_bm import (
    load_file,
    expand_vent_lines,
    vent_counts,
    diagonal_vent_points,
)


class Day05Tests(unittest.TestCase):
    def test_load_file(self):
        vent_ends = load_file("data/day05_vents_test.txt")
        self.assertEqual(
            20, len(vent_ends),
        )
        self.assertEqual(
            ([0, 9], [5, 9], [8, 2]), (vent_ends[0], vent_ends[1], vent_ends[19])
        )

    def test_expand_vent_lines(self):
        # test Part 1 horizontal and vertical lines
        vent_xy_pair = [[3, 9], [3, 12]]
        self.assertEqual(
            [[3, 9], [3, 10], [3, 11], [3, 12]], expand_vent_lines(vent_xy_pair)
        )
        vent_xy_pair = [[3, 12], [6, 12]]
        self.assertEqual(
            [[3, 12], [4, 12], [5, 12], [6, 12]], expand_vent_lines(vent_xy_pair)
        )
        vent_xy_pair = [[3, 12], [3, 9]]
        self.assertEqual(
            [[3, 9], [3, 10], [3, 11], [3, 12]], expand_vent_lines(vent_xy_pair)
        )
        vent_xy_pair = [[6, 12], [3, 12]]
        self.assertEqual(
            [[3, 12], [4, 12], [5, 12], [6, 12]], expand_vent_lines(vent_xy_pair)
        )
        # test multiple lines
        vent_xy_pairs = [[6, 12], [3, 12], [5, 10], [5, 12]]
        self.assertEqual(
            [[3, 12], [4, 12], [5, 12], [6, 12], [5, 10], [5, 11], [5, 12]],
            expand_vent_lines(vent_xy_pairs),
        )
        # test Part 2 diagonal lines
        vent_xy_pair = [[3, 9], [7, 12]]
        self.assertEqual(
            [[3, 9], [4, 10], [5, 11], [6, 12]],
            expand_vent_lines(vent_xy_pair, include_diagonals=True),
        )
        vent_xy_pair = [[3, 9], [7, 12], [6, 12], [3, 12]]
        self.assertEqual(
            [[3, 9], [4, 10], [5, 11], [6, 12], [3, 12], [4, 12], [5, 12], [6, 12]],
            expand_vent_lines(vent_xy_pair, include_diagonals=True),
        )
        vent_xy_pair = [[3, 9], [7, 12]]
        self.assertEqual([], expand_vent_lines(vent_xy_pair, include_diagonals=False))
        vent_xy_pair = [[3, 9], [7, 12], [6, 12], [3, 12]]
        self.assertEqual(
            [[3, 12], [4, 12], [5, 12], [6, 12]],
            expand_vent_lines(vent_xy_pair, include_diagonals=False),
        )

    def test_vent_counts(self):
        vent_xy_points = [[3, 12], [4, 88], [5, 12], [6, 66], [4, 88], [6, 66], [4, 88]]
        self.assertEqual(
            ({(4, 88): 3, (5, 12): 1, (6, 66): 2, (3, 12): 1}, 4),
            vent_counts(vent_xy_points),
        )
        self.assertEqual(
            2, vent_counts(vent_xy_points, 2)[1],
        )
        self.assertEqual(
            0, vent_counts(vent_xy_points, 9)[1],
        )

    def test_solution_part_1(self):
        vent_ends = load_file("data/day05_vents_test.txt")
        vent_points = expand_vent_lines(vent_ends)
        self.assertEqual(5, vent_counts(vent_points, 2)[1])
        vent_ends = load_file("data/day05_vents_bm.txt")
        vent_points = expand_vent_lines(vent_ends)
        self.assertEqual(7436, vent_counts(vent_points, 2)[1])

    def test_solution_part_2(self):
        vent_ends = load_file("data/day05_vents_test.txt")
        vent_points = expand_vent_lines(vent_ends, include_diagonals=True)
        self.assertEqual(12, vent_counts(vent_points, 2)[1])
        vent_ends = load_file("data/day05_vents_bm.txt")
        vent_points = expand_vent_lines(vent_ends, include_diagonals=True)
        self.assertEqual(21104, vent_counts(vent_points, 2)[1])

    def test_diagonal_vent_points(self):
        # also, confirm tests without diagonals
        # test diagonals
        # vent_xy_pairs = [[3, 12], [6, 12]]
        self.assertEqual(
            [[4, 10], [5, 11], [6, 12]], diagonal_vent_points(4, 10, 6, 12),
        )
        self.assertEqual(
            [[6, 10], [5, 11], [4, 12]], diagonal_vent_points(6, 10, 4, 12),
        )
        self.assertEqual(
            [[4, 12], [5, 11], [6, 10]], diagonal_vent_points(4, 12, 6, 10),
        )
