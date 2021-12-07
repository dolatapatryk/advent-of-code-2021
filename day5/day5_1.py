from point import Point
from line import Line

file = open('input.txt', 'r')

lines = []
max_number = 0
for line in file:
    line = line.strip()
    if line == '':
        continue
    points = line.split(' -> ')
    x1, y1 = points[0].split(',')
    x2, y2 = points[1].split(',')
    
    if x1 == x2 or y1 == y2:
        start = Point(int(x1), int(y1))
        end = Point(int(x2), int(y2))
        lines.append(Line(start, end))
        max_number = max(int(x1), int(x2), int(y1), int(y2), max_number)

diagram = []
for i in range(max_number+1):
    row = []
    for j in range(max_number+1):
        row.append(0)
    diagram.append(row)

for line in lines:
    # x - col, y - row
    x1, y1, x2, y2 = line.get_coords()
    if x1 == x2:
        fixed_range = range(y1, y2+1) if y2 > y1 else range(y2, y1+1)
        for i in fixed_range:
            diagram[i][x1] += 1
    if y1 == y2:
        fixed_range = range(x1, x2+1) if x2 > x1 else range(x2, x1+1)
        for i in fixed_range:
            diagram[y1][i] += 1

result = 0
for row in diagram:
    for val in row:
        if val > 1:
            result += 1

print('result =', result)

file.close()