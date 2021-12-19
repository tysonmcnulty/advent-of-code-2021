from collections import defaultdict, deque
from itertools import filterfalse
from functools import partial

def load_cave_connections(cave_connections_file):
    with open(cave_connections_file, "r") as file:
        return [ set(line.strip().split("-")) for line in file ]

class CaveMap:
    def __init__(self, caves = [], connections = []):
        self._neighborhoods = defaultdict(lambda: set())
        for cave in caves:
            self.add_cave(cave)
        for conn in connections:
            self.add_connection(*conn)

    def add_cave(self, cave):
        self._neighborhoods[cave]

    def add_connection(self, cave1, cave2):
        self._neighborhoods[cave1].add(cave2)
        self._neighborhoods[cave2].add(cave1)

    def add_path(self, *caves):
        if len(caves) == 1:
            self.add_node(caves[0])

        for i in range(len(caves) - 1):
            self.add_connection(caves[i], caves[i + 1])

    def find_all_paths(self, start, end, revisitable = lambda cave, partial_path: False):
        paths = set()

        if start not in self._neighborhoods.keys():
            return paths

        partial_paths = deque()
        partial_paths.append(tuple([start]))

        while partial_paths:
            current_path = partial_paths.popleft()
            current_cave = current_path[-1]
            if (current_cave == end):
                paths.add(current_path)
                continue

            neighbors = self._neighborhoods[current_cave]
            unvisitable_neighbors = set(filterfalse(
                partial(revisitable, partial_path = current_path),
                current_path
            ))
            partial_paths.extend(current_path + (n,)
                for n in neighbors - unvisitable_neighbors
            )

        return paths

    def __eq__(self, other):
        return self._neighborhoods == other._neighborhoods
