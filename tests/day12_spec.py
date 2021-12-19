import unittest

from src.day12 import load_cave_connections, CaveMap

class Day12Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cave_connections_test = load_cave_connections('data/day12_cave_connections_test.txt')
        cls.cave_connections_tm = load_cave_connections('data/day12_cave_connections_tm.txt')

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

    def test_cave_graph(self):
        cave_graph_test = CaveMap(connections = self.cave_connections_test)

        expected_cave_graph = CaveMap()
        expected_cave_graph.add_cave("start")
        expected_cave_graph.add_cave("end")
        expected_cave_graph.add_cave("A")
        expected_cave_graph.add_connection("start", "b")
        expected_cave_graph.add_connection("end", "b")
        expected_cave_graph.add_path("c", "A", "b", "d")
        expected_cave_graph.add_path("start", "A", "end")

        self.assertEqual(expected_cave_graph, cave_graph_test)
