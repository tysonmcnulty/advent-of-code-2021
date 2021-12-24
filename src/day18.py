from ast import literal_eval

def load_snailfish_numbers(snailfish_numbers_file):
    with open(snailfish_numbers_file, "r") as file:
        return list(map(
            SnailfishNumber.from_literal,
            (line.strip() for line in file)))

class SnailfishNumber:

    @staticmethod
    def from_literal(literal):
        return SnailfishNumber(literal_eval(literal))

    def __init__(self, pair):
        self._pair = list(map(
            lambda n: n if isinstance(n, int) or isinstance(n, SnailfishNumber) else SnailfishNumber(n),
            pair))

        assert len(self._pair) == 2, f"Invalid pair: {self._pair}"

    @property
    def magnitude(self):
        left_magnitude, right_magnitude = tuple(map(
            lambda n: n if isinstance(int, n) else n.magnitude, self._pair))

        return 3 * left_magnitude + 2 * right_magnitude

    @property
    def pair(self): return self._pair

    def reduce(self):
        return self

    def __add__(self, other):
        return SnailfishNumber([self, other])

    def __radd__(self, other):
        return SnailfishNumber([other, self])

    def __eq__(self, other):
        return self.pair == other.pair

    def __str__(self):
        return str(self.pair)

    def __repr__(self):
        return ''.join([
            "SnailfishNumber([",
            f"{str(self.pair[0])}, ",
            str(self.pair[1]),
            "])"
        ])
