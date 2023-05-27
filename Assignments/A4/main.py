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


def topological_sort_DFS(graph: DirectedGraph, node, topological_sorted_nodes, fully_processed_nodes, in_process_nodes):
    in_process_nodes.add(node)

    for neighbor in graph.parse_outbound_edges(node):
        if neighbor in in_process_nodes:
            return False

        if neighbor not in fully_processed_nodes:
            ok = topological_sort_DFS(graph, neighbor, topological_sorted_nodes, fully_processed_nodes, in_process_nodes)

            if not ok:
                return False

    in_process_nodes.remove(node)
    topological_sorted_nodes.append(node)
    fully_processed_nodes.add(node)

    return True


def solve(graph: DirectedGraph):
    topological_sorted_nodes = []
    fully_processed_nodes = set()
    in_process_nodes = set()

    for node in graph.parse_vertices():
        if node not in fully_processed_nodes:
            ok = topological_sort_DFS(graph, node, topological_sorted_nodes, fully_processed_nodes, in_process_nodes)

            if not ok:
                return []

    return topological_sorted_nodes[::-1]


def get_maximum_cost_path_between_origin_and_target_in_directed_graph_from_topological_order(origin, target, digraph: DirectedGraph, topological_sorted_nodes):
    distance_from_origin_to = []

    for _ in range(len(topological_sorted_nodes)):
        distance_from_origin_to.append(float("-inf"))

    distance_from_origin_to[origin] = 0

    print(distance_from_origin_to)

    for node in topological_sorted_nodes:
        if node == target:
            break

        for neighbor in digraph.parse_outbound_edges(node):
            cost = digraph.get_edge_cost(node, neighbor)

            if distance_from_origin_to[neighbor] < distance_from_origin_to[node] + cost:
                distance_from_origin_to[neighbor] = distance_from_origin_to[node] + cost

    print(distance_from_origin_to)

    return distance_from_origin_to[target]


def main():
    input_file_name = input("input file name: ")

    digraph = read_directed_graph_from_file_first_convention(input_file_name)

    digraph.print_graph()

    topological_sorted_nodes = solve(digraph)

    if not topological_sorted_nodes:
        print("[!] not a DAG")
    else:
        print("possible topological sort:")
        print(topological_sorted_nodes)

        origin, target = get_origin_and_target_node_from_console(digraph)

        cost_of_maximum_cost_path_between_origin_and_target = get_maximum_cost_path_between_origin_and_target_in_directed_graph_from_topological_order(origin, target, digraph, topological_sorted_nodes)

        print(f"cost of the maximum cost path between {origin} and {target}: {cost_of_maximum_cost_path_between_origin_and_target}")


if __name__ == "__main__":
    main()