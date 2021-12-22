def parse_input(lines):
    steps = []
    for line in lines:
        splitted = line.split(' ')
        mode = splitted[0]
        x,y,z = splitted[1].split(',')
        min_x,max_x = [int(val) for val in x[2:].split('..')]
        min_y,max_y = [int(val) for val in y[2:].split('..')]
        min_z,max_z = [int(val) for val in z[2:].split('..')]
        steps.append((mode, (min_x,max_x), (min_y, max_y), (min_z, max_z)))
    return steps

file = open('input2.txt', 'r')

lines = [line.strip() for line in file.readlines()]
steps = parse_input(lines)

x_ranges = []
y_ranges = []
z_ranges = []
for mode, x_range, y_range, z_range in steps:
    if len(x_ranges) == 0:
        x_ranges.append(x_range)
        continue
    range_idx = None
    x1,x2 = x_range
    for i,r in enumerate(x_ranges):
        if x1 <= r[1] and x2 >= r[0]:
            range_idx = i
            break
    if range_idx is not None:
        xr1,xr2 = x_ranges[range_idx]
        if mode == 'on':
            new_x1 = min(x1, xr1)
            new_x2 = max(x2, xr2)
        else:
            if x2 in range(xr1, xr2+1) and x1 in range(xr1, xr2+1):
                new_x1 = x1
                new_x2 = x2
                x_ranges.append((xr1, x1-1))
                x_ranges.append((x2+1, xr2))
            elif x2 in range(xr1, xr2+1):
                new_x1 = x2+1
                new_x2 = xr2
            elif x1 in range(xr1, xr2+1):
                new_x1 = xr1
                new_x2 = x1-1
        x_ranges[range_idx] = (new_x1, new_x2)
    else:
        if mode == 'on':
            x_ranges.append(x_range)
print(x_ranges)

activate_cubes = set()
# for mode, x_range, y_range, z_range in steps:
#     for x in range(x_range[0], x_range[1]+1):
#         for y in range(y_range[0], y_range[1]+1):
#             for z in range(z_range[0], z_range[1]+1):
#                 if mode == 'on':
#                     activate_cubes.add((x,y,z))
#                 else:
#                     if (x,y,z) in activate_cubes:
#                         activate_cubes.remove((x,y,z))

print(len(activate_cubes))     

file.close()