import os
import sys
import numpy as np
from numpy.lib import triu_indices 

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")

    numbers = [line.split(" ") for line in lines]
    return numbers

def is_safe(number1, number2, decreasing):
    if (number1 < number2 and decreasing) or (number1 > number2 and not decreasing):
        return False
    elif abs(number1 - number2) == 0 or abs(number1 -number2) > 3:
        return False 

    return True 

def report_safe(report:list, times: int) -> bool:
    report = np.array(report).astype(int)
    i = 0
    decreasing = True if report[0] > report[1] else False
    while i + 1 < len(report):
        #condition if not all array is decreasing or increasing
        if not is_safe(report[i], report[i + 1], decreasing):
            if times == 1:
                return False

            a = report_safe(np.delete(report, i), times + 1)
            b = report_safe(np.delete(report, i+1), times + 1)
            
            if not a and not b:
                # extreme case not assume that first position is correct
                if i == 1:
                    return report_safe(np.delete(report, 0), times + 1)

                return False
            else:
                return True
        i += 1
    return True 


reports = read_file()
safes = 0
for report in reports:
    if report_safe(report, 0):
        safes += 1

print(safes)
