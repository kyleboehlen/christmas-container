import numpy as py
from collections import Counter

def solvePuzzle(input):
    array = py.sort(py.array(input[0].split(',')).astype(int))
    minPartOneFuel = 1000000000
    minPartTwoFuel = 1000000000
    items = Counter(array).items()
    for x, y in items:
        currentPartOneFuel = 0
        currentPartTwoFuel = 0
        for value, count in items:
            fuel = abs(x - value)
            currentPartOneFuel = currentPartOneFuel + (fuel * count)
            currentPartTwoFuel = int(currentPartTwoFuel + (fuel * (fuel + 1) / 2) * count) # Triangle number
        if currentPartOneFuel <= minPartOneFuel:
            minPartOneFuel = currentPartOneFuel
        if currentPartTwoFuel <= minPartTwoFuel:
            minPartTwoFuel = currentPartTwoFuel
    
    print("Part one: " + str(minPartOneFuel))
    print("Part two: " + str(minPartTwoFuel))
