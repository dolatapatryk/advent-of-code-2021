def get_pixel_neighbourhood_bits(coords, image, step, outer_val):
    x,y = coords
    bits = ''
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            val = image.get((i,j), outer_val(step))
            bits += '1' if val == '#' else '0'
    return bits

def calc_light_pixels(image):
    result = 0
    for _, val in image.items():
        if val == '#':
            result += 1
    return result

file = open('input.txt', 'r')

algorithm = file.readline().strip()
if algorithm[0] == '.':
    outer_val = lambda _ : '.'
else:
    if algorithm[511] == '.':
        outer_val = lambda step : '.' if step%2==0 else '#'
    else:
        outer_val = lambda step : '.' if step==0 else '#'
file.readline()

x_min = 0
y_min = 0
x_max = 0
y_max = 0
image = {}
for i, line in enumerate(file.readlines()):
    for j, val in enumerate(line.strip()):
        image[(i,j)] = val
        y_max = max(y_max, j)
    x_max = max(x_max, i)

steps = 2
dmax = 5
dmin = 5
for step in range(steps):
    result_image = {}
    x_max += dmax
    x_min -= dmin
    y_max += dmax
    y_min -= dmin
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            coords = (i,j)
            bits = get_pixel_neighbourhood_bits(coords, image, step, outer_val)
            algorithm_val = int(bits, 2)
            result_image[coords] = algorithm[algorithm_val]
    image = result_image

arr = []
for i in range(x_min, x_max):
    row = []
    for j in range(y_min, y_max):
        row.append(image[(i,j)])
    arr.append(row)

for row in arr:
    print(''.join(row))

print(calc_light_pixels(image))

file.close()