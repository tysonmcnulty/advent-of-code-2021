# Day 2: Dive!


def load_steps(steps_file):
    steps = []
    with open(steps_file, "r") as dfile:
        for step in dfile:
            steps.append((step.strip()[:-2], int(step.strip()[-1:])))
    return steps


def calc_course(steps_file):
    # Part One: calculate horizontal position, depth & the product of them
    hz_pos = 0
    depth_pos = 0
    steps = load_steps(steps_file)
    for step in steps:
        if step[0] == "forward":
            hz_pos += step[1]
        elif step[0] == "down":
            depth_pos += step[1]
        elif step[0] == "up":
            depth_pos -= step[1]

    return (hz_pos, depth_pos, hz_pos * depth_pos)


def calc_aim(steps_file):
    # Part Two: using aim, calculate horizontal position, depth & the product of them
    hz_pos = 0
    depth_pos = 0
    aim = 0
    steps = load_steps(steps_file)
    for step in steps:
        if step[0] == "forward":
            hz_pos += step[1]
            depth_pos += aim * step[1]
        elif step[0] == "down":
            aim += step[1]
        elif step[0] == "up":
            aim -= step[1]

    return (hz_pos, depth_pos, hz_pos * depth_pos)
