# Day 14: Extended Polymerization
# -read the template (first line) & rules from the text file
# -parse rules into a dictionary pairs & elements
# -test each pair in the template, in reverse order
#   if a the pair matches a rule, insert the element from the rule
# -repeat test/match/insert with the preceding pair
# -Part 1: repeat the insert step for the first 10 rules
#     and add the least and most common element counts
# -Part 2: 40 steps exceeds memory; refactor template to counts of pairs
# Hint from reddit -- Count/expand the number of pairs,
# not the entire string/list! [kinda like a zip compression algorithm?!]
# [could be even faster as recursive?!]
# ...refactored from a big list/string of single characters to pairs_count


class ExtendedPolymer:
    def __init__(self, template, rules, pairs):
        self.rules = rules.copy()
        self.pairs_count = pairs.copy()
        self.last_char = template[-1]
        # don't need to count elements until the end

    def insert_steps(self, step_count):
        new_pairs = {}
        for count in range(step_count):
            new_pairs.clear()
            for pair in self.pairs_count:
                new_pair_1 = pair[0] + self.rules[pair]
                new_pair_2 = self.rules[pair] + pair[1]
                if new_pair_1 in new_pairs:
                    new_pairs[new_pair_1] += self.pairs_count[pair]
                else:
                    new_pairs[new_pair_1] = self.pairs_count[pair]
                if new_pair_2 in new_pairs:
                    new_pairs[new_pair_2] += self.pairs_count[pair]
                else:
                    new_pairs[new_pair_2] = self.pairs_count[pair]
            self.pairs_count = new_pairs.copy()
            # print(f"count: {count} pair_count: {self.pairs_count}")
        return self.pairs_count

    def calc_difference(self, steps):
        """Difference between counts of least & most common elements."""
        self.insert_steps(steps)
        element_count = {self.last_char: 1}
        for pair in self.pairs_count:
            if pair[0] in element_count:
                element_count[pair[0]] += self.pairs_count[pair]
            elif self.pairs_count[pair] > 0:
                element_count[pair[0]] = self.pairs_count[pair]
        least_count = min(element_count.values())
        most_count = max(element_count.values())
        return most_count - least_count


def load_file(polymer_file):
    """Parse from text file of template & rules."""
    with open(polymer_file, "r") as pfile:
        rules = {}  # faster w dict instead of default dict ?
        pairs = {}
        for line in pfile:
            if "->" in line:
                rules[line[:2]] = line.strip()[-1]  # ignore \n
            elif len(line) > 2:
                template = list(line.strip())
                for i in range(len(template) - 1):
                    pairs[template[i] + template[i + 1]] = 1
    return template, rules, pairs
