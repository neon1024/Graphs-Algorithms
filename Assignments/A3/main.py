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


def there_are_negative_cost_cycles_in(graph, origin):
    # Bellman-Ford algorithm to detect negative cost cycles in a graph with costs
    distance_from_origin_to = [float('inf') for _ in range(graph.get_number_of_edges())]
    distance_from_origin_to[origin] = 0

    for start in graph.parse_vertices():
        for end in graph.parse_outbound_edges(start):
            edge_cost = graph.get_edge_cost(start, end)

            if distance_from_origin_to[start] != float('inf') and distance_from_origin_to[start] + edge_cost < distance_from_origin_to[end]:
                distance_from_origin_to[end] = distance_from_origin_to[start] + edge_cost

    for start in graph.parse_vertices():
        for end in graph.parse_outbound_edges(start):
            edge_cost = graph.get_edge_cost(start, end)

            if distance_from_origin_to[start] != float('inf') and distance_from_origin_to[start] + edge_cost < distance_from_origin_to[end]:
                return True

    return False


def main():
    # read the graph
    input_file_name = input("input file name: ")

    directed_graph = read_directed_graph_from_file_first_convention(input_file_name)

    directed_graph.print_graph()

    # read the 2 nodes
    origin_node, target_node = get_origin_and_target_node_from_console(directed_graph)

    # check if there are negative cost cycles between the 2 nodes
    if there_are_negative_cost_cycles_in(directed_graph, origin_node):
        print("[!] there are negative cost cycles in the graph")
        exit(1)

    # TODO find one lowest cost walk between the given 2 nodes (matrix multiplication)
    # TODO display the minimum cost walk between the 2 nodes and its cost
    # TODO display the intermediate matrices
    # TODO test it on 3 small graphs (< 20 nodes) and draw the graphs
    # TODO 1 manual execution of a correct path (5 nodes and 10 edges)
    # TODO 1 manual execution of a negative cost cycle (5 nodes and 10 edges)
    # TODO 1 file containing a correct path and its cost + draw the graph + intermediate matrices (5 nodes and 10 edges)
    pass


if __name__ == "__main__":
    main()
