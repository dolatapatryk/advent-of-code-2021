from collections import defaultdict

file = open('input.txt', 'r')

initial = [int(x) for x in file.read().strip().split(',')]

print(initial)

fish = defaultdict(int)
for x in initial:
    if x not in fish:
        fish[x] = 0
    fish[x] += 1

for day in range(256):
    actual_fish = defaultdict(int)
    for timer, count in fish.items():
        if timer == 0:
            actual_fish[6] += count
            actual_fish[8] += count
        else:
            actual_fish[timer-1] += count
    fish = actual_fish

print('result =', sum(fish.values()))

file.close()