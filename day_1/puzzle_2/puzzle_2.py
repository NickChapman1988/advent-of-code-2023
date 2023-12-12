""" 
Day 1 - Puzzle 2 Solution 

PSEUDOCODE

1. Open calibration document
2. Iterate over each line and translate string numbers to integers proper
3. Use code from puzzle 1 to add numbers to list, and combine first and last integers
4. Sum total of all numbers in list
"""

# Open calibration document and save to
file = open('day_1/puzzle_1/calibration_document.txt', 'r', encoding="utf-8")
lines = file.readlines()

numbers_list = []

numberString = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
}

numbersList = {
    1,2,3,4,5,6,7,8,9
}

for line in lines: 

   # first_num = line.find(numberString, numbersList)
   # last_num = line.rfind(numberString, numbersList)
   # combined = str(first_num + last_num)
   # print(combined)