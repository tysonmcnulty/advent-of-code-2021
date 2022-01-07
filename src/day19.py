import re

from collections import deque

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

def shift_one(beacon, offset):
    return tuple(b - o for b, o in zip(beacon, offset))

def shift(beacons, offset):
    return set(map(lambda b: shift_one(b, offset), beacons))

def orient(beacons, orientation):
    return set(map(lambda b: rotators[orientation](*b), beacons))

class Scanner:
    def __init__(self, beacons = set()):
        self._beacons = beacons
        pass

    @property
    def beacons(self):
        return self._beacons

    def oriented(self, orientation):
        return Scanner(orient(self.beacons, orientation))

    def shifted(self, offset):
        return Scanner(shift(self.beacons, offset))

    def __eq__(self, other):
        return set(self._beacons) == set(other._beacons)

    def __hash__(self):
        return hash((self._beacons,))

def find_placement(scanner, other, threshold = 12):
    beacons = scanner.beacons
    for orientation in range(24):
        other_beacons = other.oriented(orientation).beacons
        for b in beacons:
            for o in other_beacons:
                offset = shift_one(o, b)
                shifted_other_beacons = shift(other_beacons, offset)
                if len(shifted_other_beacons & beacons) >= threshold:
                    return (offset, orientation)

    return (None, None)

def reconstruct(scanners):
    placements = [(None, None)] * len(scanners)
    unplaced = deque(enumerate(scanners))
    index, reconstruction = unplaced.popleft()

    placements[index] = ((0, 0, 0), 0)

    i = 0
    placed = 1
    while unplaced and i < placed:
        for _ in range(len(unplaced)):
            original_index, current = unplaced.popleft()
            offset, orientation = find_placement(reconstruction, current)
            if offset != None and orientation != None:
                reconstruction = Scanner(reconstruction.beacons | current.oriented(orientation).shifted(offset).beacons)
                placements[original_index] = (offset, orientation)
                print(f"Placed scanner {original_index}: {(offset, orientation)}.")
                placed += 1
            else:
                print(f"Cound not place scanner {original_index}; returning to queue.")
                unplaced.append((original_index, current))

        i += 1

    return reconstruction, placements
