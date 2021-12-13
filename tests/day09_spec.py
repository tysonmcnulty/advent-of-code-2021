import unittest
from functools import reduce

from src.day09 import load_heightmap, get_low_points, get_risk_level, get_basin

class Day09Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.heightmap = load_heightmap('data/day09_heightmap_test.txt')
        cls.heightmap_tm = load_heightmap('data/day09_heightmap_tm.txt')

    def test_load_heightmap(self):
        self.assertEqual(
            [
                [2,1,9,9,9,4,3,2,1,0],
                [3,9,8,7,8,9,4,9,2,1],
                [9,8,5,6,7,8,9,8,9,2],
                [8,7,6,7,8,9,6,7,8,9],
                [9,8,9,9,9,6,5,6,7,8],
            ],
            self.heightmap
        )

    def test_get_low_points(self):
        self.assertEqual(
            [(1, 0, 1), (9, 0, 0), (2, 2, 5), (6, 4, 5)],
            get_low_points(self.heightmap)
        )

    def test_get_risk_level(self):
        self.assertEqual(15, get_risk_level(self.heightmap))
        self.assertEqual(564, get_risk_level(self.heightmap_tm))

    def test_get_basins(self):
        basins = list(map(
            lambda p: get_basin(self.heightmap, p),
            get_low_points(self.heightmap)
        ))

        basin_sizes = list(map(len, basins))

        self.assertEqual(1134, reduce(lambda p, x: p * x, sorted(basin_sizes)[-3:]))

    def test_get_basins_tm(self):
        basins = list(map(
            lambda p: get_basin(self.heightmap_tm, p),
            get_low_points(self.heightmap_tm)
        ))

        basin_sizes = list(map(len, basins))

        self.assertEqual(1038240, reduce(lambda p, x: p * x, sorted(basin_sizes)[-3:]))
