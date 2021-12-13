import unittest

from src.day08 import load_display_data, DisplayDecoder

class Day08Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.display_data_test = load_display_data('data/day08_display_data_test.txt')
        cls.display_data_tm = load_display_data('data/day08_display_data_tm.txt')
        cls.decoders_test = list(map(lambda d: DisplayDecoder(*d), cls.display_data_test))
        cls.decoders_tm = list(map(lambda d: DisplayDecoder(*d), cls.display_data_tm))

    def test_load_display_data(self):
        self.assertEqual(
            [
                (["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"], ["fdgacbe", "cefdb", "cefbgd", "gcbe"]),
                (["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"], ["fcgedb", "cgb", "dgebacf", "gc"]),
                (["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"], ["cg", "cg", "fdcagb", "cbg"]),
                (["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"], ["efabcd", "cedba", "gadfec", "cb"]),
                (["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"], ["gecf", "egdcabf", "bgf", "bfgea"]),
                (["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"], ["gebdcfa", "ecba", "ca", "fadegcb"]),
                (["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"], ["cefg", "dcbef", "fcge", "gbcadfe"]),
                (["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"], ["ed", "bcgafe", "cdgba", "cbgef"]),
                (["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"], ["gbdfcae", "bgc", "cg", "cgb"]),
                (["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"], ["fgae", "cfgab", "fg", "bagce"]),
            ],
            self.display_data_test
        )
        self.assertEqual(200, len(self.display_data_tm))

    def test_display_decoder(self):
        easy_digit_matcher = lambda digit: digit in "1478"
        all_digit_matcher = lambda digit: digit in "0123456789"

        self.assertEqual(26, sum(map(
            lambda decoder: decoder.count_matching(easy_digit_matcher),
            self.decoders_test
        )))

        self.assertEqual(40, sum(map(
            lambda decoder: decoder.count_matching(all_digit_matcher),
            self.decoders_test
        )))

        self.assertEqual(330, sum(map(
            lambda decoder: decoder.count_matching(easy_digit_matcher),
            self.decoders_tm
        )))


    def test_readout_values(self):
        self.assertEqual(61229, sum(map(lambda d: d.get_readout_value(), self.decoders_test)))
        self.assertEqual(1010472, sum(map(lambda d: d.get_readout_value(), self.decoders_tm)))
