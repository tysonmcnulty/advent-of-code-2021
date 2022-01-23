# Day 10: Syntax Scoring
# Part 1: Find the illegal closing character which corrupts a
#   line of navigation subsystem output.

# -read initial lines
# -in each line, search for the first incorrect closing character
# -starting from the left, find the first unused closing char
#   -if no more available, this line is incomplete
# -does the first (to the left) unused opening char match?
#   -if a match, mark both positions as used; search (right) for next closing char
#   -if not a match, save the illegal closing char; move to next line
# -Part 1 solution: calc the total syntax score for all illegal closing chars found
# Part 2: autocomplete the incomplete lines; ignore the corrupt lines


class NavData:
    def __init__(self, nav_lines=[]):
        self.lines = nav_lines
        self._pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
        self._pairs_2 = {"(": ")", "[": "]", "{": "}", "<": ">"}
        self._illegal_count = {")": 0, "]": 0, "}": 0, ">": 0}
        self._syntax_error_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        self._autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}
        self._completion_strings = []

    @property
    def syntax_error_score(self):
        return sum(
            self._illegal_count[x] * self._syntax_error_points[x]
            for x in self._illegal_count
        )

    @property
    def autocomplete_score(self):
        score_list = []
        for completion_string in self._completion_strings:
            score = 0
            for char in completion_string:
                score *= 5
                score += self._autocomplete_points[char]
            score_list.append(score)
        score_list.sort()
        return score_list[len(score_list) // 2]  # the middle score

    def first_illegal_char(self, line):
        line = list(line)
        for pos, char in enumerate(line):
            if char in self._pairs.keys():  # a closing char?
                # search left for a matching opener
                for left_pos in range(pos - 1, -1, -1):  # inclusive of first char
                    if line[left_pos] == self._pairs[char]:
                        # a good match; mark both positions as used "x"
                        line[left_pos] = "x"
                        line[pos] = "x"
                        break
                    elif line[left_pos] != "x":
                        # a bad match; exit and return the illegal char
                        return char, line
        return None, line  # line is not corrupt; could be incomplete (unclosed openers)

    @property
    def solution_part_1(self):
        for line in self.lines:
            bad_char, _ = self.first_illegal_char(line)
            if bad_char is not None:
                self._illegal_count[bad_char] += 1
        return self.syntax_error_score

    def autocomplete_line(self, line):
        """Finds closing characters for unmatched openers if line not corrupted."""
        completion_string = ""
        char, line = self.first_illegal_char(line)  # line returns as a list
        if char is None:  # line is not corrupt; could be incomplete
            completion_string = "".join(self._pairs_2[x] for x in line if x != "x")
        return completion_string[::-1]  # reverse the order

    @property
    def solution_part_2(self):
        for line in self.lines:
            completion_string = self.autocomplete_line(line)
            if len(completion_string) > 0:
                self._completion_strings.append(completion_string)
        return self.autocomplete_score


def load_file(navigation_subsystem_file):
    """Read the corrupted & incomplete output."""

    with open(navigation_subsystem_file, "r") as nfile:
        lines = []
        for line in nfile:
            lines.append(line.strip())
    return lines
