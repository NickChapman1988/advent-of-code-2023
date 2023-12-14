""" 
Day 4 Puzzle 1 Solution

1. Split each line using the | as the delimiter
2. Loop through to see if the each number in the 1st list is in the 2nd list
3. If yes AND score = 0: score +1
4. If yes AND score > 0: score + score
5. For each line add score to total score and reset score to 0

"""

file = open('day_4/puzzle_1/scratchcards.txt', 'r', encoding="utf-8")
lines = file.readlines()

score = 0

for line in lines:
    
    # split lines at the \n that keep getting added to input
    #input = line.split("\n")[0]
    
    # split the card ID off the line
    numbers = line.split(":")[1]
    
    # split lines at the | and then split each half at the spaces to create list of individual strings
    winning_numbers_list = numbers.split("|")[0].split(" ")
    player_numbers_list = numbers.split("|")[1].split(" ")

    
    # filter empty strings from each number list
    filtered_winning_numbers = list(filter(None, winning_numbers_list))
    filtered_player_numbers = list(filter(None, player_numbers_list))

    
    # convert each list from strings to integers
    winning_numbers = list(map(int, filtered_winning_numbers))
    player_numbers = list(map(int, filtered_player_numbers))

    # convert each list to a set in order to use intersection function
    winning_numbers_set = set(winning_numbers)
    player_numbers_set = set(player_numbers)

    

    match_count = 0
    matching_numbers = winning_numbers_set.intersection(player_numbers_set)
    match_count = len(matching_numbers)

    if match_count > 0:
        score += 2 ** (match_count - 1)
        
print(score)

