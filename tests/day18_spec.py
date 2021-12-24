import unittest

from src.day18 import load_snailfish_numbers, SnailfishNumber

class Day18Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.snailfish_numbers_test = load_snailfish_numbers('data/day18_snailfish_numbers_test.txt')
        cls.snailfish_numbers_tm = load_snailfish_numbers('data/day18_snailfish_numbers_tm.txt')

    def test_snailfish_number_add(self):
        SN = SnailfishNumber
        self.assertEqual(SN([1, [2, 3]]), 1 + SN([2, 3]))

    # def test_homework(self):
    #     self.assertEqual(4140, sum(self.snailfish_numbers_test).magnitude)
