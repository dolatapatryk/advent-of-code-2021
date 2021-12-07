class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def __str__(self):
        return "Line: {} -> {}".format(str(self.start), str(self.end))

file = open('input2.txt', 'r')

lines = []
for line in file:
    line = line.strip()
    if line == '':
        continue
    points = line.split(' -> ')
    x1, y1 = points[0].split(',')
    x2, y2 = points[1].split(',')
    
    if x1 == x2 or y1 == y2:
        start = Point(x1, y1)
        end = Point(x2, y2)
        lines.append(Line(start, end))

for line in lines:
    print(line)

file.close()