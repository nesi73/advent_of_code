import numpy as np
import sys

def read_correspondences(txt_file):
    print(f"Reading {txt_file} file")
    time = ""
    distance = ""

    with open(txt_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.replace("\n", "")
            if "Time" in line:
                time = line.replace(" ", "").split(":")[-1]
            else:
                distance = line.replace(" ", "").split(":")[-1]
        f.close()
    
    print(time)
    return int(time), int(distance)

def calculate_total_travel(time, min_distance):
    time_holding_button = np.linspace(1, time - 1, time - 1)
    time_travelling = time - time_holding_button
    distance_travelled = time_travelling * time_holding_button

    return len(distance_travelled[distance_travelled > min_distance])

time, distance = read_correspondences(sys.argv[1])

number_ways = 1
possibilities_to_win = calculate_total_travel(time, distance)
number_ways *= possibilities_to_win

print(f"{number_ways} result of multiply the numbers of ways for beat the record in each race")
