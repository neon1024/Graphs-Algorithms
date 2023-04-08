from Assignments.A2.CustomExceptions import EdgeAlreadyExistsError, EdgeDoesNotExistsError, VertexAlreadyExistsError, VertexDoesNotExistsError, InvalidNumberOfEdgesError, InvalidNumberOfVerticesError, \
    NodesMustBeDifferentError
from Assignments.A2.UndirectedGraph import UndirectedGraph


def read_undirected_graph_from_file_first_convention(file_name: str):
    # TODO modify for undirected graphs
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

        undirected_graph = UndirectedGraph(number_of_vertices)

        for _ in range(number_of_edges):
            tokens = file.readline()
            tokens = tokens.strip()
            tokens = tokens.split()

            origin = int(tokens[ORIGIN])
            target = int(tokens[TARGET])
            cost = int(tokens[COST])
            undirected_graph.add_edge(origin, target, cost)

    return undirected_graph


def write_undirected_graph_to_file(undirected_graph, file_name):
    # TODO modify for undirected graphs
    NULL_NODE_SYMBOL = -1
    with open(file_name, "w") as file:
        for vertex in undirected_graph.parse_vertices():
            null_vertex = True
            for target in undirected_graph.parse_outbound_edges(vertex):
                file.write(f"{vertex} {target} {undirected_graph.get_edge_cost(vertex, target)}\n")
                null_vertex = False
            if null_vertex:
                file.write(f"{vertex} {NULL_NODE_SYMBOL}\n")


def add_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target):
        raise EdgeAlreadyExistsError()

    cost = int(input("cost: "))
    undirected_graph.add_edge(origin, target, cost)


def get_edge_cost(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target) == 0:
        raise EdgeDoesNotExistsError()

    print(undirected_graph.get_edge_cost(origin, target))


def modify_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target) == 0:
        raise EdgeDoesNotExistsError()

    new_cost = int(input("new cost: "))
    undirected_graph.set_edge_cost(origin, target, new_cost)


def remove_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target) == 0:
        raise EdgeDoesNotExistsError()

    undirected_graph.remove_edge(origin, target)


def check_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target):
        print("Edge exists")
    else:
        print("Edge does not exists")


def get_number_of_edges(undirected_graph):
    print(undirected_graph.get_number_of_edges())


def add_vertex(undirected_graph):
    vertex = int(input("new vertex: "))

    if undirected_graph.is_vertex(vertex):
        raise VertexAlreadyExistsError()

    undirected_graph.add_vertex(vertex)


def get_degree(undirected_graph):
    vertex = int(input("vertex: "))

    if undirected_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()

    print(undirected_graph.get_degree(vertex))


def remove_vertex(undirected_graph):
    vertex = int(input("vertex: "))

    if undirected_graph.is_vertex(vertex) == 0:
        raise VertexDoesNotExistsError()

    undirected_graph.remove_vertex(vertex)


def check_vertex(undirected_graph):
    vertex = int(input("vertex: "))

    if undirected_graph.is_vertex(vertex):
        print("Vertex exists")

    print("Vertex does not exists")


def get_number_of_vertices(undirected_graph):
    print(undirected_graph.get_number_of_vertices())


def parse_vertices(undirected_graph):
    for vertex in undirected_graph.parse_vertices():
        print(vertex)


def parse_edges(undirected_graph):
    vertex = int(input("vertex: "))

    if undirected_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistsError()

    for neighbor in undirected_graph.parse_edges(vertex):
        print(neighbor)


def print_graph(undirected_graph):
    undirected_graph.print_graph()


def exit_program(undirected_graph):
    # output_file_name = "output.txt"
    # write_undirected_graph_to_file(undirected_graph, output_file_name)
    exit()


def DFS(undirected_graph, root, visited_nodes, components):
    visited_nodes.append(root)

    for neighbor in undirected_graph.parse_edges(root):
        if neighbor not in visited_nodes:
            print(f"{neighbor} -> ", end="")
            visited_nodes.append(neighbor)
            components[root].append(neighbor)
            components[neighbor] = [root]
            DFS(undirected_graph, neighbor, visited_nodes, components)


def find_the_connected_components_of_an_undirected_graph_using_DFS(undirected_graph):
    visited_nodes = []
    graphs = []

    for root in undirected_graph.parse_vertices():
        if root not in visited_nodes:
            print(f"{root} -> ", end="")
            components = {root: []}
            DFS(undirected_graph, root, visited_nodes, components)
            graphs.append(components)

    print("None")
    
    for graph in graphs:
        print(graph)


def print_menu_options():
    print("1: add edge")
    print("2: get edge cost")
    print("3: modify edge")
    print("4: remove edge")
    print("5: check edge")
    print("6: get number of edges")

    print("7: add vertex")
    print("8: get degree")
    print("9: remove vertex")
    print("10: check vertex")
    print("11: get number of vertices")
    print("12: parse vertices")
    print("13: parse edges")
    print("14: print graph")

    print("15: find the connected components of the graph using DFS")

    print("x: exit")


def main():
    # TODO create a list with the connected components generated as graph objects
    # while True:
    #     try:
    #         input_file_name = input("file name: ")
    #         input_file_name = input_file_name.strip()
    #         undirected_graph = read_undirected_graph_from_file_first_convention(input_file_name)
    #         break
    #     except Exception as error:
    #         print(error)

    undirected_graph = UndirectedGraph(14)

    undirected_graph.add_edge(0, 1, 1)
    undirected_graph.add_edge(0, 2, 2)
    undirected_graph.add_edge(1, 3, 3)
    undirected_graph.add_edge(3, 4, 4)
    undirected_graph.add_edge(3, 6, 5)
    undirected_graph.add_edge(2, 5, 6)
    undirected_graph.add_edge(7, 8, 7)
    undirected_graph.add_edge(9, 10, 8)
    undirected_graph.add_edge(10, 11, 9)
    undirected_graph.add_edge(11, 12, 10)
    undirected_graph.add_edge(11, 13, 11)

    menu_options = {
        "1": add_edge,
        "2": get_edge_cost,
        "3": modify_edge,
        "4": remove_edge,
        "5": check_edge,
        "6": get_number_of_edges,
        "7": add_vertex,
        "8": get_degree,
        "9": remove_vertex,
        "10": check_vertex,
        "11": get_number_of_vertices,
        "12": parse_vertices,
        "13": parse_edges,
        "14": print_graph,
        "15": find_the_connected_components_of_an_undirected_graph_using_DFS,
        "x": exit_program
    }

    while True:
        try:
            print_menu_options()

            chosen_option = input("> ")

            menu_options[chosen_option](undirected_graph)

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
        except NodesMustBeDifferentError as error:
            print(error)


if __name__ == "__main__":
    main()
