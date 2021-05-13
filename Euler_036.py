# Problem 36
# Double-base palindromes

import time
start = time.time()

def base10to2(base10Int):
    base2Temp = [] 
    base2Column = 1
    while base10Int != 0:
        if base10Int % (base2Column * 2) == base2Column:
            base10Int -= base2Column
            base2Temp.insert(0,'1')
        else:
            base2Temp.insert(0,'0')
        base2Column *= 2
    
    base2Str = ''.join(base2Temp)
    return base2Str

limit = 1_000_000

# find base 10 palindromes
base10Palindromes = []
for num in range(1,limit):
    numString = str(num)
    if numString == numString[::-1]:
        base10Palindromes.append(num)

print(f'Found base 10 palindromes in {time.time() - start} seconds') 

# find base 2 palindromes
base2Palindromes = []
sumComboPalindromes = 0

for pal10 in base10Palindromes:
    base2Str = base10to2(pal10)
    if base2Str == base2Str[::-1]:
        sumComboPalindromes += pal10

print(f'found base 2 palindromes in {time.time() - start} seconds') 
print(f'the pal sum is {sumComboPalindromes}')
