def solvePuzzle(input):
    depth = 0
    horizontal = 0
    for i in input:
        parts = i.split()
        num = int(parts[1])
        match parts[0]:
            case "forward":
                horizontal += num
            case "down":
                depth += num
            case "up":
                depth -= num
        
    print("Part one: " + str(depth * horizontal))

    depth = 0
    horizontal = 0
    aim = 0
    for i in input:
        parts = i.split()
        num = int(parts[1])
        match parts[0]:
            case "down":
                aim += num
            case "up":
                aim -= num
            case "forward":
                horizontal += num
                depth += aim * num

    print("Part two: " + str(depth * horizontal))
