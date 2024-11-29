import os
import numpy as np 

lines = open("puzzle.txt").read().strip()
lines = lines.split('\n')

matrix = []

for i in range(len(lines)):
    row = []
    for j in range(len(lines[0])):
        row.append(lines[i][j])
    matrix.append(row)

matrix = np.array(matrix)
movements = ["n", "w", "s", "e"]

def move(matrix):
    new_matrix = matrix                           
    for i in range(matrix.shape[0]):
        possible_pos_to_move = 0
        for j in range(matrix.shape[1]):
            if matrix[i][j] == "#":
                possible_pos_to_move = j + 1
            elif matrix[i][j] == "O":
                new_matrix[i][j] = "."
                new_matrix[i][possible_pos_to_move] = "O"
                possible_pos_to_move += 1
    return new_matrix

def same_matrix(initial_matrix, matrix):
    return np.all(initial_matrix == matrix)

def calculate_weigth(matrix):
    total = matrix.shape[0]
    result = 0

    for _value, row in enumerate(matrix):
        value = total - _value
        result += len(np.where(row == "O")[0]) * value

    return result


def move_platform(matrix):
    for movement in movements:
        if movement == "n":
            matrix = matrix.transpose()
        elif movement == "s":
            matrix = matrix.transpose()[:,::-1]
        elif movement == "e":
            matrix = matrix[:,::-1]

        matrix = move(matrix)
        
        if movement == "n":
            matrix = matrix.transpose()
        elif movement == "s":
            matrix = matrix.transpose()[::-1]
        elif movement == "e":
            matrix = matrix[:, ::-1]
    return matrix

import sys 
import copy 

#start program
total_solutions= []
for i in range(int(sys.argv[1])):
    matrix = move_platform(matrix)
    solution = calculate_weigth(matrix)
    if solution not in total_solutions:
        total_solutions.append(solution)
    else:
        print(solution)
