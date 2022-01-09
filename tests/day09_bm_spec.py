import unittest

from src.day09_bm import (
    load_file,
    pad_9s,
    local_mins,
    solution_part_1,
    basin_sizes,
    find_neighbors,
    solution_part_2,
)


class Day09Tests(unittest.TestCase):
    def test_load_file(self):
        height_map = load_file("data/day09_smoke_test.txt")
        self.assertEqual(5, len(height_map))
        self.assertEqual("219", height_map[0][:3])
        height_map = load_file("data/day09_smoke_bm.txt")
        self.assertEqual(100, len(height_map))
        self.assertEqual("65434", height_map[1][-5:])
        self.assertEqual("4599", height_map[99][:4])

    def test_pad_9s(self):
        height_map = load_file("data/day09_smoke_test.txt")
        padded_map = pad_9s(height_map)
        self.assertEqual(7, len(padded_map))
        self.assertEqual([9, 9, 9], padded_map[0][:3])
        self.assertEqual([9, 2, 1, 9], padded_map[1][:4])
        self.assertEqual([6, 7, 8, 9], padded_map[5][-4:])
        self.assertEqual([9, 9, 9, 9, 9], padded_map[6][-5:])

    def test_local_mins(self):
        height_map = load_file("data/day09_smoke_test.txt")
        padded_map = pad_9s(height_map)
        self.assertEqual(
            {(1, 2): 1, (1, 10): 0, (3, 3): 5, (5, 7): 5}, local_mins(padded_map)
        )

    def test_solution_part_1(self):
        low_points = local_mins(pad_9s(load_file("data/day09_smoke_test.txt")))
        self.assertEqual(15, solution_part_1(low_points))
        low_points = local_mins(pad_9s(load_file("data/day09_smoke_bm.txt")))
        # 207 low points add up to 462
        self.assertEqual(462, solution_part_1(low_points))

    def test_find_neighbors(self):
        padded_map = pad_9s(load_file("data/day09_smoke_test.txt"))
        self.assertEqual(
            {(1, 1), (1, 2), (2, 1)}, find_neighbors(padded_map, 1, 2, {(1, 2)})
        )
        neighbors = find_neighbors(padded_map, 3, 3, {(3, 3)})
        self.assertEqual(14, len(neighbors))

    def test_basin_sizes(self):
        padded_map = pad_9s(load_file("data/day09_smoke_test.txt"))
        low_points = local_mins(padded_map)
        self.assertEqual([3, 9, 14, 9], basin_sizes(padded_map, low_points))
        # self.assertEqual([3, 9, 14, 9], sizes)

    def test_solution_part_2(self):
        padded_map = pad_9s(load_file("data/day09_smoke_test.txt"))
        low_points = local_mins(padded_map)
        self.assertEqual(1134, solution_part_2(padded_map, low_points))
        padded_map = pad_9s(load_file("data/day09_smoke_bm.txt"))
        low_points = local_mins(padded_map)
        # Part 2 solution: 120 * 112 * 104 = 1397760
        self.assertEqual(1397760, solution_part_2(padded_map, low_points))
