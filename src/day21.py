import re

def load_starting_spaces(starting_squares_file):
    with open(starting_squares_file, "r") as file:
        matches = (re.match(r"(Player \d+) starting position: (\d+)", line).groups() for line in file)

        return dict(map(lambda m: (m[0], int(m[1])), matches))
