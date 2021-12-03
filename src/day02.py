from functools import reduce

def load_steps(steps_file):
    steps = []
    with open(steps_file, "r") as dfile:
        for line in dfile:
            direction, amount = line.split(' ')
            steps.append([direction, int(amount)])

    return steps

def calc_position(steps_file):

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

    return reduce(advance, steps, { "x": 0, "y": 0 })
