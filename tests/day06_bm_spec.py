import unittest

from src.day06_bm import (
    load_file,
    load_file_part_2,
    age_one_day,
    age_one_day_part_2,
    part_1_simulation,
    part_2_simulation,
)


class Day05Tests(unittest.TestCase):
    def test_load_file(self):
        ages = load_file("data/day06_lanternfish_test.txt")
        self.assertEqual(5, len(ages))
        self.assertEqual([3, 4, 3, 1, 2], ages)
        ages = load_file("data/day06_lanternfish_bm.txt")
        self.assertEqual(300, len(ages))
        self.assertEqual([1, 4, 2, 4, 5], ages[:5])
        self.assertEqual([4, 2, 2, 2, 3], ages[-5:])

    def test_age_one_day(self):
        ages = [3, 4, 3, 1, 2]  # the test data
        self.assertEqual([2, 3, 2, 0, 1], age_one_day(ages))
        self.assertEqual([1, 2, 1, 6, 0, 8], age_one_day([2, 3, 2, 0, 1]))
        self.assertEqual([0, 1, 0, 5, 6, 7, 8], age_one_day([1, 2, 1, 6, 0, 8]))

    def test_part_1__simulation(self):
        ages = [3, 4, 3, 1, 2]  # the test data
        self.assertEqual(26, len(part_1_simulation(ages, 18)))
        self.assertEqual(5934, len(part_1_simulation(ages, 80)))
        ages_bm = load_file("data/day06_lanternfish_bm.txt")
        self.assertEqual(349549, len(part_1_simulation(ages_bm, 80)))
        # # Part 2: 256 days ...list of fish too big

    def test_load_file_part_2(self):
        age_counts = load_file_part_2("data/day06_lanternfish_test.txt")
        # list of test data is [3, 4, 3, 1, 2]
        self.assertEqual(9, len(age_counts))
        self.assertEqual(5, sum(age_counts))
        self.assertEqual(
            [0, 1, 1, 2, 1, 0, 0, 0, 0], age_counts,
        )
        age_counts = load_file_part_2("data/day06_lanternfish_bm.txt")
        self.assertEqual(300, sum(age_counts))
        self.assertEqual(
            [0, 80, 53, 51, 63, 53, 0, 0, 0], age_counts,
        )

    def test_age_one_day_part_2(self):
        age_counts = [0, 1, 1, 2, 1, 0, 0, 0, 0]  # the test data
        self.assertEqual(
            [1, 1, 2, 1, 0, 0, 0, 0, 0], age_one_day_part_2(age_counts),
        )
        self.assertEqual(
            [1, 2, 1, 0, 0, 0, 1, 0, 1],
            age_one_day_part_2([1, 1, 2, 1, 0, 0, 0, 0, 0]),
        )
        self.assertEqual(
            [2, 1, 0, 0, 0, 1, 1, 1, 1],
            age_one_day_part_2([1, 2, 1, 0, 0, 0, 1, 0, 1]),
        )

    def test_part_2__simulation(self):
        age_counts = [0, 1, 1, 2, 1, 0, 0, 0, 0]  # the test data
        self.assertEqual(26, sum(part_2_simulation(age_counts, 18)))
        age_counts = [0, 1, 1, 2, 1, 0, 0, 0, 0]  # the test data
        self.assertEqual(5934, sum(part_2_simulation(age_counts, 80)))
        age_counts_bm = load_file_part_2("data/day06_lanternfish_bm.txt")
        self.assertEqual(349549, sum(part_2_simulation(age_counts_bm, 80)))
        # Part 2: 256 days ...big numbers
        age_counts = [0, 1, 1, 2, 1, 0, 0, 0, 0]  # the test data
        self.assertEqual(26984457539, sum(part_2_simulation(age_counts, 256)))
        age_counts_bm = load_file_part_2("data/day06_lanternfish_bm.txt")
        self.assertEqual(1589590444365, sum(part_2_simulation(age_counts_bm, 256)))

