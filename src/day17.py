from functools import partial
from itertools import chain
from math import sqrt, ceil

def load_target_area(target_area_file):
    with open(target_area_file, "r") as file:
        range_specs = next(file).strip().removeprefix("target area: ").split(",")
        return list(map(
            lambda spec: list(map(int, spec.strip()[2:].split(".."))),
            range_specs
        ))

def launch_probe(velocity, start = (0, 0)):
    dx, dy = velocity
    x, y = start
    while True:
        yield (x, y)
        x += dx
        y += dy
        if dx > 0: dx -= 1
        dy -= 1

def in_target_area(min_x, max_x, min_y, max_y, position):
    x, y = position
    return min_x <= x and x <= max_x and min_y <= y and y <= max_y

def past_target_area(max_x, min_y, position):
    x, y = position
    return max_x < x or min_y > y

def detect(probe, target_area):
    min_x, max_x, min_y, max_y = chain.from_iterable(target_area)
    is_in = partial(in_target_area, min_x, max_x, min_y, max_y)
    is_past = partial(past_target_area, max_x, min_y)
    while True:
        position = next(probe)
        if is_in(position): return True
        if is_past(position): return False

def aim_high(target_area):
    target_x, target_y = target_area
    min_x = ceil(-.5 + sqrt(.25 + 2 * target_x[0]))
    max_y = -1 - target_y[0]
    return (min_x, max_y)

def aim(target_area):
    target_x, target_y = target_area
    min_dx, max_dy = aim_high(target_area)

    dx_range = range(min_dx, target_x[1] + 1)
    dy_range = range(target_y[0], max_dy + 1)

    return {
        (dx, dy) for dx in dx_range for dy in dy_range
            if detect(launch_probe((dx, dy)), target_area)
    }

def get_highest_y_position(velocity):
    _, y = velocity
    return int(y * (y + 1) / 2)
