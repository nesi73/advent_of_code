import os
import sys
import numpy as np

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    antenas = []
    matrix = []
    for l in lines:
        cols = []
        for r in l:
            cols.append(r)
            if r != "." and r not in antenas:
                antenas.append(r)
        matrix.append(cols)
    return matrix, antenas

def search_antenna(matrix, frequency):
    return np.where(np.array(matrix) == frequency)

def search_antinodes(frequencies, shape, antinodes):
    cont = 0
    for idx in range(len(frequencies)):
        for idx2 in range(len(frequencies)):
            if idx == idx2:
                continue
            result = np.add(frequencies[idx], np.subtract(frequencies[idx], frequencies[idx2]))
            if result[0] >= 0 and result[0] < shape[0] and result[1] >= 0 and result[1] < shape[1]:
                
                if [result[0], result[1]] not in antinodes:
                    antinodes.append([result[0], result[1]])
    return cont

def union_where(solution):
    solution_ = []
    for idx in range(len(solution[0])):
        solution_.append([solution[0][idx], solution[1][idx]])
    return solution_

matrix, antenas = read_file()
antinodes = []
for a in antenas:
    antena = search_antenna(matrix, a)
    antena = union_where(antena)
    search_antinodes(antena, np.array(matrix).shape, antinodes)

print(len(antinodes))
