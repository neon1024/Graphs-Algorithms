from Assignments.A1.domain.CustomExceptions import EdgeAlreadyExistsError, EdgeDoesNotExistsError, VertexAlreadyExistsError


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

    def set_edge_cost(self, origin, target, new_cost):
        self.__costs[(origin, target)] = new_cost

    def is_edge(self, origin, target):
        # only 1 of these may be True
        return target in self.__successors[origin] and origin in self.__predecessors[target] and (origin, target) in self.__costs.keys()

    def add_edge(self, origin, target, cost):
        if self.is_edge(origin, target) == 0:
            self.__successors[origin].append(target)
            self.__predecessors[target].append(origin)
            self.__costs[(origin, target)] = cost
            self.__number_of_edges += 1
        else:
            raise EdgeAlreadyExistsError()

    def remove_edge(self, origin, target):
        if self.is_edge(origin, target):
            del self.__costs[(origin, target)]
            self.__number_of_edges -= 1
        else:
            raise EdgeDoesNotExistsError()

    def add_vertex(self, vertex):
        if vertex in self.__successors:
            raise VertexAlreadyExistsError()
        else:
            self.__predecessors[vertex] = []
            self.__successors[vertex] = []
            self.__number_of_vertices += 1


    def parse_vertices(self):
        for vertex in self.__successors:
            yield vertex

    def parse_inbound_edges(self, vertex):
        for origin in self.__predecessors[vertex]:
            yield origin

    def parse_outbound_edges(self, vertex):
        for target in self.__successors[vertex]:
            yield target

    def print_graph(self):
        for i in range(self.__number_of_vertices):
            print(f"{i}: ", end="")

            for successor in self.__successors[i]:
                print(f"{successor}", end=" ")

            print()
