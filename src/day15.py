def load_risk_levels(risk_levels_file):
    with open(risk_levels_file, "r") as file:
        return [ list(map(int, line.strip())) for line in file ]
