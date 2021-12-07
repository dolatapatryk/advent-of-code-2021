from collections import defaultdict

file = open('input.txt', 'r')

initial = [int(x) for x in file.read().strip().split(',')]
initial.sort()
med = initial[len(initial)//2]
print(med)
result = 0
for x in initial:
    result += abs(x-med)
print(result)

initial_positions_count = defaultdict(int)
max_val = 0
for x in initial:
    if x not in initial_positions_count:
        initial_positions_count[x] = 0
    initial_positions_count[x] += 1
    max_val = max(max_val, x)
print(max_val)

min_fuel = float('inf')
for i in range(max_val):
    value = 0
    for position, count in initial_positions_count.items():
        value += abs(position - i) * count
    min_fuel = min(min_fuel, value)

print(min_fuel)


file.close()