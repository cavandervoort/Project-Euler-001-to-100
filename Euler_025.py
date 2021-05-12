# Problem 25
# 1000-digit Fibonacci number

fibs = [1,1]
digits = 1000
for num in range(100000):
    fibs.append(fibs[num]+fibs[num+1])
    if len(str(fibs[num+2])) == digits:
        break
print(f'The {len(fibs)} fib has {digits} digits')