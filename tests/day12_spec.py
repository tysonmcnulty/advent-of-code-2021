import os
import unittest

from collections import Counter

from src.day12 import load_cave_connections, CaveMap

class Day12Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cave_connections_test = load_cave_connections('data/day12_cave_connections_test.txt')
        cls.cave_connections_tm = load_cave_connections('data/day12_cave_connections_tm.txt')
        cls.cave_map_test = CaveMap(connections = cls.cave_connections_test)
        cls.cave_map_tm = CaveMap(connections = cls.cave_connections_tm)

    def test_load_cave_connections(self):
        self.assertEqual([
            { "start", "A" },
            { "start", "b" },
            { "A", "c" },
            { "A", "b" },
            { "b", "d" },
            { "A", "end" },
            { "b", "end" },
        ], self.cave_connections_test)

    def test_cave_map(self):
        expected_cave_map = CaveMap()
        expected_cave_map.add_cave("start")
        expected_cave_map.add_cave("end")
        expected_cave_map.add_cave("A")
        expected_cave_map.add_connection("start", "b")
        expected_cave_map.add_connection("end", "b")
        expected_cave_map.add_path("c", "A", "b", "d")
        expected_cave_map.add_path("start", "A", "end")

        self.assertEqual(expected_cave_map, self.cave_map_test)

    def test_find_all_paths_when_revisitable_is_never(self):
        self.assertEqual(set(), CaveMap().find_all_paths("A", "A"))
        self.assertEqual({tuple("A")}, CaveMap(caves = ["A"]).find_all_paths("A", "A"))
        self.assertEqual(set(), CaveMap(caves = ["A", "B"]).find_all_paths("A", "B"))
        self.assertEqual({("A", "B")}, CaveMap(connections = [{"A", "B"}]).find_all_paths("A", "B"))

        self.assertEqual({
            ("start", "A", "end"),
            ("start", "b", "end"),
            ("start", "A", "b", "end"),
            ("start", "b", "A", "end"),
        }, self.cave_map_test.find_all_paths("start", "end"))


    def test_find_all_paths_when_large_caves_are_revisitable(self):
        self.assertEqual({
            ("start", "A", "b", "A" , "c", "A", "end"),
            ("start", "A", "c", "A" , "b", "A", "end"),
            ("start", "A", "c", "A" , "b", "end"),
            ("start", "b", "A", "c" , "A", "end"),
            ("start", "A", "c", "A" , "end"),
            ("start", "A", "b", "A" , "end"),
            ("start", "A", "b", "end"),
            ("start", "A", "end"),
            ("start", "b", "A", "end"),
            ("start", "b", "end"),
        }, self.cave_map_test.find_all_paths("start", "end", revisitable = is_large_cave))

        all_paths_tm = self.cave_map_tm.find_all_paths("start", "end", revisitable = is_large_cave)
        self.assertEqual(4338, len(all_paths_tm))

    def test_find_all_paths_when_large_caves_and_one_small_cave_are_revisitable(self):
        self.assertEqual({
            ('start', 'A', 'end'),
            ('start', 'b', 'end'),
            ('start', 'A', 'b', 'end'),
            ('start', 'b', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'end'),
            ('start', 'b', 'A', 'b', 'end'),
            ('start', 'b', 'd', 'b', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'end'),
            ('start', 'A', 'b', 'A', 'b', 'end'),
            ('start', 'A', 'b', 'd', 'b', 'end'),
            ('start', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'b', 'A', 'b', 'A', 'end'),
            ('start', 'b', 'd', 'b', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'b', 'd', 'b', 'A', 'end'),
            ('start', 'b', 'A', 'c', 'A', 'b', 'end'),
            ('start', 'A', 'c', 'A', 'c', 'A', 'b', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'A', 'b', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'd', 'b', 'end'),
            ('start', 'A', 'b', 'A', 'c', 'A', 'b', 'end'),
            ('start', 'b', 'A', 'c', 'A', 'c', 'A', 'end'),
            ('start', 'b', 'A', 'c', 'A', 'b', 'A', 'end'),
            ('start', 'b', 'A', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'),
        }, self.cave_map_test.find_all_paths("start", "end", revisitable = is_large_cave_or_no_small_caves_revisited))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_find_all_paths_when_large_caves_and_one_small_cave_are_revisitable_tm(self):
        all_paths_tm = self.cave_map_tm.find_all_paths("start", "end", revisitable = is_large_cave_or_no_small_caves_revisited)
        self.assertEqual(114189, len(all_paths_tm))

is_large_cave = lambda cave, partial_path: cave.isupper()

is_large_cave_or_no_small_caves_revisited = lambda cave, partial_path: cave.isupper() or (
    cave not in { "start", "end" } and
    not any(times_visited >= 2 for cave, times_visited in Counter(partial_path).items() if cave.islower())
)
