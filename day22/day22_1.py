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

def check_cuboid_is_in_range(x_range, y_range, z_range):
    for val in [x_range[0], x_range[1], y_range[0], y_range[1], z_range[0], z_range[1]]:
        if val < -50 or val > 50:
            return False
    return True


file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
steps = parse_input(lines)

activate_cubes = set()
for mode, x_range, y_range, z_range in steps:
    if not check_cuboid_is_in_range(x_range, y_range, z_range):
        continue
    for x in range(x_range[0], x_range[1]+1):
        for y in range(y_range[0], y_range[1]+1):
            for z in range(z_range[0], z_range[1]+1):
                if mode == 'on':
                    activate_cubes.add((x,y,z))
                else:
                    if (x,y,z) in activate_cubes:
                        activate_cubes.remove((x,y,z))

print(len(activate_cubes))     

file.close()