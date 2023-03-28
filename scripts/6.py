import numpy as py

def solvePuzzle(input):
    input = input[0].split(",")
    newFish = [0]*2
    currentFish = [0]*7
    for i in input:
        currentFish[int(i)] += 1
    for i in range(256):
        # Roll fish
        currentFish = list(py.roll(currentFish, -1))
        newSpawn = currentFish[6]
        newFish = list(py.roll(newFish, -1))
        currentFish[6] += newFish[1]
        newFish[1] = newSpawn
        if i == 79:
            totalFish = sum(currentFish) + sum(newFish)
            print("Part one: " + str(totalFish))
    totalFish = sum(currentFish) + sum(newFish)
    print("Part two: " + str(totalFish))