import unittest

from src.day10_bm import (
    load_file,
    NavData,
)


class Day08Tests(unittest.TestCase):
    def test_load_file(self):
        lines = load_file("data/day10_chunks_test.txt")
        self.assertEqual(10, len(lines))
        self.assertEqual("[({(", lines[0][:4])
        self.assertEqual("]]]>[]]", lines[-1][-7:])

    def test_NavData(self):
        sample = [[4, 1, 55, 88], [34, 222, 90, 1]]
        nav_data = NavData(sample)
        self.assertEqual(2, len(nav_data.lines))
        self.assertEqual([222, 90, 1], nav_data.lines[1][-3:])
        nav_data = NavData(load_file("data/day10_chunks_test.txt"))
        self.assertEqual("[({(", nav_data.lines[0][:4])
        nav_data._illegal_count["]"] += 3
        self.assertEqual(171, nav_data.syntax_error_score)
        nav_data._illegal_count["}"] += 2
        self.assertEqual(2565, nav_data.syntax_error_score)

    def test_illegal_char(self):
        nav_data = NavData(load_file("data/day10_chunks_test.txt"))
        self.assertIsNone(nav_data.first_illegal_char(r"[<>({}){}[([])<>]]")[0])
        self.assertEqual(
            "}", nav_data.first_illegal_char(r"{([(<{}[<>[]}>{[]{[(<()>")[0]
        )
        self.assertEqual(
            (">", ["{", "x", "x", "x", "x", ">"]),
            nav_data.first_illegal_char(r"{()()>"),
        )  # verify checking first char
        self.assertEqual(
            ["x", "x", "x", "x", "x", "x"], nav_data.first_illegal_char(r"{()()}")[1],
        )  # complete, uncorrupted line
        self.assertEqual(
            ["{", "x", "x", "("], nav_data.first_illegal_char(r"{()(")[1],
        )  # incomplete, uncorrupted line

    def test_solution_part_1(self):
        nav_data = NavData(load_file("data/day10_chunks_test.txt"))
        self.assertEqual(26397, nav_data.solution_part_1)
        nav_data = NavData(load_file("data/day10_chunks_bm.txt"))
        # Part 1 solution: 323613 from 45 corrupt lines of 90
        self.assertEqual(323613, nav_data.solution_part_1)

    def test_autocomplete_score(self):
        nav_data = NavData()
        nav_data._completion_strings = [r"}}]])})]", r")}>]})", r"]})"]
        # nav_data._completion_strings = [r"}}]])})]"]  # 288957
        # nav_data._completion_strings = [r")}>]})"]  # 5566
        self.assertEqual(5566, nav_data.autocomplete_score)

    def test_autocomplete_line(self):
        nav_data = NavData()
        self.assertEqual(
            r"}}]])})]", nav_data.autocomplete_line(r"[({(<(())[]>[[{[]{<()<>>")
        )

    def test_solution_part_2(self):
        nav_data = NavData(load_file("data/day10_chunks_test.txt"))
        self.assertEqual(288957, nav_data.solution_part_2)
        nav_data = NavData(load_file("data/day10_chunks_bm.txt"))
        # Part 2 solution: 3103006161 middle autocomplete score
        self.assertEqual(3103006161, nav_data.solution_part_2)
