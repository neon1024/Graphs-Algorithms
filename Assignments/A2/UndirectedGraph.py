from Assignments.A2.CustomExceptions import EdgeDoesNotExistsError, EdgeAlreadyExistsError, VertexAlreadyExistsError, VertexDoesNotExistsError, NodesMustBeDifferentError


class UndirectedGraph:
    """
    An undirected graph of N vertices, where vertices are from 0 to N-1
    """

    def __init__(self, number_of_vertices):
        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = 0
        self.__neighbors = {i: [] for i in range(number_of_vertices)}
        self.__costs = {}

    def get_number_of_vertices(self):
        return self.__number_of_vertices

    def get_number_of_edges(self):
        return self.__number_of_edges

    def get_degree(self, vertex):
        return len(self.__neighbors[vertex])

    def get_edge_cost(self, origin, target):
        if self.is_edge(origin, target):
            return self.__costs[(origin, target)]
        else:
            raise EdgeDoesNotExistsError()

    def set_edge_cost(self, origin, target, new_cost):
        if self.is_edge(origin, target):
            self.__costs[(origin, target)] = new_cost
            self.__costs[(target, origin)] = new_cost
        else:
            raise EdgeDoesNotExistsError()

    def is_edge(self, origin, target):
        return (origin, target) in self.__costs.keys() and (target, origin) in self.__costs.keys()

    def add_edge(self, origin, target, cost):
        # TODO: return True on success, False otherwise
        if origin == target:
            raise NodesMustBeDifferentError()

        if self.is_edge(origin, target):
            raise EdgeAlreadyExistsError()

        if self.is_vertex(origin) == 0:
            self.add_vertex(origin)

        if self.is_vertex(target) == 0:
            self.add_vertex(target)

        self.__neighbors[origin].append(target)
        self.__neighbors[target].append(origin)
        self.__costs[(origin, target)] = cost
        self.__costs[(target, origin)] = cost
        self.__number_of_edges += 1

    def remove_edge(self, origin, target):
        # TODO: return True on success, False otherwise
        if self.is_edge(origin, target) == 0:
            raise EdgeDoesNotExistsError()

        self.__neighbors[origin].remove(target)
        self.__neighbors[target].remove(origin)

        del self.__costs[(origin, target)]
        del self.__costs[(target, origin)]

        self.__number_of_edges -= 1

    def add_vertex(self, vertex):
        # TODO: return True on success, False otherwise
        if vertex in self.__neighbors.keys():
            raise VertexAlreadyExistsError()

        self.__neighbors[vertex] = []
        self.__number_of_vertices += 1

    def remove_vertex(self, vertex):
        # TODO: return True on success, False otherwise
        if self.is_vertex(vertex) == 0:
            raise VertexDoesNotExistsError()

        while len(self.__neighbors[vertex]) != 0:
            self.remove_edge(vertex, self.__neighbors[vertex][0])

        del self.__neighbors[vertex]

        self.__number_of_vertices -= 1

    def is_vertex(self, vertex):
        return vertex in self.__neighbors.keys()

    def parse_vertices(self):
        for vertex in self.__neighbors:
            yield vertex

    def parse_edges(self, vertex):
        for neighbour in self.__neighbors[vertex]:
            yield neighbour

    def print_graph(self):
        for node in self.__neighbors.keys():
            print(f"{node}: {self.__neighbors[node]}")
