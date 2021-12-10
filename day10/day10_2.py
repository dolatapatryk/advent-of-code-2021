from collections import deque

file = open('input.txt', 'r')

def is_line_corrupted(line):
    line = line.strip()
    openers = deque()
    is_corrupted = False
    for c in line:
        if c in ['(', '[', '{', '<']:
            openers.append(c)
        elif c == ')':
            if openers[-1] != '(':
                is_corrupted = True
                break
            else:
                openers.pop()
        elif c == ']':
            if openers[-1] != '[':
                is_corrupted = True
                break
            else:
                openers.pop()
        elif c == '}':
            if openers[-1] != '{':
                is_corrupted = True
                break
            else:
                openers.pop()
        elif c == '>':
            if openers[-1] != '<':
                is_corrupted = True
                break
            else:
                openers.pop()
    return is_corrupted

not_corrupted = [line.strip() for line in file.readlines() if not is_line_corrupted(line)]
openers_chars = ['(', '[', '{', '<']
points = {'(': 1, '[': 2, '{': 3, '<': 4}

res = []
for line in not_corrupted:
    openers = deque()
    for c in line:
        if c in openers_chars:
            openers.append(c)
        else:
            openers.pop()
    openers.reverse()
    result = 0
    for opener in openers:
        result *= 5
        result += points[opener]
    res.append(result)

res.sort()
middle = res[len(res)//2]
print('result =', middle)
    

file.close()