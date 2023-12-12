""" Day 1 - Puzzle 1 Solution 

PSEUDOCODE

1. Open calibration document
2. Iterate over each line and pull out all integers
3. Combine first and last integers from each line, add double digit to list of numbers
4. If only one integer on a line, replicate it to make a two-digit number (eg 7 becomes 77)
5. Add all numbers in the list for a grand total
"""

# Open calibration document and save to
file = open('day_1/puzzle_1/calibration_document.txt', 'r', encoding="utf-8")
lines = file.readlines()

numbers_list = []

for line in lines:
    nums = [i for i in line if i.isdigit()]
    numbers_list.append(int(nums[0] + nums[-1]))

total = sum(numbers_list)
print(f'Day 1 Puzzle 1 solution: {total}')