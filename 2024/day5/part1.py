import os
import sys

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")

    ording_rules = []
    page_numbers = []
    
    ording_rules_bool = True 
    for line in lines:
        if line == "":
            ording_rules_bool = False 
            continue

        if ording_rules_bool:
            ording_rules.append(line.split("|"))            
        else:
            page_numbers.append(line.split(","))

    return ording_rules, page_numbers

def get_middle_element(_list: list)->int:
    return int(_list[len(_list)//2])

def create_position_dict(_list: list) -> dict:
    positions = {}
    position = 0
    for l in _list:
        positions[l] = position
        position += 1
    return positions 

def comprobate_rules(rules, page):
    correct = True 
    for rule in rules:
        try:
            if page[rule[0]] > page[rule[1]]:
                correct = False
                print(rule[0], rule[1])
                print(page)
                print("-------------")
                break
        except:
            continue

    return correct

ording_rules, page_numbers = read_file()

result = 0
for page in page_numbers:
    di = create_position_dict(page)
    correct = comprobate_rules(ording_rules, di)
    if correct:
        result += get_middle_element(list(di.keys()))
print(result)
