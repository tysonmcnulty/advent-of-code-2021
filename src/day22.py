import re

from functools import reduce

def load_reboot_steps(reboot_steps_file):
    with open(reboot_steps_file, "r") as file:
        reboot_steps = []
        for line in file:
            groups = re.match(r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", line).groups()
            state = groups[0]
            x_min, x_max, y_min, y_max, z_min, z_max = map(int, groups[1:7])
            reboot_steps.append((state, Cuboid((x_min, x_max + 1), (y_min, y_max + 1), (z_min, z_max + 1))))

        return reboot_steps

class Cuboid:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __eq__(self, other):
        return (isinstance(other, Cuboid)
            and self.x == other.x
            and self.y == other.y
            and self.z == other.z)

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def z(self): return self._z

    def volume(self):
        return (self.x[1] - self.x[0]) * (self.y[1] - self.y[0]) * (self.z[1] - self.z[0])

    def overlaps(self, other):
        return ((self.x[0] < other.x[1] and other.x[0] < self.x[1])
            and (self.y[0] < other.y[1] and other.y[0] < self.y[1])
            and (self.z[0] < other.z[1] and other.z[0] < self.z[1]))

    def split_x(self, *values):
        return self._split_dimension(self.x, lambda x: Cuboid(x, self.y, self.z), *values)

    def split_y(self, *values):
        return self._split_dimension(self.y, lambda y: Cuboid(self.x, y, self.z), *values)

    def split_z(self, *values):
        return self._split_dimension(self.z, lambda z: Cuboid(self.x, self.y, z), *values)

    def _split_dimension(self, dimension, factory, *values):
        cuboids = set()
        min, max = dimension
        for v in sorted(values):
            if v <= min: continue
            elif v < max:
                cuboids.add(factory((min, v)))
                min = v
            else: break

        cuboids.add(factory((min, max)))
        return cuboids

    def __add__(self, other):
        if not isinstance(other, Cuboid): raise ValueError()

        return (self - other) | { other }

    def __sub__(self, other):
        if not isinstance(other, Cuboid): raise ValueError()
        if not self.overlaps(other): return { self }

        difference = set()
        for z_split in self.split_z(*other.z):
            if not z_split.overlaps(other):
                difference.add(z_split)
                continue

            for y_split in z_split.split_y(*other.y):
                if not y_split.overlaps(other):
                    difference.add(y_split)
                    continue

                for x_split in y_split.split_x(*other.x):
                    if not x_split.overlaps(other):
                        difference.add(x_split)
                        continue

        return difference

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"Cuboid({self.x},{self.y},{self.z})"

def reboot(steps):
    cuboids = set()

    for state, cuboid in steps:
        next_cuboids = reduce(lambda acc, c: acc | (c - cuboid), cuboids, set())
        if state == "on":
            next_cuboids.add(cuboid)

        cuboids = next_cuboids

    return cuboids

def total_volume(cuboids):
    return reduce(lambda acc, c: acc + c.volume(), cuboids, 0)
