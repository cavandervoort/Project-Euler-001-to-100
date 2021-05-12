# Problem 15
# Lattice paths

import math

# first calculate the number of paths to the daigonal midline of the grid

numPathsToMidDiagonal = []

numerator = math.factorial(20)
runningNumPaths = 1
for pos in range(21):
    numPathsToMidDiagonal.append(int(runningNumPaths))
    runningNumPaths *= (20 - pos) / (pos + 1)

# total paths is equal to the sum of squares of paths to each point on diagonal midline    

totalPaths = 0

for pathsToMidline in numPathsToMidDiagonal:
    totalPaths += pathsToMidline ** 2
    
print(totalPaths)
