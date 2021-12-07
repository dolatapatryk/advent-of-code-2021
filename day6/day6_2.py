def get_descendants_count(timer, days_left):
    if timer+1 > days_left:
        return 0
    result = 0
    count = (days_left - timer+1) / 7 + 1
    for i in range(count):
        if i == 0:
            result += get_descendants_count(8, days_left-)

DAYS = 18

file = open('input2.txt', 'r')

line = file.readline().strip()
initial_fish = []
for number in line.split(','):
    initial_fish.append(int(number))

for fish in initial_fish:
    descendants = get_descendants_count(fish, DAYS)
    counter = 0
    for i in range(descendants):



print('result =', len(fish_arr))

file.close()