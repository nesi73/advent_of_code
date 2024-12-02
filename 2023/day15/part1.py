
def read_file(path):
    file = open(path).read().strip()
    return file.split(',')

def calculate_HASH(ascii_values):
    current_value = 0

    for value in ascii_values:
        current_value = (current_value + value) * 17 % 256
    return current_value

def get_ASCII(_str):
    ascii_values = []
    for char in _str:
        ascii_values.append(ord(char))
    
    return ascii_values

import sys
lines = read_file(sys.argv[1])
solution = 0
for line in lines:
    ascii_values = get_ASCII(line)
    hash_solution = calculate_HASH(ascii_values)
    solution += hash_solution

print(solution)
