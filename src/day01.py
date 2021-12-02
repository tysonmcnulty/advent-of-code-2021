# Day 1: Sonar Sweep

# read depths from text field into a list of integers
def load_depths(depths_file):
    depths = []

    with open(depths_file, "r") as dfile:
        for line in dfile:
            depths.append(int(line.strip()))

    return depths

# compare each depth to the previous
# return number of increases
def calc_increases(depths_file, bin_size = 1):

    depths = load_depths(depths_file)

    depth_increased_count = 0
    for i in range(bin_size, len(depths)):
        if depths[i] > depths[i - bin_size]:
            depth_increased_count += 1

    return depth_increased_count
