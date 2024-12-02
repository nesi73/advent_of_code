import os
import sys
import numpy as np 

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")

    left, rigth = [],[]

    for line in lines:
        left.append(line.split("  ")[0])
        rigth.append(line.split("  ")[1])

    return left, rigth

def similariy_score(left:list, rigth: list) -> int:
    left = np.array(left).astype(int)
    rigth = np.array(rigth).astype(int)

    solution = 0
    for i in range(len(left)):
        appear = len(np.where(rigth == left[i])[0])
        solution += left[i] * appear
    return solution

left, rigth = read_file()
solution = similariy_score(left, rigth)
print(solution)

