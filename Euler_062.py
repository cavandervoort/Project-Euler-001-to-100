# Problem 62

digitSetDict = {}

for i in range(10000):
    iCubed = i ** 3
    iCubedDigits = "".join(sorted([dig for dig in str(iCubed)]))
    try:
        digitSetDict[iCubedDigits][0] += 1
        digitSetDict[iCubedDigits][1].append(iCubed)
    except:
        digitSetDict[iCubedDigits] = [1,[iCubed]]
    if digitSetDict[iCubedDigits][0] >= 5:
        print(f'There are {digitSetDict[iCubedDigits][0]} permutations for {i}^3 ({iCubed}).')
        digitSetDict[iCubedDigits][1].sort()
        print(f'The smallest cube is {digitSetDict[iCubedDigits][1][0]}')
