# Day 8: Seven Segment Search
# Debug scrambled  signals to a 7-segment digits display

# -read the scrambled 4-digit outputs in 2nd half of each line
#       for now, ignore the 10 unique signal patterns on each line
# -Part 1:count the outputs that display 1, 4, 7 or 8 letters (display segments)
# -Part2: map the scrambled signal wires to the correct segments
# -refactor load_file() to include the 10 signals from the 1st half
# -work out rules for decoding the scrambled signals
# for each line, unscramble the 4-digit display output


class SevenSegmentMap:
    """This class processes one line of the input file for Part 2."""

    def __init__(self, signal, output):
        self.signal = signal
        self.output = output
        self.known_lengths = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
        self.segments_map = {}  # dict of sets
        self.digit_map = []

        # digits 1, 4, 7 & 8 use unique counts of segments
        self.segments_map[1] = set(
            y for y in [x for x in self.signal if len(x) == 2][0]
        )
        self.segments_map[4] = set(
            y for y in [x for x in self.signal if len(x) == 4][0]
        )
        self.segments_map[7] = set(
            y for y in [x for x in self.signal if len(x) == 3][0]
        )
        self.segments_map[8] = set(
            y for y in [x for x in self.signal if len(x) == 7][0]
        )

        # digits 0, 6 & 9 use 6 segments; compare missing segments to known digits
        digits_069 = [x for x in self.signal if len(x) == 6]
        for digit in digits_069:
            unused_segment = [x for x in "abcdefg" if x not in digit][0]
            if unused_segment in self.segments_map[1]:
                self.segments_map[6] = set(x for x in digit)
            elif (
                unused_segment in self.segments_map[4]
                and unused_segment not in self.segments_map[7]
            ):
                self.segments_map[0] = set(x for x in digit)
            else:
                self.segments_map[9] = set(x for x in digit)

        # digits 2, 3 & 5 use 5 segments; compare missing segments to known digits
        digits_235 = [x for x in self.signal if len(x) == 5]
        for digit in digits_235:
            unused_segments = [x for x in "abcdefg" if x not in digit]
            if (
                unused_segments[0] not in self.segments_map[6]
                and unused_segments[1] not in self.segments_map[9]
            ):
                self.segments_map[5] = set(x for x in digit)
            elif (
                unused_segments[1] not in self.segments_map[6]
                and unused_segments[0] not in self.segments_map[9]
            ):
                self.segments_map[5] = set(x for x in digit)
            elif (
                unused_segments[0] in self.segments_map[1]
                or unused_segments[1] in self.segments_map[1]
            ):
                self.segments_map[2] = set(x for x in digit)
            else:
                self.segments_map[3] = set(x for x in digit)

        # decode the four digits in the output display
        self.output_number = ""
        for digit in output:
            digit_set = set(x for x in digit)
            num = [k for k, v in self.segments_map.items() if v == digit_set][0]
            self.output_number += str(num)
        self.output_number = int(self.output_number)


def solution_part_2(signals, outputs):
    decoded_numbers = []
    for line_num in range(len(signals)):
        ssm = SevenSegmentMap(signals[line_num], outputs[line_num])
        decoded_numbers.append(ssm.output_number)
    return sum(decoded_numbers)


def load_file(entries_file):
    """Read the scrambled 4-digit display in 2nd half of each line; 
    For now, ignore the 10 unique signal patterns on each line"""

    with open(entries_file, "r") as efile:
        signals = []
        outputs = []
        for line in efile:
            half_lines = [x.strip() for x in line.split("|")]
            signal = [x for x in half_lines[0].split(" ")]
            signals.append(signal)
            output = [x for x in half_lines[1].split(" ")]
            outputs.append(output)
    return signals, outputs


def count_digits_1478(outputs):
    """ digits 1, 4, 7, 8 use 2, 4, 3, or 7 segments"""
    # flatten the list of lists and count the desired lengths
    count = len(
        [len(x) for sublist in outputs for x in sublist if len(x) in [2, 4, 3, 7]]
    )
    return count
