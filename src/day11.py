def load_octopi(octopi_file):
    with open(octopi_file, "r") as file:
        octopi = []
        for line in file:
            octopi.append(list(map(int, line.strip())))

        return OctopusGrid(octopi)

class OctopusGrid:
    def __init__(self, octopi):
        self._octopi = octopi

    def __eq__(self, other):
        return self._octopi == other._octopi
