import os
import sys

def read_file():
    lines = open(sys.argv[1]).read().strip()
    lines = lines.split("\n")
    return lines

print(read_file())
