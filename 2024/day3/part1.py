import os
import sys
import re

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    return lines

def custom_regrex(texto):
    return re.findall(r'mul\((\d+,\d+)\)', texto)

def multiply(results, solution):
    for result in results:
        number1, number2 = result.split(",")
        solution += int(number1) * int(number2)
    return solution

lines=read_file()
solution = 0
for line in lines:
    results = custom_regrex(line)
    solution = multiply(results, solution)
print(solution)
