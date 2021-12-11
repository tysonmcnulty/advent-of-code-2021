from math import ceil
from abc import ABC, abstractmethod

def load_crab_positions(crab_positions_file):
    with open(crab_positions_file, "r") as file:
        return list(map(int, file.__next__().strip().split(',')))

class CrabPositionOptimizer(ABC):
    @abstractmethod
    def get_fuel_consumption(self, from_position, to_position):
        pass

    def get_total_fuel_consumption(self, crab_positions, position):
        return sum(map(
            lambda x: self.get_fuel_consumption(position, x),
            crab_positions
        ))

    @abstractmethod
    def get_optimum(self, crab_positions):
        pass


class LinearCrabPositionOptimizer(CrabPositionOptimizer):
    def get_fuel_consumption(self, from_position, to_position):
        return abs(to_position - from_position)

    def get_optimum_position(self, crab_positions):
        return sorted(crab_positions)[ceil(len(crab_positions)/2)]

    def get_optimum(self, crab_positions):
        optimum_position = self.get_optimum_position(crab_positions)
        total_fuel_consumption_at_optimum_position = self.get_total_fuel_consumption(
            crab_positions,
            optimum_position
        )
        return optimum_position, total_fuel_consumption_at_optimum_position

class TriangularCrabPositionOptimizer(CrabPositionOptimizer):
    def get_fuel_consumption(self, from_position, to_position):
        distance = abs(to_position - from_position)
        return int((distance**2 + distance)/2)

    def get_optimum_position_candidate(self, crab_positions):
        return int(sum(crab_positions)/len(crab_positions))

    def get_optimum(self, crab_positions):
        initial_optimum_position_candidate = self.get_optimum_position_candidate(crab_positions)

        optimum_position_search_range = range(
            initial_optimum_position_candidate - 2,
            initial_optimum_position_candidate + 2
        )

        optimum_candidates = list(map(
            lambda x: (x, self.get_total_fuel_consumption(crab_positions, x)),
            optimum_position_search_range
        ))

        local_optimum = min(optimum_candidates, key=lambda c: c[1])

        return local_optimum
