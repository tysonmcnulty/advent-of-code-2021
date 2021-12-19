# Day 3: Binary Diagnostic
# refactored to use a string of most common bits, instead of a list


def load_report(report_file):
    reports = []
    with open(report_file, "r") as rfile:
        for line in rfile:
            reports.append(line.strip())
    return reports


def most_common_bits_str(reports_list):
    bit_counts = [0] * len(reports_list[0])

    for line in reports_list:
        for num, rbit in enumerate(line):
            bit_counts[num] += int(rbit)

    most_common_list = [
        "1" if x >= (len(reports_list) / 2) else "0" for x in bit_counts
    ]
    return "".join(most_common_list)


def calc_power_str(report_file):
    """Part 1: Calculate power consumption rating of the submarine
    as the product of gamma rate and epsilon rate.
    Gats string instead of list for the most common bits."""
    reports = load_report(report_file)

    gamma_str = most_common_bits_str(reports)
    gamma_rate = int(gamma_str, base=2)
    # gamma_rate = int("".join(map(str, gamma_list)), 2)  # most common bits

    epsilon_str = "".join(
        ["1" if x == "0" else "0" for x in gamma_str]
    )  # inverse of binary
    epsilon_rate = int(epsilon_str, base=2)

    result = gamma_rate * epsilon_rate
    return result


def calc_life_support_str(report_file):
    """Part 2: Calculate life support rating of the submarine
    as product of oxygen generator rating and CO2 scrubber rating.
    Gats string instead of list for the most common bits."""

    reports = load_report(report_file)
    O2_lines = reports[::]
    CO2_lines = reports[::]

    for bit_num in range(len(reports[0])):
        if len(O2_lines) > 1:
            most_O2_bit = most_common_bits_str(O2_lines)[bit_num]
            O2_lines = [x for x in O2_lines if x[bit_num] == most_O2_bit]
        if len(CO2_lines) > 1:
            most_CO2_bit = most_common_bits_str(CO2_lines)[bit_num]
            CO2_lines = [x for x in CO2_lines if x[bit_num] != most_CO2_bit]
        if len(O2_lines) + len(CO2_lines) <= 2:
            break

    O2_rating = int(O2_lines[0], base=2)
    CO2_rating = int(CO2_lines[0], base=2)
    life_support_rating = O2_rating * CO2_rating
    return life_support_rating

