from collections import defaultdict, deque
from functools import partial

def load_octopus_energy_levels(octopus_energy_levels_file):
    with open(octopus_energy_levels_file, "r") as file:
        octopus_energy_levels = []
        for line in file:
            octopus_energy_levels.append(list(map(int, line.strip())))

        return octopus_energy_levels


class EventEmitter:
    def __init__(self):
        self._listeners = defaultdict(lambda: [])

    def add_listener(self, event_name, listener):
        self._listeners[event_name].append(listener)

    def emit(self, event_name, event_data = None):
        for listener in self._listeners[event_name]:
            listener(event_data)

class OctopusGrid(EventEmitter):
    def __init__(self, octopus_energy_levels):
        self._grid = []
        self._actions = deque()
        self._len = 0
        for j, energy_level_row in enumerate(octopus_energy_levels):
            self._grid.append([])
            for i, energy_level in enumerate(energy_level_row):
                octopus = Octopus(energy_level)
                octopus.add_listener("flash", partial(self.on_flash, position = (i, j)))
                self._grid[-1].append(octopus)
                self._len += 1

        super().__init__()

    def __iter__(self):
        return (o for row in self._grid for o in row)

    def __eq__(self, other):
        return self._grid == other._grid

    def __len__(self):
        return self._len

    def __repr__(self):
        row_as_str = lambda r: '[' + ', '.join(str(o.energy_level()) for o in r) + ']'
        rows_str = ",".join(row_as_str(row) for row in self._grid)
        return f"OctopusGrid([{rows_str}])"

    def get_neighbor_positions(self, position):
        in_grid = lambda i, j: (
            0 <= j and j < len(self._grid) and
            0 <= i and i < len(self._grid[j])
        )

        return { (i, j)
            for i in range(position[0] - 1, position[0] + 2)
            for j in range(position[1] - 1, position[1] + 2)
            if in_grid(i, j)
        } - { position }

    def on_flash(self, _, position):
        def propagate_flash():
            for neighbor_position in self.get_neighbor_positions(position):
                i, j = neighbor_position
                self._grid[j][i].absorb()

        self._actions.append(propagate_flash)

    def step(self, num_steps = 1):
        for _ in range(num_steps):
            self.emit("step")
            for o in self: self._actions.append(o.charge)
            while self._actions:
                self._actions.popleft()()


class Octopus(EventEmitter):
    def __init__(self, energy_level):
        self._energy_level = energy_level
        super().__init__()

    def __eq__(self, other):
        return self._energy_level == other._energy_level

    @property
    def energy_level(self):
        return self._energy_level

    def charge(self):
        if self._energy_level == 9:
            self.flash()
        else:
            self._energy_level += 1

    def absorb(self):
        if self._energy_level > 0:
            self.charge()

    def flash(self):
        self._energy_level = 0
        self.emit("flash")
