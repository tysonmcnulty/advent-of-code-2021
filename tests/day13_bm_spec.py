import unittest

from src.day13_bm import (
    load_file,
    TransparentOrigamiPaper,
)


class Day12Tests(unittest.TestCase):
    def test_load_file(self):
        dots, instructions = load_file("data/day13_origami_test.txt")
        self.assertEqual(18, len(dots))
        self.assertEqual(2, len(instructions))
        dots, instructions = load_file("data/day13_origami_bm.txt")
        self.assertEqual(776, len(dots))
        self.assertEqual(12, len(instructions))

    def test_fold(self):
        paper = TransparentOrigamiPaper(*load_file("data/day13_origami_test.txt"))
        self.assertEqual(17, paper.fold("y", 7))
        # Part 1 solution: count after first fold = 638 dots
        paper = TransparentOrigamiPaper(*load_file("data/day13_origami_bm.txt"))
        self.assertEqual(
            638, paper.fold(paper.instructions[0][0], paper.instructions[0][1])
        )

    def test_fold_all(self):
        paper = TransparentOrigamiPaper(*load_file("data/day13_origami_test.txt"))
        self.assertEqual(16, paper.fold_all())  # grid reads as capital "O"
        # Part 2: read 8 capital letters from printed grid
        # Part 2 solution: CJCKBAPB
        paper = TransparentOrigamiPaper(*load_file("data/day13_origami_bm.txt"))
        self.assertEqual(97, paper.fold_all())

    # def test_CaveMap(self):
    #     cmap = CaveMap(["aa-bb", "CC-dd"])
    #     self.assertEqual(
    #         {"aa": ["bb"], "bb": ["aa"], "CC": ["dd"], "dd": ["CC"]}, cmap.nodes
    #     )
