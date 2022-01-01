import unittest

from src.day08_bm import (
    load_file,
    count_digits_1478,
    SevenSegmentMap,
    solution_part_2,
)


class Day08Tests(unittest.TestCase):
    def test_load_file(self):
        signals, outputs = load_file("data/day08_7segment_test.txt")
        self.assertEqual(10, len(signals))
        self.assertEqual("be", signals[0][0])
        self.assertEqual("gfec", signals[1][9])
        self.assertEqual(10, len(outputs))
        self.assertEqual("fdgacbe", outputs[0][0])
        self.assertEqual("bagce", outputs[9][3])
        signals, outputs = load_file("data/day08_7segment_bm.txt")
        self.assertEqual(200, len(outputs))

    def test_count_digits_1478(self):
        outputs = load_file("data/day08_7segment_test.txt")
        self.assertEqual(26, count_digits_1478(outputs))
        outputs = load_file("data/day08_7segment_bm.txt")
        # Part 1 solution...
        self.assertEqual(239, count_digits_1478(outputs))

    def test_process_one_line_part_2(self):
        signal = [
            "be",
            "cfbegad",
            "cbdgef",
            "fgaecd",
            "cgeb",
            "fdcge",
            "agebfd",
            "fecdb",
            "fabcd",
            "edb",
        ]
        output = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
        ssm = SevenSegmentMap(signal, output)
        self.assertEqual({"b", "e"}, ssm.segments_map[1])
        self.assertEqual({"c", "g", "e", "b"}, ssm.segments_map[4])
        self.assertEqual({"e", "d", "b"}, ssm.segments_map[7])
        self.assertEqual({"a", "b", "c", "d", "e", "f", "g"}, ssm.segments_map[8])
        self.assertEqual({"a", "c", "d", "e", "f", "g"}, ssm.segments_map[6])
        self.assertEqual({"a", "b", "d", "e", "f", "g"}, ssm.segments_map[0])
        self.assertEqual({"b", "c", "d", "e", "f", "g"}, ssm.segments_map[9])
        self.assertEqual({"c", "d", "e", "f", "g"}, ssm.segments_map[5])
        self.assertEqual({"a", "b", "c", "d", "f"}, ssm.segments_map[2])
        self.assertEqual({"b", "c", "d", "e", "f"}, ssm.segments_map[3])
        self.assertEqual(8394, ssm.output_number)

    def test_solution_part_2(self):
        signals, outputs = load_file("data/day08_7segment_test.txt")
        self.assertEqual(61229, solution_part_2(signals, outputs))
        signals, outputs = load_file("data/day08_7segment_bm.txt")
        self.assertEqual(946346, solution_part_2(signals, outputs))
