def negate_binary(binary):
    result = ''
    for bit in binary:
        result += '1' if bit == '0' else '0'
    return result

def most_common_bit_value(measurements, position):
    ones = 0
    zeros = 0
    for measurement in measurements:
        measurement = measurement.strip()
        if measurement[position] == '1':
            ones += 1
        else:
            zeros += 1
    if ones == zeros:
        return '1'
    return '1' if ones > zeros else '0'

def least_common_bit_value(measurements, position):
    return negate_binary(most_common_bit_value(measurements, position))


def filter_by_bit_value_at_position(measurements, position, bit_value):
    return [measurement for measurement in measurements if measurement.strip()[position] == bit_value]


file = open("input.txt", 'r')
lines = file.readlines()
input_size = len(lines)
binary_len = len(lines[0].strip())


# oxygen
filtered_measurements = lines
for index in range(binary_len):
    most_common_bit = most_common_bit_value(filtered_measurements, index)
    filtered_measurements = filter_by_bit_value_at_position(filtered_measurements, index, most_common_bit)
    if len(filtered_measurements) == 1:
        break
oxygen_value = int(filtered_measurements[0].strip(), 2)
print(oxygen_value)

# co2
filtered_measurements = lines
for index in range(binary_len):
    least_common_bit = least_common_bit_value(filtered_measurements, index)
    filtered_measurements = filter_by_bit_value_at_position(filtered_measurements, index, least_common_bit)
    if len(filtered_measurements) == 1:
        break
co2_value = int(filtered_measurements[0].strip(), 2)
print(co2_value)

result = oxygen_value * co2_value
print('result =', result)

file.close()