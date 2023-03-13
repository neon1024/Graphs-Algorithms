class DirectedGraph:
    """
    A directed graph of N vertices, where vertices are from 0 to N-1
    """

    def __init__(self, number_of_vertices):
        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = 0
        self.__predecessors = {}
        self.__successors = {}
        self.__costs = {}

        for index in range(number_of_vertices):
            self.__predecessors[index] = []
            self.__successors[index] = []

    def get_number_of_vertices(self):
        return self.__number_of_vertices

    def get_number_of_edges(self):
        return self.__number_of_edges

    def get_in_degree(self, vertex):
        return len(self.__predecessors[vertex])

    def get_out_degree(self, vertex):
        return len(self.__successors[vertex])

    def get_edge_cost(self, origin, target):
        return self.__costs[(origin, target)]

    def is_edge(self, origin, target):
        # only 1 of these can be True
        return target in self.__successors[origin] and origin in self.__predecessors[target] and (origin, target) in self.__costs.keys()

    def add_edge(self, origin, target, cost):
        self.__successors[origin].append(target)
        self.__predecessors[target].append(origin)
        self.__costs[(origin, target)] = cost
        self.__number_of_edges += 1

    def set_edge_cost(self, origin, target, new_cost):
        self.__costs[(origin, target)] = new_cost
