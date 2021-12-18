def load_cave_connections(cave_connections_file):
    with open(cave_connections_file, "r") as file:
        return [ tuple(line.strip().split("-")) for line in file ]
