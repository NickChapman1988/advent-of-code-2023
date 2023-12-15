"""
Day 5 Puzzle 1 Solution

"""

file = open('day_5/puzzle_1/seeds.txt', 'r', encoding="utf-8")
lines = file.readlines()

seeds = lines.split("\n\n")[0].split(" ");


seedToSoil = lines.split("\n\n")[1].split("\n");


soilToFertilizer = lines.split("\n\n")[2].split("\n");


fertilizerToWater = lines.split("\n\n")[3].split("\n");

waterToLight = lines.split("\n\n")[4].split("\n");


lightToTemperature = lines.split("\n\n")[5].split("\n");

  
temperatureToHumidity = lines.split("\n\n")[6].split("\n");


humidityToLocation = lines.split("\n\n")[7].split("\n");
