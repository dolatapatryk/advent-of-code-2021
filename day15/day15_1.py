from cavern import Cavern

file = open('input.txt', 'r')

vertices = {(i,j):int(risk) for i,line in enumerate(file.readlines()) for j,risk in enumerate(line.strip())}

cavern = Cavern(vertices)
cavern.dijkstra((0, 0))

file.close()