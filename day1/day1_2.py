file = open('input.txt', 'r')

lines = file.readlines()
size = len(lines)
max_index = size - 1
first_sum = True
previous_sum = None
result = 0
for i in range(size):
    if i+1 > max_index or i+2 > max_index:
        break
    actual = int(lines[i])
    plus1 = int(lines[i+1])
    plus2 = int(lines[i+2])
    actual_sum = actual + plus1 + plus2
    print('actual sum = {}'.format(actual_sum))
    if first_sum:
        first_sum = False
        previous_sum = actual_sum
        continue
    if actual_sum > previous_sum:
        print("{} > {}".format(actual_sum, previous_sum))
        result += 1
    previous_sum = actual_sum

print("result = {}".format(result))

file.close()