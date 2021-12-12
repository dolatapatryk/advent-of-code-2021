from collections import deque

def add_edge_to_graph(vertex1, vertex2, graph):
    add_to_graph_dict(vertex1, vertex2, graph)
    add_to_graph_dict(vertex2, vertex1, graph)


def add_to_graph_dict(key, value, graph):
    if key == 'end':
        return
    if key not in graph:
        graph[key] = [value]
    else:
        graph[key].append(value)

def can_visit(vertex, visited):
    return not (vertex.islower() and vertex in visited)

def visit(vertex, graph, visited, paths):
    visited.append(vertex)
    if vertex == 'end':
        paths.append(list(visited))
        visited.pop()
        return
    adjacents = [a for a in graph[vertex] if can_visit(a, visited)]
    for adj in adjacents:
        visit(adj, graph, visited, paths)
    visited.pop()

file = open('input.txt', 'r')

edges = [line.strip() for line in file.readlines()]

graph = {}
for edge in edges:
    vertex1, vertex2 = edge.split('-')
    add_edge_to_graph(vertex1, vertex2, graph)

paths = []
visit('start', graph, deque(), paths)
# for path in paths:
#     print(path)
print(len(paths))


file.close()