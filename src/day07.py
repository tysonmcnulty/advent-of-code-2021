from math import ceil

def load_crab_positions(crab_positions_file):
    with open(crab_positions_file, "r") as file:
        return list(map(int, file.__next__().strip().split(',')))

def get_optimal_alignment(crab_positions):
    optimal_position = sorted(crab_positions)[ceil(len(crab_positions)/2)]

    fuel_usage = lambda x: sum(map(lambda n: abs(x - n), crab_positions))

    return (optimal_position, fuel_usage(optimal_position))
