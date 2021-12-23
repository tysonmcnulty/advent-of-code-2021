from itertools import chain

def load_bingo(bingo_file):
    board_rows = []
    num_rows_per_board = 5
    with open(bingo_file, "r") as file:
        draws = next(file).strip().split(',')

        for line in file:
            if not line.isspace():
                board_rows.append(line.strip().split())

    boards = [
        BingoBoard(board_rows[i:(i + num_rows_per_board)])
            for i in range(0, len(board_rows), num_rows_per_board)
    ]

    return (boards, draws)

class BingoBoard:
    def __init__(self, grid):
        self._grid = grid
        row_size = len(grid[0])
        column_size = len(grid)

        self.bingos = [
            *[set([grid[i][j]
                for i in range(column_size)])
                    for j in range(row_size)],
            *[set([grid[i][j]
                for j in range(column_size)])
                    for i in range(row_size)]
        ]

    @property
    def grid(self):
        return self._grid

    def __eq__(self, other):
        return self.grid == other.grid

    def has_bingo(self, draws):
        return any(map(lambda b: b <= draws, self.bingos))

    def get_score(self, draws):
        sum_of_unmarked_values = sum(map(int, set(chain.from_iterable(self._grid)) - set(draws)))
        last_draw_value = int(draws[-1])
        return sum_of_unmarked_values * last_draw_value


def find_wins(boards, draws):
    won_board_indices = set()
    for j in range(len(draws)):
        for i, board in enumerate(boards):
            if i not in won_board_indices and board.has_bingo(set(draws[:(j + 1)])):
                won_board_indices.add(i)
                yield (i, j)
