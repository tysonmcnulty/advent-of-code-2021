import os
import unittest

from collections import Counter

from src.day21 import load_pawns, DiracDiceGame, DeterministicDie, QuantumDie, count_all_played_turns, count_all_wins

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
        game = DiracDiceGame(self.pawns_test)

        self.assertEqual(((4, 8), (0, 0), 0), game.state)
        self.assertEqual(0, die.num_rolls)

        game = game.play_turn(die.roll_many(3))
        self.assertEqual(((10, 8), (10, 0), 1), game.state)
        self.assertEqual(3, die.num_rolls)

        game = game.play_turn(die.roll_many(3))
        self.assertEqual(((10, 3), (10, 3), 0), game.state)
        self.assertEqual(6, die.num_rolls)

        game = game.play_turn(die.roll_many(3))
        self.assertEqual(((4, 3), (14, 3), 1), game.state)
        self.assertEqual(9, die.num_rolls)

        game = game.play_turn(die.roll_many(3))
        self.assertEqual(((4, 6), (14, 9), 0), game.state)
        self.assertEqual(12, die.num_rolls)

        while not any(map(lambda score: score >= 1000, game.state[1])):
            game = game.play_turn(die.roll_many(3))

        self.assertEqual(((10, 3), (1000, 745), 1), game.state)
        self.assertEqual(993, die.num_rolls)

    def test_deterministic_game_tm(self):
        die = DeterministicDie()
        game = DiracDiceGame(self.pawns_tm)

        while not any(map(lambda score: score >= 1000, game.state[1])):
            game = game.play_turn(die.roll_many(3))

        self.assertEqual((1008, 788), game.score)
        self.assertEqual(861, die.num_rolls)

    def test_quantum_die(self):
        die = QuantumDie()

        self.assertEqual(Counter({ 1: 1, 2: 1, 3: 1 }), die.roll_many(1))
        self.assertEqual(Counter({ 2: 1, 3: 2, 4: 3, 5: 2, 6: 1 }), die.roll_many(2))
        self.assertEqual(Counter({ 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }), die.roll_many(3))

    def test_quantum_game_p1_wins(self):
        quantum_die = QuantumDie()
        p1_game = DiracDiceGame((5, 5), (16, 16), 0)

        next_game_counter, p1_wins, p2_wins = count_all_played_turns(p1_game, quantum_die.roll_many(3))

        self.assertEqual(Counter({
            DiracDiceGame((1, 5), (17, 16), 1): 7,
            DiracDiceGame((2, 5), (18, 16), 1): 6,
            DiracDiceGame((3, 5), (19, 16), 1): 3,
            DiracDiceGame((4, 5), (20, 16), 1): 1,
        }), next_game_counter)
        self.assertEqual(Counter({
            DiracDiceGame((8, 5), (24, 16), 1): 1,
            DiracDiceGame((9, 5), (25, 16), 1): 3,
            DiracDiceGame((10, 5), (26, 16), 1): 6,
        }), p1_wins)
        self.assertEqual(Counter(), p2_wins)

    def test_quantum_game_p2_wins(self):
        quantum_die = QuantumDie()
        p2_game = DiracDiceGame((5, 5), (16, 16), 1)

        next_game_counter, p1_wins, p2_wins = count_all_played_turns(p2_game, quantum_die.roll_many(3))

        self.assertEqual(Counter({
            DiracDiceGame((5, 1), (16, 17), 0): 7,
            DiracDiceGame((5, 2), (16, 18), 0): 6,
            DiracDiceGame((5, 3), (16, 19), 0): 3,
            DiracDiceGame((5, 4), (16, 20), 0): 1,
        }), next_game_counter)
        self.assertEqual(Counter(), p1_wins)
        self.assertEqual(Counter({
            DiracDiceGame((5, 8), (16, 24), 0): 1,
            DiracDiceGame((5, 9), (16, 25), 0): 3,
            DiracDiceGame((5, 10), (16, 26), 0): 6,
        }), p2_wins)

    def test_count_all_wins_short_game(self):
        quantum_die = QuantumDie()
        game = DiracDiceGame()

        p1_wins, p2_wins = count_all_wins(game, quantum_die, winning_score=10)
        self.assertEqual(
            (3825777, 1873814),
            (sum(p1_wins.values()), sum(p2_wins.values()))
        )

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_count_all_wins(self):
        quantum_die = QuantumDie()
        game = DiracDiceGame(self.pawns_test)

        p1_wins, p2_wins = count_all_wins(game, quantum_die)
        self.assertEqual(
            (444356092776315, 341960390180808),
            (sum(p1_wins.values()), sum(p2_wins.values()))
        )

    @unittest.skipUnless(bool(os.getenv('AOC_RUN_SLOW_TESTS')), 'slow test')
    def test_count_all_wins_tm(self):
        quantum_die = QuantumDie()
        game = DiracDiceGame(self.pawns_tm)

        p1_wins, p2_wins = count_all_wins(game, quantum_die)

        self.assertEqual(
            (131180774190079, 123918341809156),
            (sum(p1_wins.values()), sum(p2_wins.values()))
        )
