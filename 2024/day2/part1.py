import os
import sys
import numpy as np
from numpy.lib import triu_indices 

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")

    numbers = [line.split(" ") for line in lines]
    return numbers

def is_safe(report:list) -> bool:
    report = np.array(report).astype(int)
    
    decreasing = True if report[0] > report[1] else False
    for i in range(len(report) - 1):
        #condition if not all array is decreasing or increasing
        if (report[i] < report[i+1] and decreasing) or (report[i] > report[i+1] and not decreasing):
            return False  
        elif abs(report[i] - report[i+1]) == 0 or abs(report[i] - report[i+1]) > 3:
            return False
    return True 


reports = read_file()
safes = 0
for report in reports:
    safes += 1 if is_safe(report) else 0

print(safes)
