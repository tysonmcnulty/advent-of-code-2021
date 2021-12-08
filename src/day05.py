from math import copysign

def load_vent_lines(vent_lines_file):
    vent_lines = []
    with open(vent_lines_file, "r") as file:
        for vent_line_spec in file:
            vent_lines.append(VentLine(vent_line_spec))

    return vent_lines

class VentLine:
    def __init__(self, vent_line_spec):
        p1, p2 = [coord.strip().split(',') for coord in vent_line_spec.split('->')]
        x1, y1 = list(map(int, p1))
        x2, y2 = list(map(int, p2))
        if x1 == x2:
            self.vent_points = set([ (x1, y) for y in range(y1, y2, int(copysign(1, y2 - y1))) ]) | set([(x2, y2)])
        elif y1 == y2:
            self.vent_points = set([ (x, y1) for x in range(x1, x2, int(copysign(1, x2 - x1))) ]) | set([(x2, y2)])
        else:
            self.vent_points = set()

    def __eq__(self, other):
        return self.vent_points == other.vent_points
