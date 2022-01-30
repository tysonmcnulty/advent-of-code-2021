import unittest

from src.day12_bm_alt import (
    read_puzzle,
    dfs,
    solve,
)


class Day12Tests_alt(unittest.TestCase):
    """stuck on day 12 reversion DFS; try solution by Gravitar64 on subreddit at 
    https://www.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/"""

    def test_read_puzzle(self):
        puzzle = read_puzzle("data/day12_pathing_10_test.txt")
        self.assertEqual(6, len(puzzle))
        self.assertEqual(["A", "b"], puzzle["start"])
        self.assertEqual(["b"], puzzle["d"])

    def test_dfs(self):
        puzzle = read_puzzle("data/day12_pathing_10_test.txt")
        self.assertEqual(10, dfs("start", puzzle, {"start"}, False))
        self.assertEqual(36, dfs("start", puzzle, {"start"}, True))
        puzzle = read_puzzle("data/day12_pathing_19_test.txt")
        self.assertEqual(19, dfs("start", puzzle, {"start"}, False))
        puzzle = read_puzzle("data/day12_pathing_226_test.txt")
        self.assertEqual(226, dfs("start", puzzle, {"start"}, False))
        # Part 1 solution:
        puzzle = read_puzzle("data/day12_pathing_bm.txt")
        self.assertEqual(3510, dfs("start", puzzle, {"start"}, False))
        # Part 2 solution:
        puzzle = read_puzzle("data/day12_pathing_bm.txt")
        self.assertEqual(122880, dfs("start", puzzle, {"start"}, True))
