import unittest

from src.day12 import load_cave_connections

class Day12Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cave_connections_test = load_cave_connections('data/day12_cave_connections_test.txt')
        cls.cave_connections_tm = load_cave_connections('data/day12_cave_connections_tm.txt')

    def test_load_cave_connections(self):
        self.assertEqual([
            ("start", "A"),
            ("start", "b"),
            ("A", "c"),
            ("A", "b"),
            ("b", "d"),
            ("A", "end"),
            ("b", "end"),
        ], self.cave_connections_test)
