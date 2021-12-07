from point import Point

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_coords(self):
        return (self.start.x, self.start.y, self.end.x, self.end.y)
    
    def __str__(self):
        return "Line: {} -> {}".format(str(self.start), str(self.end))