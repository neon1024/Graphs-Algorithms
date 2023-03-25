from domain.DirectedGraph import DirectedGraph


def get_directed_graph_from_first_file_convention():
    NUMBER_OF_VERTICES = 0
    NUMBER_OF_EDGES = 1
    ORIGIN = 0
    TARGET = 1
    COST = 2

    file_name = input("input file: ")
    file_name = file_name.strip()

    with open(file_name, "r") as file:
        tokens = file.readline()
        tokens = tokens.strip()
        tokens = tokens.split()

        number_of_vertices = int(tokens[NUMBER_OF_VERTICES])
        number_of_edges = int(tokens[NUMBER_OF_EDGES])

        directed_graph = DirectedGraph(number_of_vertices)

        for _ in range(number_of_edges):
            tokens = file.readline()
            tokens = tokens.strip()
            tokens = tokens.split()

            origin = int(tokens[ORIGIN])
            target = int(tokens[TARGET])
            cost = int(tokens[COST])

            directed_graph.add_edge(origin, target, cost)

    return directed_graph


def main():
    # make the MVP
    # optimise on it

    directed_graph = get_directed_graph_from_first_file_convention()


if __name__ == "__main__":
    main()
