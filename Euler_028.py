# Problem 28
# Number spiral diagonals

diagSum = 1
for radius in range(1,501):
    diagSum += ((2*radius) ** 2 + 1 + (2*radius - 1) ** 2) / 2
    diagSum += (2*radius) ** 2 + 1
    diagSum += ((2*radius) ** 2 + 1 + (2*radius + 1) ** 2) / 2
    diagSum += (2*radius + 1) ** 2

print(int(diagSum))
