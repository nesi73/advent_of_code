import os
from typing import final
import numpy as np

def is_valid(dots, numbers):
    current = 0
    seen = []
    for c in dots:
        if c==".":
            if current> 0:
                seen.append(current)
            current = 0
        elif c=="#":
            current+=1
        else:
            assert False
    if current > 0:
        seen.append(current)
    return seen==numbers

def get_combinations(dots, numbers, i):
    if i == len(dots):
        return 1 if is_valid(dots, numbers) else 0
    if dots[i] == "?":
        # You have two options # or . so compute both
        return (get_combinations(dots[:i]+"#"+dots[i+1:], numbers, i+1) +
                get_combinations(dots[:i]+"."+dots[i+1:], numbers, i+1))
    else:
        # Continue searching
        return get_combinations(dots, numbers, i+1)


def read_txt(path):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
        
        final_dots, final_numbers = [], []
        for i, line in enumerate(lines):
            dots, numbers = line.split(" ")
            numbers = [int(x) for x in numbers.split(",")]
            final_dots.append(dots)
            final_numbers.append(numbers)
        f.close()
    return final_dots, final_numbers

final_dots, final_numbers = read_txt("input.txt")
ans = 0

for i in range(len(final_dots)):
    dots, numbers = final_dots[i], final_numbers[i]
    print(dots, numbers)
    ans += get_combinations(dots, numbers, 0)

print(ans)
