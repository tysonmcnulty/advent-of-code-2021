# Day 10: Dumbo Octopus
# -read the energy levels from text file


class EnergyLevelsGrid:
    def __init__(self, energy_grid=[]):
        # pad grid with 0's row & column top, bottom, left & right
        energy_grid = [[0] * len(energy_grid)] + energy_grid + [[0] * len(energy_grid)]
        energy_grid = [[0] + row + [0] for row in energy_grid]
        self.grid = energy_grid[:]
        self.flash_count_this_step = 0
        self.flash_count_total = 0
        # self.already_flashed = [[False] * len(self.grid)] * len(self.grid)
        self.already_flashed = [
            [False for i in range(len(self.grid))] for j in range(len(self.grid))
        ]

    def flash_adjacents(self, row_num, col_num):
        # if > 9, increase all 8 adjacent levels by 1
        self.grid[row_num - 1][col_num - 1] += 1
        self.grid[row_num - 1][col_num] += 1
        self.grid[row_num - 1][col_num + 1] += 1
        self.grid[row_num][col_num - 1] += 1
        self.grid[row_num][col_num + 1] += 1
        self.grid[row_num + 1][col_num - 1] += 1
        self.grid[row_num + 1][col_num] += 1
        self.grid[row_num + 1][col_num + 1] += 1

    def step(self):
        # increase all energy levels by 1
        self.grid = [[x + 1 for x in row] for row in self.grid]
        # flash each >9 non-pad point: increase all 8 adjacent values by 1
        # TODO make multiple passes till all possibles flashed only once
        old_count = -1  # at least one pass, even if count = 0
        self.flash_count_this_step = 0
        while old_count < self.flash_count_this_step:
            old_count = self.flash_count_this_step
            for row_num, row in enumerate(self.grid[1:-1]):
                for col_num, col in enumerate(row[1:-1]):
                    if (
                        self.grid[row_num + 1][col_num + 1] > 9
                        and not self.already_flashed[row_num + 1][col_num + 1]
                    ):
                        self.flash_adjacents(row_num + 1, col_num + 1)
                        self.already_flashed[row_num + 1][col_num + 1] = True
                        self.flash_count_this_step += 1
        # revert all flashed positions to 0 & restore pad values to 0
        self.grid[0] = [0] * len(self.grid)
        self.grid[-1] = [0] * len(self.grid)
        for row_num, row in enumerate(self.grid):
            row[0] = 0
            row[-1] = 0
            # reset flashed positions to 0
            self.grid[row_num] = [0 if x > 9 else x for x in self.grid[row_num]]
        # self.already_flashed = [[False] * len(self.grid)] * len(self.grid)
        self.already_flashed = [
            [False for i in range(len(self.grid))] for j in range(len(self.grid))
        ]
        self.flash_count_total += self.flash_count_this_step
        return self.flash_count_this_step

    def solution_part_1(self, steps=1):
        # Part 1: How many total flashes after 100 steps?
        for step_count in range(steps):
            self.step()
        return self.flash_count_total

    def solution_part_2(self, max_steps=100):
        # Part 2: First step when all flash simultaneously?
        octopus_count = (len(self.grid) - 2) ** 2  # minus pad rows
        for step_count in range(max_steps):
            if self.step() == octopus_count:
                break
        return step_count + 1


def load_file(energy_levels_file):
    """Read the square grid of digits representing energy levels
    and convert to a list of lists of integers (values may temporarily get >9)."""

    with open(energy_levels_file, "r") as efile:
        energy_levels_grid = []
        for line in efile:
            # list_of_digits =
            energy_levels_grid.append([int(x) for x in line.strip()])
    return energy_levels_grid
