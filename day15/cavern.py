import sys
from math import sqrt
from heapdict import heapdict

class Cavern:

    def __init__(self, cavern):
        self.max_idx = (int(sqrt(len(cavern))) - 1)
        self.graph = cavern
        self.adjacency = self.get_adjacency()

    def dijkstra(self, start_vertex):
        distances = {key:sys.maxsize for key in self.graph.keys()}
        distances[start_vertex] = 0
        shortest_path = []
        queue = heapdict()
        for coords, dist in distances.items():
            queue[coords] = dist

        while queue:
            coords, dist = queue.popitem()
            shortest_path.append(coords)

            for adj in self.adjacency[coords]:
                if distances[adj] > (dist + self.graph[adj]):
                    distances[adj] = dist + self.graph[adj]
                    queue[adj] = dist + self.graph[adj]
        # print(distances)
        print(distances[(self.max_idx, self.max_idx)])

    def get_adjacency(self):
        adjacency = {}
        for coords, _ in self.graph.items():
            x,y = coords
            adjacency[coords] = self.get_adjacent(x, y)
        return adjacency

    def get_adjacent(self, x, y):
        top = (x-1, y) if (x-1,y) in self.graph else None
        bottom = (x+1, y) if (x+1,y) in self.graph else None
        left = (x, y-1) if (x,y-1) in self.graph else None
        right = (x, y+1) if (x,y+1) in self.graph else None
        return [x for x in [top, bottom, left, right] if x is not None]