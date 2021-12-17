file = open('input.txt', 'r')

line = file.read().strip()[13:]
x,y = line.split(', ')
min_x, max_x = [int(val) for val in x[2:].split('..')]
min_y, max_y = [int(val) for val in y[2:].split('..')]

result = 0
for v_x in range(-500, 500):
    for v_y in range(500):
        x,y = (0,0)
        highest_y = 0
        found = False
        dx = v_x
        dy = v_y
        for _ in range(200):
            x += dx
            y += dy
            highest_y = max(highest_y, y)
            if min_x <= x <= max_x and min_y <= y <= max_y:
                found = True
            dx += -1 if dx > 0 else 1 if dx < 0 else 0
            dy -= 1
        if found:
            result = max(result, highest_y)
print(result)
file.close()