"""
lcm - least common multiple
Se suele utilizar en problemas relacionados con ciclos y repetición, especialmente en programación y matemáticas. 

Por ejemplo:
Evento A ocurre cada 4 minutos.
Evento B ocurre cada 6 minutos.

Múltiplos de 4: 4, 8, 12, 16, 20, 24, ...
Múltiplos de 6: 6, 12, 18, 24, ...

El primer múltiplo que aparece en ambas listas es 12. Esto significa que el evento A y el evento B ocurrirán juntos cada 12 minutos.
"""

import math
import re

def calculate_least_common_multiple(results) -> int:
    """
    Calculate lcm of a list of numbers
    @param results: list of numbers
    @return lcm: least common multiple of the list
    """

    lcm = results[0]
    for i in results[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

def read_map(txt_file):
    print(f"Reading {txt_file} file")

    with open(txt_file, "r") as f:
        input_txt = f.read()
    f.close()

    instructions=input_txt.split("\n")[0]
    regex = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'

    return list(instructions), re.findall(regex, input_txt)

class DesertMap():
    def __init__(self, instructions, map):
        self.map_desert = {}
        self.instructions = []
        self.initial_nodes = []
        
        self.create_map(map)
        self.add_instructions(instructions)
        self.select_initial_nodes()

    def create_map(self, map):
        """
        Convert txt map to a dictionary -> key_node : (left_node, right_node)
        """
        for direction in map:
            self.map_desert[direction[0]] = (direction[1], direction[2])

    def add_instructions(self, instructions):
        """
        Add instructions to follow in the desert, 0 for left and 1 for right
        """
        for instruction in instructions:
            self.instructions.append(0) if instruction == "L" else self.instructions.append(1)
    
    def select_initial_nodes(self):
        """
        Get all key nodes that end with "A" to start the navigation
        """
        self.initial_nodes = [node for node in self.map_desert.keys() if node[-1] == "A"]
    
    def navigate_desert(self):
        """
        Move through the desert following the instructions until all nodes end with "Z"
        """
        total_movements = []

        for node in self.initial_nodes:
            movements = 0
            
            while node[-1] != "Z":
                node = self.map_desert[node][self.instructions[movements % len(self.instructions)]]
                movements += 1
            total_movements.append(movements)
        
        return calculate_least_common_multiple(total_movements)

if __name__ == "__main__":
    instructions, map = read_map("input2.txt")
    
    desertMap = DesertMap(instructions, map)
    total_movements = desertMap.navigate_desert()
    print("Total movements: ", total_movements)