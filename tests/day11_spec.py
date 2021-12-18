import unittest

from src.day11 import load_octopus_energy_levels, OctopusGrid

class Day11Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.octopus_energy_levels_test = load_octopus_energy_levels('data/day11_octopus_energy_levels_test.txt')
        cls.octopus_energy_levels_tm = load_octopus_energy_levels('data/day11_octopus_energy_levels_tm.txt')

    def test_load_octopus_energy_levels(self):
        self.assertEqual([
            [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
            [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
            [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
            [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
            [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
            [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
            [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
            [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
            [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
            [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
        ], self.octopus_energy_levels_test)

    def test_step(self):
        grid = OctopusGrid([
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1]
        ])

        grid.step()
        self.assertEqual(OctopusGrid([
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ]), grid)

        grid.step()
        self.assertEqual(OctopusGrid([
            [4, 5, 6, 5, 4],
            [5, 1, 1, 1, 5],
            [6, 1, 1, 1, 6],
            [5, 1, 1, 1, 5],
            [4, 5, 6, 5, 4],
        ]), grid)

    def test_count_flashes(self):
        flash_detector = FlashDetector()
        grid = OctopusGrid(self.octopus_energy_levels_test)
        grid.add_listener("step", flash_detector.on_step)
        for o in grid:
            o.add_listener("flash", flash_detector.increment)

        grid.step()
        grid_after_step_001 = OctopusGrid(
            load_octopus_energy_levels('data/day11_octopus_energy_levels_test_step_001.txt')
        )
        self.assertEqual(grid_after_step_001, grid)
        self.assertEqual(0, flash_detector.amount)

        grid.step()
        grid_after_step_002 = OctopusGrid(
            load_octopus_energy_levels('data/day11_octopus_energy_levels_test_step_002.txt')
        )
        self.assertEqual(grid_after_step_002, grid)
        self.assertEqual(35, flash_detector.amount)

        grid.step()
        grid_after_step_003 = OctopusGrid(
            load_octopus_energy_levels('data/day11_octopus_energy_levels_test_step_003.txt')
        )
        self.assertEqual(grid_after_step_003, grid)
        self.assertEqual(80, flash_detector.amount)

        grid.step(7)
        grid_after_step_010 = OctopusGrid(
            load_octopus_energy_levels('data/day11_octopus_energy_levels_test_step_010.txt')
        )
        self.assertEqual(grid_after_step_010, grid)
        self.assertEqual(204, flash_detector.amount)

        grid.step(90)
        grid_after_step_100 = OctopusGrid(
            load_octopus_energy_levels('data/day11_octopus_energy_levels_test_step_100.txt')
        )
        self.assertEqual(grid_after_step_100, grid)
        self.assertEqual(1656, flash_detector.amount)

    def test_flash_detector_tm(self):
        flash_detector = FlashDetector()
        grid_tm = OctopusGrid(self.octopus_energy_levels_tm)
        grid_tm.add_listener("step", flash_detector.on_step)
        for o in grid_tm:
            o.add_listener("flash", flash_detector.increment)

        grid_tm.step(100)
        grid_tm_after_step_100 = OctopusGrid(
            load_octopus_energy_levels('data/day11_octopus_energy_levels_tm_step_100.txt')
        )
        self.assertEqual(grid_tm_after_step_100, grid_tm)
        self.assertEqual(1562, flash_detector.amount)

        is_synchronized = lambda: flash_detector.last_step_count == len(grid_tm)

        while not is_synchronized(): grid_tm.step()

        self.assertEqual(268, flash_detector.steps)
        for o in grid_tm: self.assertEqual(0, o.energy_level)


class FlashDetector:
    def __init__(self):
        self._flash_counts = []

    def increment(self, *_):
        self._flash_counts[-1] += 1

    def on_step(self, *_):
        self._flash_counts.append(0)

    @property
    def amount(self):
        return sum(self._flash_counts)

    @property
    def last_step_count(self):
        return self._flash_counts[-1]

    @property
    def steps(self):
        return len(self._flash_counts)
