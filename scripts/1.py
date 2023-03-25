def solvePuzzle(input):
    previous = None
    count = 0
    for i in input:
        num = int(i)
        if previous != None:
            if num > previous:
                count = count + 1
        previous = num

    print("Part one: " + str(count))

    count = 0
    for index, num in enumerate(input):
        if (index + 3 < len(input)):
            firstRange = int(num) + int(input[index + 1]) + int(input[index + 2])
            secondRange = int(input[index + 1]) + int(input[index + 2]) + int(input[index + 3])
            if (secondRange > firstRange):
                count = count + 1
    
    print("Part two: " + str(count))

