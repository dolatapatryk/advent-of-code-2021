from cavern import Cavern
from math import sqrt

file = open('input.txt', 'r')

vertices = {(i,j):int(risk) for i,line in enumerate(file.readlines()) for j,risk in enumerate(line.strip())}
offset = int(sqrt(len(vertices)))

new_vertices = {}
for coords, risk in vertices.items():
    new_vertices[coords] = risk
    x, y = coords
    for i in range(5):
        x_offset = i*offset
        for j in range(5):
            if i == 0 and j == 0:
                continue
            risk_offset = i+j
            new_risk = risk+risk_offset
            new_risk = new_risk if new_risk <= 9 else new_risk%9
            y_offset = j*offset
            new_vertices[(x+x_offset, y+y_offset)] = new_risk

cavern = Cavern(new_vertices)
cavern.dijkstra((0, 0))

file.close()