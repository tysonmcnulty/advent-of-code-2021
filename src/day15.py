from functools import partial
from collections import defaultdict

def load_risk_levels(risk_levels_file):
    with open(risk_levels_file, "r") as file:
        return [ list(map(int, line.strip())) for line in file ]

def navigate(cave, start):
    def get_total_risk_level(min_risks, start, end, exclude_start = False):
        return min_risks[end] if not exclude_start else min_risks[end] - min_risks[start]

    def get_safest_path(hops_back, position):
        current_position = position
        safest_path_back = []
        while current_position != None:
            safest_path_back.append(current_position)
            current_position = hops_back[current_position]

        return list(reversed(safest_path_back))

    hops_back = defaultdict(lambda: None)
    min_risks = defaultdict(lambda: float("inf"))
    min_risks[start] = cave.get_risk_level(start)
    unvisited_positions = { start }

    while unvisited_positions:
        p = min(unvisited_positions, key = lambda p: min_risks[p])
        unvisited_positions -= { p }

        for n in cave.get_neighbors(p):
            risk = min_risks[p] + cave.get_risk_level(n)
            if risk < min_risks[n]:
                min_risks[n] = risk
                hops_back[n] = p
                unvisited_positions |= { n }

    return partial(get_total_risk_level, min_risks, start), partial(get_safest_path, hops_back)

class Cave:
    def __init__(self, risk_levels):
        self._risk_levels = risk_levels

    def get_neighbors(self, position):
        i, j, = position
        neighbors = set()
        if j > 0: neighbors.add((i, j - 1))
        if i > 0: neighbors.add((i - 1, j))
        if j < len(self._risk_levels) - 1: neighbors.add((i, j + 1))
        if i < len(self._risk_levels[j]) - 1: neighbors.add((i + 1, j))

        return neighbors

    def get_risk_level(self, position):
        i, j = position
        return self._risk_levels[j][i]
