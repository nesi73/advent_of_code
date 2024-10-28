import numpy as np  
import itertools


def read_galaxy(path):
    print(f"Reading {path} file")

    histories = []
    with open(path, "r") as f:
        lines = [linea.strip() for linea in f.readlines()]        
        board = np.array(np.zeros((len(lines), len(lines[0])))).astype(str)
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                board[i][j] = str(char)
        
        f.close()
    return board

def expand_galaxy(galaxy):
    rows = np.where(np.all(galaxy == '.', axis=1))
    cols = np.where(np.all(galaxy == '.', axis=0))

    return rows[0], cols[0]

def get_min_distance(galaxy, size=1):
    rows, cols = expand_galaxy(galaxy)

    positions_galaxies = np.where(galaxy == '#')
    union_positions = list(zip(positions_galaxies[0], positions_galaxies[1]))
    total_distance = 0

    combinations = list(itertools.combinations(union_positions, 2))

    for pos1, pos2 in combinations:
        min_position_x = min(pos1[0], pos2[0])
        max_position_x = max(pos1[0], pos2[0])
        min_position_y = min(pos1[1], pos2[1])
        max_position_y = max(pos1[1], pos2[1])

        sum = 0
        sum += len(np.where((rows >= min_position_x) & (rows <= max_position_x))[0]) * size
        sum += len(np.where((cols >= min_position_y) & (cols <= max_position_y))[0]) * size
        total_distance += abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + sum
    return total_distance

import time 

galaxy = read_galaxy("input2.txt")
start = time.time()
print(f"Expand galaxy time: {time.time() - start}")
start = time.time()
distance = get_min_distance(galaxy, 1000000 - 1)
print(f"Get min distance time: {time.time() - start}")
print(distance)