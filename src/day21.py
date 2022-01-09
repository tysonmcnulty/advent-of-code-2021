import re

from collections import Counter
from itertools import product
from functools import cache

def load_pawns(starting_squares_file):
    with open(starting_squares_file, "r") as file:
        return tuple(int(re.match(r"Player \d+ starting position: (\d+)", line).groups()[0]) for line in file)

class DiracDiceGame:
    def __init__(self, pawns = (0, 0), score = (0, 0), player_index = 0):
        self._pawns = pawns
        self._score = score
        self._player_index = player_index

    @property
    def state(self): return (self.pawns, self.score, self.player_index)

    @property
    def pawns(self): return self._pawns

    @property
    def score(self): return self._score

    @property
    def player_index(self): return self._player_index

    def __repr__(self):
        return f"DiracDiceGame({self.state})"

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def play_turn(self, roll):
        next_pawns_list = list(self.pawns)
        next_pawns_list[self.player_index] = (next_pawns_list[self.player_index] + roll - 1) % 10 + 1
        next_pawns = tuple(next_pawns_list)

        next_score_list = list(self.score)
        next_score_list[self.player_index] += next_pawns[self.player_index]
        next_score = tuple(next_score_list)

        next_player_index = (self.player_index + 1) % 2

        return DiracDiceGame(next_pawns, next_score, next_player_index)

class DeterministicDie:
    def __init__(self):
        self._num_rolls = 0
        self._value = 100

    def roll(self):
        self._value = self._value % 100 + 1
        self._num_rolls += 1
        return self._value

    def roll_many(self, times = 3):
        return sum(self.roll() for _ in range(times))

    @property
    def num_rolls(self):
        return self._num_rolls

class QuantumDie:
    @cache
    def roll(self):
        return Counter((1, 2, 3))

    @cache
    def roll_many(self, times = 3):
        if times == 1: return self.roll()

        return Counter(map(sum, product((1, 2, 3), repeat = times)))


def count_all_played_turns(game, quantum_die_rolls, winning_score = 21):
    next_game_counter = Counter()
    p1_wins_counter = Counter()
    p2_wins_counter = Counter()
    for roll, multiplicity in quantum_die_rolls.items():
        next_game = game.play_turn(roll)
        if next_game.score[0] >= winning_score:
            p1_wins_counter[next_game] += multiplicity
        elif next_game.score[1] >= winning_score:
            p2_wins_counter[next_game] += multiplicity
        else:
            next_game_counter[next_game] += multiplicity

    return next_game_counter, p1_wins_counter, p2_wins_counter

def count_all_wins(game, quantum_die, rolls_per_turn = 3, winning_score = 21):
    p1_wins = Counter()
    p2_wins = Counter()
    continuing = Counter()

    continuing[game] = 1

    while len(continuing.keys()) > 0:
        no_wins = Counter()
        for game, multiplicity in continuing.items():
            next_no_wins, next_p1_wins, next_p2_wins = count_all_played_turns(game, quantum_die.roll_many(rolls_per_turn), winning_score)
            for k, v in next_no_wins.items(): no_wins[k] += v * multiplicity
            for k, v in next_p1_wins.items(): p1_wins[k] += v * multiplicity
            for k, v in next_p2_wins.items(): p2_wins[k] += v * multiplicity

        continuing = no_wins

    return p1_wins, p2_wins
