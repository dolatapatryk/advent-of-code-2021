file = open("input.txt", 'r')

counter = 0
previous = None
result = 0
for measure in file:
    if counter == 0:
        previous = int(measure)
        counter += 1
        continue
    if int(measure) > previous:
        result += 1
    counter += 1
    previous = int(measure)

print("result = ", result)