import unittest

from src.day04 import load_bingo, BingoBoard, find_win

class Day04Tests(unittest.TestCase):
    def test_load_bingo(self):
        boards, draws = load_bingo('data/day04_bingo_test.txt')
        self.assertEqual(
            ["7","4","9","5","11","17","23","2","0","14","21","24","10","16","13","6","15","25","12","22","18","20","8","19","3","26","1"]
            , draws
        )

        self.assertEqual(
            [
                BingoBoard([
                    ["22", "13", "17", "11", "0"],
                    ["8", "2", "23", "4", "24"],
                    ["21", "9", "14", "16", "7"],
                    ["6", "10", "3", "18", "5"],
                    ["1", "12", "20", "15", "19"]
                ]),
                BingoBoard([
                    ["3", "15", "0", "2", "22"],
                    ["9", "18", "13", "17", "5"],
                    ["19", "8", "7", "25", "23"],
                    ["20", "11", "10", "24", "4"],
                    ["14", "21", "16", "12", "6"]
                ]),
                BingoBoard([
                    ["14", "21", "17", "24", "4"],
                    ["10", "16", "15", "9", "19"],
                    ["18", "8", "23", "26", "20"],
                    ["22", "11", "13", "6", "5"],
                    [ "2", "0", "12", "3", "7"]
                ])
            ],
            boards
        )

        tm_boards, tm_draws = load_bingo('data/day04_bingo_tm.txt')
        self.assertEqual(100, len(tm_draws))
        self.assertEqual(100, len(tm_boards))

    def test_find_win(self):
        boards, draws = load_bingo('data/day04_bingo_test.txt')

        winning_board_index, winning_draw_index = find_win(boards, draws)
        self.assertEqual(winning_board_index, 2)
        self.assertEqual(winning_draw_index, 11)

        self.assertFalse(any(map(lambda c: c.has_bingo(set(draws[:11])), boards)))

        self.assertFalse(boards[0].has_bingo(set(draws[:12])))
        self.assertFalse(boards[1].has_bingo(set(draws[:12])))
        self.assertTrue(boards[2].has_bingo(set(draws[:12])))

        self.assertEqual(4512, boards[2].get_score(draws[:12]))

    def test_find_win_tm(self):
        boards, draws = load_bingo('data/day04_bingo_tm.txt')

        winning_board_index, winning_draw_index = find_win(boards, draws)

        self.assertEqual(winning_board_index, 36)
        self.assertEqual(winning_draw_index, 30)
        self.assertEqual(5685, boards[36].get_score(draws[:31]))
