import sys 
import numpy as np
from enum import Enum

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

class Ranking(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7

def get_value_card(card):
    return int(cards.index(card))

def get_rank(cards):
    if len(cards) == 5 and np.all(cards == [1,1,1,1,1]):
        return Ranking.HIGH_CARD
    elif len(cards) == 4 and np.all(cards == [2,1,1,1]):
        return Ranking.ONE_PAIR
    elif len(cards) == 3 and np.all(cards == [2,2,1]):
        return Ranking.TWO_PAIR
    elif len(cards) == 3 and np.all(cards == [3,1,1]):
        return Ranking.THREE_OF_KIND
    elif len(cards) == 2 and np.all(cards == [3,2]):
        return Ranking.FULL_HOUSE
    elif len(cards) == 2 and np.all(cards == [4,1]):
        return Ranking.FOUR_OF_KIND
    elif len(cards) == 1 and np.all(cards == [5]):
        return Ranking.FIVE_OF_KIND

def read_correspondences(txt_file):
    print(f"Reading {txt_file} file")
    hands = []
    points = []

    with open(txt_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.replace("\n", "")
            split_line =  line.split(" ")
            hand_ = [l for l in split_line[0]]
            hands.append(hand_)
            
            points.append(split_line[1])

        f.close()
    
    return np.array(hands), np.array(points).astype(int)

def calculate_rank_hand(hand):

    i = 0
    results = []
    while len(hand) > 1:
        equals = hand[hand != hand[i]]
        results.append(abs(len(equals) - len(hand)))
        hand = equals
    
    if len(hand) == 1:
        results.append(1)

    return np.sort(np.array(results).astype(int))[::-1]

def sort_by_lower_card(hands):
    """
    First we need to calculate the value of each card because exists K, Q, T, A..., then we sort the hands by the lower card
    """
    value_cards_hand = []
    for i in range(len(hands)):
        hand = hands[i]
        hand = [get_value_card(x) for x in hand]
        value_cards_hand.append(hand)
    
    sorted_indices = sorted(range(len(value_cards_hand)), key=lambda i: value_cards_hand[i])

    return hands[sorted_indices]

def calculate_rank(hands):
    """
    Return if is a high card, one pair, two pair, three of kind, full house, four of kind or five of kind for each hand
    """
    rank = []
    for i in range(len(hands)):
        result = calculate_rank_hand(hands[i])
        rank.append(int(get_rank(result).value))
    return np.array(rank)

def get_original_position(hands, hand):
    for i in range(len(hands)):
        if np.all(hands[i] == hand):
            return i

if __name__ == "__main__":
    hands, points = read_correspondences(sys.argv[1])

    rank = calculate_rank(hands)
    # when we have the rank of each hand, we need to sort the equals hands, this is, if we have two hands with the same rank, we need to sort them by the lower card

    index_visited = []
    dict_ = {} # key: rank, value: hands
    for i in range(len(rank)):
        if i in index_visited:
            continue

        # get hands with the same rank
        equals_idx = np.where(rank == int(rank[i]))

        # add to the visited index for not to visit again
        index_visited = np.concatenate((index_visited, equals_idx[0]))
        
        # sort by lower card
        hands_ = sort_by_lower_card(hands[equals_idx])
        dict_[int(rank[i])] = hands_
    
    # When we have the hands sorted by rank and lower card, we need to calculate the winnings
    cont = 1
    total_winnings = 0
    sorted_keys= sorted(dict_.keys())
    for key in sorted_keys:
        for hand in dict_[key]:
            idx_original = get_original_position(hands, hand) # get the original position of the hand for get the points
            total_winnings += points[idx_original]*cont
            cont += 1

    print(total_winnings)