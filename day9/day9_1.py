file = open('input2.txt', 'r')

lines = [line.strip() for line in file.readlines()]

heightmap = {(i, j):int(val) for i, line in enumerate(lines) for j, val in enumerate(line)}

result = 0
for i, j in heightmap.keys():
    val = heightmap[(i, j)]
    top = heightmap.get((i-1, j), 9)
    bottom = heightmap.get((i+1, j), 9)
    left = heightmap.get((i, j-1), 9)
    right = heightmap.get((i, j+1), 9)
    if val < top and val < bottom and val < left and val < right:
        result += val+1
print('result =', result)
        

file.close()