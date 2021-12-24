import unittest

from src.day17 import load_target_area, launch_probe, aim, aim_high, get_highest_y_position

class Day17Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.target_area_test = load_target_area('data/day17_target_area_test.txt')
        cls.target_area_tm = load_target_area('data/day17_target_area_tm.txt')

    def test_load_target_area(self):
        self.assertEqual([[20, 30], [-10, -5]], self.target_area_test)
        self.assertEqual([[56, 76], [-162, -134]], self.target_area_tm)

    def test_launch_probe(self):
        probe = launch_probe((6, 3))

        positions = [ next(probe) for _ in range(10) ]

        self.assertEqual([
            (0, 0), (6, 3), (11, 5), (15, 6), (18, 6),
            (20, 5), (21, 3), (21, 0), (21, -4), (21, -9)
        ], positions)

    def test_aim_high(self):
        velocity_test = aim_high(self.target_area_test)
        self.assertEqual((6, 9), velocity_test)
        self.assertEqual(45, get_highest_y_position(velocity_test))

        velocity_tm = aim_high(self.target_area_tm)
        self.assertEqual((11, 161), velocity_tm)
        self.assertEqual(13041, get_highest_y_position(velocity_tm))

    def test_aim(self):
        velocities_test = aim(self.target_area_test)
        self.assertEqual(112, len(velocities_test))

        velocities_tm = aim(self.target_area_tm)
        self.assertEqual(1031, len(velocities_tm))
