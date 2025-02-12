import os
import sys
import re 

TOKENS_A = 3
TOKENS_B = 1
ADD_NUMBER = 10000000000000

def read_file():
    lines = open("puzzle.txt").read().strip()
    lines = lines.split("\n")
    
    games = []
    dict_ = {}
    for l in lines:
        if l == "":
            games.append(dict_)
            dict_ = {}
            continue
        key = l.split(":")[0][-1]
        value = l.split(":")[-1]
        numbers = re.findall(r'\d+', value)
        if key != "A" and key != "B":
            dict_["prize"] = {'x': int(numbers[0]) + ADD_NUMBER, 'y': int(numbers[1]) + ADD_NUMBER, 'cont':0}
        else:
            dict_[key] = {'x': int(numbers[0]), 'y': int(numbers[1]), 'cont':0}
    
    games.append(dict_)
    return games

def calculate_cost_tokens(x, y):
    # calculate the spend of the game
    return x * TOKENS_A + y * TOKENS_B

def cramer_method(buttom_a, buttom_b, prize):
    """ 
    calculate the cramer method
    cost_buttom_a_x * x + cost_buttom_a_y * y = cost_prize
    cost_buttom_b_x * x + cost_buttom_b_y * y = cost_prize
    """
    determinant_sistem = buttom_a["x"] * buttom_b["y"] - buttom_a["y"] * buttom_b["x"]
    determinant_x = prize["x"] * buttom_b["y"] - prize["y"] * buttom_b["x"]
    determinant_y = buttom_a["x"] * prize["y"] - buttom_a["y"] * prize["x"]

    x = determinant_x / determinant_sistem
    y = determinant_y / determinant_sistem
    return x, y

def is_valid_game(x, y):
    """
    x and y must be integer numbers
    """
    return x.is_integer() and y.is_integer()

games = read_file()
result = 0
for game in games:
    x, y = cramer_method(game["A"], game["B"], game["prize"])
    if is_valid_game(x, y):
        tokens = calculate_cost_tokens(x, y)
        result += tokens

print("Total tokens: ", result)
