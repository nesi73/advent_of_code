import os
import sys
import numpy as np 

MOVEMENTS = 1800000

class Map:
    def __init__(self, row, col):
        self.row, self.col = row, col
        self.map = np.zeros((row, col))

    def add_robot(self, robot):
        self.map[robot.p[0]][robot.p[1]] += 1
    
    def safety_factor(self):
        # Divide the map in 4 quadrants
        quadrants = []
        middle_row = self.row // 2
        middle_col = self.col // 2
        quadrants.append(self.map[:middle_row, :middle_col])
        quadrants.append(self.map[:middle_row, middle_col+1:])
        quadrants.append(self.map[middle_row+1:, :middle_col])
        quadrants.append(self.map[middle_row+1:, middle_col+1:])
        
        # Get the sum of each quadrant    
        solution = 1
        for q in [np.sum(q) for q in quadrants]:
            solution *= q
        return solution
    
    def unique_robots(self):
        #search if exists positions > 1
        return np.sum(self.map > 1)

class Robot:
    p = [] #where x represents the number of tiles the robot is from the left wall and y represents the number of tiles from the top wall (when viewed from above)
    v = [] #Positive x means the robot is moving to the right, and positive y means the robot is moving down.
    
    def move(self, limit_row, limit_col):
        x = self.p[0] + self.v[0]
        y = self.p[1] + self.v[1]
        if x < 0 or x >= limit_row:
            x = abs(limit_row - abs(x))
        if y < 0 or y >= limit_col:
            y = abs(limit_col - abs(y))

        self.p = [x,y]

def get_max_positions(robots: list):
    """
    Get max position of robots for get row, col of the map
    """
    row, col = 0,0 
    for r in robots:
        if r.p[0] > row:
            row = r.p[0]
        if r.p[1] > col:
            col = r.p[1]

    return row + 1, col + 1

def read_file():
    lines = open("puzzle.txt").read().strip()
    lines = lines.split("\n")
    
    robots = []
    for l in lines:
        robot = Robot()
        p,v = l.split(" ")
        robot.p = list(map(int, p.split("=")[-1].split(",")))[::-1]
        robot.v = list(map(int, v.split("=")[-1].split(",")))[::-1]
        robots.append(robot)
        
    return robots

def write_file(map):
    with open("solution.txt", "w") as f:
        for row in map:
            # 0 convert to " " and 1 convert to "X"
            line = ""
            for i in range(len(row)):
                if row[i] == 0:
                    line += " "
                else:
                    line += "X"
            f.write(line)
            f.write("\n")

robots=read_file()
row, col = get_max_positions(robots)

for i in range(MOVEMENTS):
    m = Map(row, col)
    for robot in robots:
        robot.move(row, col)
        m.add_robot(robot)
    if m.unique_robots() < 1:
        write_file(m.map)
        print("Solution found: ", i + 1)
        break
    # print(m.map)