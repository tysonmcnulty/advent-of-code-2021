# Day 9: Smoke Basin
# Find 2D local minimums where smoke settles in low spots of lava tube caves.
# Part 2: find adjacent points 'connected to' each low point


def load_file(height_map_file):
    """Read the 2D grid of heights (digits range 0-9)."""

    with open(height_map_file, "r") as hfile:
        height_map = []
        for line in hfile:
            height_map.append(line.strip())
    return height_map


def pad_9s(height_map):
    """Place rows & columns of '9's at top, bottom, left & right of original data;
    Convert each row from a string to a list of digits."""
    padded_map = [[9] + [int(x) for x in row] + [9] for row in height_map]
    padded_map = [[9] * len(padded_map[0])] + padded_map + [[9] * len(padded_map[0])]
    return padded_map


def local_mins(padded_map):
    """Part 1: Find values in an array that are smaller than its
    four neighbors (above, below, left & right)."""
    low_points = {}
    for row_num, row in enumerate(padded_map[1:-1]):
        for digit_num, digit in enumerate(row[1:-1]):
            # row & digit nums are 1 larger than indexes in padded_map,
            # so digit is at padded_map[row_num + 1][digit_num + 1]
            if digit < min(
                padded_map[row_num + 1][digit_num + 0],
                padded_map[row_num + 1][digit_num + 2],
                padded_map[row_num + 0][digit_num + 1],
                padded_map[row_num + 2][digit_num + 1],
            ):
                low_points[row_num + 1, digit_num + 1] = digit
    return low_points


def solution_part_1(low_points):
    """sum of 1 + height of each low point"""
    return sum([x + 1 for x in low_points.values()])


def find_neighbors(p_map, row_num, col_num, neighbors):
    """Adds adjacent (row,col) tuples <9 to a set (above, below, right, left);
    A recursive function preloaded with the coordinates of a local minimum point."""
    if p_map[row_num][col_num + 1] < 9:
        if (row_num, col_num + 1) not in neighbors:
            neighbors.add((row_num, col_num + 1))
            find_neighbors(p_map, row_num, col_num + 1, neighbors)
    if p_map[row_num][col_num - 1] < 9:
        if (row_num, col_num - 1) not in neighbors:
            neighbors.add((row_num, col_num - 1))
            find_neighbors(p_map, row_num, col_num - 1, neighbors)
    if p_map[row_num + 1][col_num] < 9:
        if (row_num + 1, col_num) not in neighbors:
            neighbors.add((row_num + 1, col_num))
            find_neighbors(p_map, row_num + 1, col_num, neighbors)
    if p_map[row_num - 1][col_num] < 9:
        if (row_num - 1, col_num) not in neighbors:
            neighbors.add((row_num - 1, col_num))
            find_neighbors(p_map, row_num - 1, col_num, neighbors)
    return neighbors


def basin_sizes(padded_map, low_points):
    """Part 2: A basin is comprised of all digits < 9 that are adjacent
    (above, below, left & right) to the low point digit or each other, inclusive."""
    sizes = []
    for point in low_points:
        sizes.append(
            len(find_neighbors(padded_map, point[0], point[1], {(point[0], point[1])}))
        )

    return sizes


def solution_part_2(padded_map, low_points):
    sizes = basin_sizes(padded_map, low_points)
    sizes.sort()
    return sizes[-3] * sizes[-2] * sizes[-1]
