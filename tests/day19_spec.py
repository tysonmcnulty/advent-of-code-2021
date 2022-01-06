import unittest

from src.day19 import load_scanners, Scanner, find_placement, place_all

class Day19Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.scanners_test = load_scanners('data/day19_scanners_test.txt')
        cls.scanners_tm = load_scanners('data/day19_scanners_tm.txt')

    def test_get_beacons(self):
        self.assertEqual({
            (404,-588,-901),
            (528,-643,409),
            (-838,591,734),
            (390,-675,-793),
            (-537,-823,-458),
            (-485,-357,347),
            (-345,-311,381),
            (-661,-816,-575),
            (-876,649,763),
            (-618,-824,-621),
            (553,345,-567),
            (474,580,667),
            (-447,-329,318),
            (-584,868,-557),
            (544,-627,-890),
            (564,392,-477),
            (455,729,728),
            (-892,524,684),
            (-689,845,-530),
            (423,-701,434),
            (7,-33,-71),
            (630,319,-379),
            (443,580,662),
            (-789,900,-551),
            (459,-707,401),
        }, self.scanners_test[0].get_beacons())

    def test_find_placement(self):
        self.assertEqual((None, None), find_placement(
            Scanner({(1,1,1)}), Scanner(), threshold = 1
        ))
        self.assertEqual((None, None), find_placement(
            Scanner({(0, 0, 0)}), Scanner({(0, 0, 1)}), threshold = 2
        ))
        self.assertEqual(((-100, -100, -100), 0), find_placement(
            Scanner({(0, 0, 0), (1, 2, 3), (2, 3, 4)}),
            Scanner({(100, 100, 100), (101, 102, 103), (102, 103, 104)}),
            threshold = 3
        ))
        self.assertEqual(((-100, -100, -100), 0), find_placement(
            Scanner({(0, 0, 0), (1, 2, 3), (2, 3, 4), (-2, -7, 15)}),
            Scanner({(100, 100, 100), (101, 102, 103), (102, 103, 104), (-4, 3, -10)}),
            threshold = 3
        ))
        self.assertEqual((None, None), find_placement(
            Scanner({(0, 0, 0), (1, 2, 3), (2, 3, 4), (-2, -7, 15)}),
            Scanner({(100, 100, 100), (101, 102, 103), (102, 103, 104), (-4, 3, -10)}),
            threshold = 4
        ))
        self.assertEqual(((68, -1246, -43), 2), find_placement(
            self.scanners_test[0],
            self.scanners_test[1],
            threshold = 12
        ))
        self.assertEqual(((1125, -72, 168), 20), find_placement(
            self.scanners_test[4].oriented(8),
            self.scanners_test[2],
            threshold = 12
        ))
        self.assertEqual(((-160, -1134, 23), 2), find_placement(
            self.scanners_test[1].oriented(2),
            self.scanners_test[3],
            threshold = 12
        ))
        self.assertEqual(((-88, 113, 1104), 8), find_placement(
            self.scanners_test[1].oriented(2),
            self.scanners_test[4],
            threshold = 12
        ))

    def test_place_all(self):
        self.assertEqual({
            ((0, 0, 0), self.scanners_test[0]),
            ((68, -1246, -43), self.scanners_test[1].oriented(2)),
            ((68, -1246, -43), self.scanners_test[2].oriented(20)),
            ((1105, -1205, 1229), self.scanners_test[3].oriented(2)),
            ((-92, -2380, -20), self.scanners_test[4].oriented(8)),
        }, place_all(self.scanners_test))
