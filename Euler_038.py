# Problem 38
# Pandigital multiples

# Clue is that 918273645 is given, so my answer must be greater; thus, first digit of 
# int must be 9. No more 1 digit options for int, and 2 and 3 digits don't work bc 9X 
# and 9XX ints can't produce 9 char str. Thus, I will only look through 4 digit 
# integers, beginning with '9'

panMax = 0 # 918273645
for num in range(9876,9181,-1):
    testNum = str(num) + str(num * 2)
    digits = [x for x in str(testNum)]
    digits.sort()
    if digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print(f'Largest pandigital: {testNum}')
        break
