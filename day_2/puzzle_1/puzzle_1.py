"""
Day 2 Puzzle 1 Solution

PSEUDOCODE

1. Assign id of each game based on lines of input (first line = ID 1, second line = ID 2 etc.)
2. Set number of red, green and blue cubes to 12, 13 and 14
3. Compare red, green and blue cubes in each game to set numbers
4. If game is possible, add game ID to list of IDs
"""

""" 
Solution code is correct - however, initial attempt was unable to obtain correct answer due to program inserting '\n' onto the end of random lines in the input file, 
thereby rendering the strings differently (i.e. "red" cannot be read because it appears as "red\n")

Added additional split() to remove the \n wherever it appears to get correct input
"""


# Open conundrum document and save to
file = open('day_2/puzzle_1/conundrum_input.txt', 'r', encoding="utf-8")
lines = file.readlines()

indexTotal = 0

for line in lines:
    input = line.split("\n")[0]
    gameIndex = input.split(":")[0]
    index = int(gameIndex.split(" ")[1])
    game = input.split(":")[1].split(";")
    
    possible = True
    
    for g in game:
        redCount= 0
        greenCount = 0
        blueCount = 0
        cubes = g.split(",")
        
        for cube in cubes:
            hand = cube.split(" ")
            handCount = hand[1]
            handColour = hand[-1]
            
            if handColour == "red":
                redCount = int(handCount)
            elif handColour == "blue":
                blueCount = int(handCount)
            elif handColour == "green":
                greenCount = int(handCount)

        if (redCount > 12 or greenCount > 13 or blueCount > 14):
            possible = False
        
    if possible == True:
        indexTotal += index

print(indexTotal)
