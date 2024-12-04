import os
import sys
import numpy as np 

QUERY="XMAS"

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
    positions_x = np.where(matrix == QUERY[0])
    directions = ["up", "down", "left", "rigth", "dul", "dur", "ddl", "ddr"]
    solution = 0
    for i in range(len(positions_x[0])):
        for direction in directions:
            solution += recursive(matrix, [positions_x[0][i], positions_x[1][i]], 0, direction)    
            
    print(solution)

def get_new_position(position:list, direction:str, matrix_shape:list):
    if direction == "up":
        position[0] -= 1
    elif direction == "down":
        position[0] += 1
    elif direction == "left":
        position[1] -= 1
    elif direction == "rigth":
        position[1] += 1
    elif direction == "dul":
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

def recursive(matrix: np.ndarray, position: list, current_position_query: int, direction:str):
    if matrix[position[0]][position[1]] == QUERY[current_position_query] and current_position_query == len(QUERY) - 1:
        return 1
    elif matrix[position[0]][position[1]] == QUERY[current_position_query]:
        new_position = get_new_position(position, direction, matrix.shape)
        
        if new_position is None:
            return 0

        return recursive(matrix, new_position, current_position_query + 1, direction)
    else:
        return 0

matrix = read_file()
print(matrix)
brute_force(matrix)
