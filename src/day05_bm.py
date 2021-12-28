# Day 5: Hydrothermal Venture

# -read start & end XY points of vent lines from file
# -data structure: dictionary of x,y tuple keys with count values
#       syntax:  [x for x in vvv.keys() if vvv[x] > 1]
# -generate all points where vents occur; save vent counts for each point
# -for now, skip if not horizontal or vertical line (same x or y coord)
# -Part 1: count points where >1 vent occurs


def load_file(vents_file):
    """ vents_file has start & end x,y pairs; 
    for now, ignore if x or y is not the same (hz or vert)"""

    vent_ends = []
    with open(vents_file, "r") as vfile:
        vent_ends = []
        for line in vfile:
            vent_xy = [[int(num) for num in x.split(",")] for x in line.split(" -> ")]
            vent_ends += vent_xy

    return vent_ends


def diagonal_vent_points(start_x, start_y, end_x, end_y):
    # Part 2: handle diagonal vent lines
    vent_points = []

    # use inclusive ranges, but messy?
    if start_y > end_y:
        y_span = [y for y in range(start_y, end_y - 1, -1)]
    elif start_y < end_y:
        y_span = [y for y in range(start_y, end_y + 1)]
    if start_x > end_x:
        x_span = [x for x in range(start_x, end_x - 1, -1)]
    elif start_x < end_x:
        x_span = [x for x in range(start_x, end_x + 1)]

    for index, y in enumerate(y_span):
        x = x_span[index]
        vent_points.append([x, y])
    return vent_points


def expand_vent_lines(vent_xy_pairs, include_diagonals=False):
    vent_points = []
    for index in range(0, len(vent_xy_pairs), 2):
        start_x, start_y, end_x, end_y = (
            vent_xy_pairs[index][0],
            vent_xy_pairs[index][1],
            vent_xy_pairs[index + 1][0],
            vent_xy_pairs[index + 1][1],
        )
        # Part 1: diagonal vent lines not considered
        if start_x == end_x:
            if start_y > end_y:
                start_y, end_y = end_y, start_y
            for y in range(start_y, end_y + 1):
                vent_points.append([start_x, y])
        elif start_y == end_y:
            if start_x > end_x:
                start_x, end_x = end_x, start_x
            for x in range(start_x, end_x + 1):
                vent_points.append([x, start_y])
        elif include_diagonals:
            # Part 2: also consider diagonal vent lines
            vent_points += diagonal_vent_points(start_x, start_y, end_x, end_y)
    return vent_points


def vent_counts(vent_points, minimum_count=0):
    point_counts = {}
    for point in vent_points:
        t_point = tuple(point)
        if t_point in point_counts:
            point_counts[t_point] += 1
        else:
            point_counts[t_point] = 1
    filtered_count = len(
        [x for x in point_counts.keys() if point_counts[x] >= minimum_count]
    )
    return point_counts, filtered_count
