import unittest

from collections import Counter

from src.day13 import load_instructions

class Day13Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.instructions_test = load_instructions('data/day13_instructions_test.txt')
        cls.instructions_tm = load_instructions('data/day13_instructions_tm.txt')

    def test_load_cave_connections(self):
        self.assertEqual((
            {
                (6, 10),
                (0, 14),
                (9, 10),
                (0, 3),
                (10, 4),
                (4, 11),
                (6, 0),
                (6, 12),
                (4, 1),
                (0, 13),
                (10, 12),
                (3, 4),
                (3, 0),
                (8, 4),
                (1, 10),
                (2, 14),
                (8, 10),
                (9, 0),
            },
            [ "y=7", "x=5" ]
        ), self.instructions_test)

        self.assertEqual(1022, len(self.instructions_tm[0]))
        self.assertEqual(12, len(self.instructions_tm[1]))
