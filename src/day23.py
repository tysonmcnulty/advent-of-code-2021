import re

from collections import defaultdict
from functools import cache
from heapq import heappush, heappop

def load_amphipod_diagram(amphipod_diagram_file):
    amphipods = set()
    with open(amphipod_diagram_file, "r") as file:
        for line_number, line in enumerate(file):
            for column_number, char in enumerate(line):
                match = re.match(r"[ABCD]", char)
                if match:
                    amphipods.add((char, (column_number, line_number)))

    return frozenset(amphipods)

class Organizer:
    class Graph:
        DEFAULT_NODES = {
            (1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1),
            (3, 2), (5, 2), (7, 2), (9, 2),
            (3, 3), (5, 3), (7, 3), (9, 3)
        }

        DEFAULT_EDGES = {
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

        FULL_NODES = DEFAULT_NODES | {
            (3, 4), (5, 4), (7, 4), (9, 4),
            (3, 5), (5, 5), (7, 5), (9, 5)
        }

        FULL_EDGES = DEFAULT_EDGES | {
            frozenset({(3, 3), (3, 4)}),
            frozenset({(3, 4), (3, 5)}),
            frozenset({(5, 3), (5, 4)}),
            frozenset({(5, 4), (5, 5)}),
            frozenset({(7, 3), (7, 4)}),
            frozenset({(7, 4), (7, 5)}),
            frozenset({(9, 3), (9, 4)}),
            frozenset({(9, 4), (9, 5)}),
        }

        def __init__(self, nodes, edges):
            self._adjacencies = dict()
            self.add_nodes(*nodes)
            self.add_edges(*edges)

        def add_nodes(self, *nodes):
            for n in nodes: self._adjacencies[n] = self._adjacencies.get(n, set())

        def add_edges(self, *edges):
            for e in edges:
                n1, n2 = e
                self.add_nodes(n1, n2)
                self._adjacencies[n1].add(n2)
                self._adjacencies[n2].add(n1)

        def neighbors(self, node):
            return self._adjacencies[node]

        @property
        def nodes(self):
            return self._adjacencies.keys()

        @property
        def edges(self):
            return { frozenset({ n1, n2 }) for n1, adj in self._adjacencies.items() for n2 in adj }

        def removed(self, nodes = set(), edges = set()):
            return Organizer.Graph(
                nodes = self.nodes - nodes,
                edges = filter(
                    lambda e: not any(map(lambda n: n in nodes, e)),
                    self.edges - edges))

        def navigate(self, start):
            def cost(current, neighbor):
                return abs(current[0] - neighbor[0]) + abs(current[1] - neighbor[1])

            min_risks = defaultdict(lambda: float("inf"))
            min_risks[start] = 0
            unvisited_positions = { start }

            while unvisited_positions:
                p = min(unvisited_positions, key = lambda p: min_risks[p])
                unvisited_positions.remove(p)

                for n in self.neighbors(p):
                    risk = min_risks[p] + cost(p, n)
                    if risk < min_risks[n]:
                        min_risks[n] = risk
                        unvisited_positions.add(n)

            return min_risks


    DEFAULT_TARGET = frozenset({
        ("A", (3, 2)), ("A", (3, 3)),
        ("B", (5, 2)), ("B", (5, 3)),
        ("C", (7, 2)), ("C", (7, 3)),
        ("D", (9, 2)), ("D", (9, 3)),
    })

    FULL_TARGET = frozenset({
        ("A", (3, 2)), ("A", (3, 3)), ("A", (3, 4)), ("A", (3, 5)),
        ("B", (5, 2)), ("B", (5, 3)), ("B", (5, 4)), ("B", (5, 5)),
        ("C", (7, 2)), ("C", (7, 3)), ("C", (7, 4)), ("C", (7, 5)),
        ("D", (9, 2)), ("D", (9, 3)), ("D", (9, 4)), ("D", (9, 5)),
    })

    DEFAULT_GRAPH = Graph(nodes = Graph.DEFAULT_NODES, edges = Graph.DEFAULT_EDGES)
    FULL_GRAPH = Graph(nodes = Graph.FULL_NODES, edges = Graph.FULL_EDGES)

    def __init__(self, target = DEFAULT_TARGET, graph = DEFAULT_GRAPH):
        self._target = target
        self._graph = graph

    @cache
    def target_nodes(self, type):
        return set(filter(lambda n: (type, n) in self.target, self.graph.nodes))

    @cache
    def sorted_target_nodes(self, type):
        return sorted(self.target_nodes(type))

    @property
    @cache
    def hallway_nodes(self):
        return set(filter(lambda n: n[1] == 1, self.graph.nodes))

    @property
    def target(self):
        return self._target

    @property
    def graph(self):
        return self._graph

    def get_available_moves(self, amphipods):
        occupied_nodes = set(map(lambda a: a[1], amphipods))

        available_moves = set()
        for amphipod in amphipods:
            type, node = amphipod
            others = amphipods - { amphipod }
            allowed = self.allowed_next_nodes(amphipod, others)
            if not allowed: continue

            min_costs = self.graph.removed(nodes = occupied_nodes - { node }).navigate(node)
            for next_node, cost in min_costs.items():
                if next_node in allowed:
                    available_moves.add((
                        cost * self.cost_modifier(type),
                        frozenset(others | { (type, next_node) })
                    ))

        return available_moves

    def cost_modifier(self, type):
        return { "A": 1, "B": 10, "C": 100, "D": 1000 }[type]

    def allowed_next_nodes(self, amphipod, others):
        type, node = amphipod
        targets = self.target_nodes(type)
        amphipods_at_target_nodes = set(filter(lambda o: o[1] in targets, others))
        target_nodes_match_target_type = all(map(lambda a: a[0] == type, amphipods_at_target_nodes))

        if node not in self.hallway_nodes:
            if node in targets and target_nodes_match_target_type:
                return set()
            else:
                return self.hallway_nodes
        else:
            if not target_nodes_match_target_type:
                return set()
            for target_node in reversed(self.sorted_target_nodes(type)):
                if (type, target_node) in amphipods_at_target_nodes: continue
                return (type, target_node)

    def organize(self, amphipods):
        min_costs = defaultdict(lambda: float("inf"))
        min_costs[amphipods] = 0
        available_moves = []
        heappush(available_moves, (0, amphipods))

        count = 0
        while True:
            current_move = heappop(available_moves)
            # count += 1
            # print(f"current move: {current_move}")
            # print(f" ↳ total cost: {min_costs[current_move[1]]}")

            if current_move[1] == self.target: break

            for next_move in self.get_available_moves(current_move[1]):
                next_cost, next_amphipods = next_move
                total_cost = min_costs[current_move[1]] + next_cost
                if total_cost < min_costs[next_amphipods]:
                    min_costs[next_amphipods] = total_cost
                    heappush(available_moves, (total_cost, next_amphipods))

            # print(f"explored {count} of {count + len(available_moves)} known moves")

        return min_costs[self.target]
