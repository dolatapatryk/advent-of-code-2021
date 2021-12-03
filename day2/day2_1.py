file = open("input.txt", 'r')

horizontal = 0
depth = 0
for command in file:
    splitted = command.split(' ')
    direction = splitted[0]
    value = int(splitted[1])
    if direction == 'forward':
        horizontal += value
    else:
        if direction == 'down':
            depth += value
        else:
            depth -= value

result = horizontal * depth

print("result = {}".format(result))

file.close()