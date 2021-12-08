from itertools import chain
from math import copysign
from functools import reduce
from collections import defaultdict

def load_vent_lines(vent_lines_file):
    vent_lines = []
    with open(vent_lines_file, "r") as file:
        for vent_line_spec in file:
            vent_lines.append(VentLine(vent_line_spec))

    return vent_lines

class VentLine:
    def __init__(self, vent_line_spec):
        p1, p2 = [coord.strip().split(',') for coord in vent_line_spec.split('->')]
        self.ends = { tuple(map(int, p1)), tuple(map(int, p2)) }

    def __eq__(self, other):
        return self.ends == other.ends

    def get_points(self):
        x1, y1, x2, y2 = chain.from_iterable(list(self.ends))
        y_step = 0 if y1 == y2 else int(copysign(1, y2 - y1))
        x_step = 0 if x1 == x2 else int(copysign(1, x2 - x1))
        num_points = (abs(x1 - x2) if x_step != 0 else abs(y1 - y2)) + 1
        return { (x1 + i * x_step, y1 + i * y_step) for i in range(0, num_points) }

    def get_crossings(self, other):
        return self.get_points() & other.get_points()

    def is_diagonal(self):
        x1, y1, x2, y2 = chain.from_iterable(list(self.ends))
        return abs(x1 - x2) == abs(y1 - y2)

    def __str__(self):
        return f"VentLine{self.get_points()}"

def count_all_crossings(vent_lines, ignore_diagonals = False):
    filtered_vent_lines = list(filter(lambda v: not v.is_diagonal() if ignore_diagonals else True, vent_lines))

    def update_crossings(crossings_record, vent_line_enum):
        i, vent_line = vent_line_enum
        for j in range(i + 1, len(filtered_vent_lines)):
            crossings = vent_line.get_crossings(filtered_vent_lines[j])
            for c in crossings:
                crossings_record[c] += 1

        return crossings_record

    all_crossings_record = reduce(
        update_crossings,
        enumerate(filtered_vent_lines),
        defaultdict(lambda: 0)
    )

    return len(all_crossings_record.keys())
