import unittest

from src.day10 import load_navigation_subsystem, parse, get_total_syntax_error_score, get_completion_score, get_total_completion_score

class Day10Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.navigation_subsystem_test = load_navigation_subsystem('data/day10_navigation_subsystem_test.txt')
        cls.navigation_subsystem_tm = load_navigation_subsystem('data/day10_navigation_subsystem_tm.txt')

    def test_load_heightmap(self):
        self.assertEqual(
            [
                "[({(<(())[]>[[{[]{<()<>>",
                "[(()[<>])]({[<{<<[]>>(",
                "{([(<{}[<>[]}>{[]{[(<()>",
                "(((({<>}<{<{<>}{[]{[]{}",
                "[[<[([]))<([[{}[[()]]]",
                "[{[{({}]{}}([{[{{{}}([]",
                "{<[[]]>}<{[{[{[]{()[[[]",
                "[<(<(<(<{}))><([]([]()",
                "<{([([[(<>()){}]>(<<{{",
                "<{([{{}}[<[[[<>{}]]]>[]]",
            ],
            self.navigation_subsystem_test
        )

    def test_parse(self):
        corrupted_line = parse("<{([]}]")
        self.assertEqual(("}", '<{('), next(corrupted_line))
        self.assertEqual("]", next(corrupted_line)[0])
        self.assertEqual(None, next(corrupted_line)[0])

        incomplete_line = parse("{}()[]<>{({}[])<>}")
        self.assertEqual((None, ''), next(incomplete_line))

    def test_get_syntax_error_score(self):
        self.assertEqual(26397, get_total_syntax_error_score(self.navigation_subsystem_test))
        self.assertEqual(464991, get_total_syntax_error_score(self.navigation_subsystem_tm))

    def test_get_completion_score(self):
        self.assertEqual(288957, get_completion_score("[({([[{{"))

    def test_get_total_completion_score(self):
        self.assertEqual(288957, get_total_completion_score(self.navigation_subsystem_test))
        self.assertEqual(3662008566, get_total_completion_score(self.navigation_subsystem_tm))
