# Day 1: Sonar Sweep

# - read depths from text field into a list of integers
# - compare each depth to the previous, sarting with the 2nd
# - track how many increase (total 2000)


def calc_increases(depths_file):

    depths = []

    with open(depths_file, "r") as dfile:  # day01_depths_test.txt for testing
        for line in dfile:
            depths.append(int(line.strip()))
    print(depths)

    depth_increased_count = 0
    depth_count = 1
    for num, depth in enumerate(depths):
        if num > 0:  # no compare for first entry
            depth_count += 1
            if depths[num] > depths[num - 1]:
                depth_increased_count += 1

    print(f"depth increased {depth_increased_count} times of {depth_count} total")
    # potential answer: depth increased 1462 times of 2000 total

    return depth_increased_count


calc_increases("day01_depths_test.txt")
