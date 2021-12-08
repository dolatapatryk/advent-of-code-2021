# segments:
# 0 - 6
# 1 - 2
# 2 - 5
# 3 - 5
# 4 - 4
# 5 - 5
# 6 - 6
# 7 - 3
# 8 - 7
# 9 - 6
# unique - 1, 4, 7, 8

unique_segments = [2, 4, 3, 7]
file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]

X = []
for line in lines:
    splitted = line.split(' | ')
    signal = splitted[0]
    output = splitted[1]
    X.append((signal, output))

result = 0
for x in X:
    signal, output = x
    for digit in output.split(' '):
        segments = len(digit)
        if segments in unique_segments:
            result += 1

print('result =', result)

file.close()