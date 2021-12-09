import unittest

from src.day07 import load_crab_positions, get_optimal_alignment

class Day07Tests(unittest.TestCase):
    def test_load_crab_positions(self):
        self.assertEqual([16,1,2,0,4,2,7,1,2,14], load_crab_positions('data/day07_crab_positions_test.txt'))

    def test_get_optimal_alignment(self):
        self.assertEqual((2, 37), get_optimal_alignment(load_crab_positions('data/day07_crab_positions_test.txt')))
        self.assertEqual((376, 352707), get_optimal_alignment(load_crab_positions('data/day07_crab_positions_tm.txt')))
