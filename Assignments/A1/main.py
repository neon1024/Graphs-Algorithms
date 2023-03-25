import copy

from Assignments.A1.presentation.console import Console
from Assignments.A1.repository.directed_graph_repository import Repository
from Assignments.A1.service.directed_graph_service import Service
from domain.DirectedGraph import DirectedGraph


def read_directed_graph_from_file_first_convention(file_name: str):
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


def test_directed_graph(directed_graph):
    assert directed_graph.get_number_of_vertices() == 4
    assert directed_graph.get_number_of_edges() == 5

    for vertex in directed_graph.parse_vertices():
        print(vertex)

    assert directed_graph.is_edge(0, 1) == True
    assert directed_graph.is_edge(0, 2) == False

    assert directed_graph.get_in_degree(2) == 2
    assert directed_graph.get_out_degree(2) == 2

    for target in directed_graph.parse_outbound_edges(2):
        print(target)

    for origin in directed_graph.parse_inbound_edges(2):
        print(origin)

    assert directed_graph.get_edge_cost(1, 2) != 100
    directed_graph.set_edge_cost(1, 2, 100)
    assert directed_graph.get_edge_cost(1, 2) == 100

    assert directed_graph.is_edge(3, 1) == False
    assert directed_graph.get_number_of_edges() == 5
    directed_graph.add_edge(3, 1, 10)
    assert directed_graph.get_number_of_edges() == 6
    assert directed_graph.is_edge(3, 1) == True

    assert directed_graph.is_edge(2, 2) == True
    assert directed_graph.get_number_of_edges() == 6
    directed_graph.remove_edge(2, 2)
    assert directed_graph.get_number_of_edges() == 5
    assert directed_graph.is_edge(2, 2) == False

    assert directed_graph.get_number_of_vertices() == 4
    directed_graph.add_vertex(4)
    assert directed_graph.get_number_of_vertices() == 5

    directed_graph.remove_vertex(0)
    assert directed_graph.get_number_of_vertices() == 4
    assert directed_graph.get_number_of_edges() == 3

    directed_graph.print_graph()

    directed_graph_deepcopy = copy.deepcopy(directed_graph)

    directed_graph_deepcopy.remove_vertex(1)

    directed_graph.print_graph()
    directed_graph_deepcopy.print_graph()


def write_directed_graph_to_file(directed_graph, file_name):
    NULL_NODE_SYMBOL = -1
    with open(file_name, "w") as file:
        for vertex in directed_graph.parse_vertices():
            null_vertex = True
            for target in directed_graph.parse_outbound_edges(vertex):
                file.write(f"{vertex} {target} {directed_graph.get_edge_cost(vertex, target)}\n")
                null_vertex = False
            if null_vertex:
                file.write(f"{vertex} {NULL_NODE_SYMBOL}\n")


def main():
    file_name = "first_format.txt"

    # file_name = input("file name: ")
    # file_name = file_name.strip()

    directed_graph = read_directed_graph_from_file_first_convention(file_name)
    directed_graph.print_graph()

    # test_directed_graph(directed_graph)

    directed_graph.add_vertex(4)

    file_name = "output.txt"

    write_directed_graph_to_file(directed_graph, file_name)


if __name__ == "__main__":
    main()
