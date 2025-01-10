import os
import sys
import numpy as np
import copy

def read_file():
    #lines = open(sys.argv[1]).read().strip()
    lines = open("puzzle.txt").read().strip()

    lines = lines.split("\n")
    rows, cols = (len(lines), len(lines[0]))
    matrix = [["" for _ in range(cols)] for _ in range(rows)]
    for i, line in enumerate(lines):
        for j, l in enumerate(line):
            matrix[i][j] = l 
    return matrix

def get_possibles_stops(stops_search, stops, position):
    final_stops = []
    for idx_stop, s in enumerate(stops_search):
        if s == position:
            final_stops.append([stops[0][idx_stop], stops[1][idx_stop]])
    return np.array(final_stops)

def get_final_moves(board, move="X"):
    return len(np.where(np.array(board) == move)[0])

def find_first_stop(stops, pos_guard, guard, shape_board):
    """
    return if finish and the final position of the guard
    """
    possibles_stops = []
    try:
        if guard == "^":
            possibles_stops = get_possibles_stops(stops[1], stops, pos_guard[1])
            resultado = possibles_stops[possibles_stops[:, 0] < pos_guard[0]][-1]
            resultado = [resultado[0] + 1, resultado[1]]
        elif guard == "v":
            possibles_stops = get_possibles_stops(stops[1], stops, pos_guard[1])
            resultado = possibles_stops[possibles_stops[:, 0] > pos_guard[0]][0]
            resultado = [resultado[0] - 1, resultado[1]]
        elif guard == "<":
            possibles_stops = get_possibles_stops(stops[0], stops, pos_guard[0])
            resultado = possibles_stops[possibles_stops[:, 1] < pos_guard[1]][-1]
            resultado = [resultado[0], resultado[1] + 1]
        else:
            possibles_stops = get_possibles_stops(stops[0], stops, pos_guard[0])
            resultado = possibles_stops[possibles_stops[:, 1] > pos_guard[1]][0]
            resultado = [resultado[0], resultado[1] - 1]
    except:
        if guard == "^":
            return True, [0, pos_guard[1]]
        elif guard == "v":
            return True, [shape_board[0] - 1, pos_guard[1]]
        elif guard == "<":
            return True, [pos_guard[0], 0]
        
        return True, [pos_guard[0], shape_board[1] - 1]
    return False, resultado
        

def find_stops(board, stop="#"):
    return np.where(np.array(board) == stop)

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

def rotate_guard(guard):
    if guard == "^":
        return ">"
    elif guard == ">":
        return "v"
    elif guard == "v":
        return "<"
    return "^"

def print_board(board, pos1, pos2):
    if pos1[0] == pos2[0]:
        _max, _min = max(pos1[1], pos2[1]), min(pos1[1], pos2[1]), 
        board[pos1[0], _min:_max + 1] = 'X'
    else:
        _max, _min = max(pos1[0], pos2[0]), min(pos1[0], pos2[0]), 
        board[_min:_max + 1, pos1[1]] = 'X'
    return board

def algorithm(board, board_visited, guard, pos):
    new_pos = move_guard(guard, pos)

    if board[new_pos[0]][new_pos[1]] == ".":
        finish, new_pos = find_first_stop(positions_stops, new_pos, guard, board_visited.shape)
        board_visited = print_board(board_visited, pos, new_pos)
        if finish:
            return
        board[pos[0]][pos[1]] = "."
        board[new_pos[0]][new_pos[1]] = guard
    else:
        guard = rotate_guard(guard)
        board[pos[0]][pos[1]] = guard
        new_pos = pos 
    algorithm(board, board_visited, guard, new_pos)

import time
start = time.time()
matrix = read_file()
positions_stops = find_stops(matrix)
pos_initial_guard, guard = find_guard(matrix)
board_visited = np.array(copy.copy(matrix))
algorithm(matrix, board_visited, guard, pos_initial_guard)
print(get_final_moves(board_visited))
print(time.time() - start)