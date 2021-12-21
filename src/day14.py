from collections import defaultdict, Counter
from functools import reduce
from math import ceil

def load_instructions(instructions_file):
    with open(instructions_file, "r") as file:
        polymer_template = next(file).strip()

        insertion_rules = defaultdict(lambda: "")
        for line in file:
            if line.isspace(): continue
            pair, element = map(lambda str: str.strip(), line.split("->"))
            insertion_rules[pair] = element

        return polymer_template, insertion_rules

def grow(polymer_template, insertion_rules, steps = 1):
    polymer = polymer_template
    for _ in range(steps):
        polymer = reduce(
            lambda p, e: p + insertion_rules[p[-1] + e] + e,
            polymer[1:],
            polymer[0]
        )

    return polymer

class ElementCounter:
    def __init__(self, polymer_template, insertion_rules):
        self._pair_counter = Counter([ polymer_template[i:i+2] for i in range(len(polymer_template) - 1) ])

        def update_pair_propagation_rules(pair_propagation_rule, insertion_rule_item):
            pair, element = insertion_rule_item
            pair_propagation_rule[pair] = (pair[0] + element, element + pair[1])
            return pair_propagation_rule

        self._pair_propagation_rules = reduce(
            update_pair_propagation_rules,
            insertion_rules.items(),
            defaultdict(lambda pair: [ pair ])
        )

    @property
    def counts(self):
        element_pair_counter = Counter()
        for pair, pair_count in self._pair_counter.items():
            for element in pair:
                element_pair_counter[element] += pair_count

        for element, count in element_pair_counter.items():
            element_pair_counter[element] = ceil(count / 2)

        return element_pair_counter

    def grow(self):
        counter = Counter()
        for pair, pair_count in self._pair_counter.items():
            for propagated_pair in self._pair_propagation_rules[pair]:
                counter[propagated_pair] += pair_count

        self._pair_counter = counter

