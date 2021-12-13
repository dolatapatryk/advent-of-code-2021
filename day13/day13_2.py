file = open('input.txt', 'r')

positions = {}
folds = []

read_folds = False
for line in file.readlines():
    line = line.strip()
    if line == '':
        read_folds = True
        continue
    if not read_folds:
        x,y = line.split(',')
        positions[(int(x), int(y))] = '#'
    else:
        fold = line.split(' ')[2].split('=')
        folds.append(fold)

for axis, val in folds:
    val = int(val)
    if axis == 'y':
        # zginamy poziomo w górę, czyli wszystkie '#' poniżej linii idą na górę
        for x,y in list(positions):
            if y > val:
                new_y = val - abs(y - val)
                positions[(x, new_y)] = '#'
                del positions[(x, y)]
    else:
        # zginamy pionowe na lewo, czyli wszystkie '#' na prawo od linii idą na lewo
        for x, y in list(positions):
            if x > val:
                new_x = val - abs(x - val)
                positions[(new_x, y)] = '#'
                del positions[(x, y)]

print('result =', len(positions))

max_x = 0
max_y = 0
for y,x in positions.keys():
    max_x = max(max_x, x)
    max_y = max(max_y, y)

res = []
for x in range(max_x + 1):
    row = []
    for y in range(max_y + 1):
        c = '#' if (y,x) in positions else ' '
        row.append(c)
    res.append(row)

for row in res:
    print(row)

file.close()