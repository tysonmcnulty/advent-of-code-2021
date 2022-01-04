import os
import unittest

from functools import reduce

from src.day18 import load_snailfish_numbers, SnailfishNumber

SN = SnailfishNumber

class Day18Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.snailfish_numbers_test = load_snailfish_numbers('data/day18_snailfish_numbers_test.txt')
        cls.snailfish_numbers_tm = load_snailfish_numbers('data/day18_snailfish_numbers_tm.txt')

    def test_snailfish_number_add(self):
        self.assertEqual(SN([1, [2, 3]]), 1 + SN([2, 3]))
        self.assertEqual(SN([[1, 2], 3]), SN([1, 2]) + 3)
        self.assertEqual(
            SN([[[1, 2], [3, 4]], [5, 6]]),
            reduce(
                lambda x, y: x + y,
                [SN([1, 2]), SN([3, 4]), SN([5, 6])]))

    def test_traverse(self):
        number = SN([[[1, 2], [3, 4]], [5, 6]])
        traversal = [
            (1, (0, 0, 0)),
            (2, (0, 0, 1)),
            (3, (0, 1, 0)),
            (4, (0, 1, 1)),
            (5, (1, 0)),
            (6, (1, 1))
        ]

        self.assertEqual(traversal, number.traverse())
        self.assertEqual(number, SN.from_traversal(traversal))

    def test_snailfish_number_reduce(self):
        self.assertEqual(
            SN([[[[0,9],2],3],4]),
            SN([[[[[9,8],1],2],3],4]).reduced()
        )
        self.assertEqual(
            SN([7,[6,[5,[7,0]]]]),
            SN([7,[6,[5,[4,[3,2]]]]]).reduced()
        )
        self.assertEqual(
            SN([[6,[5,[7,0]]],3]),
            SN([[6,[5,[4,[3,2]]]],1]).reduced()
        )

    def test_add(self):
        self.assertEqual(
            SN([[[[0,7],4],[[7,8],[6,0]]],[8,1]]),
            SN([[[[4,3],4],4],[7,[[8,4],9]]]) + SN([1,1])
        )

        self.assertEqual(
            SN([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]),
            SN([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]) + SN([7,[[[3,7],[4,3]],[[6,3],[8,8]]]])
        )

    def test_load_snailfish_numbers(self):
        self.assertEqual([
            SN([[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]),
            SN([[[5,[2,8]],4],[5,[[9,9],0]]]),
            SN([6,[[[6,2],[5,6]],[[7,6],[4,7]]]]),
            SN([[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]),
            SN([[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]),
            SN([[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]),
            SN([[[[5,4],[7,7]],8],[[8,3],8]]),
            SN([[9,3],[[9,9],[6,[4,9]]]]),
            SN([[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]),
            SN([[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]),
        ], self.snailfish_numbers_test)

    def test_magnitude(self):
        self.assertEqual([
            143,
            1384,
            445,
            791,
            1137,
            3488,
        ], list(map(lambda it: it.magnitude, [
            SN([[1,2],[[3,4],5]]),
            SN([[[[0,7],4],[[7,8],[6,0]]],[8,1]]),
            SN([[[[1,1],[2,2]],[3,3]],[4,4]]),
            SN([[[[3,0],[5,3]],[4,4]],[5,5]]),
            SN([[[[5,0],[7,4]],[5,5]],[6,6]]),
            SN([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]),
        ])))

    def test_add_homework(self):
        expected_sum = SN([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]])
        self.assertEqual(expected_sum, reduce(lambda a, b: a + b, self.snailfish_numbers_test))
        self.assertEqual(4140, expected_sum.magnitude)

    def test_add_homework_tm(self):
        self.assertEqual(3892, reduce(lambda a, b: a + b, self.snailfish_numbers_tm).magnitude)

    def test_largest_sum(self):
        sums = ((a, b, a + b) for a in self.snailfish_numbers_test for b in self.snailfish_numbers_test if a != b)
        max_sum = max(sums, key = lambda it: it[2].magnitude)

        self.assertEqual((
            SN([[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]),
            SN([[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]),
            SN([[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]),
        ), max_sum)

        self.assertEqual(3993, max_sum[2].magnitude)

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_largest_sum_tm(self):
        sums = ((a, b, a + b) for a in self.snailfish_numbers_tm for b in self.snailfish_numbers_tm if a != b)
        max_sum = max(sums, key = lambda it: it[2].magnitude)
        self.assertEqual(3993, max_sum[2].magnitude)
