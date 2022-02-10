import unittest

from src.day14_bm import (
    load_file,
    ExtendedPolymer,
)


class Day14Tests(unittest.TestCase):
    def test_load_file(self):
        template, rules, pairs = load_file("data/day14_polymer_test.txt")
        self.assertEqual("NNCB", "".join(template))
        self.assertEqual(16, len(rules))
        self.assertEqual("C", rules["CN"])
        self.assertEqual(3, len(pairs))
        self.assertEqual({"NN": 1, "NC": 1, "CB": 1}, pairs)
        template, rules, pairs = load_file("data/day14_polymer_bm.txt")
        self.assertEqual("SHHNCOPHONHFBVNKCFFC", "".join(template))
        self.assertEqual(100, len(rules))
        self.assertEqual("B", rules["KC"])
        self.assertEqual(19, len(pairs))

    def test_insert_step(self):
        poly = ExtendedPolymer(*load_file("data/day14_polymer_test.txt"))
        # self.assertEqual("NCNBCHB", poly.insert_steps(1))
        self.assertEqual(
            # {"NN": 0, "NC": 1, "CB": 0, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1},
            {"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1},
            poly.insert_steps(1),
        )
        # 2 steps, should be NBCCNBBBCBHCB
        poly = ExtendedPolymer(*load_file("data/day14_polymer_test.txt"))
        self.assertEqual(
            {
                # "NN": 0,
                # "NC": 0,
                "CB": 2,
                "CN": 1,
                "NB": 2,
                "BC": 2,
                # "CH": 0,
                # "HB": 0,
                "CC": 1,
                "BB": 2,
                "BH": 1,
                "HC": 1,
            },
            poly.insert_steps(2),
        )
        # 3 steps
        poly = ExtendedPolymer(*load_file("data/day14_polymer_test.txt"))
        self.assertEqual(
            {
                "NB": 4,
                "BB": 4,
                "BC": 3,
                "CN": 2,
                "NC": 1,
                "CC": 1,
                "BN": 2,
                "CH": 2,
                "HB": 3,
                "BH": 1,
                "HH": 1,
            },
            poly.insert_steps(3),
        )
        # # 2 more steps
        # self.assertEqual("NBBBCNCCNBBNBNBBCHBHHBCHB", poly.insert_steps(2))
        # # 7 more steps
        # self.assertEqual(3073, len(poly.insert_steps(10 - 3)))

    def test_solution_part_1_2(self):
        poly = ExtendedPolymer(*load_file("data/day14_polymer_test.txt"))
        # Part 1 retested after refactoring to pairs_count from a big string
        self.assertEqual(1588, poly.calc_difference(10))
        poly = ExtendedPolymer(*load_file("data/day14_polymer_bm.txt"))
        # Part 1 solution: difference = 2549 after 10 steps (N:3200 - C:651)
        self.assertEqual(2549, poly.calc_difference(10))
        # # Part 2 same as Part 1 but 40 steps
        poly = ExtendedPolymer(*load_file("data/day14_polymer_test.txt"))
        self.assertEqual(2188189693529, poly.calc_difference(40))
        poly = ExtendedPolymer(*load_file("data/day14_polymer_bm.txt"))
        # Part 2 solution: difference after 40 steps
        # (N:3343348437631 - C:826447333421)
        self.assertEqual(2516901104210, poly.calc_difference(40))
