from functools import reduce

def load_lanternfish(lanternfish_file):
    with open(lanternfish_file, "r") as file:
        return list(map(int, file.__next__().strip().split(',')))

def create_population(lanternfish):
    def update_population(population, lanternfish_member):
        population[lanternfish_member] += 1
        return population

    return reduce(
        update_population,
        lanternfish,
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    )

def simulate(population):
    reproducing_fish = population.pop(0)
    population.append(reproducing_fish)
    population[6] += reproducing_fish
    return population
