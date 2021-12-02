def load_steps(steps_file):
    steps = []
    with open(steps_file, "r") as dfile:
        for line in dfile:
            direction, amount = line.split(' ')
            steps.append([direction, int(amount)])

    return steps
