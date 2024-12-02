import os
import sys
import numpy as np

def remove_spaces_and_cast_int(_list_: list, space="")-> list:
    new_list = []

    for l in _list_:
        if l != space:
            new_list.append(int(l))
    
    return new_list


def read_cards(txt_file):
    print(f"Reading {txt_file} file")
    all_winners, all_my_numbers = [], []

    with open(txt_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.replace("\n", "")

            winners = line.split("|")[0].split(":")[-1].split(" ")
            my_numbers = line.split("|")[-1].split(" ")
            
            winners = remove_spaces_and_cast_int(winners)
            my_numbers = remove_spaces_and_cast_int(my_numbers)
            
            all_winners.append(winners)
            all_my_numbers.append(my_numbers)

        f.close()
    return all_winners, all_my_numbers

def count_winners(winners, my_numbers, current_card):
    cont = current_card
    cards_added = []

    for num in my_numbers:
        if num in winners:
            cont += 1
            cards_added.append(cont)

    return cards_added

if __name__ == "__main__":

    if len(sys.argv) < 1:
        print("You have to pass input txt")
    else:
        winners, my_numbers = read_cards(sys.argv[1])
        
        cards_added_total = np.ones((len(winners)))
        for i in range(len(winners)):
            result = count_winners(winners[i], my_numbers[i], i + 1)
            
            if cards_added_total[i] > 1:
                for r in result:
                    cards_added_total[r - 1] += cards_added_total[i]
            else:
                for r in result:
                    cards_added_total[r - 1] += 1

        print(sum(cards_added_total))
