from Assignments.A1.domain.DirectedGraph import DirectedGraph


class Repository:
    def __init__(self):
        self.__directed_graph = DirectedGraph(0)

    def create_directed_graph(self, number_of_vertices):
        self.__directed_graph = DirectedGraph(number_of_vertices)

    def add_edge(self, origin, target, cost):
        self.__directed_graph.add_edge(origin, target, cost)
