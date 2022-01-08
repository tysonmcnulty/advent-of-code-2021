import os
import unittest

from collections import Counter
from functools import reduce
from itertools import combinations

from src.day20 import load_image

class Day20Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.image_test = load_image('data/day20_image_test.txt')
        cls.image_tm = load_image('data/day20_image_tm.txt')

    def test_render(self):
        image, _ = self.image_test

        self.assertEqual("\n".join([
            "#..#.",
            "#....",
            "##..#",
            "..#..",
            "..###",
        ]), image.render())

        self.assertEqual("\n".join([
            "...........",
            "...........",
            "...........",
            "...#..#....",
            "...#.......",
            "...##..#...",
            ".....#.....",
            ".....###...",
            "...........",
            "...........",
            "...........",
        ]), image.render(padding = 3))

    def test_enhance(self):
        image, enhance = self.image_test

        image_enhanced_once = enhance(image)
        self.assertEqual("\n".join([
            ".##.##.",
            "#..#.#.",
            "##.#..#",
            "####..#",
            ".#..##.",
            "..##..#",
            "...#.#.",
        ]), image_enhanced_once.render())

        image_enhanced_twice = enhance(image_enhanced_once)
        self.assertEqual("\n".join([
            "...............",
            "...............",
            "...............",
            "..........#....",
            "....#..#.#.....",
            "...#.#...###...",
            "...#...##.#....",
            "...#.....#.#...",
            "....#.#####....",
            ".....#.#####...",
            "......##.##....",
            ".......###.....",
            "...............",
            "...............",
            "...............",
        ]), image_enhanced_twice.render(padding = 3))

        self.assertEqual(35, Counter(image_enhanced_twice.render())["#"])

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_enhance_tm(self):
        image, enhance = self.image_tm

        image_enhanced_twice = enhance(enhance(image))

        self.assertEqual(5622, Counter(image_enhanced_twice.render())["#"])

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_enhance_many(self):
        image_test, enhance_test = self.image_test
        enhance_50x_test = apply_many(enhance_test, 50)

        self.assertEqual(3351, Counter(enhance_50x_test(image_test).render())["#"])

        image_tm, enhance_tm = self.image_tm
        enhance_50x_tm = apply_many(enhance_tm, 50)

        self.assertEqual(20395, Counter(enhance_50x_tm(image_tm).render())["#"])

def apply_many(fn, times):
    return lambda arg: reduce(lambda x, _: fn(x), range(times), arg)
