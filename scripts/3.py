def solvePuzzle(input):
    gamma = ''
    epsilon = ''
    # instaniate proper length array
    common = [0]*(len(input[0]))
    for binary in input:
        # split decimal string into array
        binary = [*binary]
        for index, num in enumerate(binary):
            num = int(num)
            # We'll count how many 1 vs 0s by incrementing/decrementing the value at that index
            if num:
                common[index] += 1
            else:
                common[index] -= 1

    for num in common:
        num = int(num)
        # If less than 0 then 0 was more common than 1
        if num < 0:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    # Convert from binary (base 2) to decimal
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print("Part one: " + str(gamma * epsilon))

    
