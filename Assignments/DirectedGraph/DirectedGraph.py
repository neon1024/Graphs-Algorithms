from Assignments.DirectedGraph.CustomExceptions import EdgeAlreadyExistError, EdgeDoesNotExistError, VertexAlreadyExistError, VertexDoesNotExistError


class DirectedGraph:
    """
    Directed graph of N vertices, where vertices are from 0 to N-1
    Edges are represented as a dictionary, where the key is a node and the value is a list of the nodes that form an outbound edge with the node
    Each edge has a cost represented as a dictionary of tuples where we have the starting node, target node and the cost
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
        if not self.is_edge(origin, target):
            raise EdgeDoesNotExistError()

        return self.__costs[(origin, target)]

    def set_edge_cost(self, origin, target, new_cost):
        if not self.is_edge(origin, target):
            raise EdgeDoesNotExistError()

        self.__costs[(origin, target)] = new_cost

    def is_edge(self, origin, target):
        return target in self.__successors[origin] and origin in self.__predecessors[target] and (origin, target) in self.__costs.keys()

    def add_edge(self, origin, target, cost):
        if not self.is_edge(origin, target) == 0:
            raise EdgeAlreadyExistError()

        self.__successors[origin].append(target)
        self.__predecessors[target].append(origin)
        self.__costs[(origin, target)] = cost
        self.__number_of_edges += 1

    def remove_edge(self, origin, target):
        if not self.is_edge(origin, target):
            raise EdgeDoesNotExistError()

        del self.__costs[(origin, target)]
        self.__successors[origin].remove(target)
        self.__predecessors[target].remove(origin)
        self.__number_of_edges -= 1

    def add_vertex(self, vertex):
        if vertex in self.parse_vertices():
            raise VertexAlreadyExistError()

        self.__predecessors[vertex] = []
        self.__successors[vertex] = []
        self.__number_of_vertices += 1

    # TODO debug
    def remove_vertex(self, vertex):
        if vertex not in self.parse_vertices():
            raise VertexDoesNotExistError()

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

    def is_vertex(self, vertex):
        return vertex in self.parse_vertices()

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
