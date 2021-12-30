import unittest

from src.day07_bm import (
    load_file,
    CrabsData,
)


class Day07Tests(unittest.TestCase):
    def test_load_file(self):
        crabs = load_file("data/day07_crabs_test.txt")
        self.assertEqual(10, len(crabs))
        self.assertEqual([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], crabs)

    def test_CrabsData(self):
        crabs = CrabsData([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(10, len(crabs.positions))
        self.assertEqual([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], crabs.positions)

    def test_get_sum(self):
        crabs = CrabsData([1, 3, 5])
        self.assertEqual(4, crabs.get_sum(3))
        crabs = CrabsData(load_file("data/day07_crabs_test.txt"))
        self.assertEqual(71, crabs.get_sum(10))
        self.assertEqual(37, crabs.get_sum(2))
        crabs = CrabsData(load_file("data/day07_crabs_test.txt"))
        crabs.part_2_flag = True
        self.assertEqual(206, crabs.get_sum(2))
        self.assertEqual(168, crabs.get_sum(5))

    def test_best_direction(self):
        crabs = CrabsData()
        crabs._known_sums = {5: 10, 6: 14, 7: 25}
        self.assertEqual(-1, crabs.best_direction(6))
        crabs._known_sums = {5: 25, 6: 14, 7: 10}
        self.assertEqual(1, crabs.best_direction(6))
        crabs._known_sums = {5: 20, 6: 14, 7: 20}
        self.assertEqual(0, crabs.best_direction(6))
        # pick a starting mid-pointpoint
        crabs._known_sums = {5: 25, 6: 14, 7: 10}
        self.assertEqual(1, crabs.best_direction())
        crabs = CrabsData([1, 3, 5, 7, 9])
        self.assertEqual(20, crabs.get_sum(9))
        self.assertEqual(0, crabs.best_direction())

    def test_next_point(self):
        crabs = CrabsData([1, 3, 5, 7, 9])
        self.assertEqual(5, crabs.next_point())
        self.assertEqual(5, crabs.next_point())
        crabs = CrabsData(load_file("data/day07_crabs_test.txt"))
        self.assertEqual(3, crabs.next_point())
        self.assertEqual(1, crabs.next_point(3))
        self.assertEqual(2, crabs.next_point(1))
        self.assertEqual(2, crabs.next_point(2))

    def test_solution_part_1_2(self):
        # Part 1...
        crabs = CrabsData(load_file("data/day07_crabs_test.txt"))
        self.assertEqual((2, 37), crabs.solution_part_1_2())
        crabs = CrabsData(load_file("data/day07_crabs_bm.txt"))
        self.assertEqual((345, 343605), crabs.solution_part_1_2())
        # Part 2...
        crabs.part_2_flag = True
        crabs = CrabsData(load_file("data/day07_crabs_test.txt"))
        self.assertEqual((5, 168), crabs.solution_part_1_2(part_2=True))
        crabs = CrabsData(load_file("data/day07_crabs_bm.txt"))
        self.assertEqual((475, 96744904), crabs.solution_part_1_2(part_2=True))

    def test_fuel_cost(self):
        crabs = CrabsData()
        self.assertEqual(6, crabs.fuel_cost(3, 6))
        self.assertEqual(66, crabs.fuel_cost(16, 5))
        self.assertEqual(15, crabs.fuel_cost(0, 5))
        self.assertEqual(45, crabs.fuel_cost(14, 5))

