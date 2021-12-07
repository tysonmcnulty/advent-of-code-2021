import unittest

from src.day04 import load_bingo, BingoCard, get_earliest_win

class Day04Tests(unittest.TestCase):
    def test_load_bingo(self):
        cards, draws = load_bingo('data/day04_bingo_test.txt')
        self.assertEqual(
            ["7","4","9","5","11","17","23","2","0","14","21","24","10","16","13","6","15","25","12","22","18","20","8","19","3","26","1"]
            , draws
        )

        self.assertEqual(
            [
                BingoCard([
                    ["22", "13", "17", "11", "0"],
                    ["8", "2", "23", "4", "24"],
                    ["21", "9", "14", "16", "7"],
                    ["6", "10", "3", "18", "5"],
                    ["1", "12", "20", "15", "19"]
                ]),
                BingoCard([
                    ["3", "15", "0", "2", "22"],
                    ["9", "18", "13", "17", "5"],
                    ["19", "8", "7", "25", "23"],
                    ["20", "11", "10", "24", "4"],
                    ["14", "21", "16", "12", "6"]
                ]),
                BingoCard([
                    ["14", "21", "17", "24", "4"],
                    ["10", "16", "15", "9", "19"],
                    ["18", "8", "23", "26", "20"],
                    ["22", "11", "13", "6", "5"],
                    [ "2", "0", "12", "3", "7"]
                ])
            ],
            cards
        )

        tm_cards, tm_draws = load_bingo('data/day04_bingo_tm.txt')
        self.assertEqual(100, len(tm_draws))
        self.assertEqual(100, len(tm_cards))

    def test_get_earliest_win(self):
        cards, draws = load_bingo('data/day04_bingo_test.txt')
        winning_card, winning_draw_index = get_earliest_win(cards, draws)

        self.assertFalse(cards[0].has_bingo(set(draws[:12])))
        self.assertFalse(cards[1].has_bingo(set(draws[:12])))
        self.assertTrue(cards[2].has_bingo(set(draws[:12])))
        self.assertFalse(cards[2].has_bingo(set(draws[:11])))

        self.assertEqual(winning_card, cards[2])
        self.assertEqual(winning_draw_index, 11)
