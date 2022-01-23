import unittest

from src.day11_bm import (
    load_file,
    EnergyLevelsGrid,
)


class Day11Tests(unittest.TestCase):
    def test_load_file(self):
        energy_grid = load_file("data/day11_octopi_test.txt")
        self.assertEqual(10, len(energy_grid))
        self.assertEqual([5, 4, 8, 3], energy_grid[0][:4])
        self.assertEqual([1, 5, 2, 6], energy_grid[-1][-4:])

    def test_EnergyLevelGrid(self):
        egrid = EnergyLevelsGrid([[1, 2], [3, 4]])
        self.assertEqual(
            [[0, 0, 0, 0], [0, 1, 2, 0], [0, 3, 4, 0], [0, 0, 0, 0]], egrid.grid
        )
        # self.assertEqual([[1, 2], [3, 4]], egrid.grid)

    def test_step(self):
        egrid = EnergyLevelsGrid([[1, 2], [3, 4]])
        egrid.step()
        self.assertEqual(
            [[0, 0, 0, 0], [0, 2, 3, 0], [0, 4, 5, 0], [0, 0, 0, 0]], egrid.grid
        )
        # self.assertEqual([[2, 3], [4, 5]], egrid.grid)
        egrid.grid = [[0, 0, 0, 0], [0, 2, 9, 0], [0, 4, 5, 0], [0, 0, 0, 0]]
        egrid.step()
        self.assertEqual(
            [[0, 0, 0, 0], [0, 4, 0, 0], [0, 6, 7, 0], [0, 0, 0, 0]], egrid.grid
        )
        egrid.grid = [[0, 0, 0, 0], [0, 2, 9, 0], [0, 4, 9, 0], [0, 0, 0, 0]]
        egrid.step()
        self.assertEqual(
            [[0, 0, 0, 0], [0, 5, 0, 0], [0, 7, 0, 0], [0, 0, 0, 0]], egrid.grid
        )

    def test_solution_part_1(self):
        energy_grid = load_file("data/day11_octopi_test.txt")
        egrid = EnergyLevelsGrid(energy_grid)
        self.assertEqual(204, egrid.solution_part_1(steps=10))
        egrid = EnergyLevelsGrid(energy_grid)
        self.assertEqual(1656, egrid.solution_part_1(steps=100))
        energy_grid = load_file("data/day11_octopi_bm.txt")
        # Part 1: How many total flashes after 100 steps?
        egrid = EnergyLevelsGrid(energy_grid)
        self.assertEqual(1725, egrid.solution_part_1(steps=100))

    def test_solution_part_2(self):
        energy_grid = load_file("data/day11_octopi_test.txt")
        egrid = EnergyLevelsGrid(energy_grid)
        self.assertEqual(195, egrid.solution_part_2(max_steps=200))
        energy_grid = load_file("data/day11_octopi_bm.txt")
        # Part 2: First step when all flash simultaneously?
        egrid = EnergyLevelsGrid(energy_grid)
        self.assertEqual(308, egrid.solution_part_2(max_steps=500))

    def test_flash_adjacents(self):
        egrid = EnergyLevelsGrid([[1, 20], [30, 4]])
        egrid.flash_adjacents(1, 2)  # value 20 after padding
        self.assertEqual(
            [[0, 1, 1, 1], [0, 2, 20, 1], [0, 31, 5, 1], [0, 0, 0, 0]], egrid.grid
        )

