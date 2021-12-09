import unittest

from src.day07 import LinearCrabPositionOptimizer, load_crab_positions

class Day07Tests(unittest.TestCase):
    def test_load_crab_positions(self):
        self.assertEqual([16,1,2,0,4,2,7,1,2,14], load_crab_positions('data/day07_crab_positions_test.txt'))

    def test_get_optimal_position(self):
        crab_positions_test = load_crab_positions('data/day07_crab_positions_test.txt')
        crab_positions_tm = load_crab_positions('data/day07_crab_positions_tm.txt')

        linear_optimizer = LinearCrabPositionOptimizer()
        self.assertEqual((2, 37), linear_optimizer.get_optimum(crab_positions_test))
        self.assertEqual((376, 352707), linear_optimizer.get_optimum(crab_positions_tm))
