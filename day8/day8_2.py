#       aaaa
#      b    c
#      b    c
#       dddd
#      e    f
#      e    f
#       gggg

# 0: abcefg (6)
# 6: abdefg (6)
# 9: abcdfg (6)

# 2: acdeg (5)
# 3: acdfg (5)
# 5: abdfg (5)

# 1: cf (2)
# 4: bcdf (4)
# 7: acf (3)
# 8: abcdefg (7)

def parse_input(lines):
    X = []
    for line in lines:
        splitted = line.split(' | ')
        signal = splitted[0]
        output = splitted[1]
        X.append((signal, output))
    return X

unique_segments = [2, 4, 3, 7]
digit_segments = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd' 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}
file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
X = parse_input(lines)
# sort string = s = ''.join(sorted(s))
result = 0
for x in X:
    mappings = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    candidates = {'a': set(), 'b': set(), 'c': set(), 'd': set(), 'e': set(), 'f': set(), 'g': set()}
    signal, output = x
    for digit in signal.split(' '):
        segments_count = len(digit)
        letters = [l for l in digit]
        if segments_count == 2:
            candidates['c'].update(letters)
            candidates['f'].update(letters)
        if segments_count == 3:
            candidates['a'].update(letters)
            candidates['c'].update(letters)
            candidates['f'].update(letters)
    # for digit in output.split(' '):
    #     segments = len(digit)
    #     if segments in unique_segments:
    #         result += 1

print('result =', result)

file.close()