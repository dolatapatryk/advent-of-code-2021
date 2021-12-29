from collections import deque

file = open('input.txt', 'r')

instructions = [line.strip() for line in file.readlines()]
file.close()

# after each 'inp' thera are similar 17 instructions
# instructions differ only at 4th, 5th and 15th instruction (after 'inp')
# 4th - (div z n) where n is 1 or 26
# 5th - (add x n) where n is [11,12,13,-5,-3,14,15,-16,14,15,-7,-11,-6,-11]
# 15th - (add y n) where in is [16,11,12,12,12,2,11,4,12,9,10,11,6,15]

# inp w     --> w = input
# mul x 0   --> x = 0
# add x z   --> x = z
# mod x 26  --> x = z%26
# div z n   --> z = z//forth[i]
# add x n   --> x = z%26 + fifth[i]
# eql x w   --> x = 1 if x==input else x = 0
# eql x 0   --> x = 1 if x==0 else x = 0
# mul y 0   --> y = 0
# add y 25  --> y = 25
# mul y x   --> y = y*x = 25*x = 25*0 or 25*1 = 0 or 25
# add y 1   --> y = 1 or 26
# mul z y   --> z = z*y = z//forth[1] * 1 or z//forth[i]*26
# mul y 0   --> y = 0
# add y w   --> y = input
# add y n   --> y = input + fifteenth[i]
# mul y x   --> y = y*x = (input + fifteenth[i]) * (0 or 1)
# add z y   --> z = z+y = (z//forth[1] * 1 or z//forth[i]*26) + ((input + fifteenth[i]) * (0 or 1))

forth       = [1,   1,  1,  26, 26, 1,  1,  26, 1,  1,  26,  26, 26,  26]
fifth       = [11,  12, 13, -5, -3, 14, 15,-16, 14, 15, -7, -11, -6, -11]
fifteenth   = [16,  11, 12, 12, 12, 2,  11, 4,  12, 9,  10,  11,  6,  15]

# w = input i.e. w in [1,9]
# x[t+1] = if ((z[t] % 26) + fifth[t]) != input then 1 else 0
# y[t+1] =  25*x[t+1] + 1 (always 1 or 26)   and then   y[t+1] = input + fifteenth[t]
# z[t+1] = (z[t]//forth[t] * y[t+1] (1or26)) + (input + fifteenth[t])

w = [9]*14
stack = deque()
for i in range(14):
    if fifth[i] >= 11:
        stack.append((i, fifteenth[i]))
    else:
        elem = stack.pop()
        temp = elem[1] + fifth[i]
        digit = 9
        for j in range(1,10):
            if j + temp in range(1,10):
                digit = j
                break
        w[elem[0]] = digit
        w[i] = digit + temp
print(''.join(str(x) for x in w))