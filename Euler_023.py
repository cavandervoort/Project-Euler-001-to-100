# Problem 23
# Non-abundant sums

def isAbNum(n):
    sumDiv = 1
    nSqrRoot = int(n ** 0.5)
    for div in range(2,nSqrRoot+1):
        if n % div == 0:
            sumDiv += div + (n/div)
    if n / nSqrRoot == nSqrRoot:
        sumDiv -= nSqrRoot
    if sumDiv > n:
        return True
    return False

def isAbSum(i,abNums):
    for abNum in abNums:
        diff = i - abNum
        if diff in abNums:
            return True
        elif abNum > (i / 2):
            return False
    return False

# find the abundant numbers under 28124
abNums = {}
for n in range(1,28124):
    if isAbNum(n):
        abNums[n] = 0

# find all numbers that are not the sum of two abundant numbers
sumNonAbNums = 0
for testNum in range(1,28124):
    if not isAbSum(testNum,abNums):
        sumNonAbNums += testNum

print(f'The sum of ints that are not a sum of two abundant numbers is {sumNonAbNums}')
