import unittest

from functools import partial

from src.day21 import load_pawns, DiracDiceGame, DeterministicDie

class Day21Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pawns_test = load_pawns('data/day21_pawns_test.txt')
        cls.pawns_tm = load_pawns('data/day21_pawns_tm.txt')

    def test_load_pawns(self):
        self.assertEqual((4, 8), self.pawns_test)
        self.assertEqual((7, 2), self.pawns_tm)

    def test_deterministic_game(self):
        die = DeterministicDie()
        def roll_three():
            nonlocal die
            return sum(die.roll() for _ in range(3))

        game = DiracDiceGame(self.pawns_test)

        self.assertEqual(((4, 8), (0, 0), 0), game.state)
        self.assertEqual(0, die.num_rolls)

        game = game.play_turn(roll_three())
        self.assertEqual(((10, 8), (10, 0), 1), game.state)
        self.assertEqual(3, die.num_rolls)

        game = game.play_turn(roll_three())
        self.assertEqual(((10, 3), (10, 3), 0), game.state)
        self.assertEqual(6, die.num_rolls)

        game = game.play_turn(roll_three())
        self.assertEqual(((4, 3), (14, 3), 1), game.state)
        self.assertEqual(9, die.num_rolls)

        game = game.play_turn(roll_three())
        self.assertEqual(((4, 6), (14, 9), 0), game.state)
        self.assertEqual(12, die.num_rolls)

        while not any(map(lambda score: score >= 1000, game.state[1])):
            game = game.play_turn(roll_three())

        self.assertEqual(((10, 3), (1000, 745), 1), game.state)
        self.assertEqual(993, die.num_rolls)

    def test_deterministic_game_tm(self):
        die = DeterministicDie()
        def roll_three():
            nonlocal die
            return sum(die.roll() for _ in range(3))

        game = DiracDiceGame(self.pawns_tm)

        while not any(map(lambda score: score >= 1000, game.state[1])):
            game = game.play_turn(roll_three())

        self.assertEqual((1008, 788), game.score)
        self.assertEqual(861, die.num_rolls)
