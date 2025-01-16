import os
import sys
import copy

def read_file():
    lines = open("puzzle.txt").read().strip()
    lines = lines.split("\n")
    return lines

def add_blocks(array, elem, n):
    for i in range(n):
        array.append(elem)

def create_blocks(line):
    final_char = []
    char = ""
    for idx in range(len(line)):
        if idx%2 == 0:
            char = str(idx//2)
        else:
            char="."
        add_blocks(final_char, char, int(line[idx]))
    return final_char

def algorithm(line):
    #i: left cont j: rigth cont 
    i, j = 0, len(line) - 1
    
    while i < j:
        while line[j] == "." and i < j:
            j -= 1

        while line[i] != "." and i < j:
            i += 1
        
        if i < j:
            line[i] = line[j]
            line[j] = "."
            i+=1
            j-=1
    
    solution = 0
    for idx, char in enumerate(line):
        if char == ".":
            break
        solution += idx * int(char)
    return solution

lines = read_file()
line = create_blocks(lines[0])
print(algorithm(line))

