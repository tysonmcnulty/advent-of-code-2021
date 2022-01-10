import os
import unittest

from src.day23 import load_amphipod_diagram, AmphipodGraph

class Day23Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amphipods_test = load_amphipod_diagram('data/day23_amphipod_diagram_test.txt')
        cls.amphipods_tm = load_amphipod_diagram('data/day23_amphipod_diagram_tm.txt')
        cls.amphipods_target = load_amphipod_diagram('data/day23_amphipod_diagram_target.txt')

    def test_load_amphipod_diagram(self):
        self.assertEqual({
            "A": {(3, 3), (9, 3)},
            "B": {(3, 2), (7, 2)},
            "C": {(5, 2), (7, 3)},
            "D": {(5, 3), (9, 2)}
        }, dict(self.amphipods_test))

        self.assertEqual({
            "A": {(7, 2), (7, 3)},
            "B": {(5, 2), (9, 3)},
            "C": {(3, 2), (3, 3)},
            "D": {(5, 3), (9, 2)}
        }, dict(self.amphipods_tm))

        self.assertEqual({
            "A": {(3, 2), (3, 3)},
            "B": {(5, 2), (5, 3)},
            "C": {(7, 2), (7, 3)},
            "D": {(9, 2), (9, 3)}
        }, dict(self.amphipods_target))

    def test_amphipod_graph(self):
        amphipod_graph = AmphipodGraph()
        self.assertEqual({
            (1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1),
            (3, 2), (5, 2), (7, 2), (9, 2),
            (3, 3), (5, 3), (7, 3), (9, 3)
        }, amphipod_graph.nodes)

        self.assertEqual({
            frozenset({(1, 1), (2, 1)}),
            frozenset({(2, 1), (4, 1)}),
            frozenset({(2, 1), (3, 2)}),
            frozenset({(3, 2), (3, 3)}),
            frozenset({(3, 2), (4, 1)}),
            frozenset({(4, 1), (6, 1)}),
            frozenset({(4, 1), (5, 2)}),
            frozenset({(5, 2), (5, 3)}),
            frozenset({(5, 2), (6, 1)}),
            frozenset({(6, 1), (8, 1)}),
            frozenset({(6, 1), (7, 2)}),
            frozenset({(7, 2), (7, 3)}),
            frozenset({(7, 2), (8, 1)}),
            frozenset({(8, 1), (10, 1)}),
            frozenset({(8, 1), (9, 2)}),
            frozenset({(9, 2), (9, 3)}),
            frozenset({(9, 2), (10, 1)}),
            frozenset({(10, 1), (11, 1)}),
        }, amphipod_graph.edges)
