import os
from re import S
import sys

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split(" ")
    
    return lines

def convert(stone, blink):
    if stone == '0':
        blink.append('1')
    elif len(stone) > 1 and len(stone)%2==0:
        middle = int(len(stone)/2)
        left = str(int(stone[:middle]))
        right = str(int(stone[middle:]))
        blink.append(left)
        blink.append(right)
    else:
        blink.append(str(int(stone)*2024))

def algorithm(stones):
    blink = []
    for stone in stones:
        convert(stone, blink)
    return blink

stones = read_file()
for blink_id in range(int(sys.argv[2])):
    stones = algorithm(stones)
print(len(stones))
