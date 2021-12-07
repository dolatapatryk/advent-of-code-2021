from collections import defaultdict
# S_n = (a_1 + a_n)/2 * n
def arithmetic_sum(end_value):
    return (1 + end_value)/2 * (end_value)

file = open('input.txt', 'r')

initial = [int(x) for x in file.read().strip().split(',')]

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
        value += arithmetic_sum(abs(position - i)) * count
    min_fuel = min(min_fuel, value)

print(min_fuel)


file.close()