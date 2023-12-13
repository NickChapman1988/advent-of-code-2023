"""
Day 2 Puzzle 2 Solution

PSEUDOCODE
1. Open input as for puzzle 1
2. Declare 0 variables for highest colours
3. Loop through each set of cubes as before, set highest of each cube colour to variables
4. Multiple highest count for each colour together
5. Add each total to overall total
"""

file = open('day_2/puzzle_1/conundrum_input.txt', 'r', encoding="utf-8")
lines = file.readlines()
output = 0

for line in lines:
    input = line.split("\n")[0]
    game = input.split(":")[1].split(";")
    
    redHighest = 0
    greenHighest = 0
    blueHighest = 0
    
    for sets in game:
        
        cubes = sets.split(",")
        
        for cube in cubes:
            hand = cube.split(" ")
            handCount = int(hand[1])
            handColour = hand[-1]
            
            if handColour == "red" and handCount > redHighest:
                redHighest = +handCount
            elif handColour == "blue" and handCount > blueHighest:
                blueHighest = +handCount
            elif handColour == "green" and handCount > greenHighest:
                greenHighest = +handCount

    output += redHighest * blueHighest * greenHighest 
        
print(output)
