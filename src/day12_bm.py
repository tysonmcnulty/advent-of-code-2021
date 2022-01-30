# Day 12: Passage Pathing
# -read the cave map (connections between caves) from text file
# -parse node connections (graph edges) into a dict as an adjacency list
# -set up pathing stack, visited set & path list
# -write recursive depth first search (DFS) code
# -modify DFS code for multiple visits to large (capitalized) caves
# -count number of distinct paths (valid from 'start' to 'end')


class CaveMap:
    def __init__(self, cave_map=[]):
        # parse into a lookup table of node connections
        self.nodes = dict()  # all connections in the map
        self.visited = set()  # except large caves can visit multiple
        self.adjacent = []  # a moving stack
        # self.current_path = []  # a cumulative stack
        self.distinct_paths = []  # all paths found, incl invalid
        for entry in cave_map:
            node1, node2 = entry.split("-")
            if node1 in self.nodes:
                self.nodes[node1].append(node2)
            else:
                self.nodes[node1] = [node2]
                # if node1[0].isupper():
                # # visit small caves only once
                # self.visited.add(node1)
            if node2 in self.nodes:
                self.nodes[node2].append(node1)
            else:
                self.nodes[node2] = [node1]
                # if not node2[0].isupper():
                #     self.small_caves_not_visited.add(node2)
        self.nodes["end"] = []  # terminate valid paths
        return

    def search(
        self, node="start", adjacent_nodes=[], visited_nodes={"start"}, current_path=[],
    ):
        """Based on recursive DFS; Count valid paths (to 'end').
        Part 1: Visit small caves max of once."""
        # TODO for now, allow only one visit per node
        current_path.append(node)
        if node == "end":
            self.distinct_paths.append(current_path[:])
            # ?? return 1  # expanded from counter-based  solution by Gravitar64 on
            # https://www.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/
        for neighbor in self.nodes[node]:

            visited_nodes.append(node)  # TODO except 'end' or small caves
        if adjacent_nodes:  # advance
            node = adjacent_nodes.pop()
            adjacent_nodes = [n for n in self.nodes[node] if n not in visited_nodes]
            self.search(node, adjacent_nodes, visited_nodes, current_path)
        else:  # reached 'end' or dead end; remember path; backtrack
            self.distinct_paths.append(current_path[:])
            # self.search()  # TODO avoid prior paths?
            current_path.pop()
            node = current_path.pop()
            adjacent_nodes = [n for n in self.nodes[node] if n not in visited_nodes]
            self.search(node, adjacent_nodes, visited_nodes, current_path)


def load_file(node_connections_file):
    """Read lines from text file of connections between caves (nodes);
    return as a simple list."""

    with open(node_connections_file, "r") as cfile:
        cave_map = []
        for line in cfile:
            cave_map.append(line.strip())
    return cave_map
