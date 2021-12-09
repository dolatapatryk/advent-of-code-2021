file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]

heightmap = {(i, j):int(val) for i, line in enumerate(lines) for j, val in enumerate(line)}

result = 0
for i, j in heightmap.keys():
    val = heightmap[(i, j)]
    top = heightmap.get((i-1, j), 100)
    bottom = heightmap.get((i+1, j), 100)
    left = heightmap.get((i, j-1), 100)
    right = heightmap.get((i, j+1), 100)
    if val < top and val < bottom and val < left and val < right:
        result += val+1
print('result =', result)
        

file.close()