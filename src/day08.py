from functools import reduce

def load_display_data(display_data_file):
    def read_display_data_line(line):
        digit_data, readout_data = line.strip().split("|")
        encoded_digits = [ d for d in digit_data.strip().split()]
        readout = [ r for r in readout_data.strip().split()]

        return encoded_digits, readout

    with open(display_data_file, "r") as file:
        return list(map(read_display_data_line, file))

class DisplayDecoder:
    def __init__(self, encoded_digits, readout):
        def by_length(acc, curr):
            acc[len(curr)].add(curr)
            return acc

        encoded_digits_by_length = reduce(
            by_length,
            encoded_digits,
            (None, None, set(), set(), set(), set(), set(), set())
        )

        enc_one = frozenset(list(encoded_digits_by_length[2])[0])
        enc_seven = frozenset(list(encoded_digits_by_length[3])[0])
        enc_four = frozenset(list(encoded_digits_by_length[4])[0])
        enc_two_three_five = frozenset(map(frozenset, list(encoded_digits_by_length[5])))
        enc_zero_six_nine = frozenset(map(frozenset, list(encoded_digits_by_length[6])))
        enc_eight = frozenset(list(encoded_digits_by_length[7])[0])

        enc_three = next(e for e in enc_two_three_five if enc_one <= e)
        enc_nine = next(e for e in enc_zero_six_nine if enc_four <= e)
        enc_six = next(e for e in enc_zero_six_nine if (enc_eight - enc_seven) <= e)
        enc_two = next(e for e in enc_two_three_five if (enc_eight - enc_nine) <= e)

        enc_five = next(iter(enc_two_three_five - { enc_two, enc_three }))
        enc_zero = next(iter(enc_zero_six_nine - { enc_six, enc_nine }))

        self._decodings = {
            enc_zero: "0",
            enc_one: "1",
            enc_two: "2",
            enc_three: "3",
            enc_four: "4",
            enc_five: "5",
            enc_six: "6",
            enc_seven: "7",
            enc_eight: "8",
            enc_nine: "9"
        }

        self._decoded_readout = ''.join(map(self.decode_digit, readout))

    def decode_digit(self, encoded_digit):
        return self._decodings.get(frozenset(encoded_digit)) or "X"

    def count_matching(self, matcher):
        return sum(1 for _ in filter(matcher, self._decoded_readout))

    def get_readout_value(self):
        return int(self._decoded_readout, base = 10)
