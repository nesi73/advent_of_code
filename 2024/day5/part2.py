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

def is_correct(_list):
    pos = 0
    for l in _list:
        if l != pos:
            return False
        pos+=1
    return True

def get_middle(_dict)->int:
    middle = len(_dict)//2

    inverted_dict = {value: key for key, value in _dict.items()}
    return int(inverted_dict[middle])

def algorithm(page, rules):
    dict_cont = {}
    for p in page:
        dict_cont[p] = 0

    for rule in rules:
        if rule[0] in page and rule[1] in page:
            dict_cont[rule[1]] += 1
    
    return dict_cont


ording_rules, page_numbers = read_file()

result = 0
for page in page_numbers:
    result_dict = algorithm(page, ording_rules)
    if not is_correct(result_dict.values()):
        result += get_middle(result_dict)
print(result)
