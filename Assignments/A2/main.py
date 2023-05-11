from Assignments.UndirectedGraph.CustomExceptions import EdgeAlreadyExistError, EdgeDoesNotExistError, VertexAlreadyExistError, VertexDoesNotExistError, InvalidNumberOfEdgesError, InvalidNumberOfVerticesError, \
    NodesMustBeDifferentError
from Assignments.UndirectedGraph.UndirectedGraph import UndirectedGraph


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

            for target in undirected_graph.parse_edges(vertex):
                file.write(f"{vertex} {target} {undirected_graph.get_edge_cost(vertex, target)}\n")
                null_vertex = False

            if null_vertex:
                file.write(f"{vertex} {NULL_NODE_SYMBOL}\n")


def add_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target):
        raise EdgeAlreadyExistError()

    cost = int(input("cost: "))
    undirected_graph.add_edge(origin, target, cost)


def get_edge_cost(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target) == 0:
        raise EdgeDoesNotExistError()

    print(undirected_graph.get_edge_cost(origin, target))


def modify_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target) == 0:
        raise EdgeDoesNotExistError()

    new_cost = int(input("new cost: "))
    undirected_graph.set_edge_cost(origin, target, new_cost)


def remove_edge(undirected_graph):
    origin = int(input("origin: "))
    target = int(input("target: "))

    if undirected_graph.is_edge(origin, target) == 0:
        raise EdgeDoesNotExistError()

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
        raise VertexAlreadyExistError()

    undirected_graph.add_vertex(vertex)


def get_degree(undirected_graph):
    vertex = int(input("vertex: "))

    if undirected_graph.is_vertex(vertex) == False:
        raise VertexDoesNotExistError()

    print(undirected_graph.get_degree(vertex))


def remove_vertex(undirected_graph):
    vertex = int(input("vertex: "))

    if undirected_graph.is_vertex(vertex) == 0:
        raise VertexDoesNotExistError()

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
        raise VertexDoesNotExistError()

    for neighbor in undirected_graph.parse_edges(vertex):
        print(neighbor)


def print_graph(undirected_graph):
    undirected_graph.print_graph()


def exit_program(undirected_graph):
    output_file_name = "output.txt"
    write_undirected_graph_to_file(undirected_graph, output_file_name)
    exit()


def DFS(undirected_graph, root, visited_nodes, components, costs):
    # for each neighbor of the given root that is not yet visited we perform a DFS
    for neighbor in undirected_graph.parse_edges(root):
        if neighbor not in visited_nodes:
            # mark the node as visited
            visited_nodes.append(neighbor)

            # add the node as a neighbor of the root in the new graph
            components[root].append(neighbor)

            # also add the root as a neighbor of the node in the new graph
            components[neighbor] = [root]

            # get the edge cost from the original graph
            edge_cost = undirected_graph.get_edge_cost(root, neighbor)

            # store the edge cost
            costs[(root, neighbor)] = edge_cost
            costs[(neighbor, root)] = edge_cost

            # perform the DFS on the neighbor of the root
            DFS(undirected_graph, neighbor, visited_nodes, components, costs)

            print(f"{neighbor} -> ", end="")


def find_the_connected_components_of_an_undirected_graph_using_DFS(undirected_graph):
    visited_nodes = []  # store the visited nodes
    graphs = []  # store the connected components as graphs
    costs = {}  # store the edge costs of all edges

    # traverse each node of the graph that is not yet visited and pass it as the root to the DFS function
    for root in undirected_graph.parse_vertices():
        if root not in visited_nodes:
            # mark the root as visited
            visited_nodes.append(root)

            # a dictionary of node: [neighbors] representing a new graph based on a connected component
            components = {root: []}

            # perform the DFS on the chosen node
            DFS(undirected_graph, root, visited_nodes, components, costs)

            # store the information about the connected component as a dictionary
            graphs.append(components)

            print(f"{root} -> ", end="")

    print("None")
    print()

    # constructing the graphs based on the connected components found
    for graph in graphs:
        new_undirected_graph = UndirectedGraph(0)

        for node in graph.keys():
            isolated_node = True

            for neighbor in graph[node]:
                if new_undirected_graph.is_edge(node, neighbor) == 0:
                    new_undirected_graph.add_edge(node, neighbor, costs[(node, neighbor)])
                    isolated_node = False

            if isolated_node and new_undirected_graph.is_vertex(node) == 0:
                new_undirected_graph.add_vertex(node)

        print("Connected Component:")
        new_undirected_graph.print_graph()
        print()


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
    # undirected_graph = UndirectedGraph(14)
    #
    # undirected_graph.add_edge(0, 1, 1)
    # undirected_graph.add_edge(0, 2, 2)
    # undirected_graph.add_edge(1, 3, 3)
    # undirected_graph.add_edge(3, 4, 4)
    # undirected_graph.add_edge(3, 6, 5)
    # undirected_graph.add_edge(2, 5, 6)
    # undirected_graph.add_edge(7, 8, 7)
    # undirected_graph.add_edge(9, 10, 8)
    # undirected_graph.add_edge(10, 11, 9)
    # undirected_graph.add_edge(11, 12, 10)
    # undirected_graph.add_edge(11, 13, 11)
    while True:
        input_file_name = input("input file name: ")

        try:
            undirected_graph = read_undirected_graph_from_file_first_convention(input_file_name)

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
        except VertexDoesNotExistError as error:
            print(error)
        except VertexAlreadyExistError as error:
            print(error)
        except EdgeDoesNotExistError as error:
            print(error)
        except EdgeAlreadyExistError as error:
            print(error)
        except InvalidNumberOfVerticesError as error:
            print(error)
        except InvalidNumberOfEdgesError as error:
            print(error)
        except NodesMustBeDifferentError as error:
            print(error)


if __name__ == "__main__":
    main()
