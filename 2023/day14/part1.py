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

def move_north(matrix):
    new_matrix = matrix
    for j in range(matrix.shape[1]):
        possible_pos_to_move = 0
        for i in range(matrix.shape[0]):
            if matrix[i][j] == "#":
                possible_pos_to_move = i + 1
            elif matrix[i][j] == "O":
                new_matrix[i][j] = "."
                new_matrix[possible_pos_to_move][j] = "O"
                possible_pos_to_move += 1
    return new_matrix

def calculate_weigth(matrix):
    total = matrix.shape[0]
    result = 0

    for _value, row in enumerate(matrix):
        value = total - _value
        result += len(np.where(row == "O")[0]) * value

    return result

new = move_north(matrix)
result = calculate_weigth(new)
print(result)
