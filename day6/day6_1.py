class Fish:
    def __init__(self, timer):
        self.timer = timer

    def produce_fish(self):
        self.timer = 6
        return Fish(8)

    def decrement_timer(self):
        self.timer -= 1

    def get_timer(self):
        return self.timer

    def __str__(self):
        return 'Fish, timer={}'.format(self.timer)

file = open('input.txt', 'r')

line = file.readline().strip()
initial_fish = []
for number in line.split(','):
    initial_fish.append(Fish(int(number)))

fish_arr = initial_fish
for i in range(80):
    new_fish = []
    for fish in fish_arr:
        fish.decrement_timer()
        if fish.get_timer() == -1:
            new_fish.append(fish.produce_fish())
    fish_arr = fish_arr + new_fish

print('result =', len(fish_arr))

file.close()