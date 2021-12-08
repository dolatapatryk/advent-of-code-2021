#       aaaa
#      b    c
#      b    c
#       dddd
#      e    f
#      e    f
#       gggg

# 0: abcefg (6)             0 and 6 are similar, difference in one letter c:d
# 6: abdefg (6)             0 and 9 are similar, difference in one letter e:d
# 9: abcdfg (6)             6 and 9 are less similar, difference in two letters d:c, e:d

# 2: acdeg (5)              2 and 3 are similar, difference in one letter e:f
# 3: acdfg (5)              3 and 5 are similar, difference in one letter c:b
# 5: abdfg (5)              2 and 5 are similar, difference in two letters c:b, e:f

# 1: cf (2)                 1 and 7 are similar, differ in one extra letter in 7 'a'
# 4: bcdf (4)               1 and 4 are less similar, differ in 2 extra letters in 4 'b', 'f'
# 7: acf (3)                
# 8: abcdefg (7)            8 and 0, eight's got extra 'd'
from itertools import permutations

SEGMENTS_DIGIT = {
    'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5,
    'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9
}

def parse_input(lines):
    X = []
    for line in lines:
        splitted = line.split(' | ')
        signal = splitted[0]
        output = splitted[1]
        X.append((signal, output))
    return X

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
X = parse_input(lines)

segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
perms = list(permutations(segments))
result = 0
for x in X:
    signal, output = x
    all_digits = signal + ' ' + output
    unique_digits = set([''.join(sorted(digit)) for digit in all_digits.split(' ')])

    mappings = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    for i, permutation in enumerate(perms):
        for j in range(ord('a'), ord('g')+1):
            mappings[chr(j)] = permutation[j-ord('a')]
        valid = True
        for digit in unique_digits:
            mapped = [mappings[l] for l in digit]
            mapped.sort()
            mapped = ''.join(mapped)
            if mapped not in SEGMENTS_DIGIT:
                valid = False
                break
        if valid:
            break

    number = ''
    for digit in output.split(' '):
        digit = ''.join(sorted(digit))
        mapped = [mappings[l] for l in digit]
        mapped.sort()
        mapped = ''.join(mapped)
        number += str(SEGMENTS_DIGIT[mapped])
    result += int(number)

print('result =', result)
file.close()