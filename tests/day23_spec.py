import os
import unittest

from src.day23 import load_amphipod_diagram, Organizer

class Day23Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amphipods_test = load_amphipod_diagram('data/day23_amphipod_diagram_test.txt')
        cls.amphipods_tm = load_amphipod_diagram('data/day23_amphipod_diagram_tm.txt')
        cls.amphipods_target = load_amphipod_diagram('data/day23_amphipod_diagram_target.txt')
        cls.amphipods_full_test = load_amphipod_diagram('data/day23_amphipod_diagram_full_test.txt')
        cls.amphipods_full_tm = load_amphipod_diagram('data/day23_amphipod_diagram_full_tm.txt')
        cls.amphipods_full_target = load_amphipod_diagram('data/day23_amphipod_diagram_full_target.txt')


    def test_load_amphipod_diagram(self):
        self.assertEqual({
            ("A", (3, 3)), ("A", (9, 3)),
            ("B", (3, 2)), ("B", (7, 2)),
            ("C", (5, 2)), ("C", (7, 3)),
            ("D", (5, 3)), ("D", (9, 2)),
        }, self.amphipods_test)

        self.assertEqual({
            ("A", (7, 2)), ("A", (7, 3)),
            ("B", (5, 2)), ("B", (9, 3)),
            ("C", (3, 2)), ("C", (3, 3)),
            ("D", (5, 3)), ("D", (9, 2)),
        }, self.amphipods_tm)

        self.assertEqual(Organizer.DEFAULT_TARGET, self.amphipods_target)
        self.assertEqual(Organizer.FULL_TARGET, self.amphipods_full_target)

    def test_amphipod_graph(self):
        organizer = Organizer()
        self.assertEqual({
            (1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1),
            (3, 2), (5, 2), (7, 2), (9, 2),
            (3, 3), (5, 3), (7, 3), (9, 3)
        }, organizer.graph.nodes)

    def test_available_moves(self):
        organizer = Organizer()

        self.assertEqual(set(), organizer.get_available_moves(self.amphipods_target))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_organize(self):
        amphipod_organizer = Organizer()

        self.assertEqual(12521, amphipod_organizer.organize(self.amphipods_test))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_organize_tm(self):
        amphipod_organizer = Organizer()

        self.assertEqual(13558, amphipod_organizer.organize(self.amphipods_tm))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_organize_full_test(self):
        amphipod_organizer = Organizer(
            target = Organizer.FULL_TARGET,
            graph = Organizer.FULL_GRAPH
        )

        self.assertEqual(44169, amphipod_organizer.organize(self.amphipods_full_test))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_organize_full_tm(self):
        amphipod_organizer = Organizer(
            target = Organizer.FULL_TARGET,
            graph = Organizer.FULL_GRAPH
        )

        self.assertEqual(44169, amphipod_organizer.organize(self.amphipods_full_tm))
