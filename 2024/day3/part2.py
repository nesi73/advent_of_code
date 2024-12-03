import os
import sys
import re

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    return lines

def get_numbers(texto):
      return re.findall(r'mul\((\d+,\d+)\)', texto)

def custom_regrex(sequence: str, query: str) -> iter:
    """
    return position and value of the query found
    """
    return re.finditer(query, sequence)

def iter2dict(_iter:iter) -> dict:
    # key: result regrex, value: position regrex 
    _dict = {}
    for i in _iter:
        _dict[i.group()] = i.span()
    return _dict 

def remove_unnecessary(w):
    """
    only for debug 
    """

    final = []
    correct = True 
    for e in w:
        for f in final:
            if e[0] >= f[0] and e[1] <= f[1]:
                correct = False
                break 
        if correct:
            final.append(e)
        correct = True
    return final 

def colored(sequence, warning_list):
    """
    only for debug
    """
    new_string = ""
    print(sequence)
    print(warning_list)
    warning_list=remove_unnecessary(warning_list)

    start = 0
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    for pos in warning_list:
        new_string += f"{GREEN}{sequence[start:pos[0]]}{RESET}"
        new_string += f"{RED}{sequence[pos[0]:pos[1]]}{RESET}"
        start = pos[1]
    new_string += f"{GREEN}{sequence[start:]}{RESET}"
    print(new_string)

def iter2list(_iter:iter) -> list:
    return [i.span() for i in _iter]

def multiply(results, solution):
    for result in results:
        result = get_numbers(result)[0]
        number1, number2 = result.split(",")
        solution += int(number1) * int(number2)
    return solution

def warning_zones(do:list, donot:list, final:int) -> list:
    do_sort = sorted(do)
    donot_sort = sorted(donot)
    warning_zones_list = []
    
    for dn in donot_sort:
        check = False 
        for do in do_sort:
            if do[0] >= dn[0]:
                check = True 
                warning_zones_list.append([dn[0],do[0]])
                break
        if not check:
            warning_zones_list.append([dn[0], final])
    return warning_zones_list
    
def get_outside_warning_zones(mul: dict, warning_list: list)->list:
    final = []
    
    for m in mul:
        correct = True 
        for w_l in warning_list:
            if mul[m][0] > w_l[0] and mul[m][0] < w_l[1]:
                correct = False
                break
        if correct:
            final.append(m)
    return final

lines=read_file()
solution = 0

for line in lines:
    # Find mul(x,x), do() and don't() in the text
    results_mul = custom_regrex(line, r'mul\((\d+,\d+)\)')
    results_do = custom_regrex(line, r'do\(\)')
    results_donot = custom_regrex(line, r'don\'t\(\)')
    # ------------------------------------

    # transform iter to correct values
    dict_mul = iter2dict(results_mul)
    do = iter2list(results_do)
    donot = iter2list(results_donot)
    # -------------------------------------
    
    # Calculate warning zones
    warning_list = warning_zones(do, donot, len(line))
    #colored(line, warning_list)
    # -------------------------------------
    
    # Get values of mul(x,x) that is outside of warning zones
    results = get_outside_warning_zones(dict_mul, warning_list)
    # -------------------------------------

    solution = multiply(results, solution)
print(solution)
