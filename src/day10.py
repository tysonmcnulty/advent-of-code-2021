from functools import reduce

def load_navigation_subsystem(navigation_subsystem_file):
    with open(navigation_subsystem_file, "r") as file:
        return list(map(lambda l: l.strip(), file))

def parse(line):
    context = []
    for char in line:
        if char in "([{<":
            context.append(char)
        else:
            if f"{context[-1]}{char}" not in { "()", "{}", "[]", "<>" }:
                yield (char, ''.join(context))

            del context[-1]

    yield (None, ''.join(context))


def get_syntax_error_score(char):
    return { None: 0, ")": 3, "]": 57, "}": 1197, ">": 25137 }[char]

def get_total_syntax_error_score(navigation_subsystem):
    syntax_errors = map(
        lambda line: next(parse(line))[0],
        navigation_subsystem
    )

    return sum(map(get_syntax_error_score, syntax_errors))

def get_completion_score(context):
    point_values = { "(": 1, "[": 2, "{": 3, "<": 4 }

    return reduce(
        lambda score, char: 5 * score + point_values[char],
        reversed(context),
        0
    )

def get_total_completion_score(navigation_subsystem):
    incomplete_parse_results = filter(
        lambda parse_result: parse_result[0] is None,
        map(
            lambda line: next(parse(line)),
            navigation_subsystem
        )
    )

    sorted_completion_scores = sorted(map(
        lambda result: get_completion_score(result[1]),
        incomplete_parse_results
    ))

    print(sorted_completion_scores)

    return sorted_completion_scores[int(len(sorted_completion_scores)/2)]
