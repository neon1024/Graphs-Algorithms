class Service:
    def __init__(self, repository):
        self.__repository = repository

    def read_directed_graph_from_file_first_convention(self, file_name):
        NUMBER_OF_VERTICES = 0
        NUMBER_OF_EDGES = 1
        ORIGIN = 0
        TARGET = 1
        COST = 2

        with open(file_name, "r") as file:
            tokens = file.readline()
            tokens = tokens.strip()
            tokens = tokens.split()

            number_of_vertices = int(tokens[NUMBER_OF_VERTICES])
            number_of_edges = int(tokens[NUMBER_OF_EDGES])

            self.__repository.create_directed_graph(number_of_vertices)

            for _ in range(number_of_edges):
                tokens = file.readline()
                tokens = tokens.strip()
                tokens = tokens.split()

                origin = int(tokens[ORIGIN])
                target = int(tokens[TARGET])
                cost = int(tokens[COST])
                self.__repository.add_edge(origin, target, cost)
