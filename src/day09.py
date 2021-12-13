from math import inf
from collections import deque

def load_heightmap(heightmap_file):
    with open(heightmap_file, "r") as file:
        return list(map(lambda line: list(map(int, line.strip())), file))

def create_get_neighbors(heightmap):
    def get_neighbors(point):
        i, j, _ = point
        neighbors = set()
        if j > 0: neighbors.add((i, j - 1, heightmap[j - 1][i]))
        if i > 0: neighbors.add((i - 1, j, heightmap[j][i - 1]))
        if j < len(heightmap) - 1: neighbors.add((i, j + 1, heightmap[j + 1][i]))
        if i < len(heightmap[j]) - 1: neighbors.add((i + 1, j, heightmap[j][i + 1]))

        return neighbors

    return get_neighbors

def get_low_points(heightmap):

    get_neighbors = create_get_neighbors(heightmap)

    def is_low_point(point):
        neighbors = get_neighbors(point)
        return not any(map(lambda it: heightmap[j][i] >= it[2], neighbors))

    low_points = []
    for j in range(len(heightmap)):
        for i in range(len(heightmap[j])):
            point = (i, j, heightmap[j][i])
            if is_low_point(point):
                low_points.append(point)

    return low_points

def get_risk_level(heightmap):
    return sum(map(
        lambda point: point[2] + 1,
        get_low_points(heightmap)
    ))

def get_basin(heightmap, start):
    get_neighbors = create_get_neighbors(heightmap)
    visited_points = { start }
    unvisited_points = deque(get_neighbors(start))

    while len(unvisited_points) > 0:
        current_point = unvisited_points.popleft()
        if current_point[2] == 9: continue
        visited_points.add(current_point)
        unvisited_neighbors = get_neighbors(current_point) - visited_points
        unvisited_points.extend(unvisited_neighbors)

    return visited_points
