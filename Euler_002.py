# Problem 2
# Even Fibonacci numbers
old = 1
new = 1
runningSum = 0
while new <= 4000000:
    if new % 2 == 0:
        runningSum += new
    new,old = old+new,new

print(f'The last even Fibonacci number added is {old}, and the sum is {runningSum}')