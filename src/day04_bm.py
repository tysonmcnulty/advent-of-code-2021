# Day 4: Giant Squid

# -read draw numbers and boards from file; ??data structure list or dict?
# -mark all board positions that match the drawn number; change to None?
# -check a(ll) board(s) for a completely-marked row or column; all None's?
# -calc sum of all unmarked positions on the winning board
# -sum times latest drawn number = puzzle solution


class BingoCard:
    def __init__(self, card_data):
        self._card_data = card_data
        self.winner = False
        self.winning_turn = None

    def mark_card(self, drawn_number, draw_turn=None):
        if not self.winner:
            for row in range(5):
                for column in range(5):
                    if self._card_data[row][column] == drawn_number:
                        self._card_data[row][column] = None
            self.winner = self.check_for_winner()
            if self.winner:
                self.winning_turn = draw_turn
        return self.winner

    def check_for_winner(self):
        for row in range(5):
            self.winner = self.winner or all(x is None for x in self._card_data[row])
        if not self.winner:
            for column in range(5):
                self.winner = self.winner or all(
                    x[column] is None for x in self._card_data
                )
        return self.winner

    @property
    def unmarked_sum(self):
        return sum(sum(x for x in row if not x is None) for row in self._card_data)

    # def list_is_all_none(num_list):
    #     # return len([x for x in num_list if not x is None]) == 0
    #     return all(x is None for x in num_list)  # uses generator, not list; or use not any


def load_file(bingo_file):
    """ bingo_file has draw numbers in the first line 
    followed by 5-line space-delimited 5x5 matrices, 
    separated by a blank line."""
    bingo_data = []
    with open(bingo_file, "r") as bfile:
        for line in bfile:
            # cleans leading, trailing & double spaces (not >2)
            bingo_data.append(line.strip().replace("  ", " "))
    return bingo_data


def parse_data(bingo_data):
    """Read draw numbers from first line.
    Read 5x5 tables following each blank line."""
    draws = bingo_data[0].split(",")
    draws = [int(x) for x in draws]

    card_lines = []
    for line in bingo_data[1:]:
        if line != "":
            # next 5 lines per card
            card_line = [int(x) for x in line.split(" ")]
            card_lines.append(card_line)

    return draws, card_lines


def create_cards(card_lines):
    cards = []
    for card_num in range(0, len(card_lines), 5):
        five_lines = []
        for line_num in range(card_num, card_num + 5):
            five_lines.append(card_lines[line_num])
        cards.append(BingoCard(five_lines))
    # Tyson's fully generator version ...
    # boards = [
    #         BingoBoard(board_rows[i:(i + num_rows_per_board)])
    #             for i in range(0, len(board_rows), num_rows_per_board)
    #     ]
    return cards


def mark_all_cards(cards, draws):
    """Returns turn number for each card's first winning bingo. 
    Remains None if card does not bingo."""
    winning_turns = []
    for card in cards:
        for draw_turn, drawn_number in enumerate(draws):
            if not card.winner:
                card.mark_card(drawn_number, draw_turn)
            else:
                break
        winning_turns.append(card.winning_turn)
    return winning_turns


def part_1_solution(cards, draws):
    winning_turns = mark_all_cards(cards, draws)
    first_winning_turn = min(x for x in winning_turns if not x is None)
    first_winner_drawn_number = draws[first_winning_turn]
    first_winner_card = cards[winning_turns.index(first_winning_turn)]
    first_winner_card_sum = first_winner_card.unmarked_sum
    return (
        first_winning_turn,
        first_winner_drawn_number,
        first_winner_card_sum,
        first_winner_drawn_number * first_winner_card_sum,
    )


def part_2_solution(cards, draws):
    winning_turns = mark_all_cards(cards, draws)
    last_winning_turn = max(x for x in winning_turns if not x is None)
    last_winner_drawn_number = draws[last_winning_turn]
    last_winner_card = cards[winning_turns.index(last_winning_turn)]
    last_winner_card_sum = last_winner_card.unmarked_sum
    return (
        last_winning_turn,
        last_winner_drawn_number,
        last_winner_card_sum,
        last_winner_drawn_number * last_winner_card_sum,
    )
