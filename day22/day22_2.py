import bisect

def parse_input(lines):
    steps = []
    X = set()
    Y = set()
    Z = set()
    for line in lines:
        splitted = line.split(' ')
        mode = splitted[0]
        x,y,z = splitted[1].split(',')
        min_x,max_x = [int(val) for val in x[2:].split('..')]
        min_y,max_y = [int(val) for val in y[2:].split('..')]
        min_z,max_z = [int(val) for val in z[2:].split('..')]
        X.add(min_x)
        X.add(max_x+1)
        Y.add(min_y)
        Y.add(max_y+1)
        Z.add(min_z)
        Z.add(max_z+1)
        steps.append((mode, (min_x,max_x+1), (min_y, max_y+1), (min_z, max_z+1)))
    X = sorted(X)
    Y = sorted(Y)
    Z = sorted(Z)
    return steps,X,Y,Z

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
steps, X, Y, Z = parse_input(lines)

grid = {}
for mode, x_range, y_range, z_range in steps:
    x1 = bisect.bisect_left(X, x_range[0])
    x2 = bisect.bisect_left(X, x_range[1])  
    y1 = bisect.bisect_left(Y, y_range[0])
    y2 = bisect.bisect_left(Y, y_range[1])  
    z1 = bisect.bisect_left(Z, z_range[0])
    z2 = bisect.bisect_left(Z, z_range[1])  
    for x in range(x1,x2):
        for y in range(y1,y2):
            for z in range(z1,z2):
                grid[(x,y,z)] = 1 if mode == 'on' else 0

result = 0
for (x,y,z),val in grid.items():
    result += val * (X[x+1] - X[x]) * (Y[y+1] - Y[y]) * (Z[z+1] - Z[z])

print(result)

file.close()