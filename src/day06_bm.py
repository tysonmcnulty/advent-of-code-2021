# Day 6: Lanternfish
# Each lanternfish creates a new fish every 7 days

# -read initial list of fish ages (one line in a text file)
# -write population of fish to a history list
# -each day: (1) decrease ages by 1;
#   (2) if 0, add a new fish age 8 & rotate 0 to 6;
#   (3) write population to the history list
# -data structure: two lists of integers: fish ages & population history
# -solution to Part 1: population after 80 days
#    for big numbers, use a list of age counts instead of inefficient list of all fish
# -solution to Part 2: population after 256 days


def load_file(age_file):
    """ age_file has age of each fish at start of simulation, which decrease each day. 
    At age timer =0, age restores to 6 (0-based count) and a new fish is born with age 8."""

    with open(age_file, "r") as afile:
        for line in afile:
            ages = [int(x) for x in line.split(",")]
    return ages


def load_file_part_2(age_file):
    """For Part 2, switch data structure from list of each fish to a list of the 
    counts for each age, ranging 0 thru 9. This will handle much larger populations."""
    with open(age_file, "r") as afile:
        age_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for line in afile:
            ages = [int(x) for x in line.split(",")]
        for age in ages:
            age_counts[age] += 1
    return age_counts


def age_one_day(ages):
    ages += [9] * len([x for x in ages if x == 0])  # 9 will decrement to 8
    ages = [6 if x == 0 else x - 1 for x in ages]
    return ages


def age_one_day_part_2(age_counts):
    zero_count = age_counts[0]
    del age_counts[0]  # decrement fish ages
    age_counts.append(zero_count)  # create new fish
    age_counts[6] += zero_count  # restart old fish
    return age_counts


def part_1_simulation(ages, days):
    """Simulate lanternfish population over several days."""
    for x in range(days):
        ages = age_one_day(ages)
    return ages


def part_2_simulation(age_counts, days):
    """Simulate lanternfish population over many days using age count list (Part 2)."""
    for x in range(days):
        age_counts = age_one_day_part_2(age_counts)
    return age_counts
