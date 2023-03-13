import unittest

from Assignments.A1.domain.DirectedGraph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.read_first_file_format()

    def tearDown(self) -> None:
        pass

    def read_first_file_format(self):
        FILE_NAME = "../first_format.txt"
        NUMBER_OF_VERTICES = 0
        NUMBER_OF_EDGES = 1
        ORIGIN = 0
        TARGET = 1
        COST = 2

        with open(FILE_NAME, "r") as file:

            tokens = file.readline()
            tokens = tokens.strip()
            tokens = tokens.split()

            number_of_vertices = int(tokens[NUMBER_OF_VERTICES])
            number_of_edges = int(tokens[NUMBER_OF_EDGES])

            self.__directed_graph = DirectedGraph(number_of_vertices)

            for _ in range(number_of_edges):
                tokens = file.readline()
                tokens = tokens.strip()
                tokens = tokens.split()

                origin = int(tokens[ORIGIN])
                target = int(tokens[TARGET])
                cost = int(tokens[COST])

                self.__directed_graph.add_edge(origin, target, cost)

    def test_get_number_of_vertices(self):
        self.assertEqual(self.__directed_graph.get_number_of_vertices(), 4)

    def test_get_number_of_edges(self):
        self.assertEqual(self.__directed_graph.get_number_of_edges(), 5)

    def test_get_in_degree(self):
        self.assertEqual(self.__directed_graph.get_in_degree(0), 1)
        self.assertEqual(self.__directed_graph.get_in_degree(1), 1)
        self.assertEqual(self.__directed_graph.get_in_degree(2), 2)
        self.assertEqual(self.__directed_graph.get_in_degree(3), 1)

    def test_get_out_degree(self):
        self.assertEqual(self.__directed_graph.get_out_degree(0), 1)
        self.assertEqual(self.__directed_graph.get_out_degree(1), 1)
        self.assertEqual(self.__directed_graph.get_out_degree(2), 2)
        self.assertEqual(self.__directed_graph.get_out_degree(3), 1)

    def test_is_edge(self):
        self.assertEqual(self.__directed_graph.is_edge(0, 1), True)
        self.assertEqual(self.__directed_graph.is_edge(1, 2), True)
        self.assertEqual(self.__directed_graph.is_edge(2, 2), True)
        self.assertEqual(self.__directed_graph.is_edge(2, 3), True)
        self.assertEqual(self.__directed_graph.is_edge(3, 0), True)
        self.assertEqual(self.__directed_graph.is_edge(0, 3), False)

    def test_get_cost(self):
        self.assertEqual(self.__directed_graph.get_edge_cost(0, 1), 10)

    def test_set_edge_cost(self):
        self.__directed_graph.set_edge_cost(1, 2, 20)

        self.assertEqual(self.__directed_graph.get_edge_cost(1, 2), 20)
