# Problem 6
# Sum square difference

sumSquares,sumNums = 0,0

for num in range(1,101):
    sumSquares += num ** 2

for num in range(1,101):
    sumNums += num

sumNums *= sumNums
    
print(sumNums - sumSquares)