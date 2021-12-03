from functools import reduce

def load_steps(steps_file):
    steps = []
    with open(steps_file, "r") as dfile:
        for line in dfile:
            direction, amount = line.split(' ')
            steps.append([direction, int(amount)])

    return steps

def calc_position(steps_file, use_aim = False):

    steps = load_steps(steps_file)

    def advance(position, step):
        direction, amount = step
        if (direction == "forward"):
            position["x"] += amount
        if (direction == "down"):
            position["y"] += amount
        if (direction == "up"):
            position["y"] -= amount

        return position

    def advance_with_aim(position, step):
        direction, amount = step
        if (direction == "forward"):
            position["x"] += amount
            position["y"] += amount * position["aim"]
        if (direction == "down"):
            position["aim"] += amount
        if (direction == "up"):
            position["aim"] -= amount

        return position

    reducer = advance_with_aim if use_aim else advance

    return reduce(reducer, steps, { "x": 0, "y": 0, "aim": 0 })
