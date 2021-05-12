# Problem 20
# Factorial digit sum

def getFact(inputInt):
    runningFact = 1
    for i in range(1, inputInt + 1):
        runningFact *= i
    return runningFact
    
factSize = 100
fact = getFact(factSize)
strFact = str(fact)

digitsSum = 0
for digit in strFact:
    digitsSum += int(digit)

print(digitsSum)
