import os
import sys
from itertools import product
import numpy as np

OPERATIONS_TYPE = ["+", "*", "||"]

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    operations = []
    for l in lines:
        solution = l.split(":")[0]
        operators = l.split(":")[1].split(" ")[1:]
        operations.append([solution, operators])
    return operations

def generate_possibilities(n, numbers, solution):
    return list(product(OPERATIONS_TYPE, repeat=n))

   
def calculate_operation(number1, number2, str_operation):
    if str_operation == "+":
        return number1 + number2
    elif str_operation == "-":
        return number1 - number2
    elif str_operation == "*":
        return number1 * number2
    elif str_operation == "||":
        return int(str(number1) + str(number2))
    return number1 / number2

def is_correct(original_solution, numbers, operations):
    solution = int(numbers[0])
    for idx in range(len(operations)):
        solution = calculate_operation(int(solution), int(numbers[idx + 1]), operations[idx])
    return solution == int(original_solution)

def union(numbers, operations):
    number = numbers[0]
    final_numbers, final_operations = [], []
    for idx in range(len(operations)):
        if operations[idx] == "||":
            number += numbers[idx + 1]
        else:
            final_numbers.append(number)
            final_operations.append(operations[idx])
            number = numbers[idx + 1]
    final_numbers.append(number)
    return final_numbers, final_operations

operations = read_file()
result = 0
for operation in operations:
    list_ = generate_possibilities(len(operation[1]) - 1, operation[1], operation[0])
    
    for l in list_:
        union(operation[1], l)
        if is_correct(operation[0], operation[1], l):
            result += int(operation[0])
            break

print(result)