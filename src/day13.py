import re

def load_instructions(cave_connections_file):
    with open(cave_connections_file, "r") as file:
        dots = set()
        for dot_line in file:
            if not re.match(r"\d+,\d+", dot_line): break
            dots.add(tuple(map(int, dot_line.strip().split(","))))

        folds = list()
        for fold_line in file:
            if fold_line.isspace(): continue
            folds.append(fold_line.removeprefix("fold along ").strip())

        return (dots, folds)
