def negate_binary(binary):
    result = ''
    for bit in binary:
        result += '1' if bit == '0' else '0'
    return result

file = open("input.txt", 'r')
lines = file.readlines()
input_size = len(lines)
binary_len = len(lines[0].strip())


# oxygen


        

file.close()