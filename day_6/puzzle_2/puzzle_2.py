""" 
Day 6 Puzzle 2 Solution

"""

time = 56977793
distance = 499221010971440

waysToWin = 0

for i in range(1, time + 1):
    if i <= time:
        speed = i
            
        totalDistance = speed * (time - speed)
        if (totalDistance > distance):
            waysToWin += 1

print(waysToWin)