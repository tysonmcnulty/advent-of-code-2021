import unittest

from src.day02_bm import calc_course, load_steps, calc_aim


class DayO2Tests(unittest.TestCase):
    def test_load_steps(self):
        self.assertEqual(
            [
                ("forward", 5),
                ("down", 5),
                ("forward", 8),
                ("up", 3),
                ("down", 8),
                ("forward", 2),
            ],
            load_steps("data/day02_steps_test.txt"),
        )
        self.assertEqual(1000, len(load_steps("data/day02_steps_bm.txt")))
        self.assertEqual(1000, len(load_steps("data/day02_steps_tm.txt")))

    def test_calc_steps(self):
        self.assertEqual((15, 10, 150), calc_course("data/day02_steps_test.txt"))
        self.assertEqual((1857, 894, 1660158), calc_course("data/day02_steps_bm.txt"))
        self.assertEqual((1971, 830, 1635930), calc_course("data/day02_steps_tm.txt"))

    def test_calc_aim(self):
        self.assertEqual((15, 60, 900), calc_aim("data/day02_steps_test.txt"))
        self.assertEqual(
            (1857, 864078, 1604592846), calc_aim("data/day02_steps_bm.txt")
        )
        self.assertEqual(
            (1971, 904018, 1781819478), calc_aim("data/day02_steps_tm.txt")
        )
