import os
import sys
import numpy as np

NODE_START = 0
NODE_FINISH = 9

def read_file():
    lines = open(sys.argv[1]).read().strip()

    lines = lines.split("\n")
    
    matrix = []
    for l in lines:
        cols = []
        for c in l:
            if c == ".":
                c = "11"
            cols.append(int(c))
        matrix.append(cols)
    return np.array(matrix)

def get_positions(position, shape):
    final_positions = []
    #up
    if position[0] - 1 >= 0:
        final_positions.append([position[0] - 1, position[1]])
    #down
    if position[0] + 1 < shape[0]:
        final_positions.append([position[0] + 1, position[1]])
    #left
    if position[1] - 1 >= 0:
        final_positions.append([position[0], position[1] - 1])
    #rigth
    if position[1] + 1 < shape[1]:
        final_positions.append([position[0], position[1] + 1])

    return final_positions

def search_initial_position(matrix, elem):
    return np.where(matrix == elem)

def algorithm(matrix, current_position, current_elem, trailhead):
    if current_elem == NODE_FINISH and matrix[current_position[0]][current_position[1]] == NODE_FINISH:
        if current_position not in trailhead:
            trailhead.append(current_position)

    elif matrix[current_position[0]][current_position[1]] == current_elem:
        positions = get_positions(current_position, matrix.shape)
        for p in positions:
            algorithm(matrix, p, current_elem + 1, trailhead)

matrix = read_file()
initial_positions = search_initial_position(matrix, elem=NODE_START)
cont = 0
for i in range(len(initial_positions[0])):
    trailhead = []
    algorithm(matrix, [initial_positions[0][i],initial_positions[1][i]], NODE_START, trailhead)
    cont += len(trailhead)

print(cont)