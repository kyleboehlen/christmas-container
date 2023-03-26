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

    oxygen = input
    for i in range(len(oxygen[0])):
        print(i)
        common = getMostCommonAtIndex(oxygen, i)
        if common:
            common = "1"
        else:
            common = "0"
        oxygen = filterSet(oxygen, i, common)

        if len(oxygen) == 1:
            oxygen = oxygen[0]
            break

    c02 = input
    for i in range(len(c02[0])):
        common = getMostCommonAtIndex(c02, i)
        if common:
            common = "0"
        else:
            common = "1"
        c02 = filterSet(c02, i, common)

        if len(c02) == 1:
            c02 = c02[0]
            break

    oxygen = int(oxygen, 2)
    c02 = int(c02, 2)

    print("Part two: " + str(oxygen * c02))

def filterSet(s, index, y):
    def iteratorFunc(x):
        return x[index] == y
		
    return list(filter(iteratorFunc, s))

def getMostCommonAtIndex(input, index):
    common = 0
    for i in input:
        if int(i[index]):
            common += 1
        else:
            common -= 1
            
    return common >= 0
