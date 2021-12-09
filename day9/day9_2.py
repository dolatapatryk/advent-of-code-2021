from functools import reduce

def get_low_points(heightmap):
    low_points = []
    for i, j in heightmap.keys():
        val = heightmap[(i, j)]
        top, bottom, left, right = get_neighbours((i, j), heightmap)
        if val < top[1] and val < bottom[1] and val < left[1] and val < right[1]:
            low_points.append((i, j))
    return low_points

def get_neighbours(point, heightmap):
    i, j = point
    top = heightmap.get((i-1, j), 9)
    bottom = heightmap.get((i+1, j), 9)
    left = heightmap.get((i, j-1), 9)
    right = heightmap.get((i, j+1), 9)
    return (((i-1, j), top), ((i+1, j), bottom), ((i, j-1), left), ((i, j+1), right))

def get_basin(point, heightmap, basin):
    neighbours = get_neighbours(point, heightmap)
    for neighbour in neighbours:
        position, val = neighbour
        if val == 9 or position in basin:
            continue
        basin.append(position)
        get_basin(position, heightmap, basin)

    return basin

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]

heightmap = {(i, j):int(val) for i, line in enumerate(lines) for j, val in enumerate(line)}

low_points = get_low_points(heightmap)

basins = []
for point in low_points:
    basin = get_basin(point, heightmap, [])
    basins.append(basin)

basins.sort(key=lambda x: len(x), reverse=True)
result = reduce((lambda x, y: x * y), [len(x) for x in basins[:3]])
print('result =', result)
        

file.close()