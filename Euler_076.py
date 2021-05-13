# Problem 76
# Counting summations

# Fast because it only counts the number of combinations for a given Sum and 
# Largest Block. The organization in combos is: 
# combos[the sum of all blocks][size of largest block]
size = 100
combos = [ [ 0 for highest in range(size+1) ] for summy in range(size+1)] 

for turn in range(1,size+1):
    combos[turn][turn] = 1
    for new_block in range(1,turn+1):
        for old_highest in range(1,new_block+1):
            combos[turn][new_block] += combos[turn-new_block][old_highest]

final_count = 0
for highest in range(1,size):
    final_count += combos[size][highest]
    
print(f'{final_count} ways to write {size} as sum of two pos ints')
