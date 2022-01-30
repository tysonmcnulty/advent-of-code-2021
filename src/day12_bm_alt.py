# """stuck on day 12 reversion DFS; try solution by Gravitar64 on subreddit at
# https://www.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/"""

from time import perf_counter as pfc
from collections import defaultdict


def read_puzzle(file):
    puzzle = defaultdict(list)
    with open(file) as f:
        for row in f:
            a, b = row.strip().split("-")
            puzzle[a].append(b)
            puzzle[b].append(a)
    return puzzle


def dfs(node, graph, visited, twice, counter=0):
    if node == "end":
        return 1
    for neighb in graph[node]:
        if neighb.isupper():
            counter += dfs(neighb, graph, visited, twice)
        else:
            if neighb not in visited:
                counter += dfs(neighb, graph, visited | {neighb}, twice)
            elif twice and neighb not in {"start", "end"}:
                counter += dfs(neighb, graph, visited, False)
    return counter


def solve(puzzle):
    part1 = dfs("start", puzzle, {"start"}, False)
    part2 = dfs("start", puzzle, {"start"}, True)
    return part1, part2


start = pfc()
print(solve(read_puzzle("data/day12_pathing_bm.txt")))
print(pfc() - start)
# solution is (10,36) in 364 msec
