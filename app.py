import utilities.input as inputReader

day = input("What day would you like to run? ")

input = inputReader.openInput(day)

match day:
    case "1":
        import scripts.day01 as s
        s.solvePuzzle(input)