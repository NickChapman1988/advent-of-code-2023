"""
Day 6 Puzzle 1 Solution

"""

times = [56, 97, 77, 93]
distances = [499, 2210, 1097, 1440]

races = [[56, 499], [97, 2210], [77, 1097], [93, 1440]]
waysToWin = 1

for race in races:
    time = race[0]
    distance = race[1]
    waysToWinPerRace = 0
    winsList = []

    for i in range(1, time + 1):
        if i <= time:
            speed = i
            
            totalDistance = speed * (time - speed)
            if (totalDistance > distance):
                waysToWinPerRace += 1

    winsList.append(waysToWinPerRace)
    
    for wins in winsList:
        waysToWin = waysToWin * wins

print(waysToWin)
