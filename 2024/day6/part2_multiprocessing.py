import os
import sys
import numpy as np
import copy

IS_LOOP = False

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

def algorithm(board, guard, pos, positions_guard, positions_stops, loop):
    new_pos = move_guard(guard, pos)

    if board[new_pos[0]][new_pos[1]] == ".":
        finish, new_pos = find_first_stop(positions_stops, new_pos, guard, [len(board), len(board[0])])
        if finish:
            return
        elif new_pos in positions_guard:
            loop.append(True)
            return
        positions_guard.append(new_pos)
        board[pos[0]][pos[1]] = "."
        board[new_pos[0]][new_pos[1]] = guard
    else:
        guard = rotate_guard(guard)
        board[pos[0]][pos[1]] = guard
        new_pos = pos 
    algorithm(board, guard, new_pos, positions_guard, positions_stops, loop)

def add_obstable(board, pos):
    copy_board = copy.deepcopy(board)
    copy_board[pos[0]][pos[1]] = "#"
    return copy_board

def possible_obstruction_positions(board, free="."):
    return np.where(np.array(board) == free)


from concurrent.futures import ProcessPoolExecutor, as_completed
# Para procesamiento paralelo usa ProcessPoolExecutor en lugar de ThreadPoolExecutor

def worker(idx_obs, pos_initial_guard, guard, matrix, obstructions, loop):
    # Función que ejecuta la tarea para un índice específico
    positions_guard = [pos_initial_guard]
    new_obstacle_matrix = add_obstable(matrix, [obstructions[0][idx_obs], obstructions[1][idx_obs]])
    positions_stops = find_stops(new_obstacle_matrix)
    algorithm(new_obstacle_matrix, guard, pos_initial_guard, positions_guard, positions_stops, loop)

if __name__ == "__main__":
    import os
    from concurrent.futures import ProcessPoolExecutor
    
    import time
    start = time.time()
    matrix = read_file()
    pos_initial_guard, guard = find_guard(matrix)
    loop = []
    obstructions = possible_obstruction_positions(matrix)

    print(os.cpu_count())
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(worker, idx_obs, pos_initial_guard, guard, matrix, obstructions, loop) for idx_obs in range(len(obstructions[0]))]

    print(len(loop))
    print(time.time() - start)