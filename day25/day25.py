file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
positions = {}
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        positions[(i,j)] = c
file.close()

# '>' first, then 'v'
counter = 0
while True:
    moved = False
    new_positions = {}
    east_cucumbers = {k: v for k,v in positions.items() if v == '>'}
    south_cucumbers = {k: v for k,v in positions.items() if v == 'v'}
    for (x,y),_ in east_cucumbers.items():
        position_to_check = (x,y+1) if (x,y+1) in positions else (x, 0)
        if positions[position_to_check] != '.':
            continue
        else:
            new_positions[(x,y)] = '.'
            new_positions[position_to_check] = '>'
            moved = True
    for coords,val in new_positions.items():
        positions[coords] = val
    for (x,y),_ in south_cucumbers.items():
        position_to_check = (x+1,y) if (x+1,y) in positions else (0,y)
        if positions[position_to_check] != '.':
            continue
        else:
            new_positions[(x,y)] = '.'
            new_positions[position_to_check] = 'v'
            moved = True
    for coords,val in new_positions.items():
        positions[coords] = val
    counter += 1
    if not moved:
        break

print(counter)
