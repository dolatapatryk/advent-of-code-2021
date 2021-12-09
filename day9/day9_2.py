def get_low_points(heightmap):
    low_points = []
    for i, j in heightmap.keys():
        val = heightmap[(i, j)]
        top = heightmap.get((i-1, j), 100)
        bottom = heightmap.get((i+1, j), 100)
        left = heightmap.get((i, j-1), 100)
        right = heightmap.get((i, j+1), 100)
        if val < top and val < bottom and val < left and val < right:
            low_points.append((i, j))
    return low_points

def get_basin(point):
    i, j = point
    basin = []

    return basin

file = open('input2.txt', 'r')

lines = [line.strip() for line in file.readlines()]

heightmap = {(i, j):int(val) for i, line in enumerate(lines) for j, val in enumerate(line)}

low_points = get_low_points(heightmap)

basins = []
for point in low_points:
    basin = get_basin(point)
    basins.append(basin)

basins.sort(key=lambda x: len(x), reverse=True)
print(basins)
        

file.close()