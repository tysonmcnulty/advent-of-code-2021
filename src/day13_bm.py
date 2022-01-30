# Day 13: Transparent Origami
# -read the dot locations & folding instructions from the text file
# -parse dots into set of coordinates & list of instructions
# -folds appear to be symmetrical halves in negative direction (up or left)
#    which implies length or width is twice the fold value
#


class TransparentOrigamiPaper:
    def __init__(self, dots={}, instructions=[]):
        self.instructions = instructions
        self.grid = dots.copy()

    def fold(self, direction, fold_line):
        old_grid = self.grid.copy()
        if direction == "y":  # fold up along y horizontal
            for dot in old_grid:
                if dot[1] > fold_line:
                    self.grid.add((dot[0], (2 * fold_line) - dot[1]))
                    self.grid.remove(dot)
        else:  # fold left along x vertical
            for dot in old_grid:
                if dot[0] > fold_line:
                    self.grid.add(((2 * fold_line) - dot[0], dot[1]))
                    self.grid.remove(dot)
        return len(self.grid)  # count of visible dots

    def print_grid(self):
        """Print the grid to reveal the human-readable characters."""
        height = min(i[1] for i in self.instructions if i[0] == "y")
        width = min(i[1] for i in self.instructions if i[0] == "x")
        # template = [["."] * width] * height  # no, use comprehension
        template = [["." for i in range(width)] for j in range(height)]
        for dot in self.grid:
            template[dot[1]][dot[0]] = "#"
        for line in template:
            print("".join(line))

    def fold_all(self):
        for instr in self.instructions:
            self.fold(instr[0], instr[1])
        # Part 2 solution: grid dots form 8 capital letters
        self.print_grid()
        return len(self.grid)


def load_file(origami_file):
    """Parse from text file of dot locations & instructions."""
    with open(origami_file, "r") as ofile:
        dots = []
        for line in ofile:
            dots.append(line.strip())
    instructions = [x.split("=") for x in dots if x[:4] == "fold"]
    instructions = [[x[0][-1], int(x[1])] for x in instructions]
    dots = [x.split(",") for x in dots[: -len(instructions) - 1]]
    # dots = [[int(x[0]), int(x[1])] for x in dots]
    dots = {(int(x[0]), int(x[1])) for x in dots}
    return dots, instructions
