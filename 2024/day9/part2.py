import os
import sys
import copy

def read_file():
    lines = open("test.txt").read().strip()
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

def create_blocks2(line):
    final_char = []
    times_appear = {} #{"n": [[i,j],[i,j]]} n (n de veces que se repite el número, i,j posiciones )
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
    same_i, same_j = 0, len(line) - 1
    while i < j:
        while line[j] == "." and i < j:
            j -= 1
        same_j = j
        same_id = line[j]
        while line[same_j] == same_id and i < j:
            same_j -= 1

        while line[i] != "." and i < j:
            i += 1
        same_i = i
        while line[same_i] == "." and i < j:
            same_i += 1
        
        if same_i - i < j - same_j:
            j = same_j
            i = same_i  
        elif i < j:
            line[i:i + (j - same_j)] = line[same_j+1:j+1]
            new_array = []
            add_blocks(new_array, ".", j - same_j)
            line[same_j+1:j+1] = new_array
            i+=(j - same_j)
            j = same_j
    
    solution = 0
    for idx, char in enumerate(line):
        if char == ".":
            break
        solution += idx * int(char)
    return solution

lines = read_file()
line = create_blocks(lines[0])
print(algorithm(line))

