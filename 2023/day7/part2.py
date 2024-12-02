import sys 
import numpy as np
from enum import Enum

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

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

def all_values_dict_are_equals(dict_):
    return len(set(dict_.values())) == 1

def get_card_more_value(cards_):
    """
    Return the card with more value
    """
    cards_ = np.array(cards_)
    cards_ = [get_value_card(x) for x in cards_]
    return cards[max(cards_)]

def change_joker_to_card(hand):
    """
    Transform the hand with jokers to a hand without jokers and next use the part 1 exacly the same
    """
    original_hand = hand
    # First delete J from the hand
    hand = np.array(hand)
    number_jokers = len(hand) - len(hand[hand != "J"])
    
    # return best hand
    if number_jokers == len(original_hand):
        return np.array(["A", "A", "A", "A", "A"])
    
    hand = hand[hand != "J"]

    results = {}
    # Then count repeated cards
    while len(hand) > 1:
        equals = hand[hand != hand[0]]
        results[hand[0]] = abs(len(equals) - len(hand))
        hand = equals
        
    if len(hand) == 1:
        results[hand[0]] = 1

    new_value_J = ""
    if number_jokers > 0:
        #sorted dictionary by value
        results = dict(sorted(results.items(), key=lambda item: item[1])[::-1])
        if all_values_dict_are_equals(results):
            # en este caso escoger el valor de carta más alto
            cards = list(results.keys())
            new_value_J = get_card_more_value(cards)
        else:
            # seleccionar el valor de carta que mas se repite
            results_keys = list(results.keys())
            new_value_J = results_keys[0]

        for idx_card in range(len(original_hand)):
            if original_hand[idx_card] == "J":
                original_hand[idx_card] = new_value_J
    
    return np.array(original_hand)

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
    original_hands_ = hands.copy()

    hands_without_jokers = []
    for i in range(len(hands)):
        hands_without_jokers.append(change_joker_to_card(hands[i]))
        
    rank = calculate_rank(hands_without_jokers)
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
        hands_ = sort_by_lower_card(original_hands_[equals_idx])
        dict_[int(rank[i])] = hands_
    
    # When we have the hands sorted by rank and lower card, we need to calculate the winnings
    cont = 1
    total_winnings = 0
    sorted_keys= sorted(dict_.keys())
    tuple = []
    for key in sorted_keys:
        for hand in dict_[key]:
            idx_original = get_original_position(original_hands_, hand) # get the original position of the hand for get the points
            total_winnings += points[idx_original]*cont
            cont += 1
            tuple.append((hand, points[idx_original]))

    print(total_winnings)
