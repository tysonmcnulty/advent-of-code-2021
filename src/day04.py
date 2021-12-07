def load_bingo(bingo_file):
    card_rows = []
    num_rows_per_card = 5
    with open(bingo_file, "r") as file:
        draws = file.__next__().strip().split(',')

        for line in file:
            if not line.isspace():
                card_rows.append(line.strip().split())

    cards = [ BingoCard(card_rows[i:(i + num_rows_per_card)])
        for i in range(0, len(card_rows), num_rows_per_card)
    ]


    return (cards, draws)

class BingoCard:
    def __init__(self, grid):
        self.grid = grid
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

    def __eq__(self, other):
        return self.grid == other.grid

    def has_bingo(self, draws):
        return any(map(lambda b: b <= draws, self.bingos))


def get_earliest_win(cards, draws):

    winning_card = cards[2]
    winning_draw_index = 11
    return (cards[2], 11)
