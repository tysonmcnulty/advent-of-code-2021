import re

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

    @property
    def num_rolls(self):
        return self._num_rolls
