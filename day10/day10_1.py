from collections import deque

file = open('input.txt', 'r')

res = 0
for line in file.readlines():
    line = line.strip()
    openers = deque()
    for c in line:
        if c in ['(', '[', '{', '<']:
            openers.append(c)
        elif c == ')':
            if openers[-1] != '(':
                res += 3
                break
            else:
                openers.pop()
        elif c == ']':
            if openers[-1] != '[':
                res += 57
                break
            else:
                openers.pop()
        elif c == '}':
            if openers[-1] != '{':
                res += 1197
                break
            else:
                openers.pop()
        elif c == '>':
            if openers[-1] != '<':
                res += 25137
                break
            else:
                openers.pop()
print(res)

file.close()