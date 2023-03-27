from Assignments.A1.domain.CustomExceptions import EdgeAlreadyExistsError, EdgeDoesNotExistsError, VertexAlreadyExistsError, VertexDoesNotExistsError


class DirectedGraph:
    """
    A directed graph of N vertices, where vertices are from 0 to N-1
    """

    def __init__(self, number_of_vertices):
        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = 0
        self.__predecessors = {i: [] for i in range(number_of_vertices)}
        self.__successors = {i: [] for i in range(number_of_vertices)}
        self.__costs = {}

    def get_number_of_vertices(self):
        return self.__number_of_vertices

    def get_number_of_edges(self):
        return self.__number_of_edges

    def get_in_degree(self, vertex):
        return len(self.__predecessors[vertex])

    def get_out_degree(self, vertex):
        return len(self.__successors[vertex])

    def get_edge_cost(self, origin, target):
        if self.is_edge(origin, target):
            return self.__costs[(origin, target)]
        else:
            raise EdgeDoesNotExistsError()

    def set_edge_cost(self, origin, target, new_cost):
        if self.is_edge(origin, target):
            self.__costs[(origin, target)] = new_cost
        else:
            raise EdgeDoesNotExistsError()

    def is_edge(self, origin, target):
        # only 1 of these may be True
        return target in self.__successors[origin] and origin in self.__predecessors[target] and (origin, target) in self.__costs.keys()

    def add_edge(self, origin, target, cost):
        # TODO: return True on success, False otherwise
        if self.is_edge(origin, target) == 0:
            self.__successors[origin].append(target)
            self.__predecessors[target].append(origin)
            self.__costs[(origin, target)] = cost
            self.__number_of_edges += 1
        else:
            raise EdgeAlreadyExistsError()

    def remove_edge(self, origin, target):
        # TODO: return True on success, False otherwise
        if self.is_edge(origin, target):
            del self.__costs[(origin, target)]
            self.__number_of_edges -= 1
        else:
            raise EdgeDoesNotExistsError()

    def add_vertex(self, vertex):
        # TODO: return True on success, False otherwise
        if vertex in self.__successors:
            raise VertexAlreadyExistsError()
        else:
            self.__predecessors[vertex] = []
            self.__successors[vertex] = []
            self.__number_of_vertices += 1

    def remove_vertex(self, vertex):
        # TODO: return True on success, False otherwise
        if vertex in self.__successors:
            # remove all edges associated with vertex
            for origin in self.__predecessors[vertex]:
                if (origin, vertex) in self.__costs.keys():
                    del self.__costs[(origin, vertex)]
                    self.__number_of_edges -= 1

            for target in self.__successors[vertex]:
                if (vertex, target) in self.__costs.keys():
                    del self.__costs[(vertex, target)]
                    self.__number_of_edges -= 1

            # remove vertex from the successors of all the predecessors of vertex
            for origin in self.__predecessors[vertex]:
                self.__successors[origin].remove(vertex)

            # remove vertex from the predecessors of all the successors of vertex
            for target in self.__successors[vertex]:
                self.__predecessors[target].remove(vertex)

            # remove vertex from predecessors
            del self.__predecessors[vertex]

            # remove vertex from successors
            del self.__successors[vertex]

            self.__number_of_vertices -= 1

        else:
            raise VertexDoesNotExistsError()

    def is_vertex(self, vertex):
        return vertex in self.__successors

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
        for i in self.__successors:
            print(f"{i}: ", end="")

            for vertex in self.__successors[i]:
                print(f"{vertex}", end=" ")

            print()
