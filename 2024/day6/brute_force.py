import os
import sys
import numpy as np
import copy

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    rows, cols = (len(lines), len(lines[0]))
    matrix = [["" for _ in range(cols)] for _ in range(rows)]
    for i, line in enumerate(lines):
        for j, l in enumerate(line):
            matrix[i][j] = l 
    return matrix

def find_guard(board):
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem != "." and elem != "#":
                return [i,j], elem

def move_guard(guard, pos):
    if guard == "^":
        return [pos[0] - 1, pos[1]]
    elif guard == "<":
        return [pos[0], pos[1] - 1]
    elif guard == ">":
        return [pos[0], pos[1] + 1]
    return [pos[0] + 1, pos[1]]

def end_game(board, pos):
    return pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[0])

def rotate_guard(guard):
    if guard == "^":
        return ">"
    elif guard == ">":
        return "v"
    elif guard == "v":
        return "<"
    return "^"

def final_moves(board):
    return sum(row.count("X") for row in matrix)

def algorithm(board, visited, guard, pos):
    new_pos = move_guard(guard, pos)
    
    if end_game(board, new_pos):
        return

    if board[new_pos[0]][new_pos[1]] == ".":
        board[pos[0]][pos[1]] = "."
        board[new_pos[0]][new_pos[1]] = guard
        if new_pos not in visited:
            visited.append(new_pos)
    else:
        guard = rotate_guard(guard)
        board[pos[0]][pos[1]] = guard
        new_pos = pos 
    
    algorithm(board, visited, guard, new_pos)

matrix = read_file()
visited = []
pos_initial_guard, guard = find_guard(matrix)
print(pos_initial_guard, guard)
algorithm(matrix, visited, guard, pos_initial_guard)
print(len(visited))
