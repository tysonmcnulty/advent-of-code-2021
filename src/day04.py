def load_bingo(bingo_file):
    card_rows = []
    num_rows_per_card = 5
    with open(bingo_file, "r") as file:
        draws = file.__next__().strip().split(',')

        for line in file:
            if not line.isspace():
                card_rows.append(line.strip().split())

    cards = [ card_rows[i:(i + num_rows_per_card)] for i in range(0, len(card_rows), num_rows_per_card) ]
    return (draws, cards)
