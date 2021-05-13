# Problem 45
# Triangular, pentagonal, and hexagonal

triNVal,triNum = 1,1
pentNVal,pentNum = 1,1
hexNVal,hexNum = 1,1

while triNVal < 1000000:
    if triNum == pentNum == hexNum:
        if triNum > 40755:
            print(f'Match at {int(triNum)}')
            print(f'Counts are {triNVal}, {pentNVal}, and {hexNVal}.')
            break
    minVal = min(triNum, pentNum, hexNum)
    if triNum == minVal:
        triNVal += 1
        triNum = triNVal * (triNVal + 1) / 2
    if pentNum == minVal:
        pentNVal += 1
        pentNum = pentNVal * (3 * pentNVal - 1) / 2
    if hexNum == minVal:
        hexNVal += 1
        hexNum = hexNVal * (2 * hexNVal - 1)
