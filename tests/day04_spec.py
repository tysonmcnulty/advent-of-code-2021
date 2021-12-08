import unittest

from src.day04 import load_bingo, BingoBoard, find_wins

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

    def test_find_first_win(self):
        boards, draws = load_bingo('data/day04_bingo_test.txt')

        first_win_board_index, first_win_draw_index = find_wins(boards, draws).__next__()
        self.assertEqual(2, first_win_board_index)
        self.assertEqual(11, first_win_draw_index)
        self.assertEqual(4512, boards[first_win_board_index].get_score(draws[:(first_win_draw_index + 1)]))

        self.assertFalse(any(map(lambda b: b.has_bingo(set(draws[:first_win_draw_index])), boards)))

        self.assertFalse(boards[0].has_bingo(set(draws[:(first_win_draw_index + 1)])))
        self.assertFalse(boards[1].has_bingo(set(draws[:(first_win_draw_index + 1)])))
        self.assertTrue(boards[2].has_bingo(set(draws[:(first_win_draw_index + 1)])))

    def test_find_first_win_tm(self):
        boards, draws = load_bingo('data/day04_bingo_tm.txt')

        winning_board_index, winning_draw_index = find_wins(boards, draws).__next__()

        self.assertEqual(36, winning_board_index)
        self.assertEqual(30, winning_draw_index)
        self.assertEqual(5685, boards[36].get_score(draws[:31]))

    def test_find_last_win(self):
        boards, draws = load_bingo('data/day04_bingo_test.txt')
        *_, last_win = find_wins(boards, draws)
        last_win_board_index, last_win_draw_index = last_win

        self.assertEqual('13', draws[last_win_draw_index])
        self.assertEqual(1924, boards[last_win_board_index].get_score(draws[:(last_win_draw_index + 1)]))

    def test_find_last_win_tm(self):
        boards, draws = load_bingo('data/day04_bingo_tm.txt')
        *_, last_win = find_wins(boards, draws)

        self.assertEqual(85, last_win[1])
        self.assertEqual(21070, boards[last_win[0]].get_score(draws[:(last_win[1] + 1)]))
