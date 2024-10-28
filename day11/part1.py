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

def expand_galaxy(galaxy, size=1):
    i = 0
    while i < galaxy.shape[0]:
        if np.all(galaxy[i] == '.'):
            galaxy = np.insert(galaxy, i, np.full((size, galaxy.shape[1]), "."), axis=0)
            i += size
        i += 1

    j = 0
    while j < galaxy.shape[1]:
        if np.all(galaxy[:,j] == '.'):
            galaxy = np.insert(galaxy, j, np.full((galaxy.shape[0], size), "."), axis=1)
            j += size

        j += 1

    return galaxy

def get_min_distance(galaxy):
    positions_galaxies = np.where(galaxy == '#')
    union_positions = list(zip(positions_galaxies[0], positions_galaxies[1]))
    total_distance = 0

    combinations = list(itertools.combinations(union_positions, 2))

    for pos1, pos2 in combinations:
        total_distance += abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    return total_distance

import time 

galaxy = read_galaxy("input2.txt")
start = time.time()
galaxy_expanded = expand_galaxy(galaxy, 1000000)
print(f"Expand galaxy time: {time.time() - start}")
start = time.time()
distance = get_min_distance(galaxy_expanded)
print(f"Get min distance time: {time.time() - start}")
print(distance)