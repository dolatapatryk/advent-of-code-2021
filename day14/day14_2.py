from collections import defaultdict, Counter

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
template = lines[0]
rules = {splitted[0]:splitted[1] for line in lines[2:]  if len(splitted := line.split(' -> ')) > 0}

pairs = Counter()
chars = Counter()
for i in range(len(template) - 1):
    pairs[template[i] + template[i+1]] += 1
    chars[template[i]] += 1
chars[template[len(template)-1]] += 1

STEPS = 40
for _ in range(STEPS):
    actual_pairs = Counter()
    for pair, counter in pairs.items():
        product = rules[pair]
        actual_pairs[pair[0] + product] += counter
        actual_pairs[product + pair[1]] += counter
        chars[product] += counter
    pairs = actual_pairs

most_common = chars.most_common()
most_common_val = most_common[0][1]
least_common_val = most_common[-1][1]
result = most_common_val - least_common_val

print('result =', result)

file.close()