import os
import unittest

from src.day22 import load_reboot_steps, Cuboid, reboot, total_volume

class Day22Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reboot_steps_test = load_reboot_steps('data/day22_reboot_steps_test.txt')
        cls.reboot_steps_test_part_two = load_reboot_steps('data/day22_reboot_steps_test_part_two.txt')
        cls.reboot_steps_tm = load_reboot_steps('data/day22_reboot_steps_tm.txt')

    def test_load_reboot_steps(self):
        self.assertEqual([
            ("on", Cuboid( x=(-20, 26 + 1), y=(-36, 17 + 1), z=(-47, 7 + 1) )),
            ("on", Cuboid( x=(-20, 33 + 1), y=(-21, 23 + 1), z=(-26, 28 + 1) )),
            ("on", Cuboid( x=(-22, 28 + 1), y=(-29, 23 + 1), z=(-38, 16 + 1) )),
        ], self.reboot_steps_test[:3])

    def test_cuboid_add(self):
        first = Cuboid((0, 10), (0, 10), (0, 10))
        second = Cuboid((1, 11), (2, 12), (3, 13))

        self.assertEqual({
            Cuboid((0, 10), (0, 10), (0, 3)),
            Cuboid((0, 10), (0, 2), (3, 10)),
            Cuboid((0, 1), (2, 10), (3, 10)),
        }, first - second)

        self.assertEqual({
            Cuboid((0, 10), (0, 10), (0, 3)),
            Cuboid((0, 10), (0, 2), (3, 10)),
            Cuboid((0, 1), (2, 10), (3, 10)),
            Cuboid((1, 11), (2, 12), (3, 13))
        }, first + second)

        self.assertEqual(
            set(),
            Cuboid((0, 1), (0, 1), (0, 1)) - Cuboid((0, 10), (0, 10), (0, 10))
        )

    def test_cuboid_split(self):
        cuboid = Cuboid((0, 10), (0, 10), (0, 10))
        self.assertEqual({
            Cuboid((0, 2), (0, 10), (0, 10)),
            Cuboid((2, 5), (0, 10), (0, 10)),
            Cuboid((5, 10), (0, 10), (0, 10))
        }, cuboid.split_x(*(2, 5)))
        self.assertEqual({
            Cuboid((0, 10), (0, 3), (0, 10)),
            Cuboid((0, 10), (3, 10), (0, 10)),
        }, cuboid.split_y(*(-4, 3)))
        self.assertEqual({
            Cuboid((0, 10), (0, 10), (0, 5)),
            Cuboid((0, 10), (0, 10), (5, 10)),
        }, cuboid.split_z(*(5, 10)))

    def test_reboot_initialization(self):
        cuboids_test = reboot(self.reboot_steps_test[:20])
        self.assertEqual(590784, total_volume(cuboids_test))

        cuboids_tm = reboot(self.reboot_steps_tm[:20])
        self.assertEqual(577205, total_volume(cuboids_tm))

    def test_reboot(self):
        cuboids_test_part_two = reboot(self.reboot_steps_test_part_two)
        self.assertEqual(2758514936282235, total_volume(cuboids_test_part_two))

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_reboot_tm(self):
        cuboids_tm = reboot(self.reboot_steps_tm)
        self.assertEqual(1197308251666843, total_volume(cuboids_tm))
