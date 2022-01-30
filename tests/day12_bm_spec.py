import unittest

from src.day12_bm import (
    load_file,
    CaveMap,
)


class Day12Tests(unittest.TestCase):
    def test_load_file(self):
        cave_map = load_file("data/day12_pathing_10_test.txt")
        self.assertEqual(7, len(cave_map))
        self.assertEqual("start-A", cave_map[0])
        self.assertEqual("b-end", cave_map[-1])

    def test_CaveMap(self):
        cmap = CaveMap(["aa-bb", "CC-dd"])
        self.assertEqual(
            {"aa": ["bb"], "bb": ["aa"], "CC": ["dd"], "dd": ["CC"]}, cmap.nodes
        )
        self.assertEqual({"aa", "bb", "dd"}, cmap.small_caves_not_visited)
        cmap = CaveMap(load_file("data/day12_pathing_10_test.txt"))
        self.assertEqual(["A", "b"], cmap.nodes["start"])
        self.assertEqual({"c", "b", "d", "end", "start"}, cmap.small_caves_not_visited)

    def test_search(self):
        cmap = CaveMap(["start-aa", "aa-bb", "aa-end", "bb-end"])
        cmap.search()
