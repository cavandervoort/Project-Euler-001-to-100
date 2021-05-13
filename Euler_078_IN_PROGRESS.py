# Problem 78
# Coin partitions

'''
The code below works, but can only get through size ~1000 in one minute, which does not 
find then answer. I think my best bet is to calculate some lower values and then see if 
I can figure out the formula.

'''

import time
start = time.time()

print("The code is not fast enough to find an answer yet")

# the organization in combos is: combos[the sum of all blocks][size of larges block]
size = 1_000
combos = [ [ 0 for highest in range(size+1) ] for _ in range(size+1)] 

print(f'made combos after {time.time() - start} seconds')

for turn in range(1,size+1):
    combos[turn][turn] = 1
    for new_block in range(1,turn+1):
        for old_highest in range(1,new_block+1):
            combos[turn][new_block] += combos[turn-new_block][old_highest]

    final_count = 0
    for highest in range(1,turn+1):
        final_count += combos[turn][highest]

    if final_count % 1_000 == 0:
        print(f'Turn {turn} is divisible by 1_000 after {time.time() - start} seconds')
    
    if final_count % 10_000 == 0:
        print(f'Turn {turn} is divisible by 10_000')
    
    if final_count % 100_000 == 0:
        print(f'\nTurn {turn} is divisible by 100_000\n')
        
    if final_count % 1_000_000 == 0:
        print(f'\nTurn {turn} is divisible by one million\n')
        break

print('done')
