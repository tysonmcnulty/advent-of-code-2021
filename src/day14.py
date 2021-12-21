from collections import defaultdict

def load_instructions(instructions_file):
    with open(instructions_file, "r") as file:
        polymer_template = next(file).strip()

        insertion_rules = defaultdict(lambda: "")
        for line in file:
            if line.isspace(): continue
            pair, element = map(lambda str: str.strip(), line.split("->"))
            insertion_rules[pair] = element

        return polymer_template, insertion_rules
