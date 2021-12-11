def process_octopus(oct_coords, flashed_octopus, puzzle):
    if oct_coords in flashed_octopus:
        return
    puzzle[oct_coords] += 1
    if puzzle[oct_coords] > 9:
        flash(oct_coords, flashed_octopus, puzzle)

def flash(oct_coords, flashed_octopus, puzzle):
    flashed_octopus[oct_coords] = True
    adjacent = get_adjacent_coords(oct_coords)
    for adj in adjacent:
        if adj in puzzle and adj not in flashed_octopus:
            process_octopus(adj, flashed_octopus, puzzle)
    puzzle[oct_coords] = 0

def get_adjacent_coords(coords):
    i, j = coords
    diagonal = get_diagonal_adjacent_coords(i, j)
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] + diagonal

def get_diagonal_adjacent_coords(i, j):
    return [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    
file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
puzzle = {(i, j):int(val) for i, line in enumerate(lines) for j, val in enumerate(line)}

steps = 100
result = 0
for i in range(steps):
    flashed_octopus = {}
    for octopus in puzzle.items():
        process_octopus(octopus[0], flashed_octopus, puzzle)
    result += len(flashed_octopus)

print('result =', result)


file.close()