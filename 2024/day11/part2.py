import os
from re import S
import sys
from functools import cache

def read_file():
    lines = open("puzzle.txt").read().strip()
    lines = lines.split(" ")
    
    return lines

@cache
def cached_convert(stone):
    if stone == '0':
        return ['1']
    elif len(stone) > 1 and len(stone) % 2 == 0:
        middle = int(len(stone) / 2)
        return [str(int(stone[:middle])), str(int(stone[middle:]))]
    else:
        return [str(int(stone) * 2024)]
    
def convert(stone, blink):
    blink.extend(cached_convert(stone))

def algorithm(stones):
    blink = []
    for stone in stones:
        convert(stone, blink)
    return blink

stones = read_file()
for blink_id in range(75):
    stones = algorithm(stones)
print(len(stones))
