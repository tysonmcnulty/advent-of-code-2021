from functools import reduce
from collections import defaultdict

def load_diagnostics(diagnostics_file):
    with open(diagnostics_file, "r") as dfile:
        return [line.strip() for line in dfile]

def calc_gamma_rate(diagnostics):
    diagnostic_length = get_diagnostic_length(diagnostics)

    def update_occurrences(occurrences, diagnostic):
        for i, c in enumerate(diagnostic):
            occurrences[i][c] += 1

        return occurrences

    occurrences = reduce(
        update_occurrences,
        diagnostics,
        [defaultdict(lambda: 0) for _ in range(diagnostic_length)]
    )

    gamma_rate_str = ''.join([max(o, key = o.get) for o in occurrences])

    return int(gamma_rate_str, base = 2)

def calc_epsilon_rate(diagnostics):
    return (2**get_diagnostic_length(diagnostics) - 1) - calc_gamma_rate(diagnostics)

def get_diagnostic_length(diagnostics):
    return len(diagnostics[0])
