from ast import literal_eval
from math import floor, ceil

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

    @staticmethod
    def from_traversal(traversal):
        left = []
        right = []
        for item in traversal:
            if item[1] == tuple():
                return item[0]
            if item[1] < (1,):
                left.append((item[0], item[1][1:]))
            else:
                right.append((item[0], item[1][1:]))

        return SnailfishNumber([
            SnailfishNumber.from_traversal(left),
            SnailfishNumber.from_traversal(right)
        ])

    @property
    def magnitude(self):
        left_magnitude, right_magnitude = tuple(map(
            lambda n: n if isinstance(n, int) else n.magnitude, self._pair))

        return 3 * left_magnitude + 2 * right_magnitude

    @property
    def pair(self): return self._pair

    def reduced(self):
        i = 0
        traversal = self.traverse()

        def explode():
            nonlocal i
            nonlocal traversal
            if i - 1 >= 0:
                traversal[i - 1] = (traversal[i - 1][0] + traversal[i][0], traversal[i - 1][1])

            if i + 2 < len(traversal):
                traversal[i + 2] = (traversal[i + 1][0] + traversal[i + 2][0], traversal[i + 2][1])

            traversal[i] = (0, traversal[i][1][:-1])
            del traversal[i + 1]

        def split():
            nonlocal i
            nonlocal traversal
            left = (floor(traversal[i][0] / 2), traversal[i][1] + (0,))
            right = (ceil(traversal[i][0] / 2), traversal[i][1] + (1,))
            traversal[i] = left
            traversal.insert(i + 1, right)

        while i < len(traversal):
            if len(traversal[i][1]) > 4: explode()
            i += 1

        i = 0
        while i < len(traversal):
            if len(traversal[i][1]) > 4:
                explode()
                i = max(i - 1, 0)
            elif traversal[i][0] >= 10:
                split()
            else:
                i += 1

        return SnailfishNumber.from_traversal(traversal)

    def traverse(self, depth = tuple()):
        traversal = []
        for i in (0, 1):
            if isinstance(self._pair[i], int):
                traversal.append((self._pair[i], depth + (i,)))
            else:
                traversal += self._pair[i].traverse(depth + (i,))

        return traversal


    def __add__(self, other):
        return SnailfishNumber([self, other]).reduced()

    def __radd__(self, other):
        return SnailfishNumber([other, self]).reduced()

    def __eq__(self, other):
        try:
            return self.pair == other.pair
        except:
            return False

    def __str__(self):
        return f"[{str(self.pair[0])}, {str(self.pair[1])}]"

    def __repr__(self):
        return ''.join([
            "SnailfishNumber([",
            str(self),
            "])"
        ])
