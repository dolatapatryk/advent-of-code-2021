file = open('input2.txt', 'r')

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
        positions[(x, y)] = '#'
    else:
        fold = line.split(' ')[2].split('=')
        folds.append(fold)

print(positions)
print(folds)


file.close()