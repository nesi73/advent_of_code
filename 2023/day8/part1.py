import sys
import re

def create_dict_map(map):
    map_dict = {}
    for direction in map:
        map_dict[direction[0]] = {"L": direction[1], "R": direction[2]}
    return map_dict

def read_map(txt_file):
    print(f"Reading {txt_file} file")

    with open(txt_file, "r") as f:
        input_txt = f.read()
    f.close()

    instructions=input_txt.split("\n")[0]
    regex = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'

    return list(instructions), create_dict_map(re.findall(regex, input_txt))

def move_in_map_recursion(instructions, map, key, cont):
    if key == 'ZZZ':
        return cont
    else:
        current_instruction = instructions.pop(0)
        instructions.append(current_instruction)
        return move_in_map(instructions, map, map[key][current_instruction], cont + 1)

def move_in_map(instructions, map, key, cont):
    while True:
        if key == 'ZZZ':
            return cont
        else:
            current_instruction = instructions.pop(0)
            instructions.append(current_instruction)
            key = map[key][current_instruction]
            cont += 1

instructions, map = read_map(sys.argv[1])
total_movs = move_in_map(instructions, map, list(map.keys())[0], 0)
print(total_movs)
 
