from functools import reduce
from collections import defaultdict

def load_diagnostics(diagnostics_file):
    with open(diagnostics_file, "r") as dfile:
        return [line.strip() for line in dfile]

def calc_gamma_rate(diagnostics):
    occurrences = get_occurrences(diagnostics)
    gamma_rate_str = ''.join([max(o, key = lambda c: len(o.get(c))) for o in occurrences])
    return int(gamma_rate_str, base = 2)

def calc_epsilon_rate(diagnostics):
    occurrences = get_occurrences(diagnostics)
    epsilon_rate_str = ''.join([min(o, key = lambda c: len(o.get(c))) for o in occurrences])
    return int(epsilon_rate_str, base = 2)

def get_diagnostic_length(diagnostics):
    return len(diagnostics[0])

def get_occurrences(diagnostics):
    diagnostic_length = get_diagnostic_length(diagnostics)

    def update_occurrences(occurrences, enum_diagnostic):
        for i, c in enumerate(enum_diagnostic[1]):
            occurrences[i][c].add(enum_diagnostic[0])

        return occurrences

    return reduce(
        update_occurrences,
        enumerate(diagnostics),
        [defaultdict(lambda: set()) for _ in range(diagnostic_length)]
    )
