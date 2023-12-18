""" 
Day 7 Puzzle 1 Solution
"""

file = open('day_7/puzzle_1/puzzle_input.txt', 'r', encoding="utf-8")
lines = file.readlines()

for line in lines:
    hand = line.split(" ")[0]
    bid = line.split(" ")[1]

    handRank = 0

    handlength = len(set(hand))
    
    # five of a kind
    if handlength == 1:
        handRank = 7
    # four of a kind or full house
    elif handlength == 2:
        # four of a kind
        for card in hand:
            if (hand.count(card) == 4):
                handRank = 6
            # full house
            else:
                handRank = 5
    # three of a kind or two pair
    elif handlength == 3:
        for card in hand:
            # three of a kind
            if (hand.count(card) == 3):
                handRank = 4
            # two pair
            else:
                handRank = 3
    # one pair
    elif handlength == 4:
        handRank = 2
    # high card
    else:
        handRank = 1

    #print(hand, handRank)

    
    