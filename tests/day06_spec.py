import unittest
import os

from src.day06 import load_lanternfish, create_population, simulate

class Day06Tests(unittest.TestCase):
    def test_load_lanterfish(self):
        self.assertEqual([3, 4, 3, 1, 2], load_lanternfish('data/day06_lanternfish_test.txt'))

    def test_create_population(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0], create_population([]))
        self.assertEqual([0, 1, 1, 2, 1, 0, 0, 0, 0], create_population([3, 4, 3, 1, 2]))
        self.assertEqual([0, 155, 33, 45, 41, 26, 0, 0, 0], create_population(load_lanternfish('data/day06_lanternfish_tm.txt')))

    def test_simulate(self):
        population = create_population(load_lanternfish('data/day06_lanternfish_test.txt'))
        self.assertEqual([1, 1, 2, 1, 0, 0, 0, 0, 0], simulate(population))
        self.assertEqual([1, 2, 1, 0, 0, 0, 1, 0, 1], simulate(population))
        self.assertEqual([2, 1, 0, 0, 0, 1, 1, 1, 1], simulate(population))
        self.assertEqual([1, 0, 0, 0, 1, 1, 3, 1, 2], simulate(population))
        self.assertEqual([0, 0, 0, 1, 1, 3, 2, 2, 1], simulate(population))

        for _ in range(75): simulate(population)
        self.assertEqual(5934, sum(population))

        for _ in range(176): simulate(population)
        self.assertEqual(26984457539, sum(population))

    def test_simulate_tm(self):
        population = create_population(load_lanternfish('data/day06_lanternfish_tm.txt'))

        for _ in range(80): simulate(population)
        self.assertEqual(375482, sum(population))

        for _ in range(176): simulate(population)
        self.assertEqual(1689540415957, sum(population))
