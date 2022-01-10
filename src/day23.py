import re
from collections import defaultdict

def load_amphipod_diagram(amphipod_diagram_file):
    amphipods = defaultdict(lambda: set())
    with open(amphipod_diagram_file, "r") as file:
        for line_number, line in enumerate(file):
            for column_number, char in enumerate(line):
                match = re.match(r"[ABCD]", char)
                if match:
                    amphipods[char] |= { (column_number, line_number) }

    return frozenset(map(lambda kv: (kv[0], frozenset(kv[1])), amphipods.items()))

class AmphipodGraph:
    def __init__(
        self,
        nodes = set(),
        edges = {
            frozenset({(1, 1), (2, 1)}),
            frozenset({(2, 1), (4, 1)}),
            frozenset({(2, 1), (3, 2)}),
            frozenset({(3, 2), (3, 3)}),
            frozenset({(3, 2), (4, 1)}),
            frozenset({(4, 1), (6, 1)}),
            frozenset({(4, 1), (5, 2)}),
            frozenset({(5, 2), (5, 3)}),
            frozenset({(5, 2), (6, 1)}),
            frozenset({(6, 1), (8, 1)}),
            frozenset({(6, 1), (7, 2)}),
            frozenset({(7, 2), (7, 3)}),
            frozenset({(7, 2), (8, 1)}),
            frozenset({(8, 1), (10, 1)}),
            frozenset({(8, 1), (9, 2)}),
            frozenset({(9, 2), (9, 3)}),
            frozenset({(9, 2), (10, 1)}),
            frozenset({(10, 1), (11, 1)}),
        }
    ):
        self._adjacencies = defaultdict(lambda: set())
        for n in nodes: self.add_node(n)
        for e in edges: self.add_edge(e)

    def add_node(self, node):
        self._adjacencies[node]

    def add_edge(self, edge):
        n1, n2 = edge
        self._adjacencies[n1].add(n2)
        self._adjacencies[n2].add(n1)

    def neighbors(self, node):
        if node in self._adjacencies.keys(): return self._adjacencies[node]

        raise KeyError()

    @property
    def nodes(self):
        return self._adjacencies.keys()

    @property
    def edges(self):
        return { frozenset({n1, n2}) for n1, n1_neighbors in self._adjacencies.items() for n2 in n1_neighbors }
