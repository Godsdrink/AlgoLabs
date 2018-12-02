def main():
    input_filename = "govern.in"

    pairs = read_input(input_filename)
    certificate_order = solve(pairs)
    for certificate in certificate_order:
        print("%s" % certificate)


def read_input(filename):
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
        return [line.split() for line in lines]


def solve(pairs):
    graph = construct_graph(pairs)
    ordered_certificates = get_topological_order(graph)
    return ordered_certificates


def construct_graph(pairs):
    graph = {}

    for certificate, prerequisite in pairs:
        if certificate not in graph:
            graph[certificate] = set()
        if prerequisite not in graph:
            graph[prerequisite] = set()
        graph[certificate].add(prerequisite)

    return graph


def get_topological_order(graph):
    return tarjan_dfs(graph)


def tarjan_dfs(graph):
    topological_order = []
    topological_order_set = set()

    unvisited_vertices = set(graph.keys())

    def dfs_stack(start_vertex):

        stack = [start_vertex]

        while len(stack) > 0:
            vertex = stack.pop()
            if vertex in unvisited_vertices:
                unvisited_vertices.remove(vertex)

            unvisited_neighbors = graph[vertex].intersection(unvisited_vertices)

            if len(unvisited_neighbors) == 0:

                if vertex not in topological_order_set:
                    topological_order.append(vertex)
                    topological_order_set.add(vertex)
            else:

                stack.append(vertex)
                stack.extend(unvisited_neighbors)

    while len(unvisited_vertices) > 0:
        dfs_stack(unvisited_vertices.pop())

    return topological_order


if __name__ == "__main__":
    main()
