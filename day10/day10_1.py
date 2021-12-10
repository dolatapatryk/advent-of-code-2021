file = open('input2.txt', 'r')

lines = [line.strip() for line in file.readlines()]
print(lines)

file.close()