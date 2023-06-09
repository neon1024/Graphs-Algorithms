from copy import deepcopy

from Assignments.DirectedGraph.DirectedGraph import DirectedGraph


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


def get_origin_and_target_node_from_console(graph):
    while True:
        origin_node = int(input("origin: "))
        target_node = int(input("target: "))

        if origin_node not in graph.parse_vertices() and target_node not in graph.parse_vertices():
            print("[!] invalid nodes")
            print("[>] please try again")

        else:
            return origin_node, target_node


def find_minimum_cost_path_between_2_nodes_in(origin, target, directed_graph):
    # initialize the minimum cost paths matrix, first all entries are inf
    minimum_cost_paths_matrix = [[float('inf') for _ in range(directed_graph.get_number_of_vertices())] for _ in range(directed_graph.get_number_of_vertices())]

    # the distance from every node to itself is 0
    for node in directed_graph.parse_vertices():
        minimum_cost_paths_matrix[node][node] = 0

    # if there is a single edge between a starting node and an ending node, then the entry is the cost of that edge
    for start in directed_graph.parse_vertices():
        for end in directed_graph.parse_outbound_edges(start):
            minimum_cost_paths_matrix[start][end] = directed_graph.get_edge_cost(start, end)

    # list of nodes that form the minimum cost path between origin and target
    traversed_nodes_from_origin_to_target = []

    new_minimum_cost_paths_matrix = deepcopy(minimum_cost_paths_matrix)

    changed = True

    while changed:
        changed = False

        # display the intermediate matrix's
        for line in minimum_cost_paths_matrix:
            print(line)
        print()

        for i in range(directed_graph.get_number_of_vertices()):
            for j in range(directed_graph.get_number_of_vertices()):
                # find the new minimum cost path from i to j
                minimum_cost_path = minimum_cost_paths_matrix[i][j]

                for k in range(directed_graph.get_number_of_vertices()):
                    if minimum_cost_paths_matrix[i][k] + minimum_cost_paths_matrix[k][j] < minimum_cost_path:
                        minimum_cost_path = minimum_cost_paths_matrix[i][k] + minimum_cost_paths_matrix[k][j]
                        changed = True

                        # add the node k to the path
                        if i == origin and j == target:
                            traversed_nodes_from_origin_to_target.append(k)

                new_minimum_cost_paths_matrix[i][j] = minimum_cost_path

        minimum_cost_paths_matrix = deepcopy(new_minimum_cost_paths_matrix)

        # check for negative cost cycles
        for i in range(directed_graph.get_number_of_vertices()):
            if minimum_cost_paths_matrix[i][i] < 0:
                print("[!] negative cost cycle detected")
                print("[!] shutting down...")
                exit(1)

    # display the final matrix
    print("the final matrix is:")
    for line in minimum_cost_paths_matrix:
        print(line)
    print()

    if minimum_cost_paths_matrix[origin][target] == float("inf"):
        print(f"[!] there is no path from {origin} to {target}")
    else:
        # display the minimum cost path between the 2 nodes and its cost
        print(f"the cost of the minimum cost path from {origin} to {target} is: {minimum_cost_paths_matrix[origin][target]}")

        minimum_cost_path_between_origin_and_target = [origin] + traversed_nodes_from_origin_to_target + [target]

        print(f"the minimum cost path from {origin} to {target} is: {minimum_cost_path_between_origin_and_target}")


def main():
    # TODO https://csacademy.com/app/graph_editor/

    # read the graph
    input_file_name = input("input file name: ")

    directed_graph = read_directed_graph_from_file_first_convention(input_file_name)

    directed_graph.print_graph()

    # read the 2 nodes
    origin_node, target_node = get_origin_and_target_node_from_console(directed_graph)

    # find one lowest cost walk between the given 2 nodes (matrix multiplication)
    find_minimum_cost_path_between_2_nodes_in(origin_node, target_node, directed_graph)


if __name__ == "__main__":
    main()
