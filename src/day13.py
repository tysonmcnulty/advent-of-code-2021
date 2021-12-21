import re

from functools import reduce

def load_instructions(cave_connections_file):
    with open(cave_connections_file, "r") as file:
        dots = set()
        for dot_line in file:
            if not re.match(r"\d+,\d+", dot_line): break
            dots.add(tuple(map(int, dot_line.strip().split(","))))

        fold_specs = list()
        for fold_line in file:
            if fold_line.isspace(): continue
            fold_specs.append(fold_line.removeprefix("fold along ").strip())

        return (dots, fold_specs)

def fold(dots, fold_specs):
    def fold_once(dots, fold_spec):
        dimension, position = fold_spec.split("=")
        if dimension == "x":
            return fold_right(dots, width(dots) - int(position))
        if dimension == "y":
            return fold_down(dots, height(dots) - int(position))

    return rotate_180(reduce(fold_once, fold_specs, rotate_180(dots)))


def fold_down(dots, amount):
    return set(map(lambda d: (d[0], abs(d[1] - amount)), dots))

def fold_right(dots, amount):
    return set(map(lambda d: (abs(d[0] - amount) - 1, d[1]), dots))

def width(dots):
    return max(map(lambda d: d[0], dots))

def height(dots):
    return max(map(lambda d: d[1], dots))

def rotate_180(dots):
    max_x = width(dots)
    max_y = height(dots)
    return set(map(lambda d: (max_x - d[0], max_y - d[1]), dots))

def write_activation_code(dots, dot_symbol = "#", empty_symbol = "."):
    w = width(dots)
    h = height(dots)
    activation_code = [ [empty_symbol] * (w + 1) for _ in range(h + 1) ]
    for d in dots:
        activation_code[d[1]][d[0]] = dot_symbol

    return list(map(lambda row: ''.join(row), activation_code))
