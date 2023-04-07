import copy
import random

from Assignments.A1.domain.CustomExceptions import InvalidNumberOfVerticesError, InvalidNumberOfEdgesError, EdgeAlreadyExistsError, EdgeDoesNotExistsError, VertexAlreadyExistsError, \
    VertexDoesNotExistsError
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


def get_random_directed_graph(number_of_vertices, number_of_edges):
    if number_of_vertices < 0:
        raise InvalidNumberOfVerticesError()

    if number_of_edges > number_of_vertices ** 2:
        raise InvalidNumberOfEdgesError()

    directed_graph = DirectedGraph(number_of_vertices)

    added_edges = 0

    while added_edges < number_of_edges:
        origin = random.randint(0, number_of_vertices - 1)
        target = random.randint(0, number_of_vertices - 1)

        if not directed_graph.is_edge(origin, target):
            cost = random.randint(0, 1000)
            directed_graph.add_edge(origin, target, cost)
            added_edges += 1

    return directed_graph


def print_menu_options():
    print("1: add edge")
    print("2: get edge cost")
    print("3: modify edge")
    print("4: remove edge")
    print("5: check edge")
    print("6: get number of edges")

    print("7: add vertex")
    print("8: get in degree")
    print("9: get out degree")
    print("10: remove vertex")
    print("11: check vertex")
    print("12: get number of vertices")
    print("13: parse vertices")
    print("14: parse inbound edges")
    print("15: parse outbound edges")
    print("16: print graph")

    print("x: exit")


def add_edge(directed_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if directed_graph.is_edge(origin, target):
        raise EdgeAlreadyExistsError()
    else:
        cost = int(input("cost: "))

        directed_graph.add_edge(origin, target, cost)


def get_edge_cost(directed_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if directed_graph.is_edge(origin, target) == False:
        raise EdgeDoesNotExistsError()
    else:
        print(directed_graph.get_edge_cost(origin, target))


def modify_edge(directed_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if directed_graph.is_edge(origin, target):
        new_cost = int(input("new cost: "))
        directed_graph.set_edge_cost(origin, target, new_cost)
    else:
        raise EdgeDoesNotExistsError()


def remove_edge(directed_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if directed_graph.is_edge(origin, target) == False:
        raise EdgeDoesNotExistsError()
    else:
        directed_graph.remove_edge(origin, target)


def check_edge(directed_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if directed_graph.is_edge(origin, target):
        print("Edge exists")
    else:
        print("Edge does not exists")


def get_number_of_edges(directed_graph):
    print(directed_graph.get_number_of_edges())


def add_vertex(directed_graph):
    vertex = int(input("new vertex: "))

    if directed_graph.is_vertex(vertex):
        raise VertexAlreadyExistsError()
    else:
        directed_graph.add_vertex(vertex)


def get_in_degree(directed_graph):
    vertex = int(input("vertex: "))

    if directed_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()
    else:
        print(directed_graph.get_in_degree(vertex))


def get_out_degree(directed_graph):
    vertex = int(input("vertex: "))

    if directed_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()
    else:
        print(directed_graph.get_out_degree(vertex))


def remove_vertex(directed_graph):
    vertex = int(input("vertex: "))

    if directed_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()
    else:
        directed_graph.remove_vertex(vertex)


def check_vertex(directed_graph):
    vertex = int(input("vertex: "))

    if directed_graph.is_vertex(vertex):
        print("Vertex exists")
    else:
        print("Vertex does not exists")


def get_number_of_vertices(directed_graph):
    print(directed_graph.get_number_of_vertices())


def parse_vertices(directed_graph):
    for vertex in directed_graph.parse_vertices():
        print(vertex)


def parse_inbound_edges(directed_graph):
    vertex = int(input("vertex: "))

    if directed_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()
    else:
        for origin in directed_graph.parse_inbound_edges(vertex):
            print(origin)


def parse_outbound_edges(directed_graph):
    vertex = int(input("vertex: "))

    if directed_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()
    else:
        for target in directed_graph.parse_outbound_edges(vertex):
            print(target)


def print_graph(directed_graph):
    directed_graph.print_graph()


def exit_program(directed_graph):
    output_file_name = "output.txt"
    write_directed_graph_to_file(directed_graph, output_file_name)
    exit()


def main():
    try:
        random_directed_graph_1 = get_random_directed_graph(7, 20)

        write_directed_graph_to_file(random_directed_graph_1, "random_graph1.txt")

        random_directed_graph_2 = get_random_directed_graph(6, 40)

        write_directed_graph_to_file(random_directed_graph_2, "random_graph2.txt")
    except Exception as error:
        print(error)
    except InvalidNumberOfEdgesError as error:
        print(error)
    except InvalidNumberOfVerticesError as error:
        print(error)

    while True:
        try:
            input_file_name = input("file name: ")
            input_file_name = input_file_name.strip()
            directed_graph = read_directed_graph_from_file_first_convention(input_file_name)
            break
        except Exception as error:
            print(error)

    menu_options = {
        "1": add_edge,
        "2": get_edge_cost,
        "3": modify_edge,
        "4": remove_edge,
        "5": check_edge,
        "6": get_number_of_edges,
        "7": add_vertex,
        "8": get_in_degree,
        "9": get_out_degree,
        "10": remove_vertex,
        "11": check_vertex,
        "12": get_number_of_vertices,
        "13": parse_vertices,
        "14": parse_inbound_edges,
        "15": parse_outbound_edges,
        "16": print_graph,
        "x": exit_program
    }

    while True:
        try:
            print_menu_options()

            chosen_option = input("> ")

            menu_options[chosen_option](directed_graph)

        except Exception as error:
            print(error)
        except VertexDoesNotExistsError as error:
            print(error)
        except VertexAlreadyExistsError as error:
            print(error)
        except EdgeDoesNotExistsError as error:
            print(error)
        except EdgeAlreadyExistsError as error:
            print(error)
        except InvalidNumberOfVerticesError as error:
            print(error)
        except InvalidNumberOfEdgesError as error:
            print(error)


if __name__ == "__main__":
    main()
