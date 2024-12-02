import os
import sys

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")

    left, rigth = [],[]

    for line in lines:
        left.append(line.split("  ")[0])
        rigth.append(line.split("  ")[1])

    return left, rigth

def calculate_distance(left:list, rigth: list) -> int:
    left_sort = sorted(left)
    rigth_sort = sorted(rigth)
    
    solution = 0
    for i in range(len(left_sort)):
        solution += abs(int(left_sort[i]) - int(rigth_sort[i]))
    return solution

left, rigth = read_file()
solution = calculate_distance(left, rigth)
print(solution)

