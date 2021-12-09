from math import ceil
from abc import ABC, abstractmethod

def load_crab_positions(crab_positions_file):
    with open(crab_positions_file, "r") as file:
        return list(map(int, file.__next__().strip().split(',')))

class CrabPositionOptimizer(ABC):
    @abstractmethod
    def get_fuel_consumption(self, from_position, to_position):
        pass

    @abstractmethod
    def get_optimum(self, crab_positions):
        pass

class LinearCrabPositionOptimizer(CrabPositionOptimizer):

    def get_fuel_consumption(self, from_position, to_position):
        return abs(to_position - from_position)

    def get_optimum(self, crab_positions):
        optimum = sorted(crab_positions)[ceil(len(crab_positions)/2)]
        total_fuel_consumption_at_optimum = sum(map(
            lambda x: self.get_fuel_consumption(x, optimum),
            crab_positions
        ))

        return optimum, total_fuel_consumption_at_optimum
