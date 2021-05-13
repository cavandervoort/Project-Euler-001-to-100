# Problem 46
# Goldbach's other conjecture

primes = [2]
squares = []
test_range = 10000
prime_range = test_range ** 0.5 + 1
two_x_square_range = (test_range / 2) ** 0.5 + 1

# get the squares
for num in range(1, round(two_x_square_range)):
    squares.append(2 * num ** 2)

# get the primes while checking for composits
isDone = False
for num in range(3,test_range,2):
    is_prime = True
    for prime in primes:
        if num % prime == 0:
            is_prime = False
    if is_prime == True:
        primes.append(num)
    elif is_prime == False:
        does_square_fit = False
        for sqr in squares:
            if num - sqr in primes:
                does_square_fit = True
                break
        if does_square_fit == False:
            print(num)
            isDone = True
            break
    if isDone:
        break
