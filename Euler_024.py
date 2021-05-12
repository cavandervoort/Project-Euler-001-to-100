# Problem 24
# Lexicographic permutations

def factorial(num):
    runningFact = 1
    for i in range(1,num + 1):
        runningFact *= i
    return runningFact 

factDict = {0:1}
for n in range(1,11):
    factDict[n] = factorial(n)

perm = 999_999 # 1,000,000th permutation, but starting at 0
digitsAll = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
outputStr = ''
for dig in range(1,11):
    count = 0
    while perm >= factDict[10-dig]:
        perm -= factDict[10-dig]
        count += 1
    outputStr += digitsAll.pop(count)

print(outputStr)