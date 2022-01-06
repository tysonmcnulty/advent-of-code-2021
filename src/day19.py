import re

def load_scanners(scanners_file):
    with open(scanners_file, "r") as file:
        beacon_groups = []
        for line in file:
            if line.isspace(): continue
            if re.match(r"--- scanner \d+ ---$", line.strip()):
                beacon_groups.append(set())
            else:
                beacon_groups[-1].add(tuple(map(int, (n for n in line.strip().split(",")))))

    return list(map(Scanner, beacon_groups))

rotators = [
    lambda x, y, z: (+x, +y, +z),
    lambda x, y, z: (-x, -y, +z),
    lambda x, y, z: (-x, +y, -z),
    lambda x, y, z: (+x, -y, -z),

    lambda x, y, z: (+y, +x, -z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, +x, +z),
    lambda x, y, z: (+y, -x, +z),

    lambda x, y, z: (-y, -z, +x),
    lambda x, y, z: (+y, +z, +x),
    lambda x, y, z: (+y, -z, -x),
    lambda x, y, z: (-y, +z, -x),

    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (+z, +y, -x),
    lambda x, y, z: (+z, -y, +x),
    lambda x, y, z: (-z, +y, +x),

    lambda x, y, z: (+z, -x, -y),
    lambda x, y, z: (-z, +x, -y),
    lambda x, y, z: (-z, -x, +y),
    lambda x, y, z: (+z, +x, +y),

    lambda x, y, z: (-x, +z, +y),
    lambda x, y, z: (+x, -z, +y),
    lambda x, y, z: (+x, +z, -y),
    lambda x, y, z: (-x, -z, -y),
]

class Scanner:
    def __init__(self, beacons = set()):
        self._beacons = tuple([ frozenset(map(lambda b: r(*b), beacons)) for r in rotators ])
        pass

    def get_beacons(self, orientation = 0):
        return self._beacons[orientation]

    def oriented(self, orientation):
        return Scanner(self.get_beacons(orientation))

    def __eq__(self, other):
        return set(self._beacons) == set(other._beacons)

    def __hash__(self):
        return hash((self._beacons,))

def shift_one(beacon, offset):
    return tuple(b - o for b, o in zip(beacon, offset))

def shift(beacons, offset):
    return set(map(lambda b: shift_one(b, offset), beacons))

def find_placement(scanner, other, threshold = 12):
    beacons = scanner.get_beacons()
    for orientation in range(24):
        other_beacons = other.get_beacons(orientation)
        for b in beacons:
            for o in other_beacons:
                offset = shift_one(o, b)
                shifted_other_beacons = shift(other_beacons, offset)
                if len(shifted_other_beacons & beacons) >= threshold:
                    return (shift_one((0, 0, 0), offset), orientation)

    return (None, None)

def place_all(scanners):
    return set()
