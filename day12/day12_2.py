from collections import deque

SMALL_CAVES = set()

def add_small_caves(cave1, cave2):
    for cave in [cave1, cave2]:
        if cave not in ['start', 'end'] and cave.islower():
            SMALL_CAVES.add(cave)

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

def is_any_small_cave_visited_twice(visited):
    for cave in SMALL_CAVES:
        if visited.count(cave) == 2:
            return True
    return False

def can_visit(vertex, visited):
    if vertex in ['start', 'end'] and vertex in visited:
        return False
    if vertex.islower():
        if vertex not in visited:
            return True
        else:
            return not is_any_small_cave_visited_twice(visited)
    return True

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
    add_small_caves(vertex1, vertex2)
    add_edge_to_graph(vertex1, vertex2, graph)

paths = []
visit('start', graph, deque(), paths)
# for path in paths:
#     print(path)
print(len(paths))


file.close()