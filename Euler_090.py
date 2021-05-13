# Problem 90

def single_test(test_cube, pairs):
    cube = [digit for digit in test_cube]
    if 9 in cube:
        cube.append(6)
    for pair in pairs:   
        if pair[0] in cube or pair[1] in cube:
            continue
        else:
            return False
    return True

def cube_test(test_cube_1, test_cube_2, pairs):
    cube_1 = [digit for digit in test_cube_1]
    cube_2 = [digit for digit in test_cube_2]
    if 9 in cube_1:
        cube_1.append(6)
    if 9 in cube_2:
        cube_2.append(6)
    for pair in pairs:   
        if pair[0] in cube_1 and pair[1] in cube_2:
            continue
        elif pair[0] in cube_2 and pair[1] in cube_1:
            continue
        else:
            return False
    return True

# Step 1: find all plausible dice (having at least one digit from each digit pair)

pairs = ((0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1))
dice_count = 0
qual_count = 0
plausible_dice = []
for a in range(5):
    for b in range(a+1,6):
        for c in range(b+1,7):
            for d in range(c+1,8):
                for e in range(d+1,9):
                    for f in range(e+1,10):
                        temp_dice = [a,b,c,d,e,f]
                        dice_count += 1
                        if single_test(temp_dice, pairs):
                            plausible_dice.append(temp_dice)
                            qual_count += 1
                        
print(f'I found {qual_count} plausible dice\n')

# Step 2: review all combination pairs of plausible dice

winning_count = 0
losing_count = 0
range_up = len(plausible_dice)
for first in range(range_up):
    for second in range(first, range_up):
        if cube_test(plausible_dice[first], plausible_dice[second], pairs):
            winning_count += 1
        else:
            losing_count += 1

print(f'wins: {winning_count}')
print(f'losses: {losing_count}')
