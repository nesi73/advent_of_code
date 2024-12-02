import os
import sys

def remove_spaces_and_cast_int(_list_: list, space="")-> list:
    new_list = []

    for l in _list_:
        if l != space:
            new_list.append(int(l))

    return new_list

def read_correspondences(txt_file):
    print(f"Reading {txt_file} file")
    seeds = ""
    current_seed = ""
    correspondences = {}

    with open(txt_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.replace("\n", "")
            
            #check if line is empty
            if not line.strip():
                current_seed = ""
            elif "seeds:" in line:
                seeds = remove_spaces_and_cast_int(line.split(":")[-1].split(" "))
            elif current_seed == "":
                current_seed = line.split(":")[0]
            else:
                if current_seed not in correspondences:
                    correspondences[current_seed] = [remove_spaces_and_cast_int(line.split(" "))]
                else:
                    correspondences[current_seed].append(remove_spaces_and_cast_int(line.split(" ")))
        
        f.close()
    return seeds, correspondences

def get_location(seed, correspondences):
    for key in correspondences:
        for options in correspondences[key]:
            dst, source, space = options
            if source <= seed and source + space >= seed:
                seed = dst + abs(seed - source)
                break
    return seed

seeds, correspondences = read_correspondences(sys.argv[1])
min_location = float('inf')

for i in range(len(seeds)):
    if i%2 == 0:
        seed = seeds[i]
        result = get_location(seed, correspondences)
        min_location = result if result < min_location else min_location
    else:
        for j in range(seeds[i]):
            seed = seeds[i-1] + j
            result = get_location(seed, correspondences)
            min_location = result if result < min_location else min_location

print(f"The lowest location number is {min_location}")


