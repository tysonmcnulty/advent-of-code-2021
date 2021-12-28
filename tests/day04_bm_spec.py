import unittest

from src.day04_bm import (
    BingoCard,
    load_file,
    mark_all_cards,
    parse_data,
    create_cards,
    part_1_solution,
    part_2_solution,
)


class Day04Tests(unittest.TestCase):
    def test_load_file(self):
        self.assertEqual(
            19, len(load_file("data/day04_bingo_test.txt")),
        )

    def test_load_file_clean_spaces(self):
        self.assertEqual(
            "8 2 23 4 24", load_file("data/day04_bingo_test.txt")[3],
        )

    def test_parse_data(self):
        self.assertEqual(([2, 5, 8, 10], []), parse_data(["2,5,8,10"]))
        self.assertEqual(
            ([2, 5, 8, 10], [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24]]),
            parse_data(["2,5,8,10", "", "22 13 17 11 0", "8 2 23 4 24",]),
        )
        bingo_data = load_file("data/day04_bingo_test.txt")
        draws, card_lines = parse_data(bingo_data)
        self.assertEqual(27, len(draws))
        self.assertEqual(15, len(card_lines))

    # def test_list_is_none(self):
    #     self.assertEqual(False, list_is_all_none([1, 2, 3]))
    #     self.assertEqual(True, list_is_all_none([None, None]))
    #     self.assertEqual(False, list_is_all_none([None, 5, 66, None]))

    def test_bingocard(self):
        bcard = BingoCard([1, 2, 3])
        self.assertEqual([1, 2, 3], bcard._card_data)

    def test_create_cards(self):
        cards = create_cards(
            [
                [2, 5, 8, 10, 15],
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [6, 7, 8, 7, 6],
                [9, 8, 7, 8, 9],
            ]
        )
        self.assertEqual(5, len(cards[0]._card_data))
        card_lines = parse_data(load_file("data/day04_bingo_test.txt"))[1]
        cards = create_cards(card_lines)
        self.assertEqual(3, len(cards))
        self.assertEqual(5, len(cards[0]._card_data))
        self.assertEqual([2, 0, 12, 3, 7], cards[2]._card_data[4])
        card_lines = parse_data(load_file("data/day04_bingo_bm.txt"))[1]
        self.assertEqual(100, len(create_cards(card_lines)))

    def test_is_winner(self):
        card = BingoCard(
            [
                [2, 5, 8, 10, 15],
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [6, 7, 8, 7, 6],
                [9, 8, 7, 8, 9],
            ]
        )
        self.assertEqual(False, card.check_for_winner())
        self.assertEqual(False, card.winner)
        card = BingoCard(
            [
                [None, 5, None, None, 15],
                [22, 13, 17, None, 0],
                [8, 2, None, None, 24],
                [6, 7, 8, None, 6],
                [9, 8, 7, None, 9],
            ]
        )
        self.assertEqual(True, card.check_for_winner())
        self.assertEqual(True, card.winner)
        card = BingoCard(
            [
                [None, 5, 8, 10, 15],
                [22, 13, 17, 11, 0],
                [8, 2, None, 4, 24],
                [6, 7, 8, 7, 6],
                [9, 8, 7, 8, 9],
            ]
        )
        self.assertEqual(False, card.check_for_winner())
        self.assertEqual(False, card.winner)
        card = BingoCard(
            [
                [2, 5, 8, 10, 15],
                [22, 13, 17, 11, 0],
                [None, None, None, None, None],
                [6, 7, 8, None, 6],
                [9, 8, 7, 8, None],
            ]
        )
        self.assertEqual(True, card.check_for_winner())
        self.assertEqual(True, card.winner)

    def test_mark_card(self):
        card = BingoCard(
            [
                [None, 5, 8, 10, 15],
                [22, 13, 17, 11, 0],
                [8, 2, None, 4, 24],
                [6, 7, 8, 7, 6],
                [9, 8, 7, 8, 9],
            ]
        )
        card.mark_card(24)
        self.assertIsNone(card._card_data[2][4])
        card.mark_card(6)
        self.assertIsNone(card._card_data[3][0])
        self.assertIsNone(card._card_data[3][4])
        self.assertEqual(False, card.winner)
        self.assertEqual(False, card.mark_card(8))
        self.assertEqual(True, card.mark_card(7))
        self.assertEqual(True, card.winner)

    def test_mark_all_cards(self):
        # draws, card_lines = parse_data(load_file("data/day04_bingo_test.txt"))
        # cards = create_cards(card_lines)
        # sample_draws = [6, 10, 3, 18, 5, 22, 5, 23, 4]
        # self.assertEqual([4, 8, None], mark_all_cards(cards, sample_draws))
        draws, card_lines = parse_data(load_file("data/day04_bingo_test.txt"))
        cards = create_cards(card_lines)
        self.assertEqual([13, 14, 11], mark_all_cards(cards, draws))

    def test_unmarked_sum(self):
        card = BingoCard([[None, 10, 15], [17, 11, 0], [2, None, 4, 24],])
        self.assertEqual(83, card.unmarked_sum)

    def test_part_1_solution(self):
        draws, card_lines = parse_data(load_file("data/day04_bingo_test.txt"))
        cards = create_cards(card_lines)
        # get winning_turn, winning_draw, winning_card_sum, solution_1
        self.assertEqual((11, 24, 188, 4512), part_1_solution(cards, draws))

        draws, card_lines = parse_data(load_file("data/day04_bingo_bm.txt"))
        cards = create_cards(card_lines)
        # get winning_turn, winning_draw, winning_card_sum, solution_1
        self.assertEqual((20, 64, 809, 51776), part_1_solution(cards, draws))

    # TODO Part 2: get index & sum of LAST winning card
    #   & multiply by drawn number with the same index;
    #   known that all cards win eventually (no None winning_turns)
    def test_part_2_solution(self):
        draws, card_lines = parse_data(load_file("data/day04_bingo_test.txt"))
        cards = create_cards(card_lines)
        # get last_winning_turn, last_winning_draw,
        #   last_winning_card_sum, solution_2
        self.assertEqual((14, 13, 148, 1924), part_2_solution(cards, draws))
        draws, card_lines = parse_data(load_file("data/day04_bingo_bm.txt"))
        cards = create_cards(card_lines)
        # get last_winning_turn, last_winning_draw,
        #   last_winning_card_sum, solution_2
        self.assertEqual((91, 99, 170, 16830), part_2_solution(cards, draws))

