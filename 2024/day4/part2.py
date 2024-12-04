import os
import sys
import numpy as np 
import copy

QUERY="MAS"

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    matrix = []

    for l in lines:
        row = []
        for char in l:
            row.append(char)

        matrix.append(row)
    return np.array(matrix)

def brute_force(matrix: np.ndarray) -> int:
    positions_x = np.where(matrix == QUERY[1]) #search A
    directions = [["dul", "ddr"], ["dur", "ddl"]]
    solution = 0
    for i in range(len(positions_x[0])):
        current_solution = 0
        for direction in directions:
            current_solution += 1 if query_in_diagonal(matrix, [positions_x[0][i], positions_x[1][i]], direction) else 0
        if current_solution == 2:
            solution += 1            
    print(solution)

def get_new_position(position:list, direction:str, matrix_shape:list):
    if direction == "dul":
        position[0] -= 1
        position[1] -= 1
    elif direction == "dur":
        position[0] -= 1
        position[1] += 1
    elif direction == "ddl":
        position[0] += 1
        position[1] -= 1
    else:
        position[0] += 1
        position[1] += 1

    #comprobar que esta dentro
    if position[0] < 0 or position[1] < 0 or position[0] >= matrix_shape[0] or position[1] >= matrix_shape[1]:
        return None
    else:
        return position

def query_in_diagonal(matrix, position, directions):
    letters = []
    for direction in directions:
        new_position = get_new_position(copy.copy(position), direction, matrix.shape)
        if new_position is None:                  
            return False 
    
        letters.append(matrix[new_position[0]][new_position[1]])
    return "M" in letters and "S" in letters

matrix = read_file()
print(matrix)
brute_force(matrix)
