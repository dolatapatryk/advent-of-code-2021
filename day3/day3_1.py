def negate_binary(binary):
    result = ''
    for bit in binary:
        result += '1' if bit == '0' else '0'
    return result

file = open("input.txt", 'r')
lines = file.readlines()
input_size = len(lines)
binary_len = len(lines[0].strip())
sums = []
for i in range(binary_len):
    sums.append(0)
for diagnostic in lines:
    diagnostic = diagnostic.strip()
    counter = 0
    for bit in diagnostic:
        sums[counter] += 1 if bit == '1' else 0
        counter += 1

gamma = ''
for s in sums:
    gamma += '1' if s > input_size/2 else '0'
epsilon = negate_binary(gamma)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

result = gamma * epsilon

print("result =", result)
        

file.close()