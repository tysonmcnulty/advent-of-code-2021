# Day 7: The Treachery of Whales
# Part 1: Optimize a central 1-D point for minimum sum of distances

# -read initial list of points (1-D positions of crabs along a horizontal line)
# -select a starting point. approximatly mid-point
# -calculate sum of distances to all other points
#       from current point & both immediate neighbors
# -compare each neighbor whether ascending and/or descending ("slope")
# -if both ascending, you found the solution point (minimum sum of distances)
# -else, move in the descending direction ~half-way to nearest used point (or end)
# -repeat at new current point until a solution is found (or fail, no more moves)
# Part 1: fuel consumption is constant at 1 unit of fuel per step moved
# Part 2: fuel consumption increases by 1 unit of fuel for each step moved,
#   so add an intermediate calculation to calculate fuel cost from distance moved,
#   then save in _known_sums as in Part 1


class CrabsData:
    def __init__(self, crab_positions=[]):
        self.positions = crab_positions
        self._known_sums = {}  # sum of distances from a position to all others
        self.part_2_flag = False  # affects fuel cost
        if len(self.positions) >= 2:
            # preload with sums at end points
            _ = self.get_sum(min(self.positions))
            _ = self.get_sum(max(self.positions))

    def get_sum(self, point):
        # calculate/save or recall sum of distances from a single position
        if point in self._known_sums:
            return self._known_sums[point]
        else:
            if self.part_2_flag:
                new_sum = sum(self.fuel_cost(x, point) for x in self.positions)
            else:
                new_sum = sum(abs(x - point) for x in self.positions)
            self._known_sums[point] = new_sum
            return new_sum

    def best_direction(self, point=None):
        """test adjacent points for 'slope' or a minimum; 
        assumes one unique minimum & no maximums except ends"""
        if point is None:
            # start at approximate mid-point
            point = sum(self._known_sums.keys()) // len(self._known_sums)
        if self.get_sum(point) < self.get_sum(point + 1):
            if self.get_sum(point) < self.get_sum(point - 1):
                return 0  # found the local minimum
            else:
                return -1  # move left
        return 1  # move right

    def next_point(self, point=None):
        if point is None:
            # start at approximate mid-point
            point = sum(self._known_sums.keys()) // len(self._known_sums)
        direction = self.best_direction(point)
        if direction == 0:
            return point  # no change; found the solution
        elif direction == -1:  # next search left
            nearest_known_sum = max(
                [x for x in self._known_sums.keys() if x < (point - 1)]
            )
            next_point = (nearest_known_sum + point - 1) // 2
        else:  # next search right
            nearest_known_sum = min(
                [x for x in self._known_sums.keys() if x > (point + 1)]
            )
            next_point = (nearest_known_sum + point + 1) // 2
        return next_point

    def solution_part_1_2(self, part_2=False):
        self.part_2_flag = part_2
        previous_point = None
        for x in range(100):  # expect to need <10 cycles?
            next_point = self.next_point(previous_point)
            if previous_point == next_point:
                break
            else:
                previous_point = next_point
        return previous_point, self._known_sums[previous_point]

    def fuel_cost(self, point_1, point_2):
        # quadratic fit to sample plot: y = 0.5x^2 + 0.5x
        fcost = ((point_2 - point_1) ** 2 + abs(point_2 - point_1)) // 2
        return fcost


def load_file(crab_file):
    """Single CSV line in crab_file has position (distance from 0 end) 
    of each crab submarine along a horizontal line."""

    with open(crab_file, "r") as cfile:
        for line in cfile:
            crab_positions = [int(x) for x in line.split(",")]
    return crab_positions


# def sum_of_distances(crab_positions, point, known_sums={}):
#     if point in known_sums:
#         return known_sums[point]
#     else:
#         new_sum = sum(abs(x - point) for x in crab_positions)
#         known_sums[point] = new_sum
#         return new_sum
