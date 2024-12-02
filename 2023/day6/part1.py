import numpy as np
import sys

def read_correspondences(txt_file):
    print(f"Reading {txt_file} file")
    times = []
    distances = []

    with open(txt_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.replace("\n", "")
            if "Time" in line:
                times = line.split(":")[-1].split(" ")
            else:
                distances = line.split(":")[-1].split(" ")
        f.close()
    
    times = np.array(times)
    distances = np.array(distances)

    return times[times!=""].astype(int), distances[distances!=""].astype(int)

def calculate_total_travel(time, min_distance):
    time_holding_button = np.linspace(1, time - 1, time - 1)
    time_travelling = time - time_holding_button
    distance_travelled = time_travelling * time_holding_button

    return len(distance_travelled[distance_travelled > min_distance])

times, distances = read_correspondences(sys.argv[1])

number_ways = 1
for i in range(len(times)):
    possibilities_to_win = calculate_total_travel(times[i], distances[i])
    number_ways *= possibilities_to_win

print(f"{number_ways} result of multiply the numbers of ways for beat the record in each race")
