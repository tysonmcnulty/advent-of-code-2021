# Day 3: Binary Diagnostic


def load_report(report_file):
    reports = []
    with open(report_file, "r") as rfile:
        for line in rfile:
            reports.append(line.strip())
    return reports


def most_common_bits(reports_list):
    bit_counts = [0] * len(reports_list[0])

    for line in reports_list:
        for num, rbit in enumerate(line):
            bit_counts[num] += int(rbit)

    most_common_list = [1 if x > (len(reports_list) / 2) else 0 for x in bit_counts]
    return most_common_list


def calc_power(report_file):
    """Part 1: Calculate power consumption rating of the submarine
    as the product of gamma rate and epsilon rate."""
    reports = load_report(report_file)

    gamma_list = most_common_bits(reports)
    gamma_rate = int("".join(map(str, gamma_list)), 2)  # most common bits

    epsilon_list = [1 if x == 0 else 0 for x in gamma_list]
    epsilon_rate = int("".join(map(str, epsilon_list)), 2)  # least common bits
    # or try int(binary_string, base=2)

    result = gamma_rate * epsilon_rate
    return result


def calc_life_support(report_file):
    """Part 2: Calculate life support rating of the submarine
    as product of oxygen generator rating and CO2 scrubber rating."""
    reports = load_report(report_file)
    bit_counts = [0] * len(reports[0])

    for line in reports:
        for num, rbit in enumerate(line):
            bit_counts[num] += int(rbit)

    gamma_list = [1 if x > (len(reports) / 2) else 0 for x in bit_counts]
    epsilon_list = [1 if x == 0 else 0 for x in gamma_list]

    O2_lines = reports[::]

    most_common_list = most_common_bits(O2_lines)
    for num in range(len(gamma_list)):
        # TODO recalculate most/least/equal bit_counts for *each* filtered O2_lines list!
        if (gamma_list[num] == 1) and (len(O2_lines) > 1):
            O2_lines = [x for x in O2_lines if x[num] == "1"]
    O2_rating = int("".join(map(str, O2_lines[0])), 2)
    return O2_rating

