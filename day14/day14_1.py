from collections import Counter

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
template = lines[0]
rules = {splitted[0]:splitted[1] for line in lines[2:]  if len(splitted := line.split(' -> ')) > 0}

STEPS = 10
for _ in range(STEPS):
    result = ''
    for i, char in enumerate(template):
        if i == len(template) - 1:
            break
        next_char = template[i+1]
        rule = rules[char+next_char]
        result += rule + next_char if i > 0 else char + rule + next_char
    template = result

frequencies = Counter(template).most_common()
most_common_val = frequencies[0][1]
least_common_val = frequencies[-1][1]
result = most_common_val - least_common_val

print('result =', result)

file.close()